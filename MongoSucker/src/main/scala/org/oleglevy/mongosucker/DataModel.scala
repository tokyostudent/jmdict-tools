import org.apache.solr.common.SolrInputDocument
import reactivemongo.bson.buffer.{ArrayReadableBuffer, ArrayBSONBuffer}
import scala.Some
import scales.utils._
import scales.xml._
import ScalesXml._
import Functions._
import org.apache.commons.codec.binary.Base64
import reactivemongo.bson._


object DataModelImplicits {
  implicit object KEleReader extends BSONDocumentReader[K_ele] {
    def read(doc: BSONDocument): K_ele = K_ele(
      doc.getAs[String]("keb").get,
      doc.getAs[Seq[String]]("ke_inf").get,
      doc.getAs[Seq[String]]("ke_pri").get)
  }

  implicit object KEleWriter extends BSONDocumentWriter[K_ele] {
    def write(k_ele:K_ele): BSONDocument = BSONDocument(
      "keb" -> k_ele.keb,
      "ke_inf" -> k_ele.ke_inf,
      "ke_pri" -> k_ele.ke_pri
    )
  }

  implicit object REleReader extends BSONDocumentReader[R_ele] {
    def read(doc: BSONDocument): R_ele = {
      R_ele(doc.getAs[String]("reb").get,
      doc.getAs[Boolean]("re_nokanji").getOrElse(false),
      doc.getAs[List[String]]("re_restr").get,
      doc.getAs[List[String]]("re_inf").get,
      doc.getAs[List[String]]("re_pri").get
    )}
  }

  implicit object REleWriter extends BSONDocumentWriter[R_ele] {
    def write(r_ele:R_ele): BSONDocument = BSONDocument(
      "reb" -> r_ele.reb,
      "re_nokanji" -> r_ele.re_nokanji,
      "re_restr" -> r_ele.re_restr,
      "re_inf" -> r_ele.re_inf,
      "re_pri" -> r_ele.re_pri
    )
  }
  
  implicit object GlossReader extends BSONDocumentReader[Gloss] {
    def read(doc: BSONDocument): Gloss = Gloss(
      doc.getAs[String]("gloss").get
    )}

  implicit object GlossWriter extends BSONDocumentWriter[Gloss] {
    def write(gloss:Gloss): BSONDocument = BSONDocument(
      "gloss" -> gloss.gloss
    )}

  implicit object SenseReader extends BSONDocumentReader[Sense] {
    def read(doc: BSONDocument): Sense = Sense(
      doc.getAs[Seq[String]]("stagk").get,
      doc.getAs[Seq[String]]("stagr").get,
      doc.getAs[Seq[String]]("pos").get,
      doc.getAs[Seq[String]]("xref").get,
      doc.getAs[Seq[String]]("ant").get,
      doc.getAs[Seq[String]]("field").get,
      doc.getAs[Seq[String]]("misc").get,
      doc.getAs[Seq[String]]("s_inf").get,
      doc.getAs[Seq[String]]("lsource").get,
      doc.getAs[Seq[String]]("dial").get,
      doc.getAs[Seq[Gloss]]("glosses").get,
      doc.getAs[Seq[String]]("example").get
    )
  }

  implicit object SenseWriter extends BSONDocumentWriter[Sense] {
    def write(sense:Sense): BSONDocument = BSONDocument(
      "stagk" -> sense.stagk,
      "stagr" -> sense.stagr,
      "pos" -> sense.pos,
      "xref" -> sense.xref,
      "ant" -> sense.ant,
      "field" -> sense.field,
      "misc" -> sense.misc,
      "s_inf" -> sense.s_inf,
      "lsource" -> sense.lsource,
      "dial" -> sense.dial,
      "glosses" -> sense.glosses,
      "example" -> sense.example
    )}



  implicit object EntryReader extends BSONDocumentReader[Entry] {
    def read(doc: BSONDocument): Entry = Entry(
      doc.getAs[Int]("ent_seq").get,
      doc.getAs[Seq[K_ele]]("k_ele").get,
      doc.getAs[Seq[R_ele]]("r_ele").get,
      doc.getAs[Seq[Sense]]("sense").get)
  }

  implicit object EntryWriter extends BSONDocumentWriter[Entry] {
    def write(entry:Entry): BSONDocument = BSONDocument(
      "ent_seq" -> entry.ent_seq,
      "k_ele" -> entry.k_ele,
      "r_ele" -> entry.r_ele,
      "sense" -> entry.sense
    )}
  }

object K_ele {
  val empty:Seq[K_ele] = Seq(new K_ele("", List(), List()))
}
abstract class QueryMatchable {
  def matches(query:DictionaryQuery):Boolean
}

case class K_ele(keb:String = "",
                 ke_inf:Seq[String] = Seq(),
                 ke_pri:Seq[String] = Seq()) extends QueryMatchable
{
  def matches(query:DictionaryQuery):Boolean = {
    query.matches(keb)
  }

  def nonEmpty: Boolean = keb.nonEmpty
}



case class R_ele(reb:String = "",
                 re_nokanji:Boolean = false,
                 re_restr:Seq[String] = Seq(),
                 re_inf:Seq[String] = Seq(),
                 re_pri:Seq[String] = Seq()) extends QueryMatchable
{
  def isReadingFor(k_ele:K_ele):Boolean = re_restr.isEmpty || re_restr.exists {_ == k_ele.keb}
  def matches(query:DictionaryQuery):Boolean =
  {
    query.matches(reb)
  }
}

case class Gloss(gloss:String = "")
case class Sense(stagk:Seq[String] = Seq(),
                 stagr:Seq[String] = Seq(),
                 pos:Seq[String] = Seq(),
                 xref:Seq[String] = Seq(),
                 ant:Seq[String] = Seq(),
                 field:Seq[String] = Seq(),
                 misc:Seq[String] = Seq(),
                 s_inf:Seq[String] = Seq(),
                 lsource:Seq[String] = Seq(),
                 dial:Seq[String] = Seq(),
                 glosses:Seq[Gloss] = Seq(),
                 example:Seq[String] = Seq()) extends QueryMatchable
{
  def isSenseFor(k_ele:K_ele):Boolean             = stagk.isEmpty           ||  stagk.exists {_ == k_ele.keb}
  def isSenseFor(r_ele:R_ele):Boolean             = stagr.isEmpty           ||  stagr.exists {_ == r_ele.reb}
  def isSenseFor(reading:(R_ele, K_ele)):Boolean  = isSenseFor(reading._1)  &&  isSenseFor(reading._2)

  def getWordReadings(r_ele:Seq[R_ele], k_ele:Seq[K_ele]):Iterable[(R_ele, Seq[K_ele])] = {

    val nonEmpty_k_ele = if (k_ele.isEmpty) K_ele.empty else k_ele

    val wordReadingPairs = for ( _r_ele <- r_ele; _k_ele <- nonEmpty_k_ele if isSenseFor(_r_ele, _k_ele)) yield (_r_ele, _k_ele)
    val groupedByRele = wordReadingPairs.groupBy {_._1}

    groupedByRele.keys map {_r_ele =>
      (_r_ele, groupedByRele(_r_ele) map {_._2})
    }
  }

  def matches(query:DictionaryQuery):Boolean =
  {
    glosses.exists{g => query.matches(g.gloss)}
  }

}


object Entry
{

  val ent_seq = NoNamespaceQName("ent_seq")

  val k_ele = NoNamespaceQName("k_ele")
  val keb = NoNamespaceQName("keb")
  val ke_inf = NoNamespaceQName("ke_inf")
  val ke_pri = NoNamespaceQName("ke_pri")

  val r_ele = NoNamespaceQName("r_ele")
  val reb = NoNamespaceQName("reb")
  val re_restr = NoNamespaceQName("re_restr")
  val re_nokanji = NoNamespaceQName("re_nokanji")
  val re_inf = NoNamespaceQName("re_inf")
  val re_pri = NoNamespaceQName("re_pri")

  val sense = NoNamespaceQName("sense")
  val gloss = NoNamespaceQName("gloss")
  val stagk = NoNamespaceQName("stagk")
  val stagr = NoNamespaceQName("stagr")
  val pos = NoNamespaceQName("pos")
  val xref = NoNamespaceQName("xref")
  val ant = NoNamespaceQName("ant")
  val field = NoNamespaceQName("field")
  val misc = NoNamespaceQName("misc")
  val s_inf = NoNamespaceQName("s_inf")
  val lsource = NoNamespaceQName("lsource")
  val dial = NoNamespaceQName("dial")
  val example = NoNamespaceQName("example")


  def apply(bson64Encoded:String):Entry =
  {
    import DataModelImplicits.EntryReader
    BSON.readDocument[Entry](BSONDocument.read(ArrayReadableBuffer(Base64.decodeBase64(bson64Encoded))))
  }

  def apply(_entry:XmlPath):Entry =
  {
    val __rebList = for (_r_ele <- _entry \* r_ele) yield {
      R_ele(reb = value(_r_ele \* reb),
        re_nokanji = boolean(_r_ele \* re_nokanji),
        re_restr = (_r_ele \* re_restr map {value(_)}).toSeq,
        re_inf = (_r_ele \* re_inf map {value(_)}).toSeq,
        re_pri = (_r_ele \* re_pri map {value(_)}).toSeq
      )
    }

    val __kebList = for (_k_ele <- _entry \* k_ele) yield {
      K_ele(keb = value(_k_ele \* keb),
        ke_inf = (_k_ele \* ke_inf map {value(_)}).toSeq,
        ke_pri = (_k_ele \* ke_pri map {value(_)}).toSeq
      )
    }


    val __senseList = for (_sense <- _entry \* sense) yield {
      Sense(stagk = (_sense \* stagk map {value(_)}).toSeq,
        stagr = (_sense \* stagr map {value(_)}).toSeq,
        pos = (_sense \* pos map {value(_)}).toSeq,
        xref = (_sense \* xref map {value(_)}).toSeq,
        ant = (_sense \* ant map {value(_)}).toSeq,
        field = (_sense \* field map {value(_)}).toSeq,
        misc = (_sense \* misc map {value(_)}).toSeq,
        s_inf = (_sense \* s_inf map {value(_)}).toSeq,
        lsource = (_sense \* lsource map {value(_)}).toSeq,
        dial = (_sense \* dial map {value(_)}).toSeq,
        glosses = (_sense \* gloss map {g => Gloss(value(g))}).toSeq,
        example = (_sense \* example map {value(_)}).toSeq
      )
    }


    Entry(value(_entry \* ent_seq).toInt,
      k_ele = __kebList.toSeq,
      r_ele = __rebList.toSeq,
      sense = __senseList.toSeq)

  }
}
case class Entry(ent_seq:Int, k_ele:Seq[K_ele], r_ele:Seq[R_ele], sense:Seq[Sense])
{
  def wordReadings:Seq[(R_ele, K_ele)] = {

    for ( _r_ele <- r_ele;
          _k_ele <- k_ele if _r_ele.isReadingFor(_k_ele))
    yield (_r_ele, _k_ele)



  }


  private var cachedSolrDocument:Option[SolrInputDocument] = None
  def toSolrDocument:Option[SolrInputDocument] =
  {
    if (cachedSolrDocument.nonEmpty) return cachedSolrDocument

    if (toBsonDocument.isEmpty) return None


    val solrDoc = new SolrInputDocument()

    solrDoc.addField("ent_seq", ent_seq)

    sense.flatMap(_.glosses).map(_.gloss).foreach {
      solrDoc.addField("gloss", _)
    }

    r_ele.map(_.reb).foreach {
      solrDoc.addField("reb", _)
    }

    k_ele.map(_.keb).foreach {solrDoc.addField("keb", _)}

    solrDoc.addField("fullEntry",
                      BSONDocument.write(toBsonDocument.get,
                          new ArrayBSONBuffer).asInstanceOf[ArrayBSONBuffer].array)


    cachedSolrDocument = Some(solrDoc)

    cachedSolrDocument
  }

  private var cachedBsonDocument:Option[BSONDocument] = None
  import DataModelImplicits.EntryWriter
  def toBsonDocument:Option[BSONDocument] = {
    if (cachedBsonDocument.nonEmpty) return cachedBsonDocument


    cachedBsonDocument = Option(BSON.write(this))

    cachedBsonDocument
  }


  def toBsonSolrTuple = {
    if (toBsonDocument.isEmpty || toSolrDocument.isEmpty) {
      throw new Exception(ent_seq.toString + " is bad")
    }

    toBsonDocument.get -> toSolrDocument.get
  }
}
