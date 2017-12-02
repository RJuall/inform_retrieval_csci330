import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh import scoring


def search(query):

    ix = index.open_dir("indexdir")

    qp = QueryParser("text", schema=ix.schema)
    q = qp.parse(query, True)

    with ix.searcher() as searcher:
        print(list(searcher.lexicon("text")))
        results = searcher.search(q)

    print(results)

    return
