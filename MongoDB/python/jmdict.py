# -*- coding: shift-jis -*-

from pymongo import MongoClient
from collections import defaultdict, namedtuple, Iterable
from functools import reduce
import operator
import re


class SenseGroup:
    def __init__(self, senseList):
        self._senseList = set(senseList)

    @property
    def senseList(self):
        return self._senseList
        
    def __ge__(self, other):
        return self.senseList >= other.senseList

    def __hash__(self):
        return hash(frozenset(self._senseList))
    
    def __eq__(self, b):
        return b._senseList == self._senseList






class LookupResult:
    def __init__(self, senseGroup):
        self._senseGroup = senseGroup
        self._readings = set()

    @property
    def senseGroup(self):
        return self._senseGroup

    @property
    def readings(self):
        return self._readings

    def addReading(self, reading):
        self._readings.add(reading)

    def __hash__(self):
        return hash(str(hash(self.senseGroup)) + str(hash(frozenset(self.readings))))

    def __eq__(self, b):
        return b.senseGroup == self.senseGroup and b.readings == self.readings



class Sense:
    def __init__(self, sense):
        self._sense = sense

    @property
    def sense(self):
        return self._sense

    @sense.setter
    def sense(self, value):
        self._sense = value

    def __hash__(self):
        return hash(str(self._sense))
    
    def __eq__(self, b):
        return b.sense == self.sense


class KanjiReading:
    def __init__(self, keb, rebs):
        self._keb, self._rebs = keb, frozenset(rebs)

    @property
    def keb(self):
        return self._keb;

    @property
    def rebs(self):
        return self._rebs;

    def __hash__(self):
        return hash(str(hash(self._keb)) + str(hash(self._rebs)))

    def __eq__(self, other):
        return self.keb == other.keb and self.rebs == other.rebs

class MongoDb:
    def __init__(self, mongoDbConnection=None):
        self.jmEntries = MongoClient(mongoDbConnection).jmdict.entries

    def find(self, query):
        return self.jmEntries.find(query)

class JmDict:
    def __init__(self, db):
        self.db = db

    def generateEntries(self, reQuery, mongoResults):
        returnSet = set()
        for jmEntry in mongoResults:
            toYield = []
            senseGroups = set()

            for k_ele, keb in [(k_ele, k_ele["keb"]) for k_ele in jmEntry["k_ele"] if reQuery.search(k_ele["keb"])]:
                singleRes = {   "keb":      keb,
                                "sense":    set(),
                                "reb":      [r_ele["reb"] for r_ele in jmEntry["r_ele"]
                                                if  "re_restr" not in r_ele or
                                                    "re_restr" in r_ele and keb in r_ele["re_restr"]]}

                singleRes["sense"] = SenseGroup(Sense(sense) for sense in jmEntry["sense"] if
                                                    "stagk" not in sense or
                                                    "stagk" in sense and keb in sense["stagk"] or
                                                    "stagr" in sense and set(sense["stagr"]) & set(singleRes["reb"]))

                toYield.append(singleRes)
                senseGroups.add(singleRes["sense"])

            for r_ele, reb in [(r_ele, r_ele["reb"]) for r_ele in jmEntry["r_ele"] if reQuery.search(r_ele["reb"])]:
                kebsToReturn = [(k_ele, k_ele["keb"]) for k_ele in jmEntry["k_ele"] if k_ele["keb"] in r_ele["re_restr"]]\
                                if "re_restr" in r_ele\
                                else [(k_ele, k_ele["keb"]) for k_ele in jmEntry["k_ele"]]

                for k_ele, keb in kebsToReturn:
                    singleRes = {   "keb":      keb,
                                    "sense":    SenseGroup(Sense(sense) for sense in jmEntry["sense"] if
                                                        ("stagk" not in sense) or
                                                        ("stagk" in sense and keb in sense["stagk"]) or
                                                        ("stagr" in sense and set(sense["stagr"]) & set(singleRes["reb"]))),
                                    "reb":    [r_ele["reb"] for r_ele in jmEntry["r_ele"]
                                                if  "re_restr" not in r_ele or
                                                    "re_restr" in r_ele and keb in r_ele["re_restr"]]}

                    toYield.append(singleRes)
                    senseGroups.add(singleRes["sense"])


            for sg in senseGroups:
                nextResult = LookupResult(sg)
                for y in toYield:
                    if y["sense"] >= sg:
                        nextResult.addReading(KanjiReading(y["keb"], y["reb"]))
                
                returnSet.add(nextResult)
        
        return returnSet


    def lookup(self, term):
        reQuery = re.compile("^" + term)
    
        query = {"$or": [
                    {"r_ele.reb":{"$regex": reQuery}},
                    {"k_ele.keb":{"$regex": reQuery}}]}

        return self.generateEntries(reQuery, self.db.find(query))









#1255810 seems to be interesting
#d = JmDict(MongoDb())
#r = d.lookup("月次")
#r = d.lookup("紅葉")
#r = d.lookup("黄葉")


#r = d.lookup("月並み")
#r = d.lookup("つきなみ")
#r = d.lookup("げつじ")
#r = d.lookup("叩き")

#rr = list(r)

#try:
#    print(rr)
#except UnicodeDecodeError:
#    pass
