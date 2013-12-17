import itertools
import functools
import os
from collections import defaultdict

'''
Allows storage of elements in a matrix-like structure. The elements are accessed
by "coordinates". Each element can be added to. By default elements contain a list
to which values are added.

It is possible to get whole "column" or "rows" by specifying None as one of the coordinates
'''
class AppendableMatrix:
    def __init__(self, xAxisCls, yAxisCls, elemCls = list):
        self.matrix = defaultdict(elemCls)
        self.eleCls = elemCls
        self.xAxisCls = xAxisCls
        self.yAxisCls = yAxisCls


    def AppendAt(self, xCoord, yCoord, val):
        coord = (xCoord, yCoord)
        self.matrix[coord].append(val)

    def GetAt(self, xCoord, yCoord):
        if xCoord != self.xAxisCls and yCoord != self.yAxisCls:
            return self.matrix.get((xCoord, yCoord))

        if xCoord == self.xAxisCls:
            return {k:self.matrix[k] for k in self.matrix.keys() if k[1] == yCoord}

        if yCoord == self.yAxisCls:
            return {k:self.matrix[k] for k in self.matrix.keys() if k[0] == xCoord}

    def __str__(self):
        retString = ""
        xAxis = {k[0] for k in self.matrix.keys()}
        yAxis = {k[1] for k in self.matrix.keys()}
        
        rowHeaderWidth = max((len(s) for s in yAxis))
        

        colWidths = {}
        for col in xAxis:
            colWidths[col] = max(len(col), max((len(val) for val in self.GetAt(col, self.yAxisCls).values())))
                
        retString += " " * (1 + rowHeaderWidth)
        for col in xAxis:
            retString += "|" + str(col) + " " * (colWidths[col] - len(col))

        retString += "|" +  os.linesep


        for row in yAxis:
            retString += "|" + str(row) + " " * (rowHeaderWidth - len(row))
            for col in xAxis:
                currItem = self.GetAt(col, row)
                if currItem:
                    retString += "|" + str(currItem) + " " * (colWidths[col] - len(currItem))
    
            retString += "|" + os.linesep

        return retString


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
    
