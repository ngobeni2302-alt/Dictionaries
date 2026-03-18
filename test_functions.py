import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def test_q1(self):
        data = {"Alice": "M1", "Bob": "M1", "Clara": "M2"}
        expected = {"M1": ["Alice", "Bob"], "M2": ["Clara"]}
        self.assertEqual(invert_employee_manager_map(data), expected)

    def test_q2(self):
        data = [
            {"name": "Alice", "course": "Math"},
            {"name": "Bob", "course": "Math"},
            {"name": "Clara", "course": "Science"}
        ]
        expected = {"Math": ["Alice", "Bob"], "Science": ["Clara"]}
        self.assertEqual(group_students_by_course(data), expected)

    def test_q3(self):
        data = [
            {"title": "Book1", "author": "A"},
            {"title": "Book2", "author": "A"},
            {"title": "Book3", "author": "B"}
        ]
        expected = {"A": ["Book1", "Book2"], "B": ["Book3"]}
        self.assertEqual(group_books_by_author(data), expected)

    def test_q4(self):
        data = {"Paris": "France", "Lyon": "France", "Berlin": "Germany"}
        expected = {"France": ["Paris", "Lyon"], "Germany": ["Berlin"]}
        self.assertEqual(invert_country_city_map(data), expected)

    def test_q5(self):
        data = [1, 2, 3, 4]
        expected = {"odd": [1, 3], "even": [2, 4]}
        self.assertEqual(group_numbers_by_parity(data), expected)

    def test_q6(self):
        data = [
            {"name": "Alice", "dept": "HR"},
            {"name": "Bob", "dept": "IT"},
            {"name": "Clara", "dept": "HR"}
        ]
        expected = {"HR": ["Alice", "Clara"], "IT": ["Bob"]}
        self.assertEqual(group_employees_by_department(data), expected)

    def test_q7(self):
        data = {"Laptop": "Tech", "Phone": "Tech", "Shirt": "Clothing"}
        expected = {"Tech": ["Laptop", "Phone"], "Clothing": ["Shirt"]}
        self.assertEqual(invert_product_category_map(data), expected)

    def test_q8(self):
        data = ["apple", "banana", "avocado"]
        expected = {"a": ["apple", "avocado"], "b": ["banana"]}
        self.assertEqual(group_words_by_first_letter(data), expected)

    def test_q9(self):
        data = {"Student1": "TeacherA", "Student2": "TeacherA", "Student3": "TeacherB"}
        expected = {"TeacherA": ["Student1", "Student2"], "TeacherB": ["Student3"]}
        self.assertEqual(invert_teacher_student_map(data), expected)

    def test_q10(self):
        data = [
            {"amount": 100, "type": "deposit"},
            {"amount": 50, "type": "withdraw"},
            {"amount": 200, "type": "deposit"}
        ]
        expected = {"deposit": [100, 200], "withdraw": [50]}
        self.assertEqual(group_transactions_by_type(data), expected)

if __name__ == "__main__":
    unittest.main()