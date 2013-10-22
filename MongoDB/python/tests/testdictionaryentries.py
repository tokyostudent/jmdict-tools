# -*- coding: shift-jis -*-
from bson import ObjectId

_test1 = [{
    "_id" : ObjectId("524e2ad506cb1748ec60aadf"),
    "ent_seq" : "1012510",
    "k_ele" : [ 
        {
            "keb" : "若しかしたら",
            "ke_pri" : "ichi1"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "もしかしたら",
            "re_pri" : "ichi1"
        }
    ],
    "sense" : [ 
        {
            "pos" : [ 
                "Expressions (phrases, clauses, etc.)", 
                "adverb (fukushi)"
            ],
            "misc" : "word usually written using kana alone",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "perhaps"
                }, 
            ]
        }
    ]
}]

_test2 = [{
    "_id" : ObjectId("524e2ad506cb1748ec60baae"),
    "ent_seq" : "1226300",
    "k_ele" : [ 
        {
            "keb" : "吉祥"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "きっしょう"
        }, 
        {
            "reb" : "きちじょう"
        }
    ],
    "sense" : [ 
        {
            "pos" : "noun (common) (futsuumeishi)",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "lucky omen"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "happy"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "auspicious"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "bon pr?sage"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) gutes Omen"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "gl?ckverhei?endes Vorzeichen"
                }
            ]
        }
    ]
}]

_test3 = [{
    "_id" : ObjectId("524e2ad506cb1748ec60b68c"),
    "ent_seq" : "1171690",
    "k_ele" : [ 
        {
            "keb" : "羽撃く",
            "ke_pri" : "ichi1"
        }, 
        {
            "keb" : "羽ばたく",
            "ke_pri" : [ 
                "news2", 
                "nf43"
            ]
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "はばたく",
            "re_pri" : [ 
                "ichi1", 
                "news2", 
                "nf43"
            ]
        }
    ],
    "sense" : [ 
        {
            "pos" : [ 
                "Godan verb with `ku' ending", 
                "intransitive verb"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "to flap (wings)"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "klapwieken"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "fladderen"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "klapperen"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "klappen"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "flapperen"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "flappen"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "battre (des ailes)"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) mit den Fl?geln schlagen"
                }
            ]
        }
    ]
}]

_test4 = [{
    "_id" : ObjectId("524e2ad506cb1748ec60d91b"),
    "ent_seq" : "1628400",
    "k_ele" : [ 
        {
            "keb" : "地学",
            "ke_pri" : [ 
                "news2", 
                "nf32"
            ]
        }, 
        {
            "keb" : "地球科学"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "ちがく",
            "re_restr" : [ 
                "地学"
            ],
            "re_pri" : [ 
                "news2", 
                "nf32"
            ]
        }, 
        {
            "reb" : "ちきゅうかがく",
            "re_restr" : [ 
                "地球科学"
            ]
        }
    ],
    "sense" : [ 
        {
            "pos" : "noun (common) (futsuumeishi)",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "earth sciences (geology, mineralogy, petrology, geophysics, geochemistry, seismology, etc.)"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "aardwetenschap(pen)"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "geowetenschap(pen)"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) Geowissenschaften"
                }
            ]
        }
    ]
}]

_test5 = [{
    "_id" : ObjectId("524e2ae006cb1748ec6230f8"),
    "ent_seq" : "1000390",
    "k_ele" : [ 
        {
            "keb" : "あっと言う間に"
        }, 
        {
            "keb" : "あっという間に"
        }, 
        {
            "keb" : "あっとゆう間に"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "あっというまに",
            "re_restr" : [ 
                "あっと言う間に", 
                "あっという間に"
            ]
        }, 
        {
            "reb" : "あっとゆうまに",
            "re_restr" : [ 
                "あっと言う間に", 
                "あっとゆう間に"
            ]
        }
    ],
    "info" : {
        "audit" : [ 
            {
                "upd_date" : "2012-06-13",
                "upd_detl" : "Entry created"
            }, 
            {
                "upd_date" : "2012-06-13",
                "upd_detl" : "Entry amended"
            }
        ]
    },
    "sense" : [ 
        {
            "pos" : "Expressions (phrases, clauses, etc.)",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "just like that"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "in the twinkling of an eye"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "in the blink of an eye"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "in the time it takes to say \"ah!\""
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) im Nu"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "im Handumdrehen"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "in einem Augenblick"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "wie mit einem Schlag (etwa: in der Zeit, in der man gerade nur <Transcr.: a> sagt“)"
                }
            ]
        }
    ]
}]

_test6 = [{
    "_id" : ObjectId("524e2ad506cb1748ec60c643"),
    "ent_seq" : "1378480",
    "k_ele" : [ 
        {
            "keb" : "生う"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "おう"
        }
    ],
    "info" : {
        "audit" : [ 
            {
                "upd_date" : "2012-06-19",
                "upd_detl" : "Entry created"
            }, 
            {
                "upd_date" : "2012-06-19",
                "upd_detl" : "Entry amended"
            }
        ]
    },
    "sense" : [ 
        {
            "pos" : [ 
                "Godan verb with `u' ending", 
                "transitive verb"
            ],
            "misc" : "archaism",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "to grow"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "to spring up"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "grandir"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "pousser"
                }
            ]
        }, 
        {
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "to cut (teeth)"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "faire ses dents"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) wachsen"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "wachsen lassen"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "z?chten"
                }
            ]
        }
    ]
}]

_test7 = [{
    "_id" : ObjectId("524e2add06cb1748ec61da25"),
    "ent_seq" : "1580140",
    "k_ele" : [ 
        {
            "keb" : "出鼻"
        }, 
        {
            "keb" : "出端"
        }, 
        {
            "keb" : "出っ端"
        }, 
        {
            "keb" : "出っ鼻"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "ではな",
            "re_restr" : [ 
                "出鼻", 
                "出端"
            ]
        }, 
        {
            "reb" : "でばな",
            "re_restr" : [ 
                "出鼻", 
                "出端"
            ]
        }, 
        {
            "reb" : "でっぱな"
        }
    ],
    "sense" : [ 
        {
            "stagk" : "出鼻",
            "pos" : "noun (common) (futsuumeishi)",
            "gloss" : {
                "@xml:lang" : "eng",
                "#text" : "projecting part (of a headland, etc.)"
            }
        }, 
        {
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "outset"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "moment of departure"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "beginning of work"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "starting out"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) vorstehender Teil (eines Berges od. einer Landspitze etc.)"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "Beginn"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "Anfang"
                }
            ]
        }
    ]
}]

_test8 = [{
    "_id" : ObjectId("5265eccb06cb171d605e3df4"),
    "ent_seq" : "1578780",
    "k_ele" : [ 
        {
            "keb" : "紅葉",
            "ke_pri" : [ 
                "ichi1", 
                "news1", 
                "nf16"
            ]
        }, 
        {
            "keb" : "黄葉"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "こうよう",
            "re_pri" : [ 
                "ichi1", 
                "news1", 
                "nf16"
            ]
        }, 
        {
            "reb" : "もみじ",
            "re_pri" : "ichi1"
        }
    ],
    "sense" : [ 
        {
            "pos" : [ 
                "noun (common) (futsuumeishi)", 
                "noun or participle which takes the aux. verb suru"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "autumn colours"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "fall colors"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "leaves changing color (colour)"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "?rable"
                }, 
                {
                    "@xml:lang" : "fre",
                    "#text" : "couleurs d'automne"
                }
            ]
        }, 
        {
            "stagk" : [ 
                "紅葉"
            ],
            "stagr" : [ 
                "こうよう"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "leaves turning red"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "red leaves"
                }
            ]
        }, 
        {
            "stagk" : [ 
                "黄葉"
            ],
            "stagr" : [ 
                "こうよう"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "leaves turning yellow"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "yellow leaves"
                }
            ]
        }, 
        {
            "stagr" : [ 
                "もみじ"
            ],
            "pos" : "noun (common) (futsuumeishi)",
            "xref" : [ 
                "以呂波紅葉"
            ],
            "gloss" : {
                "@xml:lang" : "eng",
                "#text" : "(Japanese) maple (Acer japonicum)"
            }
        }, 
        {
            "stagr" : [ 
                "もみじ"
            ],
            "misc" : "colloquialism",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "venison"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "najaarskleuring"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "bontgekleurde herfstbladeren"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "herfstkleurige bladeren"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "herfstloof"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "rode bladeren"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "gele bladeren"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) rote Bl?tter"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "buntes Herbstlaub"
                }
            ]
        }
    ]
}]

results = {"test1": _test1, "test2": _test2, "test3": _test3, "test4": _test4,
           "test5": _test5, "test6": _test6, "test7": _test7, "test8": _test8
           }