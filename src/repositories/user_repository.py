"""
Entity-specific repository interfaces for User domain
"""

from abc import abstractmethod
from typing import Optional, List
from src.repositories.repository_interface import Repository
from src.domain.user import User, Student, Faculty, Admin


class UserRepository(Repository[User, str]):
    """Repository for User entities"""
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email address"""
        pass
    
    @abstractmethod
    def find_by_role(self, role: str) -> List[User]:
        """Find users by role (STUDENT, FACULTY, ADMIN)"""
        pass
    
    @abstractmethod
    def find_active_users(self) -> List[User]:
        """Find all active users"""
        pass


class StudentRepository(Repository[Student, str]):
    """Repository for Student entities"""
    
    @abstractmethod
    def find_by_student_id(self, student_id: str) -> Optional[Student]:
        """Find student by CPUT student number"""
        pass
    
    @abstractmethod
    def find_by_department(self, department: str) -> List[Student]:
        """Find students by department"""
        pass
    
    @abstractmethod
    def find_enrolled_courses(self, student_id: str) -> List[str]:
        """Find course IDs a student is enrolled in"""
        pass


class FacultyRepository(Repository[Faculty, str]):
    """Repository for Faculty entities"""
    
    @abstractmethod
    def find_by_staff_id(self, staff_id: str) -> Optional[Faculty]:
        """Find faculty by staff ID"""
        pass
    
    @abstractmethod
    def find_by_department(self, department: str) -> List[Faculty]:
        """Find faculty by department"""
        pass
    
    @abstractmethod
    def find_teaching_courses(self, faculty_id: str) -> List[str]:
        """Find course IDs a faculty member teaches"""
        pass


class AdminRepository(Repository[Admin, str]):
    """Repository for Admin entities"""
    
    @abstractmethod
    def find_by_staff_id(self, staff_id: str) -> Optional[Admin]:
        """Find admin by staff ID"""
        pass
    
    @abstractmethod
    def find_by_admin_role(self, admin_role: str) -> List[Admin]:
        """Find admins by role (SUPER_ADMIN, EVENT_ADMIN, FACILITY_ADMIN)"""
        pass