from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import List, Optional


class Role(Enum):
    STUDENT = "STUDENT"
    FACULTY = "FACULTY"
    ADMIN = "ADMIN"


class User(ABC):
    """Abstract base class for all system users"""
    
    def __init__(self, user_id: str, email: str, password_hash: str, 
                 first_name: str, last_name: str, role: Role):
        self._user_id = user_id
        self._email = email
        self._password_hash = password_hash
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._created_at = datetime.now()
        self._is_active = True
    
    @property
    def user_id(self) -> str:
        return self._user_id
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    def register(self) -> bool:
        """Register user account"""
        if not self._email.endswith("@mycput.ac.za"):
            raise ValueError("Email must be a valid CPUT email address")
        return True
    
    def login(self, password: str) -> bool:
        """Authenticate user"""
        # Simulate password verification
        return self._password_hash == password
    
    def update_profile(self, first_name: str = None, last_name: str = None) -> bool:
        """Update user profile information"""
        if first_name:
            self._first_name = first_name
        if last_name:
            self._last_name = last_name
        return True
    
    def deactivate(self) -> bool:
        """Deactivate user account"""
        self._is_active = False
        return True


class Student(User):
    """Student user class"""
    
    def __init__(self, user_id: str, email: str, password_hash: str,
                 first_name: str, last_name: str, student_id: str, department: str):
        super().__init__(user_id, email, password_hash, first_name, last_name, Role.STUDENT)
        self._student_id = student_id
        self._department = department
        self._graduation_year = None
        self._enrolled_courses = []
    
    @property
    def student_id(self) -> str:
        return self._student_id
    
    def enroll_in_course(self, course_id: str) -> bool:
        """Enroll student in a course"""
        if course_id not in self._enrolled_courses:
            self._enrolled_courses.append(course_id)
            return True
        return False
    
    def submit_assignment(self, assignment_id: str, file_path: str) -> bool:
        """Submit an assignment"""
        # Simulate submission
        return True
    
    def view_meal_plan(self) -> dict:
        """View meal plan balance"""
        return {"remaining_swipes": 32, "dining_dollars": 450.00}


class Faculty(User):
    """Faculty user class"""
    
    def __init__(self, user_id: str, email: str, password_hash: str,
                 first_name: str, last_name: str, staff_id: str, department: str):
        super().__init__(user_id, email, password_hash, first_name, last_name, Role.FACULTY)
        self._staff_id = staff_id
        self._department = department
        self._office_location = None
    
    def create_assignment(self, course_id: str, title: str, description: str, 
                          due_date: datetime, max_points: int) -> dict:
        """Create a new assignment"""
        return {
            "assignment_id": f"ASSIGN_{course_id}_{int(datetime.now().timestamp())}",
            "course_id": course_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "max_points": max_points
        }
    
    def take_attendance(self, course_id: str, date: datetime, student_ids: List[str]) -> dict:
        """Record attendance for students"""
        return {
            "course_id": course_id,
            "date": date,
            "present_count": len(student_ids),
            "records": {sid: "PRESENT" for sid in student_ids}
        }


class Admin(User):
    """Admin user class"""
    
    def __init__(self, user_id: str, email: str, password_hash: str,
                 first_name: str, last_name: str, staff_id: str, admin_role: str):
        super().__init__(user_id, email, password_hash, first_name, last_name, Role.ADMIN)
        self._staff_id = staff_id
        self._admin_role = admin_role
    
    def approve_event(self, event_id: str, decision: bool, reason: str = None) -> dict:
        """Approve or reject an event"""
        return {
            "event_id": event_id,
            "approved": decision,
            "reason": reason,
            "approved_by": self._user_id
        }
    
    def send_emergency_alert(self, title: str, message: str, audience: str) -> dict:
        """Send emergency notification to users"""
        return {
            "alert_id": f"ALERT_{int(datetime.now().timestamp())}",
            "title": title,
            "message": message,
            "audience": audience,
            "sent_at": datetime.now()
        }