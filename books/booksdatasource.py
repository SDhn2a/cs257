#!/usr/bin/env python3
'''
    booksdatasource.py
    Lev Shuster and Soren DeHaan, 2 October 2021

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
'''

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' assume no two authors have the same name. '''
        return self.surname.lower() == other.surname.lower() and self.given_name.lower() == other.given_name.lower()

    def __str__(self):
        return_string = self.given_name+" "+self.surname+" ("+str(self.birth_year)
        if self.death_year == None:
            return_string += "-)"
        else:
            return_string += "-"+str(self.death_year)+")"
        return return_string

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' assumes that no two books have the same title'''
        return self.title.lower() == other.title.lower()
    
    def __str__(self):
        ''' prints title, publication year, then the each author string method gets used'''
        return_string = self.title+", "+str(self.publication_year)+", "
        num_authors = len(self.authors)
        for author in self.authors:
            num_authors -= 1
            return_string += str(author)
            if num_authors > 0:
                return_string += " and "
        return return_string

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        self.full_author_list = []
        self.full_book_list = []

        with open(books_csv_file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                author_list = self.parse_book_authors(line[2])
                self.append_unique_authors(author_list)

                # parse books
                self.full_book_list.append(Book(line[0], int(line[1]), author_list))
                
    def append_unique_authors(self, author_list):
        ''' Helper function. Adds all Authors which are not already in the full list of
            authors to the list.'''
        for author in author_list:
            if author not in self.full_author_list:
                self.full_author_list.append(author)

    def parse_book_authors(self, author_input_string):
        ''' Helper function. Creates a list of all the Author objects in the input source,
            and returns it.'''
        
        GIVEN_NAME_COLUMN = 0
        SURNAME_COLUMN = -2
        AUTHOR_DATE_COLUMN = -1

        author_input_list = author_input_string.split("and") # in case of mult. authors
        author_list = [] # this list is what will get returned, and contains newly-parsed authors
        for author_input in author_input_list:
            author_data = author_input.split()
            author_given_name = author_data[GIVEN_NAME_COLUMN] 
            author_surname = author_data[len(author_data) + SURNAME_COLUMN]

            author_dates = author_data[len(author_data) + AUTHOR_DATE_COLUMN]
            author_dates_list = author_dates[1:-1].split("-")

            # puts all the bits togeter into an Author instance depending on if there is a death year
            if(len(author_dates_list) == 1):
                author_list.append(Author(author_surname, author_given_name, author_dates_list[0]))
            else: 
                author_list.append(Author(author_surname, author_given_name, author_dates_list[0], author_dates_list[1]))
        
        return author_list

    def authors(self, search_text=None):
        ''' Returns a list of all the Book objects in this data source whose authors' names 
            contain (case-insensitively) the search text. If search_text is None, then this
            method returns all of the Book objects. In either case, the returned list is
            sorted by author surname, breaking ties using given name (e.g. Ann Brontë comes
            before Charlotte Brontë).
        '''
        
        # So in the assignment description, we're supposed to search the *books* by author,
        # but in the original code description here, it just said to search authors. We're
        # operating under the assumption that the assignment description is the most up to
        # date, and have updated the code block description above accordingly.

        temp_book_list = []
        for book in self.full_book_list:
            for author in book.authors:
                # adds given name twice so that search 'n Bron' would return Ann Bronte and 'Bronte, A' would 
                # return Ann Bronte
                temp_full_name = author.given_name + ' ' + author.surname + ', ' + author.given_name
                if search_text == None or temp_full_name.__contains__(search_text):
                    temp_book_list.append(book)
                    break
                
        # sort by last name, with first name as tie breaker
        temp_book_list = sorted(temp_book_list, key=lambda book: book.authors[0].surname + book.authors[0].given_name)
        return temp_book_list


    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        temp_book_list = []

        # add each book to temp list if it matches search paramenter (or is empty)
        for book in self.full_book_list:
            if search_text == None or book.title.lower().__contains__(search_text.lower()):
                temp_book_list.append(book)
        
        # sort by specified catagory
        if sort_by == 'title':
            temp_book_list = sorted(temp_book_list, key=lambda book: book.title)
        elif sort_by == 'year':
            temp_book_list = sorted(temp_book_list, key=lambda book: book.publication_year)
        
        return temp_book_list

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        temp_book_list = []
        for book in self.full_book_list:
            if (start_year == None or book.publication_year >= start_year):
                if (end_year == None or book.publication_year <= end_year):
                    temp_book_list.append(book)
        temp_book_list = sorted(temp_book_list, key=lambda book: book.publication_year)
        return temp_book_list

