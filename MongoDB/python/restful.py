import tornado.ioloop
import tornado.web
from dbaccess import JmDictMongoDb
from querymatcher import JmDictQuery, QueryOptions
from entrymatrix import EntryMatrix
from json import dumps
from functools import reduce

class JmDictRestService(tornado.web.Application):
    def __init__(self):
        handlers =[(r"/v1/entry/(.*)", EntryRequestHandler)]

        tornado.web.Application.__init__(self, handlers)

        self.listen(1234)
        self.settings["dictQuery"] = JmDictQuery(JmDictMongoDb())

    
    def run(self):
        tornado.ioloop.IOLoop.instance().start()




class EntryRequestHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def get(self, entry_id):
        dictQuery = self.settings["dictQuery"]
        dbResults = yield dictQuery.query(entry_id, QueryOptions.exactMatch)

        restResult = {"queryRsp":[]}
        for m in (EntryMatrix(res) for res in dbResults):
            qr = m.match(lambda s: s == entry_id)
            
            for senseSet, rebkeb in qr.bySense():
                restResult["queryRsp"].append({"sense":list(map(lambda s: s.getJson(), senseSet)), "reading":rebkeb.getJsonByReb()})

        self.set_header("Content-Type", "application/json")
        self.finish(dumps(restResult))



if __name__ == "__main__":
    restService = JmDictRestService()
    restService.run()
