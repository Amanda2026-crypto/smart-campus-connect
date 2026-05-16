"""
User Service - Business logic for user operations
"""

from typing import Optional, List
from src.domain.user import User, Student, Faculty, Admin
from src.repositories.user_repository import UserRepository, StudentRepository, FacultyRepository, AdminRepository
from src.factories.repository_factory import RepositoryFactory


class UserService:
    """Service for user-related business logic"""
    
    def __init__(self, storage_type: str = "MEMORY"):
        self.user_repo = RepositoryFactory.get_user_repository(storage_type)
        self.student_repo = RepositoryFactory.get_student_repository(storage_type)
        self.faculty_repo = RepositoryFactory.get_faculty_repository(storage_type)
        self.admin_repo = RepositoryFactory.get_admin_repository(storage_type)
    
    def register_student(self, user_id: str, email: str, password: str,
                         first_name: str, last_name: str, student_id: str, 
                         department: str) -> Student:
        """Register a new student"""
        # Business rule: Email must be CPUT email
        if not email.endswith("@mycput.ac.za"):
            raise ValueError("Email must be a valid CPUT email address (@mycput.ac.za)")
        
        # Business rule: Student ID must be unique
        existing = self.student_repo.find_by_student_id(student_id)
        if existing:
            raise ValueError(f"Student with ID {student_id} already exists")
        
        # Business rule: Email must be unique
        if self.user_repo.find_by_email(email):
            raise ValueError(f"User with email {email} already exists")
        
        student = Student(user_id, email, password, first_name, last_name, student_id, department)
        self.student_repo.save(student)
        return student
    
    def register_faculty(self, user_id: str, email: str, password: str,
                         first_name: str, last_name: str, staff_id: str, 
                         department: str) -> Faculty:
        """Register a new faculty member"""
        if not email.endswith("@mycput.ac.za"):
            raise ValueError("Email must be a valid CPUT email address (@mycput.ac.za)")
        
        existing = self.faculty_repo.find_by_staff_id(staff_id)
        if existing:
            raise ValueError(f"Faculty with staff ID {staff_id} already exists")
        
        faculty = Faculty(user_id, email, password, first_name, last_name, staff_id, department)
        self.faculty_repo.save(faculty)
        return faculty
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        return self.user_repo.find_by_id(user_id)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.user_repo.find_by_email(email)
    
    def get_all_users(self) -> List[User]:
        """Get all users"""
        return self.user_repo.find_all()
    
    def get_all_students(self) -> List[Student]:
        """Get all students"""
        return self.student_repo.find_all()
    
    def get_students_by_department(self, department: str) -> List[Student]:
        """Get students by department"""
        return self.student_repo.find_by_department(department)
    
    def delete_user(self, user_id: str) -> bool:
        """Delete a user"""
        if not self.user_repo.exists(user_id):
            raise ValueError(f"User with ID {user_id} not found")
        self.user_repo.delete(user_id)
        return True
    
    def deactivate_user(self, user_id: str) -> bool:
        """Deactivate a user account"""
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return user.deactivate()
    
    def login(self, email: str, password: str) -> dict:
        """Authenticate a user"""
        user = self.user_repo.find_by_email(email)
        if not user:
            raise ValueError("Invalid email or password")
        
        if not user.login(password):
            raise ValueError("Invalid email or password")
        
        if not user.is_active:
            raise ValueError("Account is deactivated. Please contact admin.")
        
        return {
            "user_id": user.user_id,
            "email": user.email,
            "role": user._role.value,
            "first_name": user._first_name,
            "last_name": user._last_name
        }