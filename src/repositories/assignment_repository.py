"""
Entity-specific repository interfaces for Assignment domain
"""

from abc import abstractmethod
from typing import Optional, List
from datetime import datetime
from src.repositories.repository_interface import Repository
from src.domain.assignment import Assignment, Submission


class AssignmentRepository(Repository[Assignment, str]):
    """Repository for Assignment entities"""
    
    @abstractmethod
    def find_by_course(self, course_id: str) -> List[Assignment]:
        """Find all assignments for a course"""
        pass
    
    @abstractmethod
    def find_by_due_date_range(self, start_date: datetime, end_date: datetime) -> List[Assignment]:
        """Find assignments due within a date range"""
        pass
    
    @abstractmethod
    def find_past_due_assignments(self) -> List[Assignment]:
        """Find assignments with due date in the past"""
        pass
    
    @abstractmethod
    def find_upcoming_assignments(self, days: int) -> List[Assignment]:
        """Find assignments due in the next X days"""
        pass


class SubmissionRepository(Repository[Submission, str]):
    """Repository for Submission entities"""
    
    @abstractmethod
    def find_by_assignment(self, assignment_id: str) -> List[Submission]:
        """Find all submissions for an assignment"""
        pass
    
    @abstractmethod
    def find_by_student(self, student_id: str) -> List[Submission]:
        """Find all submissions by a student"""
        pass
    
    @abstractmethod
    def find_by_student_and_assignment(self, student_id: str, assignment_id: str) -> Optional[Submission]:
        """Find a specific student's submission for an assignment"""
        pass
    
    @abstractmethod
    def find_late_submissions(self) -> List[Submission]:
        """Find all late submissions"""
        pass
    
    @abstractmethod
    def find_ungraded_submissions(self) -> List[Submission]:
        """Find submissions that haven't been graded yet"""
        pass