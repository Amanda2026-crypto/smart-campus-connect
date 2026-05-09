"""
Unit tests for in-memory repository implementations
"""

import unittest
from datetime import datetime, timedelta
from src.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from src.repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository
from src.repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository
from src.factories.repository_factory import RepositoryFactory
from src.domain.user import Student, Faculty, Admin
from src.domain.course import Course
from src.domain.assignment import Assignment


class TestUserRepository(unittest.TestCase):
    
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.student = Student(
            user_id="STU001",
            email="student@mycput.ac.za",
            password_hash="hashed123",
            first_name="John",
            last_name="Doe",
            student_id="123456789",
            department="Computer Science"
        )
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.student)
        found = self.repo.find_by_id("STU001")
        self.assertIsNotNone(found)
        self.assertEqual(found.first_name, "John")
    
    def test_find_all(self):
        self.repo.save(self.student)
        student2 = Student(
            user_id="STU002",
            email="jane@mycput.ac.za",
            password_hash="hashed456",
            first_name="Jane",
            last_name="Smith",
            student_id="987654321",
            department="Engineering"
        )
        self.repo.save(student2)
        all_users = self.repo.find_all()
        self.assertEqual(len(all_users), 2)
    
    def test_delete(self):
        self.repo.save(self.student)
        self.repo.delete("STU001")
        found = self.repo.find_by_id("STU001")
        self.assertIsNone(found)
    
    def test_exists(self):
        self.repo.save(self.student)
        self.assertTrue(self.repo.exists("STU001"))
        self.assertFalse(self.repo.exists("NONEXISTENT"))
    
    def test_count(self):
        self.repo.save(self.student)
        self.assertEqual(self.repo.count(), 1)
    
    def test_find_by_email(self):
        self.repo.save(self.student)
        found = self.repo.find_by_email("student@mycput.ac.za")
        self.assertIsNotNone(found)
    
    def test_find_by_role(self):
        self.repo.save(self.student)
        faculty = Faculty(
            user_id="FAC001",
            email="faculty@mycput.ac.za",
            password_hash="hashed789",
            first_name="Jane",
            last_name="Smith",
            staff_id="987654321",
            department="Engineering"
        )
        self.repo.save(faculty)
        students = self.repo.find_by_role("STUDENT")
        self.assertEqual(len(students), 1)


class TestCourseRepository(unittest.TestCase):
    
    def setUp(self):
        self.repo = InMemoryCourseRepository()
        self.course = Course(
            course_id="SE301",
            course_name="Software Engineering",
            credits=15,
            department="Computer Science",
            faculty_id="FAC001",
            semester="Semester 1 2026",
            max_students=50
        )
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.course)
        found = self.repo.find_by_id("SE301")
        self.assertIsNotNone(found)
        self.assertEqual(found.course_name, "Software Engineering")
    
    def test_find_by_department(self):
        self.repo.save(self.course)
        courses = self.repo.find_by_department("Computer Science")
        self.assertEqual(len(courses), 1)


class TestAssignmentRepository(unittest.TestCase):
    
    def setUp(self):
        self.repo = InMemoryAssignmentRepository()
        self.assignment = Assignment(
            assignment_id="ASSIGN001",
            course_id="SE301",
            title="System Design",
            description="Design the system architecture",
            due_date=datetime.now() + timedelta(days=14),
            max_points=100
        )
    
    def test_save_and_find(self):
        self.repo.save(self.assignment)
        found = self.repo.find_by_id("ASSIGN001")
        self.assertIsNotNone(found)
        self.assertEqual(found._title, "System Design")
    
    def test_find_by_course(self):
        self.repo.save(self.assignment)
        assignments = self.repo.find_by_course("SE301")
        self.assertEqual(len(assignments), 1)


class TestRepositoryFactory(unittest.TestCase):
    
    def test_factory_creates_user_repository(self):
        repo = RepositoryFactory.get_user_repository("MEMORY")
        self.assertIsNotNone(repo)
    
    def test_factory_creates_course_repository(self):
        repo = RepositoryFactory.get_course_repository("MEMORY")
        self.assertIsNotNone(repo)
    
    def test_factory_invalid_storage_type(self):
        with self.assertRaises(ValueError):
            RepositoryFactory.get_user_repository("INVALID")


if __name__ == '__main__':
    unittest.main()