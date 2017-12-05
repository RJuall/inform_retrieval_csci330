# Robert Juall
# CSCI 330
# Prof. Hill
# Information Retrieval
# December 5, 2017


# This function accepts a set object of relevant documents,
#  and a text file describing all possible relevant documents.
# The function then displays the calculated Precision & Recall
#  scores.
def precision_recall(returned_docs, relevant_text):

    # with..as.. operates as a try/catch block,
    #  does not execute if file not found
    with open(relevant_text) as relevant_source:
        num_returned = len(returned_docs)

        if num_returned is not 0:
            relevant_documents = relevant_source.read().splitlines()
            relevant_doc_set = set()
            for item in relevant_documents:
                relevant_doc_set.add(item)

            num_relevant = len(relevant_doc_set)

            # Uses set operations to find the intersections of the
            #  returned documents and all relevant documents
            precision = (len(relevant_doc_set & returned_docs)/num_returned)
            recall = (len(relevant_doc_set & returned_docs)/num_relevant)

            print('{:10s} {:>8.1%}'.format("Precision:", precision))
            print('{:10s} {:>8.1%}'.format("Recall:", recall))

    return
