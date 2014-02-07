import scala._
import scala.collection.mutable.ListBuffer

trait QueryMatcher {
  def matches(v:String, q:String):Boolean
}

object StartsWithQueryMatcher extends QueryMatcher {
  def matches(v:String, q:String):Boolean = v.startsWith(q)
}

trait Translation
abstract class JmTranslation(entSeq:Int) extends Translation

case class KEleTranslation(ent_seq:Int) extends JmTranslation(ent_seq)
case class REleTranslation(ent_seq:Int) extends JmTranslation(ent_seq)
case class NonJapaneseJmTranslation(ent_seq:Int = 0, senseToReading:Seq[(List[Sense], List[WordReading])] = Seq()) extends JmTranslation(ent_seq)

case class WordReading(reading:R_ele = new R_ele(), word:Seq[K_ele] = Seq())

case class EmptyTranslation() extends Translation

trait TranslationFactory {
  def apply(entry:Entry, query:DictionaryQuery):Translation
}




/*
NonJapaneseTranslation example
Lookup english word: to become dim (returns ent_seq 1011860)

In this case the translation is this (non interesting elements ommited):
{nonJapaneseTranslation:
  [
    {senseGroup: [
                  {
                    pos: [v1, vi],
                    glosses: [to become dim, to become blurred]
                  }
               ],
    reading: [
                  {
                    ぼやける: {
                                nokanji: false,
                                pri: [ichi1]
                             }
                  }
             ]
    }
  ]
}

In the next case (ent_seq: 1408680) we look for "to defeat". The sense that contains this
also has stagk. Also there are more sense, but we dont show them in the results for "to defeat". In general,
when looking English up, only a specific sense will match (in most cases at least). This is opposed to when
looking by keb or reb, because there can be several senses that match.

{nonJapaneseTranslation:
  [
    {
      senseGroup: [
                {
                  "pos": ["v5t", "vi"],
                  "glosses": ["to conquer (e.g. an enemy)", "to defeat"]
                }
               ],
      reading:  [
                {
                  "うちかつ": {
                            nokanji: false,
                            pri: ["news2", "nf38"],
                            word: [ //note that there are only two items here because there is a stagk on the sense
                                    {
                                      "打ち勝つ": {
                                                pri: ["news2", "nf38"],
                                                inf: []
                                              }
                                    },
                                    {
                                      "打勝つ": {pri: [], inf: []}
                                    }
                                  ]
                            }
                }
              ]
    }
   ]
}


 */



object NonJapaneseTranslation extends TranslationFactory {
  private object WordReading {
    def apply(wordReadingTuple:(R_ele, Seq[K_ele])):WordReading = {
      new WordReading(wordReadingTuple._1, wordReadingTuple._2)
    }
  }

    def apply(entry:Entry, query:DictionaryQuery):JmTranslation = {

      //For non-japanese translations, if one sense matches - all senses match. There is no reason
      //to hide other senses - they might help translation
      val matchedSenses = entry.sense //.filter(_.matches(query))

      val wordReadingMap = scala.collection.mutable.Map[Set[WordReading], ListBuffer[Sense]]().withDefaultValue(ListBuffer())


      matchedSenses foreach {sense =>
        val listOfWordReadings = sense.getWordReadings(entry.r_ele, entry.k_ele) map {WordReading(_)}
        wordReadingMap(listOfWordReadings.toSet) :+= sense
      }

      new NonJapaneseJmTranslation(entry.ent_seq, wordReadingMap.toSeq.map {t => (t._2.toList, t._1.toList)})
  }
}


object KEleTranslation extends TranslationFactory {
  private case class KEleTranslationImpl() extends Translation {
    def toJson: String = ""
  }

  def apply(entry:Entry, query:DictionaryQuery):Translation = {
    new KEleTranslationImpl()






  }
}

object REleTranslation extends TranslationFactory {
  private class REleTranslationImpl() extends Translation {
    def toJson: String = ""
  }

  def apply(entry:Entry, query:DictionaryQuery):Translation = {
    new REleTranslationImpl()
  }
}


object Translation {

  class EmptyTranslation extends Translation{
    def toJson: String = "really empty here"
  }
  def apply(entry:Entry, query:DictionaryQuery):Iterable[Translation] = {
    //Check which fields matched: if for some reason both sense and keb match the query
    //we handle the situation by creating translations for all types


    val kele_translations = entry.k_ele.filter(_.matches(query)) map {_ => KEleTranslation(entry, query)}

    val rele_translations = entry.r_ele.filter(_.matches(query)) map {_ => REleTranslation(entry, query)}

    val sense_translations = entry.sense.filter(_.matches(query)) map {_ => NonJapaneseTranslation(entry, query)}

    kele_translations ++ rele_translations ++ sense_translations
    }

  val empty:Translation = new EmptyTranslation
}


//case class Translation(pronunciation:R_ele, word:Seq[K_ele], translation:Seq[Sense])