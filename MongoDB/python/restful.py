import tornado.ioloop
import tornado.web
from dbaccess import JmDictMongoDb
from querymatcher import JmDictQuery, QueryOptions, DetailLevel
from entrymatrix import EntryMatrix
from json import dumps
from functools import reduce
from time import time

class JmDictRestService(tornado.web.Application):
    def __init__(self):
        handlers =[(r"/v1/lookup/(.*)", LookupRequestHandler)]

        tornado.web.Application.__init__(self, handlers, gzip=True)

        self.listen(1234)
        self.settings["dictQuery"] = JmDictQuery(JmDictMongoDb())

    
    def run(self):
        tornado.ioloop.IOLoop.instance().start()




class LookupRequestHandler(tornado.web.RequestHandler):
    matchTypes = {"exact": QueryOptions.exactMatch, "startsWith": QueryOptions.startsWith}
    detailLevels = {"minimal": DetailLevel.minimal, "all": DetailLevel.all}

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def get(self, lookupItem):
        dictQuery = self.settings["dictQuery"]

        matchType = self.matchTypes.get(self.get_argument("matchOptions", default="exact"))
        detailLevel = self.detailLevels.get(self.get_argument("detailLevel", default="minimal"))
        matchFunction = {QueryOptions.exactMatch: lambda s: s == lookupItem,
                         QueryOptions.startsWith: lambda s: s.startswith(lookupItem)}[matchType]
        
        s = time()
        dbResults = yield dictQuery.query(lookupItem, matchType, detailLevel)
        s1 = time()


        restResult = {"queryRsp":[], "dbTime": s1 - s}
        for m in (EntryMatrix(res) for res in dbResults):
            qr = m.match(matchFunction)
            
            for senseSet, rebkeb in qr.bySense():
                restResult["queryRsp"].append({"sense":list(map(lambda s: s.getJson(), senseSet)), "reading":rebkeb.getJsonByReb()})

        self.set_header("Content-Type", "application/json")
        self.finish(dumps(restResult))



if __name__ == "__main__":
    restService = JmDictRestService()
    restService.run()
