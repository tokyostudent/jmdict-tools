import spray.json._
import DefaultJsonProtocol._

object JsonMarshaller {

  implicit object RicherDataModel {

    implicit class RichRele(r_ele:R_ele) {
      def partialJsList:List[(String, JsValue)] = {
        import r_ele._

        val nonEmptyFields = scala.collection.mutable.ListBuffer[JsField]()

        if (re_inf.nonEmpty)
          nonEmptyFields += new JsField("re_inf", re_inf.toJson)

        if (re_pri.nonEmpty)
          nonEmptyFields += new JsField("re_pri", re_pri.toJson)

        if (re_nokanji)
          nonEmptyFields += new JsField("nokanji", true.toJson)

        nonEmptyFields.toList
      }
    }
  }


  implicit object ReleToJson extends RootJsonFormat[R_ele] {
    def write(rele: R_ele): JsValue = {
      import rele._
      val nonEmptyFields = scala.collection.mutable.ListBuffer[JsField]()

      if (re_inf.nonEmpty)
        nonEmptyFields += new JsField("re_inf", re_inf.toJson)

      if (re_pri.nonEmpty)
        nonEmptyFields += new JsField("re_pri", re_pri.toJson)

      if (re_nokanji)
        nonEmptyFields += new JsField("nokanji", true.toJson)

      JsObject(nonEmptyFields.toList)
    }
    def read(json: JsValue): R_ele = new R_ele()
  }

  implicit object KeleSeqToJson extends RootJsonFormat[Seq[K_ele]] {
    import KeleToJson._
    def write(seqOfKele: Seq[K_ele]): JsValue = seqOfKele collect {
      case k if k.nonEmpty => k.toJson
    } match {
      case emptyColl if emptyColl.isEmpty => JsNull
      case nonEmptyColl => nonEmptyColl.toJson
    }

    def read(json: JsValue): Seq[K_ele] = Seq()
  }

  implicit object KeleToJson extends RootJsonFormat[K_ele] {
      def write(kele: K_ele): JsValue = {
        import kele._
        val nonEmptyFields = scala.collection.mutable.ListBuffer[JsField]()

        if (keb.nonEmpty)
          nonEmptyFields += new JsField("keb", keb.toJson)

        if (ke_inf.nonEmpty)
          nonEmptyFields += new JsField("inf", ke_inf.toJson)

        if (ke_pri.nonEmpty)
          nonEmptyFields += new JsField("pri", ke_pri.toJson)

        JsObject(nonEmptyFields.toList)
      }

    def read(json: JsValue): K_ele = new K_ele()
  }

  implicit object GlossToJson extends RootJsonFormat[Gloss] {
    def write(g:Gloss):JsValue = {
      g.gloss.toJson
    }

    def read(json: JsValue): Gloss = new Gloss()
  }
  implicit object SenseToJson extends RootJsonFormat[Sense] {
    def write(s:Sense): JsValue = {
      import s._

      val nonEmptyFields = scala.collection.mutable.ListBuffer[JsField]()
      if (field.nonEmpty)
        nonEmptyFields += new JsField("field", s.field.toJson)

      if (misc.nonEmpty)
        nonEmptyFields += new JsField("misc", s.misc.toJson)

      if (s_inf.nonEmpty)
        nonEmptyFields += new JsField("s_inf", s.s_inf.toJson)

      if (lsource.nonEmpty)
        nonEmptyFields += new JsField("lsource", s.lsource.toJson)

      if (dial.nonEmpty)
        nonEmptyFields += new JsField("dial", s.dial.toJson)

      if (glosses.nonEmpty)
        nonEmptyFields += new JsField("gloss", s.glosses.toJson)

      if (pos.nonEmpty)
        nonEmptyFields += new JsField("pos", s.pos.toJson)

      JsObject(nonEmptyFields.toList)
    }

    def read(json: JsValue): Sense = new Sense()
  }

  implicit object WordReadingToJson extends RootJsonFormat[WordReading] {

    def write(wr:WordReading): JsValue = {
      import wr._
      import RicherDataModel.RichRele


      val jsWord = "word" -> (if (word.nonEmpty) word.toJson else JsNull)

      JsObject(wr.reading.reb -> JsObject(wr.reading.partialJsList :+ jsWord))
    }

    def read(json: JsValue): WordReading = new WordReading()
  }

   implicit object NonJapaneseJmTranslationToJson extends RootJsonFormat[NonJapaneseJmTranslation] {
    def write(nonJap: NonJapaneseJmTranslation): JsValue = {
        import nonJap._

        val tttt = senseToReading map {
              case (listOfSenses, listOfWordReadings) => JsObject("senseGroup" -> listOfSenses.toJson,
                "reading" -> listOfWordReadings.toJson)
            }
            tttt.toJson
        }

     def read(json: JsValue): NonJapaneseJmTranslation = new NonJapaneseJmTranslation()
   }

  implicit object LookupResultToJson extends RootJsonFormat[LookupResult] {
    def write(lookupRes: LookupResult): JsValue = {
      lookupRes match {
        case SuccessfulLookupResult(seqOfTranslation) =>
          val jmNonJapanese = JsObject(seqOfTranslation.map {
            case nonJap@NonJapaneseJmTranslation(_, _) => nonJap.ent_seq.toString -> nonJap.toJson
          }.toList)

          JsObject("jmNonJapanese" -> jmNonJapanese, "stats" -> "shitload of stats".toJson)
      }
    }

    def read(json: JsValue): LookupResult = new SuccessfulLookupResult(Seq())
  }

}