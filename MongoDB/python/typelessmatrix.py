import itertools
import functools
import os
import unicodedata

class AppendableMatrix:
    def __init__(self, elemCls = list):
        self.matrix = {}
        self.eleCls = elemCls

    def AppendAt(self, ix, val):
        if not self.matrix.get(ix):
            self.matrix[ix] = self.eleCls()

        self.matrix[ix].append(val)

    def GetAt(self, ix):
        if ix[0] is not None and ix[1] is not None:
            return self.matrix[ix]

        if ix[0] is None:
            return {k:self.matrix[k] for k in self.matrix.keys() if k[1] == ix[1]}

        if ix[1] is None:
            return {k:self.matrix[k] for k in self.matrix.keys() if k[0] == ix[0]}

    def __str__(self):
        retString = ""
        xAxis = {k[0] for k in self.matrix.keys()}
        yAxis = {k[1] for k in self.matrix.keys()}
        
        rowHeaderWidth = max((len(s) for s in yAxis))
        

        colWidths = {}
        for col in xAxis:
            colWidths[col] = max(len(col), max((len(val) for val in self.GetAt([col, None]).values())))
                
        retString += " " * (1 + rowHeaderWidth)
        for col in xAxis:
            retString += "|" + str(col) + " " * (colWidths[col] - len(col))

        retString += "|" +  os.linesep


        for row in yAxis:
            retString += "|" + str(row) + " " * (rowHeaderWidth - len(row))
            for col in xAxis:
                currItem = self.GetAt((col, row))
                retString += "|" + str(currItem) + " " * (colWidths[col] - len(currItem))
    
            retString += "|" + os.linesep

        return unicodedata.normalize("NFKD", retString)


if __name__ == "__main__":
    testMatrix = TypelessMatrix()
    rebs = ["redb1", "refdgb2", "re24jkfskb3"]
    kebs = ["kellksjdflskb1", "kesldfjlskdfslb2", "keb3"]


    for r in rebs:
        for k in kebs:
            testMatrix[(r, k)] = r + k

    t1 = testMatrix[(rebs[0], kebs[1])]
    t2 = testMatrix[(rebs[1], None)]
    t3 = testMatrix[(None, kebs[0])]

    print(testMatrix)
    
