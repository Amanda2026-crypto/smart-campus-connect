"""
Course Service - Business logic for course operations
"""

import logging

logger = logging.getLogger(__name__)


from typing import Optional, List
from src.domain.course import Course
from src.repositories.course_repository import CourseRepository
from src.factories.repository_factory import RepositoryFactory


class CourseService:
    """Service for course-related business logic"""
    
    def __init__(self, storage_type: str = "MEMORY"):
        self.course_repo = RepositoryFactory.get_course_repository(storage_type)
    
    def create_course(self
        logger.info(f"Creating course: {course_name}"), course_id: str, course_name: str, credits: int,
                      department: str, faculty_id: str, semester: str,
                      max_students: int = 50) -> Course:
        """Create a new course"""
        # Business rule: Course ID must be unique
        if self.course_repo.exists(course_id):
            raise ValueError(f"Course with ID {course_id} already exists")
        
        # Business rule: Credits must be positive
        if credits <= 0:
            raise ValueError("Credits must be positive")
        
        # Business rule: Max students must be positive
        if max_students <= 0:
            raise ValueError("Max students must be positive")
        
        course = Course(course_id, course_name, credits, department, faculty_id, semester, max_students)
        self.course_repo.save(course)
        return course
    
    def get_course_by_id(self, course_id: str) -> Optional[Course]:
        """Get course by ID"""
        return self.course_repo.find_by_id(course_id)
    
    def get_course_by_code(self, course_code: str) -> Optional[Course]:
        """Get course by course code"""
        return self.course_repo.find_by_course_code(course_code)
    
    def get_all_courses(self) -> List[Course]:
        """Get all courses"""
        return self.course_repo.find_all()
    
    def get_courses_by_department(self, department: str) -> List[Course]:
        """Get courses by department"""
        return self.course_repo.find_by_department(department)
    
    def get_courses_by_faculty(self, faculty_id: str) -> List[Course]:
        """Get courses taught by a faculty member"""
        return self.course_repo.find_by_faculty(faculty_id)
    
    def get_courses_with_capacity(self) -> List[Course]:
        """Get courses that are not full"""
        return self.course_repo.find_courses_with_capacity()
    
    def enroll_student(self, course_id: str, student_id: str) -> Course:
        """Enroll a student in a course"""
        course = self.course_repo.find_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        
        # Business rule: Check if course is full
        if len(course._enrolled_students) >= course._max_students:
            raise ValueError(f"Course {course_id} is full")
        
        course.add_student(student_id)
        self.course_repo.save(course)
        return course
    
    def update_course(self, course_id: str, **kwargs) -> Course:
        """Update course details"""
        course = self.course_repo.find_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        
        # Update allowed fields
        if 'course_name' in kwargs:
            course._course_name = kwargs['course_name']
        if 'max_students' in kwargs:
            if kwargs['max_students'] <= 0:
                raise ValueError("Max students must be positive")
            course._max_students = kwargs['max_students']
        
        self.course_repo.save(course)
        return course
    
    def delete_course(self, course_id: str) -> bool:
        """Delete a course"""
        if not self.course_repo.exists(course_id):
            raise ValueError(f"Course with ID {course_id} not found")
        self.course_repo.delete(course_id)
        return True