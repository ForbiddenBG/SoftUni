from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def test_correctly_creating_constructor_only_with_name(self):
        student = Student("Max")
        self.assertEqual("Max", student.name)
        self.assertEqual({}, student.courses)

    def test_correctly_creating_costructor_with_name_and_courses(self):
        student = Student("Max", {"Bio": [3]})
        self.assertEqual("Max", student.name)
        self.assertEqual({"Bio": [3]}, student.courses)

    def test_correctly_adding_notes_to_existing_course(self):
        student = Student("Max", {"Bio": [3]})
        result = student.enroll("Bio", [4])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_correctly_adding_course_and_notes_with_y(self):
        student = Student("Max", {"Bio": [4]})
        result = student.enroll("Math", [4, 5], "Y")
        self.assertEqual("Course and course notes have been added.", result)

    def test_correctly_adding_course_and_notes_with_none(self):
        student = Student("Max", {"Bio": [4]})
        result = student.enroll("Math", [4, 5], "")
        self.assertEqual("Course and course notes have been added.", result)

    def test_correctly_adding_a_course(self):
        student = Student("Max", {"Bio": [4]})
        result = student.enroll("Math", [4, 5], "unknown")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], student.courses["Math"])

    def test_adding_the_notes_correctly(self):
        student = Student("Max", {"Bio": [4]})
        result = student.add_notes("Bio", 5)
        self.assertEqual("Notes have been updated", result)

    def test_adding_the_notes_incorrectly(self):
        student = Student("Max", {"Bio": [6]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("Math", 4)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_the_course_correctly(self):
        student = Student("Max", {"Bio": [4, 6], "Math": [4]})
        result = student.leave_course("Math")
        self.assertEqual("Course has been removed", result)

    def test_leaving_the_course_which_doesnt_exist(self):
        student = Student("Max", {"Bio": [4], "Math": [5]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("Geo")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
