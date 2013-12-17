# -*- coding: utf-8 -*-
from appendablematrix import AppendableMatrix
from itertools import chain, groupby
from collections import defaultdict

_test6 = {
    "ent_seq" : "1183300",
    "k_ele" : [ 
        {
            "keb" : "温い",
            "ke_pri" : "ichi1"
        }, 
        {
            "keb" : "緩い"
        }, 
        {
            "keb" : "微温い"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "ぬるい",
            "re_pri" : "ichi1"
        }, 
        {
            "reb" : "ぬくい",
            "re_restr" : [ 
                "温い"
            ]
        }
    ],
    "info" : {
        "audit" : [ 
            {
                "upd_date" : "2010-08-05",
                "upd_detl" : "Entry created"
            }, 
            {
                "upd_date" : "2010-08-10",
                "upd_detl" : "Entry amended"
            }
        ]
    },
    "sense" : [ 
        {
            "stagk" : [ 
                "温い", 
                "微温い"
            ],
            "pos" : "adjective (keiyoushi)",
            "misc" : "word usually written using kana alone",
            "s_inf" : "ぬくい is primarily used in Western Japan",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "lukewarm"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "tepid"
                }
            ]
        }, 
        {
            "stagr" : [ 
                "ぬるい"
            ],
            "xref" : [ 
                "緩い・ゆるい・1"
            ],
            "misc" : "word usually written using kana alone",
            "gloss" : {
                "@xml:lang" : "eng",
                "#text" : "lenient"
            }
        }, 
        {
            "stagr" : [ 
                "ぬくい"
            ],
            "xref" : [ 
                "温"
            ],
            "misc" : [ 
                "word usually written using kana alone", 
                "archaism"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "slow"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "stupid"
                }]
        }
    ]
}

_test7 = {
    "ent_seq" : "1391700",
    "k_ele" : [ 
        {
            "keb" : "旋風",
            "ke_pri" : [ 
                "news1", 
                "nf14"
            ]
        }, 
        {
            "keb" : "辻風"
        }, 
        {
            "keb" : "つむじ風"
        }, 
        {
            "keb" : "つじ風"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "せんぷう",
            "re_restr" : [ 
                "旋風"
            ],
            "re_pri" : [ 
                "news1", 
                "nf14"
            ]
        }, 
        {
            "reb" : "つむじかぜ",
            "re_restr" : [ 
                "旋風", 
                "つむじ風"
            ]
        }, 
        {
            "reb" : "つじかぜ",
            "re_restr" : [ 
                "旋風", 
                "辻風", 
                "つじ風"
            ]
        }
    ],
    "sense" : [ 
        {
            "pos" : "noun (common) (futsuumeishi)",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "whirlwind"
                }
            ]
        }, 
        {
            "stagr" : [ 
                "せんぷう"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "commotion"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "sensation"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "hullabaloo"
                }
            ]
        }
    ]
}

_test8 = {
    "ent_seq" : "1583140",
    "k_ele" : [ 
        {
            "keb" : "鳩尾"
        }, 
        {
            "keb" : "水落ち"
        }, 
        {
            "keb" : "水落"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "みずおち"
        }, 
        {
            "reb" : "みぞおち"
        }
    ],
    "sense" : [ 
        {
            "pos" : "noun (common) (futsuumeishi)",
            "misc" : "word usually written using kana alone",
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "pit of the stomach"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "solar plexus"
                }
            ]
        }, 
        {
            "stagk" : [ 
                "水落ち", 
                "水落"
            ],
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "place where water falls"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "[anat.] hartkuil"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "hartput"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "maagkuil"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "zonnevlecht"
                }, 
                {
                    "@xml:lang" : "dut",
                    "#text" : "plexus solaris"
                }, 
                {
                    "@xml:lang" : "ger",
                    "#text" : "(n) Mizuochi"
                }
            ]
        }
    ]
}


class cache(object):    
    '''Computes attribute value and caches it in the instance.
    Python Cookbook (Denis Otkidach) http://stackoverflow.com/users/168352/denis-otkidach
    This decorator allows you to create a property which can be computed once and
    accessed many times. Sort of like memoization.

    '''
    def __init__(self, method, name=None):
        # record the unbound-method and the name
        self.method = method
        self.name = name or method.__name__
        self.__doc__ = method.__doc__
    def __get__(self, inst, cls):
        # self: <__main__.cache object at 0xb781340c>
        # inst: <__main__.Foo object at 0xb781348c>
        # cls: <class '__main__.Foo'>       
        if inst is None:
            # instance attribute accessed on class, return self
            # You get here if you write `Foo.bar`
            return self
        # compute, cache and return the instance's attribute value
        result = self.method(inst)
        # setattr redefines the instance's attribute so this doesn't get called again
        setattr(inst, self.name, result)
        return result

class RawElem:
    maxLength = 20
    def __init__(self, rawElem):
        self._raw = rawElem
        self._hash = str(self._raw).__hash__()

    def __str__(self):
        return str(self.raw)[:RawElem.maxLength]
    
    def __len__(self):
        return min(len(self.__str__()), RawElem.maxLength)

    def __hash__(self):
        return self._hash

class K_ele(RawElem):
    @cache
    def keb(self):
        return self._raw["keb"]

    @cache
    def ke_inf(self):
        return self._raw.get("ke_inf", None)

    @cache
    def ke_pri(self):
        return self._raw.get("ke_pri", None)

    def __str__(self):
        return self.keb

    def __repr__(self):
        return "K:" + self.keb
    
    def __eq__(self, other):
        if isinstance(other, K_ele):
            return self.keb == other.keb

        return NotImplemented

    __hash__ = RawElem.__hash__
    
class R_ele(RawElem):
    @cache
    def reb(self):
        return self._raw["reb"]

    @cache
    def re_pri(self):
        return self._raw.get("re_pri", None)

    @cache
    def re_restr(self):
        return self._raw.get("re_restr", [])

    @cache
    def re_nokanji(self):
        return self._raw.get("re_nokanji", False)

    @cache
    def re_inf(self):
        return self._raw.get("re_inf", None)

    def __str__(self):
        return self.reb

    def __repr__(self):
        return "R:" + self.reb

    def __eq__(self, other):
        if isinstance(other, R_ele):
            return self.reb == other.reb

        return NotImplemented

    __hash__ = RawElem.__hash__

    '''
    Returns true if the supplied keb can be read as specified by this reb. Basically
    checks against re_restr
    '''
    def isReadingFor(self, k_ele):
        if not self.re_restr: return True
        return k_ele.keb in self.re_restr

class Sense(RawElem):
    def __repr__(self):
        return self.gloss[0]['#text']

    @cache
    def gloss(self):
        tempGloss = self._raw["gloss"]
        return tempGloss if isinstance(tempGloss, list) else [tempGloss]
    @cache
    def misc(self):
        return self._raw["misc"]
    @cache
    def field(self):
        return self._raw["field"]
    @cache
    def ant(self):
        return self._raw["ant"]
    @cache
    def xref(self):
        return self._raw["xref"]
    @cache
    def pos(self):
        return self._raw.get("pos", None)
    @cache
    def stagr(self):
        return self._raw.get("stagr", [])
    @cache
    def stagk(self):
        return self._raw.get("stagk", [])
    @cache
    def example(self):
        return self._raw["example"]
    @cache
    def dial(self):
        return self._raw["dial"]
    @cache
    def lsource(self):
        return self._raw["lsource"]
    @cache
    def s_inf(self):
        return self._raw.get("s_inf", None)

    '''
    Check restrictions for sense given a keb and reb
    '''
    def isSenseFor(self, k_ele, r_ele):
        #If there are no restrictions on kebs or rebs this sense matches all kebs and rebs
        if not self.stagk and not self.stagr: return True
        
        #If there are no restrictions on rebs, but there are restrictions on kebs and given keb is one of them
        #this sense matches
        if not self.stagr and k_ele.keb in self.stagk: return True
        
        #If there are no restrictions on kebs, but there are restrictions on rebs and given reb is one of them
        #this sense matches
        if not self.stagk and r_ele.reb in self.stagr: return True
        
        #If there are restrictions on both keb and reb and they both match the sense matches
        if self.stagk and k_ele.keb in self.stagk and self.stagr and r_ele.reb in self.stagr: return True

        #In all other cases the sense doesn't match
        return False

    '''
    Serialize a sense so that it can be used in the REST API
    '''
    def getJson(self):
        groups = []
        uniquekeys = []
        keyfunc = lambda g: g["@xml:lang"]
        byLang = defaultdict(list)
        
        for k, g in groupby(sorted(self.gloss, key=keyfunc), keyfunc):
            byLang[k] = list(map(lambda g: g["#text"], g))

        return {"pos":self.pos, "gloss":byLang, "inf": self.s_inf}


class ReadingDef:
    def __init__(self):
        self.readingDefs = []

    def addReadingDef(self, readingDef):
        pass

class RebKebAssociation:
    def __repr__(self):
        return str(self.byReb) 
    
    def __init__(self, reb, keb):
        self.byReb = {}
        self.add(reb, keb)

    def add(self, reb, keb):
        if reb in self.byReb:
            self.byReb[reb] = self.byReb[reb] + (keb,)
        else:
            self.byReb[reb] = (keb,)
    
    def getByReb(self):
        return self.byReb

    def getJsonByReb(self):
        retJson = list()
        for r_ele, k_eles in self.byReb.items():
            retJson.append({"r": r_ele.reb,
                            "inf": r_ele.re_inf,
                            "k": [{k.keb:{"inf": k.ke_inf}} for k in k_eles]})
        
        return retJson
        


class QueryResult:
    def __init__(self):
        self.senseList = {}
        self.readings = []
    
    def addSense(self, sense, rebkeb):
        reb, keb = rebkeb
        frozenSense = frozenset(sense)
        if frozenSense in self.senseList:
            self.senseList[frozenSense].add(reb, keb)
        else:
            self.senseList[frozenSense] = RebKebAssociation(reb, keb)
    
    def bySense(self):
        return ((sense, rebkeb) for sense, rebkeb  in self.senseList.items())






class EntryMatrix:
    def __init__(self, entry):
        self.kEleList = [K_ele(k) for k in entry["k_ele"]]
        self.rEleList = [R_ele(r) for r in entry["r_ele"]]
        self.senseList = [Sense(s) for s in entry["sense"]]

        self.matrix = AppendableMatrix(R_ele, K_ele, list)
        #starting looping from sense makes sure that the order of senses in the
        #list is the same
        for sense in self.senseList:
            for r in self.rEleList:
                for k in self.kEleList:
                    if r.isReadingFor(k) and sense.isSenseFor(k, r):
                        self.matrix.AppendAt(r, k, sense)



    def __str__(self):
        return str(self.matrix)

    '''
    Entry matrix is usually generated as a result of query of both rebs and kebs. The matrix doesn't
    care about the actual query, it just needs to know that it matched an entry. But to get the actual
    match it needs to see if the match was on kebs or rebs. For example, 日本 and にほん will return the
    same entry. However, if the initial query was にほん the matrix needs to check against rebs and not
    kebs.
    '''
    def match(self, query):
        matchingKeleList = (k for k in self.kEleList if query(k.keb))
        matchingReleList = (r for r in self.rEleList if query(r.reb))

        #Create a dictionary {ix:sense} of all (both rebs and kebs) that match the query. Some keys could
        #be duplicates when both keb and reb matches (for example ent_seq = 1391700, when
        #querying for つじ). Those keys will be filtered out by the dictionary automatically
        allSenses = {}
        for rele in matchingReleList:
            sense = self.matrix.GetAt(rele, K_ele)
            if sense:
                allSenses.update(sense)

        for kele in matchingKeleList:
            sense = self.matrix.GetAt(R_ele, kele)
            if sense:
                allSenses.update(sense)

        #At this point we have all senses and their rebs/kebs in allSenses. Each value is
        #a list of senses and this list is what we want to return. The values are repeated
        #and we need to combined the rebs/kebs for each value
        queryResult = QueryResult()
        for rebkeb, sense in allSenses.items():
            queryResult.addSense(sense, rebkeb)


        return queryResult



if __name__ == "__main__":
#    mat = EntryMatrix(_test7)
#    stuff2Print = str(mat)
#    mat.match(lambda s: s.startswith("つじ"))

    mat = EntryMatrix(_test6)
    stuff2Print = str(mat)
    qr = mat.match(lambda s: s.startswith("温"))

    print("-" * 20)
    for sense, rebkeb in qr.bySense():
        print(sense, end="|")
        print(rebkeb)


    print("thank you drive through")
