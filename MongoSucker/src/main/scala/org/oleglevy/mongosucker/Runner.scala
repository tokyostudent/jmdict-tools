import java.io.{StringReader, FileInputStream, InputStreamReader}
import javax.xml.stream.XMLInputFactory
import org.apache.solr.common.SolrInputDocument
import play.api.libs.iteratee._
import reactivemongo.api._
import reactivemongo.api.collections.default.BSONCollection
import reactivemongo.bson.{BSON, BSONDocument}
import scala.collection.Iterable
import scala.collection.mutable.ArrayBuffer
import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.Exception
import scala.concurrent.duration._

import scales.xml._
import ScalesXml._


import scala.collection.JavaConversions._

// to add friendly and consistent access to the data model



object Runner {
  object JmDictFactory extends scales.utils.SimpleUnboundedPool[XMLInputFactory] { pool =>

    val cdata = "http://java.sun.com/xml/stream/properties/report-cdata-event"

    def create = {
      val fac = XMLInputFactory.newInstance()
      if (fac.isPropertySupported(cdata)) {
        fac.setProperty(cdata, java.lang.Boolean.TRUE)
      }

      fac.setProperty("javax.xml.stream.isReplacingEntityReferences", java.lang.Boolean.FALSE)
      fac
    }
  }

  var _collection: BSONCollection = null
  var _db: DefaultDB = null

  val _defaultCollectionName = "small"
  val _defaultDbName = "jmdict"
  val _defaultHostList = List("localhost")

  val _defaultPageSize = 0

  def connectDB() = {

    // gets an instance of the driver
    // (creates an actor system)
    val driver = new MongoDriver
    val connection = driver.connection(_defaultHostList)

    // Gets a reference to the database "plugin"
    _db = connection(_defaultDbName)


    // Gets a reference to the collection "acoll"
    // By default, you get a BSONCollection.
    _collection = _db(_defaultCollectionName)
  }

  private var _pullXml:XmlPull = _
  private var _inputStreamReader:InputStreamReader = _
  def readXmlLoop(xmlFile:String):Iterator[Entry] = {
    _inputStreamReader = new InputStreamReader(new FileInputStream(xmlFile), "utf-8")



    _pullXml = pullXml(_inputStreamReader, parserFactoryPool = JmDictFactory)


    val xmlEntries = iterate(List(NoNamespaceQName("JMdict"), NoNamespaceQName("entry")), _pullXml)

    xmlEntries.map {Entry(_)}


  }

  def sendToMongo(entriesGroup:Iterable[BSONDocument]) = {
    val insertFuture = _collection.bulkInsert(Enumerator.enumerate(entriesGroup))

    insertFuture.onComplete {
      case _ =>  println( "mongo finished: " +
                          entriesGroup.head.getAs[Int]("ent_seq").get + "->" +
                          entriesGroup.last.getAs[Int]("ent_seq").get)
    }

    insertFuture.onFailure {
      case e:Exception => println("mongo failed: " + e.toString)

    }

    insertFuture
  }

  def sendToSolr(entriesGroup:Iterable[SolrInputDocument]) = {

    val httpPostFuture = Solr.updateRequest(entriesGroup)

    httpPostFuture.onComplete {
      case _ =>  println( "solr finished: " +
                          entriesGroup.head.getField("ent_seq").getValue + "->" +
                          entriesGroup.last.getField("ent_seq").getValue)


    }

    httpPostFuture.onFailure{
        case e: Throwable => println(e)
      }

    httpPostFuture

  }

  def runTests = {
    import DataModelImplicits.EntryReader

    val xml1 = "<hara><entry>\n<ent_seq>1000000</ent_seq>\n\n<r_ele>\n<re_nokanji/>\n<re_restr>hara4</re_restr>\n<reb>ヽ</reb>\n</r_ele>\n\n<r_ele>\n<reb>くりかえし</reb>\n</r_ele>\n\n<k_ele>\n<keb>jirbun gadol</keb>\n<ke_inf>sfsfd</ke_inf>\n<ke_pri>pripripri</ke_pri>\n\n</k_ele>\n<sense>\n<pos>n</pos>\n<gloss>repetition mark in katakana</gloss>\n</sense>\n</entry></hara>"


    _pullXml = pullXml(new StringReader(xml1), parserFactoryPool = JmDictFactory)

    val xmlEntries = iterate(List(NoNamespaceQName("hara"), NoNamespaceQName("entry")), _pullXml)

    val ee = xmlEntries.map {
      Entry(_)
    }.toList

    ee foreach {ent =>
      val bsonEntry = ent.toBsonDocument
      println(BSONDocument.pretty(bsonEntry.get))

      val unbsoned = BSON.read(bsonEntry.get)

      println(unbsoned)
      println("-------------------")
      println(ent)





    }


  }
  def main(args: Array[String]) {
    JmDictRest.run




    println("really")

    //    runTests
    return




    //val translationsFuture = Promise[Int].future //Solr.select(new QueryDsl("わりびき", Map()))


    //translationsFuture.onFailure{case f => println(f)}

    //val translations = Await.result(translationsFuture, Duration.Inf)

    //translations.foreach{println}




//    readLine()
//    return


//  val xmlEntries = readXmlLoop("/Users/oleglevy/dev/jmdict-small.xml")
    connectDB()
    val xmlEntries = readXmlLoop("/Users/oleglevy/dev/jmdict_full_nobom.xml")


    val awaitFutures = new ArrayBuffer[Future[Any]]


    for (entryGroup <- xmlEntries.grouped(1000)) {
      val t = entryGroup map {_.toBsonSolrTuple}
      awaitFutures += sendToMongo(t.map {_._1}) += sendToSolr(t.map {_._2})
    }

    awaitFutures += Solr.commitRequest


    Await.result (Future.sequence(awaitFutures), Duration.Inf)


    println("thats all, now shutting down...")


    /*
    Await.result(_db.connection.askClose()(10 seconds), 10 seconds)
    _inputStreamReader.close()

    println("thats all, now shutting down...")
*/
  }
}
