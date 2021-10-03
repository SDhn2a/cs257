'''
    books.py
    Lev Shuster and Soren DeHaan, 2 October 2021

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
    add commandline interface work here
'''

import booksdatasource, argparse
from sys import argv 

CSV_SOURCE = 'books1.csv'

''' 
    set up parse and bookdatasource, direct parse results to 
    propper booksdatasource method, and then print the results.
'''
def main(argv):
    # arg parse setup
    arguments = get_parsed_arguments()

    # booksdatasource setup
    books_list = booksdatasource.BooksDataSource(CSV_SOURCE)

    # if source_range flag is used trigger books_between_years
    if arguments.search_range or arguments.search_range != None:
        books_list = books_list.books_between_years(*arguments.search_range)

    # else if search_title flag is present determin which sort method should be used
    # then trigger booksdatasource.books
    elif arguments.search_title:
        if arguments.sort_publication_year:
            books_list = books_list.books(*arguments.search_title,'year')
        else:
            books_list = books_list.books(*arguments.search_title,'title')

    # else if search_author flag is tripped trigger booksdatasource.authors
    elif arguments.search_author or arguments.search_author != None:
        books_list = books_list.authors(*arguments.search_author)
    
    # else if sort_publication_year flag is tripped trigger booksdatasource.books
    elif arguments.sort_publication_year:
        books_list = books_list.books(None,'year')
    
    # else sort all books
    else:
        books_list = books_list.books()

    # print the results of booksdatasource
    for book in books_list:
        print(book)
    

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='List filtered book information. Will default to searching by title if no flags are provided.')
    
    # parse sorts
    parser.add_argument('--sort_publication_year','-p',action='store_true',help='displays results sorted by publication year')
    parser.add_argument('--sort_title','-t',action='store_true',help='displays results sorted by title')
    
    # parse searches
    parser.add_argument('--search_range','-R',type=int,nargs='*',help='given 2 range parameters of years, prints a list of books published between the parameters, inclusive, in order of published year; if only one range parameter is provided, prints a list of books published in that year; if no search parameter is provided, prints all books')
    parser.add_argument('--search_title','-T',nargs='*',help='prints a list of books whose names contain the search parameter; if no search parameter is provided, prints all books')
    parser.add_argument('--search_author','-A',nargs='*',help='prints a list of books whose authors\' names contain the search parameter; displayed in order of author; if no search parameter is provided, prints all books')
    
    return parser.parse_args()

    

if __name__ == '__main__':
    main(argv[1:])
