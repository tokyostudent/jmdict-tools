from pymongo import MongoClient
import xmltodict


def BuildDatabase(jmDictXml, connectionString=None):
    jmDictDatabase = MongoClient(connectionString).jmdict
    jmEntriesColl = jmDictDatabase.entries

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

    jmEntriesColl.ensure_index("r_ele.reb")
    jmEntriesColl.ensure_index("k_ele.keb")

    from bson.code import Code

    mapper = Code(open("XrefMap.js").read())

    reducer = Code(open("XrefReduce.js").read())


    jmEntriesColl.map_reduce(mapper, reducer, "xrefs")
