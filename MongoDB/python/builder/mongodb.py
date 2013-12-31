from pymongo import MongoClient
import xmltodict
from itertools import chain


def BuildDatabase(jmDictXml, connectionString=None):
    jmDictDatabase = MongoClient(connectionString).jmdict
    jmEntriesColl = jmDictDatabase.entries

    def improveDb():
        print("Making the DB better, really... Just wait")
        totalEntries = jmEntriesColl.count()
        for i, entry in zip(range(totalEntries), jmEntriesColl.find()):
            if i % (totalEntries // 100) == 0:
                print(".", end="", flush=True)

            if i % (totalEntries // 10) == 0:
                print("|", end="", flush=True)

            if "k_ele" not in entry:
                entry["k_ele"] = list()

            if "r_ele" not in entry:
                entry["r_ele"] = list()

            kebs = (k_ele["keb"] for k_ele in entry["k_ele"])
            rebs = (r_ele["reb"] for r_ele in entry["r_ele"])
            glosses = (gloss.get("#text", None) for gloss in chain(*(sense.get("gloss", None) for sense in entry["sense"] if not None)) if not None)
        
            entry["keys"] = list(chain(kebs, rebs, glosses))
            jmEntriesColl.save(entry)


    #http://stackoverflow.com/questions/2130016/splitting-a-list-of-arbitrary-size-into-only-roughly-n-equal-parts
    def chunkify(lst,n):
        return [ lst[i::n] for i in range(n) ]

    j = open(jmDictXml, "rb")

    def normalizeLists(path, key, value):
        normalizeLists.needEnlisting = {
                         "entry" : ["sense", "k_ele", "r_ele"],
                         "sense" : ["stagk", "stagr", "pos", "xref", "ant", "field", "misc", "s_inf", "lsource", "dial", "gloss", "example"],
                         "r_ele": ["re_restr", "re_inf", "re_pri"],
                         "k_ele": ["k_inf", "ke_pri"]
                         }


        if "entry" == key:
            if int(value["ent_seq"]) % 1000 == 0:
                print(value["ent_seq"])
        
        if key in normalizeLists.needEnlisting:
            for n in normalizeLists.needEnlisting[key]:
                if n in value and not isinstance(value[n], list):
                    value[n] = [value[n]];

        return key, value

    parsed = xmltodict.parse(j, postprocessor=normalizeLists)
    chunks = chunkify(parsed["JMdict"]["entry"], 5)

    jmDictDatabase.drop_collection("entries")
    jmDictDatabase.drop_collection("xrefs")

    jmEntriesColl = jmDictDatabase.entries

    for chunk in chunks:
        jmEntriesColl.insert(chunk)

    improveDb()



#    jmEntriesColl.ensure_index("r_ele.reb")
#    jmEntriesColl.ensure_index("k_ele.keb")
    jmEntriesColl.ensure_index("keys")
    jmEntriesColl.ensure_index("[keys, ent_seq]")


    from bson.code import Code

    mapper = Code(open("XrefMap.js").read())

    reducer = Code(open("XrefReduce.js").read())


    jmEntriesColl.map_reduce(mapper, reducer, "xrefs")

    
if __name__ == "__main__":
    BuildDatabase("c:/temp/jmdict.xml")