"""
In-memory implementation using HashMap (Python dict) for Assignment entities
"""

from typing import Optional, List, Dict
from datetime import datetime, timedelta
from src.repositories.assignment_repository import AssignmentRepository, SubmissionRepository
from src.domain.assignment import Assignment, Submission


class InMemoryAssignmentRepository(AssignmentRepository):
    """In-memory implementation of AssignmentRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Assignment] = {}
    
    def save(self, entity: Assignment) -> None:
        self._storage[entity._assignment_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Assignment]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Assignment]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_course(self, course_id: str) -> List[Assignment]:
        return [assignment for assignment in self._storage.values() if assignment._course_id == course_id]
    
    def find_by_due_date_range(self, start_date: datetime, end_date: datetime) -> List[Assignment]:
        return [assignment for assignment in self._storage.values() 
                if start_date <= assignment._due_date <= end_date]
    
    def find_past_due_assignments(self) -> List[Assignment]:
        now = datetime.now()
        return [assignment for assignment in self._storage.values() if assignment._due_date < now]
    
    def find_upcoming_assignments(self, days: int) -> List[Assignment]:
        now = datetime.now()
        future = now + timedelta(days=days)
        return [assignment for assignment in self._storage.values() 
                if now <= assignment._due_date <= future]


class InMemorySubmissionRepository(SubmissionRepository):
    """In-memory implementation of SubmissionRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Submission] = {}
    
    def save(self, entity: Submission) -> None:
        self._storage[entity._submission_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Submission]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Submission]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_assignment(self, assignment_id: str) -> List[Submission]:
        return [sub for sub in self._storage.values() if sub._assignment_id == assignment_id]
    
    def find_by_student(self, student_id: str) -> List[Submission]:
        return [sub for sub in self._storage.values() if sub._student_id == student_id]
    
    def find_by_student_and_assignment(self, student_id: str, assignment_id: str) -> Optional[Submission]:
        for sub in self._storage.values():
            if sub._student_id == student_id and sub._assignment_id == assignment_id:
                return sub
        return None
    
    def find_late_submissions(self) -> List[Submission]:
        return [sub for sub in self._storage.values() if sub._is_late]
    
    def find_ungraded_submissions(self) -> List[Submission]:
        return [sub for sub in self._storage.values() if sub._score is None]