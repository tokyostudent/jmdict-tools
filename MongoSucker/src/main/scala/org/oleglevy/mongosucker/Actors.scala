import akka.actor.Actor
import akka.actor.Props
import akka.event.Logging
import jp.sf.amateras.solr.scala.async.{AsyncQueryBuilder, AsyncSolrClient}
import scala.concurrent.Future
import scala.util.parsing.json.JSON
import scala.util.{Success, Failure, Try}
import akka.pattern._
import scala.concurrent.ExecutionContext.Implicits.global
import scala.async.Async.{async, await}
import spray.http.{ContentTypes, HttpEntity, ContentType}
import spray.httpx.marshalling.Marshaller
import spray.json._
import DefaultJsonProtocol._ // !!! IMPORTANT, else `convertTo` and `toJson` won't work correctly

trait PageId {
  val start:Int
  val rows:Int
  def getNext:PageId
  def toString:String
}

object PageId {
  implicit def urlPageInfoObject(urlParam:Option[String]):PageId = PageId(urlParam)

  private val _defaultPageSize = 20

  case class PageIdImpl(start:Int, rows:Int) extends PageId{
    def getNext:PageId = {
      new PageIdImpl(this.start + _defaultPageSize, this.rows)
    }

    override def toString:String = s"$start|$rows"
  }

  def apply(params:Option[String]):PageId = {
    params match {
      case None => _default
      case Some(pageIdString) =>
        Try(
          pageIdString split '|' map {_.trim.toInt} match {
            case Array(pageLength:Int, pageIndex:Int, _*) => new PageIdImpl(pageLength, pageIndex)
          }) match {
          case Failure(f) => return _default
          case Success(s) => return s
        }
    }

    _default
  }


  private val _default:PageId = new PageIdImpl(0, _defaultPageSize)
}


case class LookupRequest(q:String, pageInfo:PageId, exact:Boolean)
object LookupRequest {
  def apply(q:String, params:Map[String, String]): LookupRequest = {
    new LookupRequest(q, pageInfo = params.get("pageid"), exact = params.get("exact").nonEmpty)
  }
}


trait LookupResult

case class SuccessfulLookupResult(translations:Seq[Translation]) extends LookupResult {
}


case class FailedLookupResult(failure:Throwable) extends LookupResult {

}

class JmDictActor extends Actor {
  private def __queryBuilder(query:String, pageInfo:PageId, exact: Boolean)(solrClient:AsyncSolrClient):AsyncQueryBuilder =
  {
    val solrQuery = if (!exact) s"keb:$query OR reb:$query OR gloss:$query" else s"exact_gloss:\042$query\042"
    solrClient.query(solrQuery).start(pageInfo.start).rows(pageInfo.rows)
  }

  private def __solrFailureRecovery(throwable:Throwable) = Future {new FailedLookupResult(throwable)}

  def receive = {
    case LookupRequest(query, pageInfo, exact) => {


      val entriesFuture = Solr.select(__queryBuilder(query, pageInfo, exact))
      val dictionaryQuery = DictionaryQuery(query)

      val translationsFuture = entriesFuture.map {
        _ map {Translation(_, dictionaryQuery)}
      }  .map {_.flatten}
         .map {SuccessfulLookupResult}
         .recoverWith {case throwable => __solrFailureRecovery(throwable)}

      translationsFuture pipeTo sender


    }
  }
}