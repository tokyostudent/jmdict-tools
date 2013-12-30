import tornado.ioloop
import tornado.web
from dbaccess import JmDictMongoDb
from entrymatrix import EntryMatrix
from json import dumps
from functools import reduce
from querybuilders import LookupQueryBuilder
from time import time

class JmDictRestService(tornado.web.Application):
    def __init__(self):
        handlers =[(r"/v1/lookup/(.*)", LookupRequestHandler)]

        tornado.web.Application.__init__(self, handlers, gzip=True)

        self.listen(1234)
        self.settings["jmDictMongoDb"] = JmDictMongoDb()

    
    def run(self):
        tornado.ioloop.IOLoop.instance().start()




class LookupRequestHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def get(self, lookupItem):
        #Create the bestest query spec from all available REST parameters
        #This also builds the mongo cursor and applies sort(), limit(), etc...
        queryBuilder = LookupQueryBuilder(lookupItem, self.settings["jmDictMongoDb"], self.request.arguments)

        dbResults, findStats = yield queryBuilder.executeCursor()

        #Use the bestest query to get all the entries from the DB
        #dbResults, findStats = yield self.settings["jmDictMongoDb"].find(queryBuilder.spec, limit=queryBuilder.limit)

        #Create the response
        restResult = {"queryRsp":[], "statistics": findStats}
        for entryMatrix in (EntryMatrix(res) for res in dbResults):
            for senseSet, rebkeb in entryMatrix.match(queryBuilder.matchFunction).bySense():
                restResult["queryRsp"].append({"sense":list(map(lambda s: s.getJson(), senseSet)),
                                               "reading":rebkeb.getJsonByReb()})

        pagingInfo = queryBuilder.getPagingInfo(dbResults)
        if pagingInfo:
            restResult["page"] = pagingInfo

        

        self.set_header("Content-Type", "application/json")
        self.finish(dumps(restResult))



if __name__ == "__main__":
    restService = JmDictRestService()
    restService.run()
