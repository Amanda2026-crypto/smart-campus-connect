"""
Entity-specific repository interfaces for Event domain
"""

from abc import abstractmethod
from typing import Optional, List
from datetime import datetime
from src.repositories.repository_interface import Repository
from src.domain.event import Event, EventRegistration


class EventRepository(Repository[Event, str]):
    """Repository for Event entities"""
    
    @abstractmethod
    def find_by_organizer(self, organizer_id: str) -> List[Event]:
        """Find events created by a specific organizer"""
        pass
    
    @abstractmethod
    def find_by_status(self, status: str) -> List[Event]:
        """Find events by status (DRAFT, SUBMITTED, APPROVED, REJECTED, PUBLISHED, COMPLETED)"""
        pass
    
    @abstractmethod
    def find_published_events(self) -> List[Event]:
        """Find all published events visible to students"""
        pass
    
    @abstractmethod
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Event]:
        """Find events happening within a date range"""
        pass
    
    @abstractmethod
    def find_upcoming_events(self, days: int) -> List[Event]:
        """Find events in the next X days"""
        pass


class EventRegistrationRepository(Repository[EventRegistration, str]):
    """Repository for EventRegistration entities"""
    
    @abstractmethod
    def find_by_event(self, event_id: str) -> List[EventRegistration]:
        """Find all registrations for an event"""
        pass
    
    @abstractmethod
    def find_by_student(self, student_id: str) -> List[EventRegistration]:
        """Find all events a student is registered for"""
        pass
    
    @abstractmethod
    def find_by_student_and_event(self, student_id: str, event_id: str) -> Optional[EventRegistration]:
        """Find a specific student's registration for an event"""
        pass
    
    @abstractmethod
    def find_attendees(self, event_id: str) -> List[str]:
        """Find student IDs of attendees for an event"""
        pass