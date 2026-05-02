from datetime import datetime
from enum import Enum


class EventStatus(Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PUBLISHED = "PUBLISHED"
    COMPLETED = "COMPLETED"


class Event:
    """Event entity"""
    
    def __init__(self, event_id: str, title: str, description: str,
                 start_time: datetime, end_time: datetime, location: str,
                 organizer_id: str, max_attendees: int):
        self._event_id = event_id
        self._title = title
        self._description = description
        self._start_time = start_time
        self._end_time = end_time
        self._location = location
        self._organizer_id = organizer_id
        self._max_attendees = max_attendees
        self._status = EventStatus.DRAFT
        self._registrations = []
    
    def submit_for_approval(self) -> bool:
        """Submit event for admin approval"""
        self._status = EventStatus.SUBMITTED
        return True
    
    def approve(self) -> bool:
        """Admin approves the event"""
        self._status = EventStatus.APPROVED
        return True
    
    def reject(self, reason: str) -> bool:
        """Admin rejects the event"""
        self._status = EventStatus.REJECTED
        self._rejection_reason = reason
        return True


class EventRegistration:
    """Event registration entity"""
    
    def __init__(self, registration_id: str, event_id: str, student_id: str):
        self._registration_id = registration_id
        self._event_id = event_id
        self._student_id = student_id
        self._registered_at = datetime.now()
        self._attended = False
    
    def register(self) -> bool:
        """Register for event"""
        return True
    
    def cancel(self) -> bool:
        """Cancel registration"""
        return True
    
    def check_in(self) -> bool:
        """Mark attendance at event"""
        self._attended = True
        return True