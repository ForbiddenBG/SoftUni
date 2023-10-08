# class IntegerList:
#     def __init__(self, *args):
#         self.__data = []
#         for x in args:
#             if type(x) == int:
#                 self.__data.append(x)
#
#     def get_data(self):
#         return self.__data
#
#     def add(self, element):
#         if not type(element) == int:
#             raise ValueError("Element is not Integer")
#         self.get_data().append(element)
#         return self.get_data()
#
#     def remove_index(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         a = self.get_data()[index]
#         del self.get_data()[index]
#         return a
#
#     def get(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         return self.get_data()[index]
#
#     def insert(self, index, el):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         elif not type(el) == int:
#             raise ValueError("Element is not Integer")
#
#         self.get_data().insert(index, el)
#
#     def get_biggest(self):
#         a = sorted(self.get_data(), reverse=True)
#         return a[0]
#
#     def get_index(self, el):
#         return self.get_data().index(el)


from unittest import TestCase, main

from project.main import IntegerList


class IntegerListTest(TestCase):
    def test_if_the_constructor_initialized_correctly(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_if_the_list_correctly_take_only_integers(self):
        integer = IntegerList("asd", 3, 4, 10)
        self.assertEqual([3, 4, 10], integer._IntegerList__data)

    def test_if_the_list_doesnt_except_floats(self):
        integer = IntegerList("asd", 3.0, 4.4, 56.43)
        self.assertEqual([], integer._IntegerList__data)

    def test_if_the_list_adds_correctly_new_elements(self):
        integer = IntegerList()
        integer.add(4)
        self.assertEqual([4], integer._IntegerList__data)

    def test_if_the_list_doesnt_except_element_raises(self):
        integer = IntegerList()
        with self.assertRaises(ValueError) as ex:
            integer.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_the_list_removes_from_index_correctly_the_elements(self):
        integer = IntegerList(2, 4, 5)
        integer.remove_index(1)
        self.assertEqual([2, 5], integer._IntegerList__data)

    def test_if_the_remove_index_is_out_of_range_raises(self):
        integer = IntegerList(2)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_get_method_works_correctly(self):
        integer = IntegerList(2)
        result = integer.get(0)
        self.assertEqual(2, result)

    def test_if_the_get_method_is_out_of_range_raises(self):
        integer = IntegerList(2)
        with self.assertRaises(IndexError) as ex:
            integer.get(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_is_working_correctly(self):
        integer = IntegerList(2, 4, 5)
        integer.insert(2, 100)
        self.assertEqual([2, 4, 100, 5], integer._IntegerList__data)

    def test_insert_is_working_incorrectly_index_out_of_range_raises(self):
        integer = IntegerList(2)
        with self.assertRaises(IndexError) as ex:
            integer.insert(4, 100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_is_working_incorrectly_element_is_not_integer_raises(self):
        integer = IntegerList(2, 3, 4)
        with self.assertRaises(ValueError) as ex:
            integer.insert(1, "100")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_number_work_correctly(self):
        integer = IntegerList(2, 4, 5)
        result = integer.get_biggest()
        self.assertEqual(5, result)

    def test_get_index_of_the_element_work_correctly(self):
        integer = IntegerList(2, 4, 5)
        result = integer.get_index(4)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()