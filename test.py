import sys
import os
import argparse
import whoosh
from create_index import create_index
from search_corpus import search


def main():
    parser = argparse.ArgumentParser(description='Test File.')
    parser.add_argument('-df', '--docfolder', help='Document folder to be indexed', required=False)
    parser.add_argument('-q', '--query', help='Query string to run against the corpus', required=False)
    parser.add_argument('-r', '--relevant', help='Document showing the relevant search results', required=False)
    args = vars(parser.parse_args())

    sys.stdout.write("Testing stdout write.\n")

    sys.stdout.write("Testing command line arguments:\n")
    sys.stdout.write("This is the name of the script: " + sys.argv[0] + '\n')
    sys.stdout.write("Number of arguments: " + str(len(sys.argv)) + '\n')
    sys.stdout.write("The arguments are: " + str(sys.argv) + '\n')

    if args['docfolder']:
        sys.stdout.write("Testing file operations:\n")
        test_files = 0
        for filename in os.listdir(args['docfolder']):
            with open(args['docfolder'] + '/' + filename, 'r') as fileobj:
                sys.stdout.write(str(fileobj.readline().strip().split()[:1]) + '\n')
            test_files += 1
        sys.stdout.write("Number of files in the directory: " + str(test_files) + '\n')

        sys.stdout.write("Testing create_index:\n")
        create_index(args['docfolder'])
        sys.stdout.write("Index created!\n")

    if args['query']:
        sys.stdout.write("Testing query string:\n")
        query_terms = args['query'].split()
        print(*query_terms, sep=' ')

        sys.stdout.write("Testing search_corpus:\n")
        search(args['query'])
        sys.stdout.write("Search successful!\n")

    if args['relevant']:
        with open(args['relevant'], 'r') as relevant_file:
            sys.stdout.write("Testing relevant doc:\n")
            sys.stdout.write(relevant_file.readline())
            sys.stdout.write('\n')
    return


if __name__ == "__main__":
    main()
