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
    
    ## five of the seven test are true from the get-go because the prof-provided code 
    ## already has the compairison code written for. However we wrote these test to show 
    ## all the ways we have tested the given code instead of blindely including the provided methods.

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

