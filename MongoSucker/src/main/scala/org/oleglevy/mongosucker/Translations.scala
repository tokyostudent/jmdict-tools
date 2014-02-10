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
{jmNonJapanese:
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

/*
KEleTranslation example 1:
One exactly matching keb, one reb, one sense
Looking for "悪衣"
{
  "jmKeb": {
    "1151400": {
      "senseGroups": [
        [
          {
            "pos": [
              "n"
            ],
            "glosses": [
              "shabby clothes"
            ]
          }
        ]
      ],
      "pronunciations": [
        {
          "p": "あくい"
        }
      ],
      "words": [
        {
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            0
          ],
          "writing": [
            {
              "w": "悪衣"
            }
          ]
        }
      ]
    }
  }
}

KEleTranslation example 2: (ent_seq == 1205480)
One exactly matching keb (out of one), TWO rebs (out of two) (no restrictions), one sense
{
  "jmKeb": {
    "1205480": {
      "senseGroups": [
        [
          {
            "pos": [
              "n",
              "vs"
            ],
            "glosses": [
              "rating",
              "classification",
              "allocation",
              "grading"
            ]
          }
        ]
      ],
      "pronunciations": [
        {
          "p": "かくづけ",
          "pri": [
            "news1",
            "nf18"
          ]
        },
        {
          "p": "かくずけ",
          "inf": [
            "ik"
          ]
        }
      ],
      "words": [
        {
          "writing": [
            {
              "w": "格付け",
              "pri": [
                "news1",
                "nf18"
              ]
            }
          ],
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            0,
            1
          ]
        }
      ]
    }
  }
}

KEleTranslation example 3: (ent_seq == 1215400)
Two matching kebs (out of two) (they match because they both start with the same character),
TWO rebs (out of two) (no restrictions), one sense

{
  "jmKeb": {
    "1215400": {
      "senseGroups": [
        [
          {
            "pos": [
              "n"
            ],
            "glosses": [
              "proximity",
              "nearness",
              "soon",
              "nearby"
            ]
          }
        ]
      ],
      "pronunciations": [
        {
          "p": "まぢか",
          "pri": [
            "ichi1",
            "news1",
            "nf10"
          ]
        },
        {
          "p": "まじか",
          "inf": [
            "ik"
          ]
        }
      ],
      "words": [
        {
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            0,
            1
          ],
          "writing": [
            {
              "w": "間近",
              "pri": [
                "ichi1",
                "news1",
                "nf10"
              ]
            },
            {
              "w": "真近"
            }
          ]
        }
      ]
    }
  }
}
KEleTranslation example 4: (ent_seq == 1165500)
Three matching kebs (out of three) (they match because they both start with 一日),
two rebs (out of two) (WITH restrictions), one sense
{
  "jmKeb": {
    "1165500": {
      "senseGroups": [
        [
          {
            "pos": [
              "n",
              "n-adv"
            ],
            "glosses": [
              "all day long",
              "all the day",
              "throughout the day"
            ]
          }
        ]
      ],
      "pronunciations": [
        {
          "p": "いちにちじゅう",
          "pri": [
            "ichi1"
          ]
        },
        {
          "p": "いちにちぢゅう"
        }
      ],
      "words": [
        {
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            0,
            1
          ],
          "writing": [
            {
              "w": "一日中",
              "pri": [
                "ichi1"
              ]
            }
          ]
        },
        {
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            1
          ],
          "writing": [
            {
              "w": "一日ぢゅう"
            }
          ]
        },
        {
          "senseGroupId": 0,
          "pronunciationId": [
            0
          ],
          "writing": [
            {
              "w": "一日じゅう"
            }
          ]
        }
      ]
    }
  }
}

KEleTranslation example 5: (ent_seq == 1002960)
One matching keb (out of one), one reb (out of one) (no restrictions), three senses
{
  "jmKeb": {
    "1002960": {
      "senseGroups": [
        [
          {
            "pos": [
              "n"
            ],
            "misc": [
              "uk"
            ],
            "glosses": [
              "(one's) wife"
            ]
          },
          {
            "glosses": [
              "(someone's) wife"
            ]
          },
          {
            "glosses": [
              "landlady"
            ]
          }
        ]
      ],
      "pronunciations": [
        {
          "p": "かみさん"
        }
      ],
      "words": [
        {
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            0
          ],
          "writing": [
            {
              "上さん": null
            }
          ]
        }
      ]
    }
  }
}

KEleTranslation example 6: (ent_seq == 1283190)
Two matching keb (two of two), one reb (out of one) (no restrictions), two senses and one of them
is restricted to one keb
{
  "jmKeb": {
    "1283190": {
      "senseGroups": [
        [
          {
            "pos": [
              "adj-i"
            ],
            "glosses": [
              "high",
              "tall"
            ]
          }
        ],
        [
          {
            "glosses": [
              "expensive"
            ]
          }
        ]
      ],
      "pronunciations": [
        {
          "p": "たかい",
          "pri": [
            "ichi1",
            "news1",
            "nf08"
          ]
        }
      ],
      "words": [
        {
          "writing": [
            {
              "w": "高価い",
              "inf": [
                "iK"
              ]
            }
          ],
          "senseGroupId": [
            1
          ],
          "pronunciationId": [
            0
          ]
        },
        {
          "writing": [
            {
              "w": "高い",
              "pri": [
                "ichi1",
                "news1",
                "nf08"
              ]
            }
          ],
          "senseGroupId": [
            0
          ],
          "pronunciationId": [
            0
          ]
        }
      ]
    }
  }
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