# Robert Juall
# CSCI 330
# Prof. Hill
# Information Retrieval
# December 5, 2017

import os
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import FancyAnalyzer
from whoosh import index


# Function takes the folder name as input (no punctuation)
#  and indexes all the text files within.
# Running this function will ERASE any existing index.
def create_index(docfolder):

    # The schema for this index only has 2 fields:
    #  The filename for the document
    #  The body text of the document
    schema = Schema(
        docname=ID(stored=True),
        # The analyzer for this index includes:
        #  A stop word filter
        #  A regex tokenizer
        #  A minimum word size of 2
        #  SEE http://whoosh.readthedocs.io/en/latest/api/analysis.html#whoosh.analysis.FancyAnalyzer
        text=TEXT(analyzer=FancyAnalyzer())
    )

    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    # This command will erase any existing index at indexdir/
    ix = index.create_in("indexdir", schema)

    writer = ix.writer()

    # Iterate through the docs in the docfolder
    #  and read the body text into the search index
    for filename in os.listdir(docfolder):
        with open(docfolder + '/' + filename, 'r') as file:
            writer.add_document(docname=filename, text=file.read())
    writer.commit()

    print("Index Created!")

    return
