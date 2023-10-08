from unittest import TestCase, main
from project.library import Library


class TestLibrary(TestCase):
    def test_correctly_initialized_constructor(self):
        library = Library("Ciela")
        self.assertEqual("Ciela", library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_validating_name_correctly(self):
        library = Library("Ciela")
        library.name = "Ciela"
        self.assertEqual("Ciela", library.name)

    def test_incorect_validation_of_name_with_empty_string_raises(self):
        library = Library("Ciela")
        with self.assertRaises(ValueError) as context:
            library.name = ""
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_correctly_adding_author_and_book_that_dont_exist_in_the_dictionary(self):
        library = Library("Ciela")
        library.books_by_authors = {}
        library.add_book("Terry", "Guards")
        self.assertEqual({"Terry": ["Guards"]}, library.books_by_authors)

    def test_adding_booK_to_the_existing_author_in_the_dictionary(self):
        library = Library("Ciela")
        library.books_by_authors = {"Terry": ["Guards"]}
        library.add_book("Terry", "Mort")
        self.assertEqual({"Terry": ["Guards", "Mort"]}, library.books_by_authors)

    def test_add_reader_that_doesnt_exist_in_the_dictionary(self):
        library = Library("Ciela")
        library.readers = {}
        library.add_reader("Max")
        self.assertEqual({"Max": []}, library.readers)

    def test_adding_a_reader_that_already_exists(self):
        library = Library("Ciela")
        library.readers = {"Max": []}
        result = library.add_reader("Max")
        self.assertEqual("Max is already registered in the Ciela library.", result)

    def test_rent_a_book_with_reader_that_doesnt_exists(self):
        library = Library("Ciela")
        library.books_by_authors = {"Terry": ["Mort"]}
        library.readers = {}
        result = library.rent_book("Max", "Terry", "Mort")
        self.assertEqual("Max is not registered in the Ciela Library.", result)

    def test_rent_a_book_of_author_that_doesnt_exists(self):
        library = Library("Ciela")
        library.books_by_authors = {}
        library.readers = {"Max": []}
        result = library.rent_book("Max", "Terry", "Mort")
        self.assertEqual("Ciela Library does not have any Terry's books.", result)

    def test_rent_a_book_title_that_doesnt_exists(self):
        library = Library("Ciela")
        library.books_by_authors = {"Terry": ["Guards!"]}
        library.readers = {"Max": []}
        result = library.rent_book("Max", "Terry", "Mort")
        self.assertEqual("""Ciela Library does not have Terry's "Mort".""", result)

    def test_correctly_rent_a_book(self):
        library = Library("Ciela")
        library.books_by_authors = {"Terry": ["Mort", "The color of the magic"]}
        library.readers = {"Max": []}
        library.rent_book("Max", "Terry", "Mort")
        self.assertEqual({"Max": [{"Terry": "Mort"}]}, library.readers)
        self.assertEqual({"Terry": ["The color of the magic"]}, library.books_by_authors)


if __name__ == "__main__":
    main()