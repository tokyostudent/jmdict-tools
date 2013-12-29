from motor import MotorClient, Op
import tornado
from enum import Enum
from tornado.concurrent import Future

class JmDictMongoDb:
    def __init__(self, dbName="jmdict", collectionName="entries", **pyMongoKwArgs):
        self.mongoClient = MotorClient().open_sync()
        self.jmEntries = self.mongoClient[dbName][collectionName]

    @tornado.gen.coroutine
    def find(self, *args):
        res = yield Op(self.jmEntries.find(*args).to_list)

        return res


