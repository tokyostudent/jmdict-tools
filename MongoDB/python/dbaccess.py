from motor import MotorClient, Op
import tornado
from enum import Enum
from tornado.concurrent import Future
from time import time

class JmDictMongoDb:
    def __init__(self, dbName="jmdict", collectionName="entries", **pyMongoKwArgs):
        self.mongoClient = MotorClient().open_sync()
        self.jmEntries = self.mongoClient[dbName][collectionName]

    @property
    def entriesCollection(self):
        return self.jmEntries

    @tornado.gen.coroutine
    def cursorToList(self, cursor):
        s = time()
        res = yield Op(cursor.to_list)
        s1 = time()

        return (res, {"dbTime": s1 - s})
