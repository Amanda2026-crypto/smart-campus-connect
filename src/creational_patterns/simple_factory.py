"""
Simple Factory Pattern
Use Case: Creating different types of Users (Student, Faculty, Admin)
"""

from abc import ABC, abstractmethod


class UserFactory:
    """Simple Factory for creating User objects"""
    
    @staticmethod
    def create_user(user_type: str, **kwargs):
        """Create user based on type"""
        if user_type == "student":
            return StudentUser(
                kwargs.get('user_id'),
                kwargs.get('email'),
                kwargs.get('password'),
                kwargs.get('first_name'),
                kwargs.get('last_name'),
                kwargs.get('student_id'),
                kwargs.get('department')
            )
        elif user_type == "faculty":
            return FacultyUser(
                kwargs.get('user_id'),
                kwargs.get('email'),
                kwargs.get('password'),
                kwargs.get('first_name'),
                kwargs.get('last_name'),
                kwargs.get('staff_id'),
                kwargs.get('department')
            )
        elif user_type == "admin":
            return AdminUser(
                kwargs.get('user_id'),
                kwargs.get('email'),
                kwargs.get('password'),
                kwargs.get('first_name'),
                kwargs.get('last_name'),
                kwargs.get('staff_id'),
                kwargs.get('admin_role')
            )
        else:
            raise ValueError(f"Unknown user type: {user_type}")


class BaseUser:
    """Base user class"""
    def __init__(self, user_id, email, password, first_name, last_name):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
    
    def get_role(self):
        return self.__class__.__name__


class StudentUser(BaseUser):
    def __init__(self, user_id, email, password, first_name, last_name, student_id, department):
        super().__init__(user_id, email, password, first_name, last_name)
        self.student_id = student_id
        self.department = department


class FacultyUser(BaseUser):
    def __init__(self, user_id, email, password, first_name, last_name, staff_id, department):
        super().__init__(user_id, email, password, first_name, last_name)
        self.staff_id = staff_id
        self.department = department


class AdminUser(BaseUser):
    def __init__(self, user_id, email, password, first_name, last_name, staff_id, admin_role):
        super().__init__(user_id, email, password, first_name, last_name)
        self.staff_id = staff_id
        self.admin_role = admin_role