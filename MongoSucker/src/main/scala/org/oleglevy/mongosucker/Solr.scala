import dispatch._
import dispatch.url
import java.util
import jp.sf.amateras.solr.scala.async.{AsyncQueryBuilder, AsyncSolrClient}
import org.apache.solr.client.solrj.request.UpdateRequest
import org.apache.solr.common.SolrInputDocument
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Promise
import scala.util.Try


object Solr {
  private val _defaultSolrUrl = "http://localhost:8983/solr/jmdict"

  def updateRequest(solrDocs:util.Collection[SolrInputDocument]):Future[String] = {

    val body = new UpdateRequest().add(solrDocs).getXML

    val svc = (url(_defaultSolrUrl) / "update").POST
      .setBody(body.getBytes("UTF-8"))
      .setHeader("Content-Type", "text/xml; charset=UTF-8")


    Http(svc OK as.String)
  }

  def commitRequest:Future[Unit] = {
    val asyncSolrClient = new AsyncSolrClient(_defaultSolrUrl)
    val retFuture = asyncSolrClient.commit()
    retFuture.onComplete {r => asyncSolrClient.shutdown()}

    retFuture
  }

  def select(solrQueryMaker:AsyncSolrClient => AsyncQueryBuilder):Future[Seq[Entry]] = {
    val solrClient = new AsyncSolrClient(_defaultSolrUrl)
    val queryBuilder = solrQueryMaker(solrClient)
    val solrResultsFuture = queryBuilder.getResultAsMap()

    solrResultsFuture.onComplete {case _ => solrClient.shutdown()}

    solrResultsFuture.map {_.documents
                            .map{solrDoc => Try(Entry(solrDoc("fullEntry").toString))}
                            .filter {_.isSuccess}
                            .map{_.get}}


    }
}
