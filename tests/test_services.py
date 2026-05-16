"""
Unit tests for service layer
"""

import unittest
from datetime import datetime, timedelta
from src.services.user_service import UserService
from src.services.course_service import CourseService
from src.services.assignment_service import AssignmentService


class TestUserService(unittest.TestCase):
    
    def setUp(self):
        self.user_service = UserService()
    
    def test_register_student_success(self):
        student = self.user_service.register_student(
            "STU001", "student@mycput.ac.za", "pass123",
            "John", "Doe", "123456", "CS"
        )
        self.assertEqual(student.user_id, "STU001")
        self.assertEqual(student.email, "student@mycput.ac.za")
    
    def test_register_student_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user_service.register_student(
                "STU002", "student@gmail.com", "pass123",
                "Jane", "Doe", "789012", "CS"
            )
    
    def test_login_success(self):
        self.user_service.register_student(
            "STU003", "login@mycput.ac.za", "pass123",
            "Test", "User", "111222", "CS"
        )
        result = self.user_service.login("login@mycput.ac.za", "pass123")
        self.assertEqual(result["email"], "login@mycput.ac.za")
    
    def test_login_invalid_password(self):
        self.user_service.register_student(
            "STU004", "wrongpass@mycput.ac.za", "correct",
            "Test", "User", "333444", "CS"
        )
        with self.assertRaises(ValueError):
            self.user_service.login("wrongpass@mycput.ac.za", "wrong")


class TestCourseService(unittest.TestCase):
    
    def setUp(self):
        self.course_service = CourseService()
    
    def test_create_course_success(self):
        course = self.course_service.create_course(
            "CS101", "Intro to Programming", 15,
            "CS", "FAC001", "Semester 1 2026"
        )
        self.assertEqual(course.course_id, "CS101")
        self.assertEqual(course._course_name, "Intro to Programming")
    
    def test_create_course_duplicate_id(self):
        self.course_service.create_course(
            "CS102", "Data Structures", 15,
            "CS", "FAC001", "Semester 1 2026"
        )
        with self.assertRaises(ValueError):
            self.course_service.create_course(
                "CS102", "Algorithms", 15,
                "CS", "FAC001", "Semester 1 2026"
            )
    
    def test_get_course_by_id(self):
        self.course_service.create_course(
            "CS103", "Databases", 15,
            "CS", "FAC001", "Semester 1 2026"
        )
        course = self.course_service.get_course_by_id("CS103")
        self.assertIsNotNone(course)
        self.assertEqual(course._course_name, "Databases")


class TestAssignmentService(unittest.TestCase):
    
    def setUp(self):
        self.assignment_service = AssignmentService()
    
    def test_create_assignment_success(self):
        due_date = datetime.now() + timedelta(days=14)
        assignment = self.assignment_service.create_assignment(
            "ASSIGN001", "CS101", "Final Project",
            "Build a web app", due_date, 100
        )
        self.assertEqual(assignment._assignment_id, "ASSIGN001")
    
    def test_create_assignment_past_due(self):
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            self.assignment_service.create_assignment(
                "ASSIGN002", "CS101", "Late Assignment",
                "Description", past_date, 100
            )


if __name__ == '__main__':
    unittest.main()