"""
Repository Factory Pattern for storage abstraction.
Allows easy switching between different storage backends.
"""

from typing import Dict, Any
from src.repositories.user_repository import UserRepository, StudentRepository, FacultyRepository, AdminRepository
from src.repositories.course_repository import CourseRepository
from src.repositories.assignment_repository import AssignmentRepository, SubmissionRepository
from src.repositories.booking_repository import StudyRoomRepository, BookingRepository
from src.repositories.event_repository import EventRepository, EventRegistrationRepository

# In-memory implementations
from src.repositories.inmemory.inmemory_user_repository import (
    InMemoryUserRepository, InMemoryStudentRepository, 
    InMemoryFacultyRepository, InMemoryAdminRepository
)
from src.repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository
from src.repositories.inmemory.inmemory_assignment_repository import (
    InMemoryAssignmentRepository, InMemorySubmissionRepository
)
from src.repositories.inmemory.inmemory_booking_repository import (
    InMemoryStudyRoomRepository, InMemoryBookingRepository
)
from src.repositories.inmemory.inmemory_event_repository import (
    InMemoryEventRepository, InMemoryEventRegistrationRepository
)


class RepositoryFactory:
    """
    Factory for creating repository instances.
    Currently supports "MEMORY" storage type.
    Easily extendable to support "DATABASE", "FILESYSTEM", etc.
    """
    
    @classmethod
    def get_user_repository(cls, storage_type: str = "MEMORY") -> UserRepository:
        if storage_type == "MEMORY":
            return InMemoryUserRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_student_repository(cls, storage_type: str = "MEMORY") -> StudentRepository:
        if storage_type == "MEMORY":
            return InMemoryStudentRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_faculty_repository(cls, storage_type: str = "MEMORY") -> FacultyRepository:
        if storage_type == "MEMORY":
            return InMemoryFacultyRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_admin_repository(cls, storage_type: str = "MEMORY") -> AdminRepository:
        if storage_type == "MEMORY":
            return InMemoryAdminRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_course_repository(cls, storage_type: str = "MEMORY") -> CourseRepository:
        if storage_type == "MEMORY":
            return InMemoryCourseRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_assignment_repository(cls, storage_type: str = "MEMORY") -> AssignmentRepository:
        if storage_type == "MEMORY":
            return InMemoryAssignmentRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_submission_repository(cls, storage_type: str = "MEMORY") -> SubmissionRepository:
        if storage_type == "MEMORY":
            return InMemorySubmissionRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_study_room_repository(cls, storage_type: str = "MEMORY") -> StudyRoomRepository:
        if storage_type == "MEMORY":
            return InMemoryStudyRoomRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_booking_repository(cls, storage_type: str = "MEMORY") -> BookingRepository:
        if storage_type == "MEMORY":
            return InMemoryBookingRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_event_repository(cls, storage_type: str = "MEMORY") -> EventRepository:
        if storage_type == "MEMORY":
            return InMemoryEventRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")
    
    @classmethod
    def get_event_registration_repository(cls, storage_type: str = "MEMORY") -> EventRegistrationRepository:
        if storage_type == "MEMORY":
            return InMemoryEventRegistrationRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")


repository_factory = RepositoryFactory()