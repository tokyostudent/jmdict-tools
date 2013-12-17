from unittest import TestCase
from entrymatrix import EntryMatrix
'''
No restrictions
All senses are available for all keb/reb combinations
'''
test1 = {
    "k_ele" : [ 
        {
            "keb" : "keb1"
        }, 
        {
            "keb" : "keb2"
        }
    ],
    "r_ele" : [ 
        {
            "reb" : "reb1"
        }, 
        {
            "reb" : "reb2"
        }
    ],
    "sense" : [ 
        {
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "gloss1"
                }, 
                {
                    "@xml:lang" : "eng",
                    "#text" : "gloss2"
                }
            ]
        }, 
        {
            "gloss" : [ 
                {
                    "@xml:lang" : "eng",
                    "#text" : "gloss3"
                }
            ]
        }
    ]
}

class SyntheticsTests(TestCase):
    def test1(self):
        mat = EntryMatrix(test1)
        print(mat)

