'''
    rem to change this at the end
'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    # confirms that a error is raised if an invalid csv file location/name is provided
    def test_invalid_csv_location(self):
        self.assertRaises(FileNotFoundError, booksdatasource.BooksDataSource, 'books1.txt')

    # confirms that all the lines in the csv file is turned into a book instance
    def test_number_of_books(self):
        self.assertEqual(len(books(self.data_source)) == 42)

    # confirms that no same author is being turned into multiple author instances
    def test_number_of_authors(self):
        self.assertEqual(len(authors(self.data_source)) == 22)
    
    
    ## five of the twenty-three tests pass from the get-go because the code that was provided 
    ## already has the compairison code written for. However, we wrote these tests to show 
    ## the ways we have tested the given code instead of just including the provided methods.

    #checks if author compairison is true given the same two authors
    def test_same_authors(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("Lev", "Shuster")
        self.assertTrue(book1 == book2)
    #checks if two diffrent Authors are not equal
    def test_diffrent_authors(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("Eric", "Bradford")
        self.assertFalse(book1 == book2)
    #checks if two Authors two are diffrent but share some qualities are the same
    def test_partially_diffrent_authors(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("Eric", "Shuster")
        self.assertFalse(book1 == book2)
    #checks if two Authors which diffrent capitalization but the same information return true
    def test_same_authors_with_inconsistant_capitalization(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("LEV", "ShusTer")
        self.assertTrue(book1 == book2)

    #checks if title compairison is true given the same two titles
    def test_same_title(self):
        book1 = booksdatasource.Book("Reamde")
        book2 = booksdatasource.Book("Reamde")
        self.assertTrue(book1 == book2)
    #checks if two diffrent titles are not equal
    def test_diffrent_books(self):
        book1 = booksdatasource.Book("Reamde")
        book2 = booksdatasource.Book("Pride and Prejudice")
        self.assertFalse(book1 == book2)
    #checks if two Authors which diffrent capitalization but the same information return true
    def test_same_books_with_inconsistant_capitalization(self):
        book1 = booksdatasource.Book("Reamde")
        book2 = booksdatasource.Book("REamde")
        self.assertTrue(book1 == book2)
if __name__ == '__main__':
    unittest.main()

