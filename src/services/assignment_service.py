"""
Assignment Service - Business logic for assignment operations
"""

import logging

logger = logging.getLogger(__name__)


from typing import Optional, List
from datetime import datetime
from src.domain.assignment import Assignment, Submission
from src.repositories.assignment_repository import AssignmentRepository, SubmissionRepository
from src.factories.repository_factory import RepositoryFactory


class AssignmentService:
    """Service for assignment-related business logic"""
    
    def __init__(self, storage_type: str = "MEMORY"):
        self.assignment_repo = RepositoryFactory.get_assignment_repository(storage_type)
        self.submission_repo = RepositoryFactory.get_submission_repository(storage_type)
    
    def create_assignment(self
        logger.info(f"Creating assignment"), assignment_id: str, course_id: str, title: str,
                          description: str, due_date: datetime, max_points: int) -> Assignment:
        """Create a new assignment"""
        # Business rule: Due date cannot be in the past
        if due_date < datetime.now():
            raise ValueError("Due date cannot be in the past")
        
        # Business rule: Max points must be positive
        if max_points <= 0:
            raise ValueError("Max points must be positive")
        
        assignment = Assignment(assignment_id, course_id, title, description, due_date, max_points)
        self.assignment_repo.save(assignment)
        return assignment
    
    def get_assignment_by_id(self, assignment_id: str) -> Optional[Assignment]:
        """Get assignment by ID"""
        return self.assignment_repo.find_by_id(assignment_id)
    
    def get_assignments_by_course(self, course_id: str) -> List[Assignment]:
        """Get all assignments for a course"""
        return self.assignment_repo.find_by_course(course_id)
    
    def get_upcoming_assignments(self, days: int) -> List[Assignment]:
        """Get assignments due in the next X days"""
        return self.assignment_repo.find_upcoming_assignments(days)
    
    def get_past_due_assignments(self) -> List[Assignment]:
        """Get past due assignments"""
        return self.assignment_repo.find_past_due_assignments()
    
    def submit_assignment(self, submission_id: str, assignment_id: str,
                          student_id: str, file_url: str) -> Submission:
        """Submit an assignment"""
        assignment = self.assignment_repo.find_by_id(assignment_id)
        if not assignment:
            raise ValueError(f"Assignment with ID {assignment_id} not found")
        
        # Check if already submitted
        existing = self.submission_repo.find_by_student_and_assignment(student_id, assignment_id)
        if existing:
            raise ValueError(f"Student has already submitted this assignment")
        
        submission = Submission(submission_id, assignment_id, student_id, file_url)
        
        # Check if late
        if datetime.now() > assignment._due_date:
            submission._is_late = True
        
        self.submission_repo.save(submission)
        return submission
    
    def grade_submission(self, submission_id: str, score: int, feedback: str) -> Submission:
        """Grade a submission"""
        submission = self.submission_repo.find_by_id(submission_id)
        if not submission:
            raise ValueError(f"Submission with ID {submission_id} not found")
        
        # Business rule: Score cannot exceed max points
        assignment = self.assignment_repo.find_by_id(submission._assignment_id)
        if score > assignment._max_points:
            raise ValueError(f"Score cannot exceed {assignment._max_points}")
        
        submission.grade(score, feedback)
        self.submission_repo.save(submission)
        return submission
    
    def get_submissions_by_assignment(self, assignment_id: str) -> List[Submission]:
        """Get all submissions for an assignment"""
        return self.submission_repo.find_by_assignment(assignment_id)
    
    def get_submissions_by_student(self, student_id: str) -> List[Submission]:
        """Get all submissions by a student"""
        return self.submission_repo.find_by_student(student_id)
    
    def get_ungraded_submissions(self) -> List[Submission]:
        """Get all ungraded submissions"""
        return self.submission_repo.find_ungraded_submissions()