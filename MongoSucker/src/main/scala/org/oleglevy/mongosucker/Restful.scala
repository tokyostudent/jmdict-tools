import akka.actor.{PoisonPill, Props, ActorSystem}
import akka.util.Timeout
import scala.concurrent.Future
import scala.util.{Failure, Success}
import spray.can.server.Stats
import spray.http.ContentTypes
import spray.httpx.marshalling.Marshaller
import spray.routing.SimpleRoutingApp
import akka.pattern.ask
import scala.concurrent.duration._
import scala.concurrent.ExecutionContext.Implicits.global
import spray.httpx.SprayJsonSupport._
import JsonMarshaller._


object JmDictRest extends SimpleRoutingApp {



  def run = {
    implicit val system = ActorSystem("jmdictrest-actors")
    implicit val timeout = Timeout(450 seconds)

    startServer("0.0.0.0", 1234) {
      path("api" / "v1" / "lookup" / Segment) {queryString =>
        parameterMap {params =>
         get {
           complete {
             val actor = system.actorOf(Props[JmDictActor])

             val lookupFuture = (actor ? LookupRequest(queryString, params)).mapTo[LookupResult]

             lookupFuture.onComplete {
               case _ => actor ! PoisonPill
             }

             lookupFuture
           }
        }
      }
   }
  }
}

}