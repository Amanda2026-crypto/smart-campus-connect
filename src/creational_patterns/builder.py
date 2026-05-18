"""
Builder Pattern
Use Case: Creating complex Assignment objects with many optional fields
"""

from datetime import datetime
from typing import List, Optional


class Assignment:
    """Complex object to build"""
    
    def __init__(self):
        self.assignment_id = None
        self.course_id = None
        self.title = None
        self.description = None
        self.due_date = None
        self.max_points = None
        self.allowed_file_types = []
        self.attachments = []
        self.is_group_assignment = False
        self.rubric = None
    
    def __str__(self):
        return f"Assignment(id={self.assignment_id}, title={self.title}, due={self.due_date})"


class AssignmentBuilder:
    """Builder for Assignment objects"""
    
    def __init__(self):
        self.assignment = Assignment()
    
    def set_assignment_id(self, assignment_id: str):
        self.assignment.assignment_id = assignment_id
        return self
    
    def set_course_id(self, course_id: str):
        self.assignment.course_id = course_id
        return self
    
    def set_title(self, title: str):
        self.assignment.title = title
        return self
    
    def set_description(self, description: str):
        self.assignment.description = description
        return self
    
    def set_due_date(self, due_date: datetime):
        if due_date < datetime.now():
            raise ValueError("Due date cannot be in the past")
        self.assignment.due_date = due_date
        return self
    
    def set_max_points(self, max_points: int):
        if max_points <= 0:
            raise ValueError("Max points must be positive")
        self.assignment.max_points = max_points
        return self
    
    def add_allowed_file_type(self, file_type: str):
        self.assignment.allowed_file_types.append(file_type)
        return self
    
    def add_attachment(self, attachment_url: str):
        self.assignment.attachments.append(attachment_url)
        return self
    
    def set_as_group_assignment(self, is_group: bool = True):
        self.assignment.is_group_assignment = is_group
        return self
    
    def set_rubric(self, rubric: dict):
        self.assignment.rubric = rubric
        return self
    
    def build(self) -> Assignment:
        """Validate and return the built Assignment"""
        required_fields = ['assignment_id', 'course_id', 'title', 'due_date', 'max_points']
        for field in required_fields:
            if getattr(self.assignment, field) is None:
                raise ValueError(f"Missing required field: {field}")
        return self.assignment


class AssignmentDirector:
    """Director that knows how to build common assignment types"""
    
    @staticmethod
    def create_programming_assignment(builder: AssignmentBuilder, 
                                       assignment_id: str, course_id: str) -> Assignment:
        return (builder
                .set_assignment_id(assignment_id)
                .set_course_id(course_id)
                .set_title("Programming Assignment")
                .set_description("Implement the required functionality")
                .set_due_date(datetime.now().replace(day=datetime.now().day + 14))
                .set_max_points(100)
                .add_allowed_file_type(".py")
                .add_allowed_file_type(".java")
                .add_allowed_file_type(".zip")
                .build())
    
    @staticmethod
    def create_essay_assignment(builder: AssignmentBuilder,
                                 assignment_id: str, course_id: str) -> Assignment:
        return (builder
                .set_assignment_id(assignment_id)
                .set_course_id(course_id)
                .set_title("Essay Assignment")
                .set_description("Write a research essay on the given topic")
                .set_due_date(datetime.now().replace(day=datetime.now().day + 21))
                .set_max_points(50)
                .add_allowed_file_type(".pdf")
                .add_allowed_file_type(".docx")
                .set_rubric({"grammar": 10, "content": 30, "structure": 10})
                .build())