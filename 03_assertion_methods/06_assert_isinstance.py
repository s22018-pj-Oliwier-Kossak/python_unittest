import unittest


class Person:
    def __init__(self, name):
        self.name = name


class Worker(Person):
    pass


class TestPerson(unittest.TestCase):

    def test_case_1(self):
        self.assertIsInstance(Person, type)

    def test_case_2(self):
        person = Person("imie")
        self.assertIsInstance(person, Person)

    def test_case_3(self):
        person = Person("imie")
        self.assertIsInstance(person, Worker)


class TestWorker(unittest.TestCase):

    def test_case_1(self):
        worker = Worker("work")
        self.assertIsInstance(worker, Worker)

    def test_case_2(self):
        worker = Worker("work")
        self.assertIsInstance(worker, Person)
