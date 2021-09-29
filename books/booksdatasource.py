#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2021

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
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname.lower() == other.surname.lower() and self.given_name.lower() == other.given_name.lower()

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title.lower() == other.title.lower()

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        self.full_author_list = []
        self.full_book_list = []

        with open('books1.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                author_list = self.parse_book_authors(line[2])
                # add authors + books to big lists
                self.append_unique_authors(author_list)
                # parse books
                # self.full_book_list.append(Book(line[0], line[1], author_list))
                self.full_book_list.append(1)
                
    def append_unique_authors(self, author_list):
        for author in author_list:
            if author not in self.full_author_list:
                self.full_author_list.append(author)

    def parse_book_authors(self, author_input_string):
        author_input_list = author_input_string.split("and") # takes input, splits in case of mult. authors
        author_list = [] # this list is what will get returned, and contains newly-parsed authors
        for author_input in author_input_list:
            author_data = author_input.split()
            author_given_name = author_data[0] # the first element of author_data is the given name
            author_surname = author_data[len(author_data)-2] # the second to last element is the surname
            author_dates = author_data[len(author_data)-1] # the last element is all of the dates
            author_dates_list = author_dates[1:-1].split("-") # turns the birth/death dates into a list
            if(len(author_dates_list) == 1): # add author to list to return
                author_list.append(Author(author_given_name, author_surname, author_dates_list[0]))
            else: # add author to list to return
                author_list.append(Author(author_given_name, author_surname, author_dates_list[0], author_dates_list[1]))
        
        return author_list

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        return self.full_author_list

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
        return self.full_book_list

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
        return []

