# Team Googolplex
# October 26th, 2018
import csv
import sys
from builtins import input

import whoosh
from whoosh import index
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser


# Input is document ID and query
# d = document ID
# Q = query

def search(indexer, searchTerm):
    with indexer.searcher() as searcher:
        query = MultifieldParser(['Name', 'Location', 'Type'], schema=indexer.schema) #Search fields in Schema
        query = query.parse(searchTerm) #Parse to find search term
        results = searcher.search(query, limit=None) #Store search results
        print("Length of results: " + str(len(results))) # Number of results
        top_results = 1
        for line in results:
            if top_results == 11:
                break
            else:
                print(top_results, line['Name'], line['Size'], line['Location'], line['Type']) #Prints out only these attributes
                top_results += 1 
            


def index():
    schema = Schema(id=ID(stored=True), Name=TEXT(stored=True), Size=TEXT(stored=True), Location=TEXT(
        stored=True), Longitude=TEXT(stored=True), Latitude=TEXT(stored=True), Image=TEXT(stored=True), Type=TEXT(stored=True), Description=TEXT(stored=True)) #Schema created
    indexer = create_in('Back_End', schema) #Make sure there is a directory for the indexing method to store it's contents in  
    writer = indexer.writer() 

    csvfile = open('fullDatabase.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for element in reader: 
        writer.add_document(Name=element[0], Size=element[1], Location=element[2],
                            Longitude=element[3], Latitude=element[4], Image=element[5], Type=element[6], Description=element[7]) #For each line, store every element to it's respective attribute  #FIX THIS
        line_count += 1

    print("Total Tuples:", line_count)
    writer.commit()
    return indexer


def main():
    indexer = index()
    print('You will be prompted to input a search term. If you choose to exit then simply type exit in the command prompt')
    while True: #Prompts user 
        print(' ')
        searchTerm = input('Please enter a query: ')
        if searchTerm == 'exit': #There's no exit query results. This is how the user will exit the program
            break
        results = search(indexer, searchTerm)


if __name__ == '__main__':
    main()
