"""
Integration tests for API endpoints
"""

import unittest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


class TestUserAPI(unittest.TestCase):
    
    def test_register_student(self):
        response = client.post("/api/users/register", json={
            "user_id": "API001",
            "email": "apistudent@mycput.ac.za",
            "password": "pass123",
            "first_name": "API",
            "last_name": "Student",
            "student_id": "999888",
            "department": "CS",
            "role": "STUDENT"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["user_id"], "API001")
    
    def test_register_invalid_email(self):
        response = client.post("/api/users/register", json={
            "user_id": "API002",
            "email": "invalid@gmail.com",
            "password": "pass123",
            "first_name": "API",
            "last_name": "User",
            "student_id": "777666",
            "department": "CS",
            "role": "STUDENT"
        })
        self.assertEqual(response.status_code, 400)
    
    def test_login_success(self):
        # First register
        client.post("/api/users/register", json={
            "user_id": "API003",
            "email": "apilogin@mycput.ac.za",
            "password": "pass123",
            "first_name": "Login",
            "last_name": "Test",
            "student_id": "555444",
            "department": "CS",
            "role": "STUDENT"
        })
        
        # Then login
        response = client.post("/api/users/login", json={
            "email": "apilogin@mycput.ac.za",
            "password": "pass123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["email"], "apilogin@mycput.ac.za")
    
    def test_login_invalid(self):
        response = client.post("/api/users/login", json={
            "email": "nonexistent@mycput.ac.za",
            "password": "wrong"
        })
        self.assertEqual(response.status_code, 401)


class TestCourseAPI(unittest.TestCase):
    
    def test_create_course(self):
        response = client.post("/api/courses/", json={
            "course_id": "APICS101",
            "course_name": "API Testing Course",
            "credits": 15,
            "department": "CS",
            "faculty_id": "FAC001",
            "semester": "Semester 1 2026",
            "max_students": 50
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["course_id"], "APICS101")
    
    def test_get_course(self):
        # Create first
        client.post("/api/courses/", json={
            "course_id": "APICS102",
            "course_name": "Get Course Test",
            "credits": 15,
            "department": "CS",
            "faculty_id": "FAC001",
            "semester": "Semester 1 2026"
        })
        
        # Then get
        response = client.get("/api/courses/APICS102")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["course_name"], "Get Course Test")
    
    def test_get_nonexistent_course(self):
        response = client.get("/api/courses/NONEXISTENT")
        self.assertEqual(response.status_code, 404)


class TestBookingAPI(unittest.TestCase):
    
    def test_create_study_room(self):
        response = client.post("/api/bookings/rooms", json={
            "room_id": "APIROOM01",
            "building": "Engineering Building",
            "capacity": 6,
            "amenities": ["whiteboard", "projector"]
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["room_id"], "APIROOM01")


if __name__ == '__main__':
    unittest.main()