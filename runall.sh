#!/bin/bash

# bash runall.sh

qdir="queries"
# qdir="practice_queries" # comment out to run test
queries=`ls $qdir`
corpus="book_test"
# corpus="book_practice" # comment out to run test

python little_search_rj.py -df $corpus

for f in $queries; do
	q=`basename $f .txt`
	q=`echo $q | tr "-" " "`
	echo " ================== " $q " ================== " 
	# TODO: call your program here
	python little_search_rj.py  -q "$q" -r $qdir/$f
	echo; echo
done
