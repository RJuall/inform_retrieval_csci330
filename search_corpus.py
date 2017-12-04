# Robert Juall
# CSCI 330
# Prof. Hill
# Information Retrieval
# December 5, 2017

import whoosh.index as index
from whoosh.qparser import QueryParser
from math import ceil


def search(query):

    ix = index.open_dir("indexdir")
    corpus_size = ix.doc_count()
    max_results = ceil(0.7 * corpus_size)

    qp = QueryParser("text", schema=ix.schema)
    q = qp.parse(query, True)

    with ix.searcher() as searcher:
        results = searcher.search(q, limit=max_results)
        display_results(results)

        returned_documents = set()
        for r in results:
            returned_documents.add(r['docname'])

    return returned_documents


def display_results(results):

    search_results = results

    if search_results.is_empty is not False:
        print("Search successful!")
        iterator = 1

        for r in search_results:
            print('Result #{:1d}--> {:10s} {:35.35s} {:6s} {:6f}'
                  .format(iterator, 'Document:', r['docname'], 'Score:', r.score))
            iterator += 1
        return

    print("No results found.")

    return
