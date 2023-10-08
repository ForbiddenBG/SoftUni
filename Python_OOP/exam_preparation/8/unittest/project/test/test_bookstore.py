from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def test_correctly_initiating_constructor(self):
        bookstore = Bookstore(10)
        self.assertEqual(10, bookstore.books_limit)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore._Bookstore__total_sold_books)

    def test_validation_getter_total_sold_books(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Pooh bear": 2}
        bookstore.sell_book("Pooh bear", 2)
        bookstore.__total_sold_books = 2
        self.assertEqual(2, bookstore._Bookstore__total_sold_books)

    def test_validation_correct_book_limit(self):
        bookstore = Bookstore(7)
        bookstore.books_limit = 7
        self.assertEqual(7, bookstore.books_limit)

    def test_validation_incorrect_book_limit_with_zero_raises(self):
        bookstore = Bookstore(10)
        with self.assertRaises(ValueError) as ex:
            bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_validation_incorrect_book_limit_with_less_than_zero_raises(self):
        bookstore = Bookstore(10)
        with self.assertRaises(ValueError) as ex:
            bookstore.books_limit = -4
        self.assertEqual("Books limit of -4 is not valid", str(ex.exception))

    def test_the_total_number_of_the_values_in_available_books(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Pooh bear": 2, "Peter Pan": 5, "Hobbit": 2}
        result = bookstore.__len__()
        self.assertEqual(9, result)

    def test_receive_book_which_is_over_the_capacity_raises(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Pooh bear": 2, "Peter Pan": 5, "Hobbit": 3}
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("Lord of the rings", 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_that_is_not_in_the_book_store_correctly(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hobbit": 2}
        result = bookstore.receive_book("Lord of the rings", 2)
        self.assertEqual(4, bookstore.__len__())
        self.assertEqual({"Hobbit": 2, "Lord of the rings": 2}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual("2 copies of Lord of the rings are available in the bookstore.", result)

    def test_receive_book_that_is_in_the_book_store_correctly(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hobbit": 2, "Lord of the rings": 2}
        result = bookstore.receive_book("Lord of the rings", 2)
        self.assertEqual(6, bookstore.__len__())
        self.assertEqual({"Hobbit": 2, "Lord of the rings": 4}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual("4 copies of Lord of the rings are available in the bookstore.", result)

    def test_sell_book_that_is_not_available_in_the_bookstore_raises(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hobbit": 2}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Night watch", 2)
        self.assertEqual("Book Night watch doesn't exist!", str(ex.exception))
        self.assertEqual(2, bookstore.__len__())
        self.assertEqual({"Hobbit": 2}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore._Bookstore__total_sold_books)

    def test_sell_book_that_is_not_available_empty_dict_raises(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("The night before Christmas", 1)
        self.assertEqual("Book The night before Christmas doesn't exist!", str(ex.exception))
        self.assertEqual(0, bookstore.__len__())
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore._Bookstore__total_sold_books)

    def test_selling_more_copies_of_the_existing_book_in_the_store_raises(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hyperion": 3}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Hyperion", 10)
        self.assertEqual("Hyperion has not enough copies to sell. Left: 3", str(ex.exception))

    def test_selling_more_copies_of_zero_books_in_the_store_raises(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hyperion": 0}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Hyperion", 1)
        self.assertEqual("Hyperion has not enough copies to sell. Left: 0", str(ex.exception))

    def test_if_the_book_was_sold_successfully(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hyperion": 4}
        result = bookstore.sell_book("Hyperion", 3)
        self.assertEqual(1, bookstore.__len__())
        self.assertEqual({"Hyperion": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, bookstore._Bookstore__total_sold_books)
        self.assertEqual("Sold 3 copies of Hyperion", result)

    def test_if_the_book_was_sold_successfully_with_max_quantity(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hyperion": 4}
        result = bookstore.sell_book("Hyperion", 4)
        self.assertEqual(0, bookstore.__len__())
        self.assertEqual({"Hyperion": 0}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(4, bookstore._Bookstore__total_sold_books)
        self.assertEqual("Sold 4 copies of Hyperion", result)

    def test_correctly_representing_dunder_str(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"Hyperion": 4, "Lord of the rings": 2}
        bookstore._Bookstore__total_sold_books = 2
        result = bookstore.__str__()
        self.assertEqual('Total sold books: 2' + '\n' 'Current availability: 6' + '\n'
                         + ' - Hyperion: 4 copies' + '\n'
                         + ' - Lord of the rings: 2 copies', result)


if __name__ == "__main__":
    main()