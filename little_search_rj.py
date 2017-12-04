# Robert Juall
# CSCI 330
# Prof. Hill
# Information Retrieval
# December 5, 2017

import argparse
from create_index import create_index
from search_corpus import search
from precision_recall import precision_recall


def main():
    parser = argparse.ArgumentParser(description='RJ\'s Little Search Engine.')
    parser.add_argument('-df', '--docfolder',
                        help='Document folder to be indexed, must contain .txt files.', required=False)
    parser.add_argument('-q', '--query',
                        help='Query string to run against the indexed files.', required=False)
    parser.add_argument('-r', '--relevant',
                        help='Text file describing the relevant file results for a specific search.', required=False)
    args = vars(parser.parse_args())

    if args['docfolder']:
        print()
        create_index(args['docfolder'])

    if args['query']:
        print()
        returned_docs = search(args['query'])
        if args['relevant']:
            print()
            precision_recall(returned_docs, args['relevant'])

    print()
    return


if __name__ == "__main__":
    main()
