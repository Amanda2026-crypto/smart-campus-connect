from typing import List, Optional
from datetime import datetime


class Course:
    """Course entity"""
    
    def __init__(self, course_id: str, course_name: str, credits: int, 
                 department: str, faculty_id: str, semester: str, max_students: int = 50):
        self._course_id = course_id
        self._course_name = course_name
        self._credits = credits
        self._department = department
        self._faculty_id = faculty_id
        self._semester = semester
        self._max_students = max_students
        self._enrolled_students = []
    
    @property
    def course_id(self) -> str:
        return self._course_id
    
    @property
    def course_name(self) -> str:
        return self._course_name
    
    def add_student(self, student_id: str) -> bool:
        """Add a student to the course"""
        if len(self._enrolled_students) >= self._max_students:
            raise ValueError(f"Course {self._course_id} is full")
        if student_id not in self._enrolled_students:
            self._enrolled_students.append(student_id)
            return True
        return False
    
    def remove_student(self, student_id: str) -> bool:
        """Remove a student from the course"""
        if student_id in self._enrolled_students:
            self._enrolled_students.remove(student_id)
            return True
        return False


class Enrollment:
    """Enrollment relationship between Student and Course"""
    
    def __init__(self, enrollment_id: str, student_id: str, course_id: str):
        self._enrollment_id = enrollment_id
        self._student_id = student_id
        self._course_id = course_id
        self._enrolled_at = datetime.now()
        self._status = "ACTIVE"
        self._grade = None
    
    def drop(self) -> bool:
        """Drop the enrollment"""
        self._status = "DROPPED"
        return True
    
    def complete(self, grade: str) -> bool:
        """Mark course as completed with grade"""
        self._status = "COMPLETED"
        self._grade = grade
        return True