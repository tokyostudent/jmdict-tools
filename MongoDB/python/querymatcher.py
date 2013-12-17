# -*- coding: shift-jis -*-
from enum import Enum
from bson import son
from entrymatrix import EntryMatrix
import tornado

class QueryOptions(Enum):
    startsWith = 1
    exactMatch = 2

class JmDictQuery:
#{ name : { $regex : '^acme', $options: 'i' } } );    
    def __init__(self, jmDb):
        self.db = jmDb

    def query(self, queryString, queryOptions):
        if queryOptions is QueryOptions.startsWith:
            query = {"$or": [{"k_ele.keb":{"$regex": "^{0}".format(queryString)}}, {"r_ele.reb":{"$regex": "^{0}".format(queryString)}}]}

        if queryOptions is QueryOptions.exactMatch:
            query = {"$or": [{"k_ele.keb":queryString}, {"r_ele.reb":queryString}]}

        return self.db.find(query)

if __name__ == "__main__":
    from dbaccess import JmDictMongoDb
    db = JmDictMongoDb()
    dictQuery = JmDictQuery(db)

    totalHits = 0
    totalNonhits = 0
    for l in open("c:/temp/dict.txt", encoding="utf-8"):
        q = l.split("（")[0]
        queryRes = list(dictQuery.query(q, QueryOptions.exactMatch))
        if len(queryRes):
            try:
                pass
#                print(queryRes)
            except:
                pass
            totalHits = totalHits + 1
            for m in (EntryMatrix(m) for m in queryRes):
                qr = m.match(lambda s: s == q)
                for sense, rebkeb in qr.bySenseThenByReb():
                    str(sense)
                    str(rebkeb)
#                    print(sense, end="|")
#                    print(rebkeb)

        else:
            totalNonhits = totalNonhits +1

    tornado.ioloop.IOLoop.instance().start()

    print("hits: " + str(totalHits))
    print("nonhits: " + str(totalNonhits))
#    input()
    
    
    queryRes = dictQuery.query("日", QueryOptions.startsWith)

    print(queryRes.count())

    

    print(queryRes)


