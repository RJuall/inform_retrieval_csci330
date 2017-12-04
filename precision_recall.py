# Robert Juall
# CSCI 330
# Prof. Hill
# Information Retrieval
# December 5, 2017


def precision_recall(returned_docs, relevant_text):

    with open(relevant_text) as relevant_source:

        num_returned = len(returned_docs)

        if num_returned is not 0:
            relevant_documents = relevant_source.read().splitlines()
            relevant_doc_set = set()
            for item in relevant_documents:
                relevant_doc_set.add(item)

            num_relevant = len(relevant_doc_set)

            precision = (len(relevant_doc_set & returned_docs)/num_returned)
            recall = (len(relevant_doc_set & returned_docs)/num_relevant)

            print('{:10s} {:>8.1%}'.format("Precision:", precision))
            print('{:10s} {:>8.1%}'.format("Recall:", recall))

    return
