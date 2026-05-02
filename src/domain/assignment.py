from datetime import datetime
from typing import Optional, List


class Assignment:
    """Assignment entity"""
    
    def __init__(self, assignment_id: str, course_id: str, title: str,
                 description: str, due_date: datetime, max_points: int):
        self._assignment_id = assignment_id
        self._course_id = course_id
        self._title = title
        self._description = description
        self._due_date = due_date
        self._max_points = max_points
        self._submissions = []
    
    def publish(self) -> bool:
        """Make assignment visible to students"""
        return True
    
    def update_deadline(self, new_date: datetime) -> bool:
        """Update the due date"""
        if new_date < datetime.now():
            raise ValueError("Due date cannot be in the past")
        self._due_date = new_date
        return True


class Submission:
    """Assignment submission entity"""
    
    def __init__(self, submission_id: str, assignment_id: str, student_id: str, file_url: str):
        self._submission_id = submission_id
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._file_url = file_url
        self._submitted_at = datetime.now()
        self._is_late = False
        self._score = None
        self._feedback = None
    
    def submit(self) -> bool:
        """Submit the assignment"""
        return True
    
    def grade(self, score: int, feedback: str) -> bool:
        """Grade the submission"""
        self._score = score
        self._feedback = feedback
        return True