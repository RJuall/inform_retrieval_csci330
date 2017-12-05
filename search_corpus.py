# Robert Juall
# CSCI 330
# Prof. Hill
# Information Retrieval
# December 5, 2017

import whoosh.index as index
from whoosh.qparser import QueryParser
from math import ceil


# This function (search) accepts a string as input,
#  searches the index for the query,
#  and calls the display_results function (below) to display
#  the results of the search along with their ranking scores
# Returns a set object with the returned file names
def search(query):

    ix = index.open_dir("indexdir")
    corpus_size = ix.doc_count()
    # This will set the maximum number of results
    #  to be displayed at 60% of the corpus size
    max_results = ceil(corpus_size * 0.6)
    qp = QueryParser("text", schema=ix.schema)
    q = qp.parse(query, normalize=True)

    with ix.searcher() as searcher:
        results = searcher.search(q, limit=max_results)
        display_results(results)

        returned_documents = set()
        for r in results:
            returned_documents.add(r['docname'])

    return returned_documents


# This function (display_results) accepts a Whoosh results object
#  and displays those results in a table format with the filename,
#  ranking score, and ranking
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
