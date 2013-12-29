from cache import cache

class LookupQueryBuilder:
    @cache
    def limit(self):
        return 11

    @cache
    def spec(self):
        _beginsWithSpec = {"$or": [{"k_ele.keb":{"$regex": "^{0}".format(self.query)}}, {"r_ele.reb":{"$regex": "^{0}".format(self.query)}}]}
        _exactSpec = {"$or": [{"k_ele.keb":self.query}, {"r_ele.reb":self.query}]}
        _defaultSpec = _exactSpec

        if "beginsWith" in self.queryParams:
            return _beginsWithSpec

        if "exact" in self.queryParams:
            return _exactSpec

        return _defaultSpec

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
    
    def __init__(self, query, queryParams):
        self.query = query
        self.queryParams = queryParams