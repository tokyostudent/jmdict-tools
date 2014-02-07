libraryDependencies ++= Seq(
  "org.reactivemongo" %% "reactivemongo" % "0.10.0"
)

libraryDependencies += "org.scala-lang.modules" %% "scala-async" % "0.9.0-M4"

libraryDependencies += "jp.sf.amateras.solr.scala" %% "solr-scala-client" % "0.0.9"

libraryDependencies += "org.scalesxml" %% "scales-xml" % "0.4.5"

libraryDependencies += "net.databinder.dispatch" %% "dispatch-core" % "0.11.0"

libraryDependencies += "io.spray" % "spray-io" % "1.2.0"

libraryDependencies += "io.spray" % "spray-can" % "1.2.0"

libraryDependencies += "io.spray" % "spray-routing" % "1.2.0"

libraryDependencies += "io.spray" %%  "spray-json" % "1.2.5"

libraryDependencies += "com.typesafe.akka" %% "akka-actor" % "2.2.3"


resolvers += "spray repo" at "http://repo.spray.io"

resolvers += "Typesafe repository" at "http://repo.typesafe.com/typesafe/releases/"

resolvers += "amateras-repo" at "http://amateras.sourceforge.jp/mvn/"

resolvers += "Sonatype" at "http://oss.sonatype.org/content/repositories/public"

ideaExcludeFolders += ".idea"

ideaExcludeFolders += ".idea_modules"

