"""
In-memory implementation using HashMap (Python dict) for Course entities
"""

from typing import Optional, List, Dict
from src.repositories.course_repository import CourseRepository
from src.domain.course import Course


class InMemoryCourseRepository(CourseRepository):
    """In-memory implementation of CourseRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Course] = {}
    
    def save(self, entity: Course) -> None:
        self._storage[entity.course_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Course]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Course]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_course_code(self, course_code: str) -> Optional[Course]:
        for course in self._storage.values():
            if course.course_id == course_code:
                return course
        return None
    
    def find_by_department(self, department: str) -> List[Course]:
        return [course for course in self._storage.values() if course._department == department]
    
    def find_by_faculty(self, faculty_id: str) -> List[Course]:
        return [course for course in self._storage.values() if course._faculty_id == faculty_id]
    
    def find_by_semester(self, semester: str) -> List[Course]:
        return [course for course in self._storage.values() if course._semester == semester]
    
    def find_courses_with_capacity(self) -> List[Course]:
        return [course for course in self._storage.values() if len(course._enrolled_students) < course._max_students]