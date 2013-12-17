# -*- coding: shift-jis -*-

import unittest
from jmdict import JmDict, KanjiReading, LookupResult, Sense, SenseGroup, EntryMatrix

from unittest.mock import MagicMock, Mock
import testdictionaryentries
import deep
from printr import printr
from testdictionaryentries import results as TEST_DATA


class TestLookup(unittest.TestCase):
    def createMongoDb(self, returnValue):
        mongoDb = MagicMock()
        mongoDb.find = Mock(return_value=returnValue)

        return mongoDb

    def setUp(self):
        print(self._testMethodName)

        self.TEST_DATA = TEST_DATA[self._testMethodName.split("_")[0]]
        self.JM_DICT = JmDict(self.createMongoDb(self.TEST_DATA))

        return super().setUp()

    def SENSE(self, senseIndex = -1, resultIndex = 0, **args):
        if -1 == senseIndex:
            return self.TEST_DATA[resultIndex]["sense"]
        else:
            return self.TEST_DATA[resultIndex]["sense"][senseIndex]


    def K_ELE(self, kEleIndex = -1, resultIndex = 0, **args):
        if -1 == kEleIndex:
            return self.TEST_DATA[resultIndex]["k_ele"]
        else:
            return self.TEST_DATA[resultIndex]["k_ele"][kEleIndex]

    def KEB(self, kEleIndex = 0, **args):
        return self.K_ELE(kEleIndex, **args)["keb"]

    def R_ELE(self, rEleIndex = -1, resultIndex = 0, **args):
        if -1 == rEleIndex:
            return self.TEST_DATA[resultIndex]["r_ele"]
        else:
            return self.TEST_DATA[resultIndex]["k_ele"][rEleIndex]

    def REB(self, rEleIndex = 0, **args):
        return R_ELE(rEleIndex, **args)["reb"]

    def tearDown(self):
        self.assertIsNone(deep.diff(self.lookupRes, self.TESTED_LOOKUP_RESULTS, 1))
        
    def test1_0(self):
        self.lookupRes = self.JM_DICT.lookup("若しかしたら")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))
        
        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))
        self.TESTED_LOOKUP_RESULTS =    {r1}


    def test1_1(self):
        self.lookupRes = self.JM_DICT.lookup("もしかしたら")


        
        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0), [
                                                            self.R_ELE_REB(0, 0)
                                                        ]))

        self.TESTED_LOOKUP_RESULTS = {r1}
        
    def test2(self):
        self.lookupRes = self.JM_DICT.lookup("吉祥")

        
        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        
        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0),
                                                                self.R_ELE_REB(0, 1)
                                                            ]))
        self.TESTED_LOOKUP_RESULTS = {r1}

    def test3_0(self):
        self.lookupRes = self.JM_DICT.lookup("羽撃く")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}

    def test3_1(self):
        self.lookupRes = self.JM_DICT.lookup("羽ばたく")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 1),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}


    def test4_0(self):
        self.lookupRes = self.JM_DICT.lookup("地学")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}

    def test4_1(self):
        self.lookupRes = self.JM_DICT.lookup("地球科学")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 1),    [
                                                                self.R_ELE_REB(0, 1)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}


    def test4_2(self):
        self.lookupRes = self.JM_DICT.lookup("ちがく")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}

    def test5_0(self):
        self.lookupRes = self.JM_DICT.lookup("あっと言う間に")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0),
                                                                self.R_ELE_REB(0, 1)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}


    def test5_1(self):
        self.lookupRes = self.JM_DICT.lookup("あっというまに")

        
        r1 = LookupResult(SenseGroup([
                                    Sense(self.SENSE(0, 0))
                                ]))


        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0),
                                                                self.R_ELE_REB(0, 1)
                                                            ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 1),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS =    {r1}

    def test6_0(self):
        self.lookupRes = self.JM_DICT.lookup("生う")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0)),
                                            Sense(self.SENSE(0, 1))
                                        ]))

        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0)
                                                            ]))

        self.TESTED_LOOKUP_RESULTS = {r1}


    def test7_0(self):
        self.lookupRes = self.JM_DICT.lookup("でっぱな")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0)),
                                            Sense(self.SENSE(0, 1))
                                        ]))


        r1.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0),
                                                                self.R_ELE_REB(0, 1),
                                                                self.R_ELE_REB(0, 2)
                                                            ]))

        r2 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 1))
                                        ]))

        r2.addReading(KanjiReading(self.K_ELE_KEB(0, 0),    [
                                                                self.R_ELE_REB(0, 0),
                                                                self.R_ELE_REB(0, 1),
                                                                self.R_ELE_REB(0, 2)
                                                            ]))

        r2.addReading(KanjiReading(self.K_ELE_KEB(0, 1),    [
                                                                self.R_ELE_REB(0, 0),
                                                                self.R_ELE_REB(0, 1),
                                                                self.R_ELE_REB(0, 2)
                                                            ]))

        r2.addReading(KanjiReading(self.K_ELE_KEB(0, 2),    [
                                                                self.R_ELE_REB(0, 2)
                                                            ]))

        r2.addReading(KanjiReading(self.K_ELE_KEB(0, 3),    [
                                                                self.R_ELE_REB(0, 2)
                                                            ]))
        
        self.TESTED_LOOKUP_RESULTS = {r1, r2}


    def test8_0(self):
        self.lookupRes = self.JM_DICT.lookup("紅葉")

        r1 = LookupResult(SenseGroup(   [
                                            Sense(self.SENSE(0, 0)),
                                            Sense(self.SENSE(0, 1))
                                        ]))


    
        pass

    def test8_1(self):
        entryMatrix = EntryMatrix(self.K_ELE(), self.R_ELE(), self.SENSE())

        pass




