import unittest
import sys

sys.path.append(r"C:\Users\PC\PycharmProjects\python_unittest\08_employee")
from employee.emp import Employee


class TestselfEmployee(unittest.TestCase):
    def setUp(self):
        print("setting up...")
        self.emp = Employee('Jan', 'Kowalski', 8000)

    def tearDown(self):
        print("tearing down")
        del self.emp

    def test_email(self):
        self.assertEqual(self.emp.email, "Jan.Kowalski@email.com")

    def test_email_after_change_name(self):
        self.emp.first_name = "Name"
        self.assertEqual(self.emp.email, "Name.Kowalski@email.com")

    def test_email_after_change_last_name(self):
        self.emp.last_name = "LAST"
        self.assertEqual(self.emp.email, "Jan.LAST@email.com")

    def test_tax(self):
        self.assertEqual(self.emp.tax, 1360)

    def test_salary_after_applying_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 8800)
