import os
from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index


def create_index(docfolder):

    schema = Schema(
        docname=ID(stored=True),
        text=TEXT(analyzer=StemmingAnalyzer())
    )

    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    ix = index.create_in("indexdir", schema)

    writer = ix.writer()

    for filename in os.listdir(docfolder):
        with open(docfolder + '/' + filename, 'r') as file:
            writer.add_document(docname=filename, text=file.read())
    writer.commit()

    return
