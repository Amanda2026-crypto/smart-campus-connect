"""
Entity-specific repository interface for Course domain
"""

from abc import abstractmethod
from typing import Optional, List
from src.repositories.repository_interface import Repository
from src.domain.course import Course


class CourseRepository(Repository[Course, str]):
    """Repository for Course entities"""
    
    @abstractmethod
    def find_by_course_code(self, course_code: str) -> Optional[Course]:
        """Find course by course code (e.g., SE301)"""
        pass
    
    @abstractmethod
    def find_by_department(self, department: str) -> List[Course]:
        """Find courses by department"""
        pass
    
    @abstractmethod
    def find_by_faculty(self, faculty_id: str) -> List[Course]:
        """Find courses taught by a specific faculty member"""
        pass
    
    @abstractmethod
    def find_by_semester(self, semester: str) -> List[Course]:
        """Find courses by semester (e.g., 'Semester 1 2026')"""
        pass
    
    @abstractmethod
    def find_courses_with_capacity(self) -> List[Course]:
        """Find courses that are not full"""
        pass