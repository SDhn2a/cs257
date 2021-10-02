''' add commandline interface work here'''

import booksdatasource, sys
import argparse

def main(argv):
    arguments = get_parsed_arguments()
    books_list = booksdatasource.BooksDataSource('books1.csv')
    if arguments.search_range or arguments.search_range != None:
        books_list = books_list.books_between_years(*arguments.search_range)
    elif arguments.search_title:
        if arguments.sort_publication_year:
            books_list = books_list.books(*arguments.search_title,'year')
        else:
            books_list = books_list.books(*arguments.search_title,'title')
    elif arguments.search_author or arguments.search_author != None:
        books_list = books_list.authors(*arguments.search_author)
    elif arguments.sort_publication_year:
        books_list = books_list.books(None,'year')
    else:
        books_list = books_list.books()
    for book in books_list:
        print(book)
    

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='List filtered book information. Will default to searching by title if no flags are provided.')
    parser.add_argument('--sort_publication_year','-p',action='store_true',help='displays results sorted by publication year')
    parser.add_argument('--sort_title','-t',action='store_true',help='displays results sorted by title')
    parser.add_argument('--search_range','-R',type=int,nargs='*',help='given 2 range parameters of years, prints a list of books published between the parameters, inclusive, in order of published year; if only one range parameter is provided, prints a list of books published in that year; if no search parameter is provided, prints all books')
    parser.add_argument('--search_title','-T',nargs='*',help='prints a list of books whose names contain the search parameter; if no search parameter is provided, prints all books')
    parser.add_argument('--search_author','-A',nargs='*',help='prints a list of books whose authors\' names contain the search parameter; displayed in order of author; if no search parameter is provided, prints all books')
    return parser.parse_args()

    

if __name__ == '__main__':
    main(sys.argv[1:])
