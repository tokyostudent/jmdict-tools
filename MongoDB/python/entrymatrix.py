# -*- coding: utf-8 -*-
from typelessmatrix import AppendableMatrix

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
    def __init__(self, rawElem):
        self._raw = rawElem

    def __str__(self):
        return str(self.raw)[:20]
    
    def __len__(self):
        return min(len(self.__str__()), 20)

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
        return self.keb == other.keb

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
        return self.reb == other.reb

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

    def isSenseFor(self, k_ele, r_ele):
        if not self.stagk and not self.stagr: return True
        if not self.stagr and k_ele.keb in self.stagk: return True
        if not self.stagk and k_ele.reb in self.stagr: return True
        if self.stagk and k_ele.keb in self.stagk and self.stagr and r_ele.reb in self.stagr: return True

        return False



class EntryMatrix:
    def __init__(self, entry):
        kEleList = [K_ele(k) for k in entry["k_ele"]]
        rEleList = [R_ele(r) for r in entry["r_ele"]]
        senseList = [Sense(s) for s in entry["sense"]]

        self.matrix = AppendableMatrix(list)
        for r in rEleList:
            for k in kEleList:
                for sense in senseList:
                    if r.isReadingFor(k) and sense.isSenseFor(k, r):
                        self.matrix.AppendAt((r, k), sense)



    def __str__(self):
        return str(self.matrix)

    def match(self, query):
        pass

if __name__ == "__main__":
    mat = EntryMatrix(_test8)
    stuff2Print = str(mat)

