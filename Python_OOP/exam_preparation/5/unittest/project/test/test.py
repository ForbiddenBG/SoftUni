from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def test_correctly_initialized_constructor(self):
        student = StudentReportCard("Max", 2)
        self.assertEqual("Max", student.student_name)
        self.assertEqual(2, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_incorrect_validation_of_the_name_with_empty_string_raises(self):
        student = StudentReportCard("Max", 2)
        with self.assertRaises(ValueError) as context:
            student.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_correct_validation_of_the_name(self):
        student = StudentReportCard("Max", 2)
        student.student_name = "Max"
        self.assertEqual("Max", student.student_name)

    def test_incorrect_validation_of_the_school_year_with_value_less_than_one_raises(self):
        student = StudentReportCard("Max", 2)
        with self.assertRaises(ValueError) as context:
            student.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_incorrect_validation_of_the_school_year_with_value_bigger_than_twelve_raises(self):
        student = StudentReportCard("Max", 2)
        with self.assertRaises(ValueError) as context:
            student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_correct_validation_of_the_school_year_value_between_the_others(self):
        student = StudentReportCard("Max", 2)
        student.school_year = 5
        self.assertEqual(5, student.school_year)

    def test_correct_validation_of_the_school_year_with_value_equal_to_one(self):
        student = StudentReportCard("Max", 2)
        student.school_year = 1
        self.assertEqual(1, student.school_year)

    def test_correct_validation_of_the_school_year_with_value_equal_to_twelve(self):
        student = StudentReportCard("Max", 2)
        student.school_year = 12
        self.assertEqual(12, student.school_year)

    def test_adding_a_grade_to_subject(self):
        student = StudentReportCard("Max", 2)
        student.grades_by_subject = {}
        student.add_grade("Math", 5.00)
        self.assertEqual({"Math": [5.00]}, student.grades_by_subject)
        student.add_grade("Math", 6)
        self.assertEqual({"Math": [5.00, 6.00]}, student.grades_by_subject)

    def test_calculate_average_grade_by_subject_and_return_report(self):
        student = StudentReportCard("Max", 2)
        student.grades_by_subject = {"Math": [5.00, 5.00], "Bio": [4.00, 6.00]}
        result = student.average_grade_by_subject()
        self.assertEqual("Math: 5.00\nBio: 5.00", result)

    def test_calculate_average_grade_for_all_subjects_and_return_report(self):
        student = StudentReportCard("Max", 2)
        student.grades_by_subject = {"Math": [5.00, 5.00], "Bio": [4.00, 6.00]}
        result = student.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.00", result)

    def test_valid_repr_dunder_method(self):
        student = StudentReportCard("Max", 2)
        student.grades_by_subject = {"Math": [5.00, 5.00], "Bio": [4.00, 6.00]}
        result = student.__repr__()
        self.assertEqual("Name: Max\n"
                         "Year: 2\n"
                         "----------\n"
                         "Math: 5.00\n"
                         "Bio: 5.00\n"
                         "----------\n"
                         "Average Grade: 5.00", result)


if __name__ == "__main__":
    main()
