import unittest
from src.creational_patterns.simple_factory import UserFactory


class TestSimpleFactory(unittest.TestCase):
    
    def test_create_student(self):
        student = UserFactory.create_user(
            "student",
            user_id="STU001",
            email="student@mycput.ac.za",
            password="hashed123",
            first_name="John",
            last_name="Doe",
            student_id="123456789",
            department="Computer Science"
        )
        self.assertEqual(student.get_role(), "StudentUser")
        self.assertEqual(student.student_id, "123456789")
    
    def test_create_faculty(self):
        faculty = UserFactory.create_user(
            "faculty",
            user_id="FAC001",
            email="faculty@mycput.ac.za",
            password="hashed456",
            first_name="Jane",
            last_name="Smith",
            staff_id="987654321",
            department="Engineering"
        )
        self.assertEqual(faculty.get_role(), "FacultyUser")
        self.assertEqual(faculty.staff_id, "987654321")
    
    def test_create_admin(self):
        admin = UserFactory.create_user(
            "admin",
            user_id="ADM001",
            email="admin@mycput.ac.za",
            password="hashed789",
            first_name="Bob",
            last_name="Johnson",
            staff_id="555555555",
            admin_role="SUPER_ADMIN"
        )
        self.assertEqual(admin.get_role(), "AdminUser")
        self.assertEqual(admin.admin_role, "SUPER_ADMIN")
    
    def test_invalid_user_type(self):
        with self.assertRaises(ValueError):
            UserFactory.create_user("invalid_type")


if __name__ == '__main__':
    unittest.main()