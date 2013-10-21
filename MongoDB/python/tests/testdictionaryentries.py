# -*- coding: shift-jis -*-
from bson import ObjectId

_test1 = [{
    "_id" : ObjectId("524e2ad506cb1748ec60aadf"),
    "ent_seq" : "1012510",
    "k_ele" : [ 
        {
            "keb" : "�Ⴕ��������",
            "ke_pri" : "ichi1"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "������������",
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
            "keb" : "�g��"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "�������傤"
        }, 
        {
            "reb" : "�������傤"
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
            "keb" : "�H����",
            "ke_pri" : "ichi1"
        }, 
        {
            "keb" : "�H�΂���",
            "ke_pri" : [ 
                "news2", 
                "nf43"
            ]
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "�͂΂���",
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
            "keb" : "�n�w",
            "ke_pri" : [ 
                "news2", 
                "nf32"
            ]
        }, 
        {
            "keb" : "�n���Ȋw"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "������",
            "re_restr" : [ 
                "�n�w"
            ],
            "re_pri" : [ 
                "news2", 
                "nf32"
            ]
        }, 
        {
            "reb" : "�����イ������",
            "re_restr" : [ 
                "�n���Ȋw"
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
            "keb" : "�����ƌ����Ԃ�"
        }, 
        {
            "keb" : "�����Ƃ����Ԃ�"
        }, 
        {
            "keb" : "�����Ƃ䂤�Ԃ�"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "�����Ƃ����܂�",
            "re_restr" : [ 
                "�����ƌ����Ԃ�", 
                "�����Ƃ����Ԃ�"
            ]
        }, 
        {
            "reb" : "�����Ƃ䂤�܂�",
            "re_restr" : [ 
                "�����ƌ����Ԃ�", 
                "�����Ƃ䂤�Ԃ�"
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
                    "#text" : "wie mit einem Schlag (etwa: in der Zeit, in der man gerade nur <Transcr.: a> sagt�g)"
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
            "keb" : "����"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "����"
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
            "keb" : "�o�@"
        }, 
        {
            "keb" : "�o�["
        }, 
        {
            "keb" : "�o���["
        }, 
        {
            "keb" : "�o���@"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "�ł͂�",
            "re_restr" : [ 
                "�o�@", 
                "�o�["
            ]
        }, 
        {
            "reb" : "�ł΂�",
            "re_restr" : [ 
                "�o�@", 
                "�o�["
            ]
        }, 
        {
            "reb" : "�ł��ς�"
        }
    ],
    "sense" : [ 
        {
            "stagk" : "�o�@",
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

results = {"test1": _test1, "test2": _test2, "test3": _test3, "test4": _test4, "test5": _test5, "test6": _test6, "test7": _test7}