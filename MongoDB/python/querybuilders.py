from cache import cache

class LookupQueryBuilder:
    pageSize = 9
    
    def _prepareCursor(self):
        retCursor = self.mongoDb.entriesCollection.find(self.spec)
        retCursor.sort("ent_seq")
        retCursor.limit(self.pageSize)
        
        return retCursor


    def executeCursor(self):
        cursor = self._prepareCursor()
        return self.mongoDb.cursorToList(cursor)

    def getPagingInfo(self, queryResults):
        if len(queryResults) == self.pageSize:
            pageId = queryResults[-1]["ent_seq"]
            return {"next": pageId}

        return None

    @cache
    def spec(self):
        _beginsWithSpec = {"$or": [{"k_ele.keb":{"$regex": "^{0}".format(self.query)}}, {"r_ele.reb":{"$regex": "^{0}".format(self.query)}}]}
        _exactSpec = {"$or": [{"k_ele.keb":self.query}, {"r_ele.reb":self.query}]}
        retSpec = _exactSpec

        if "beginsWith" in self.queryParams:
            retSpec = _beginsWithSpec

        if "exact" in self.queryParams:
            retSpec = _exactSpec

        #TODO: Need to make sure that this pageId is possible
        if "pageId" in self.queryParams:
            retSpec["ent_seq"] = {"$gt": self.queryParams["pageId"][0].decode("utf-8")}


        return retSpec

    @cache
    def matchFunction(self):
        def __startsWith(s):
            return s.startswith(self.query)

        def __exact(s):
            return s == self.query

        if "beginsWith" in self.queryParams:
            return __startsWith

        if "exact" in self.queryParams:
            return __exact

        return __exact
    
    def __init__(self, query, mongoDb, queryParams):
        self.query = query
        self.queryParams = queryParams
        self.mongoDb = mongoDb