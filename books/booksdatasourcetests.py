'''
   booksdatasourcetest.py
   Lev Shuster and Soren DeHaan, 27 September 2021
    
   >> >> BEGIN IMPORTANT THING << <<

   five of the twenty-two tests pass from the get-go because the code that was provided
   already has comparison code written. However, we wrote these tests to show the ways we
   have tested the given code instead of just including the provided methods.

   >> >>  END IMPORTANT THING  << <<

'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass



    # confirms that an error is raised if an invalid csv file location/name is provided
    def test_invalid_csv_location(self):
        self.assertRaises(FileNotFoundError, booksdatasource.BooksDataSource, 'books1.txt')

    # confirms that all the lines in the csv file are turned into a book instance
    def test_number_of_books(self):
        self.assertEqual(len(books(self.data_source)) == 42)

    # confirms that no same author is being turned into multiple author instances
    def test_number_of_authors(self):
        self.assertEqual(len(authors(self.data_source)) == 22)



    # checks if author comparison is true given the same two authors
    def test_same_authors(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("Lev", "Shuster")
        self.assertTrue(book1 == book2)

    # checks if two different authors are not equal
    def test_different_authors(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("Eric", "Bradford")
        self.assertFalse(book1 == book2)

    # checks if two authors two are different but share some qualities that are the same
    def test_partially_different_authors(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("Eric", "Shuster")
        self.assertFalse(book1 == book2)

    # checks if two authors which different capitalization but the same information return true
    def test_same_authors_with_inconsistent_capitalization(self):
        book1 = booksdatasource.Author("Lev", "Shuster")
        book2 = booksdatasource.Author("LEV", "ShusTer")
        self.assertTrue(book1 == book2)



    # checks if title comparison is true given the same two titles
    def test_same_title(self):
        book1 = booksdatasource.Book("Reamde")
        book2 = booksdatasource.Book("Reamde")
        self.assertTrue(book1 == book2)

    # checks if two different titles are not equal
    def test_diffrent_books(self):
        book1 = booksdatasource.Book("Reamde")
        book2 = booksdatasource.Book("Pride and Prejudice")
        self.assertFalse(book1 == book2)

    # checks if two authors with different capitalization but the same information return true
    def test_same_books_with_inconsistant_capitalization(self):
        book1 = booksdatasource.Book("Reamde")
        book2 = booksdatasource.Book("REamde")
        self.assertTrue(book1 == book2)



    # confirms that a bad author search doesn't return results
    def test_bad_author_search(self):
        self.assertEqual(len(authors(self.data_source,"qazx")) == 0)

    # confirms that an empty author search returns all results
    def test_none_author_search(self):
        self.assertEqual(len(authors(self.data_source,None)) == 42)

    # confirms that a good author search returns the correct, sorted data
    def test_good_author_search(self):
        self.assertEqual(authors(self.data_source,"Bron")[0].title == "The Tenant of Wildfell Hall")



    # confirms that a bad search doesn't return results
    def test_bad_book_search(self):
        self.assertEqual(len(books(self.data_source,"qazx")) == 0)

    # confirms that an empty search returns all results
    def test_none_book_search(self):
        self.assertEqual(len(books(self.data_source,None)) == 42)

    # confirms that a good search returns the correct, sorted data
    def test_good_book_search(self):
        self.assertEqual(books(self.data_source,"the")[12].title == "Wuthering Heights")

    # confirms that a good search with year search tag returns the correct, sorted data
    def test_good_book_search_year(self):
        self.assertEqual(books(self.data_source,"the",'year')[12].title == "The Invisible Life of Addie LaRue")



    # confirms that a noninteger search returns an error
    def test_noninteger_range_search(self):
        self.assertRaises(SomeSortOfError,books_between_years(self.data_source,"qazx"))
        
    # confirms that a bad range search doesn't return results
    def test_impossible_range_search(self):
        self.assertEqual(len(books_between_years(self.data_source,2000,1900)) == 0)

    # confirms that an empty range search returns all results
    def test_none_range_search(self):
        self.assertEqual(len(books_between_years(self.data_source,None)) == 42)

    # confirms that a good range search returns the correct, sorted data
    def test_good_range_search(self):
        self.assertEqual(books(self.data_source,2001,2010)[1].title == "1Q84")

    # # confirms that a good range search (without end date) returns the correct, sorted data
    # def test_good_range_search_start(self):
    #     self.assertEqual(books(self.data_source,2020)[0].title == "The Invisible Life of Addie LaRue")

    # confirms that a good range search (without start date) returns the correct, sorted data
    def test_good_range_search_end(self):
        self.assertEqual(books(self.data_source,None,1815)[0].title == "Pride and Prejudice")



    # def test_unique_author(self):
    #     authors = self.data_source.authors('Pratchett')
    #     self.assertTrue(len(authors) == 1)
    #     self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

if __name__ == '__main__':
    unittest.main()
