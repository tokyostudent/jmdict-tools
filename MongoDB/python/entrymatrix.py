# -*- coding: utf-8 -*-
from appendablematrix import AppendableMatrix
from itertools import chain
from collections import defaultdict

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

    def __str__(self):
        return str(self.raw)[:RawElem.maxLength]
    
    def __len__(self):
        return min(len(self.__str__()), RawElem.maxLength)

    def __hash__(self):
        return str(self._raw).__hash__()

class K_ele(RawElem):
    @cache
    def keb(self):
        return self._raw["keb"]

    @cache
    def ke_inf(self):
        return self._raw["ke_inf"]

    @cache
    def ke_pri(self):
        return self._raw["ke_pri"]

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
        return self._raw["re_pri"]

    @cache
    def re_restr(self):
        return self._raw.get("re_restr", [])

    @cache
    def re_nokanji(self):
        return self._raw.get("re_nokanji", False)

    @cache
    def re_inf(self):
        return self._raw["re_inf"]

    def __str__(self):
        return self.reb

    def __repr__(self):
        return "R:" + self.reb

    def __eq__(self, other):
        print("eq: " + str(self) + " to " + str(other))
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
        return self._raw["gloss"]
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
        return self._raw["pos"]
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
        return self._raw["s_inf"]

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
        matchingKeleList = [k for k in self.kEleList if query(k.keb)]
        matchingReleList = [r for r in self.rEleList if query(r.reb)]

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
        invertedSenses = defaultdict(list)
        for rebkeb, sense in allSenses.items():
            invertedSenses[frozenset(sense)].append(rebkeb)


        print(allSenses)



if __name__ == "__main__":
    rele = R_ele({"reb":"sdflkjslkf"})
    print(rele == "sfsfsf")


    mat = EntryMatrix(_test7)
    stuff2Print = str(mat)
    mat.match(lambda s: s.startswith("つじ"))

