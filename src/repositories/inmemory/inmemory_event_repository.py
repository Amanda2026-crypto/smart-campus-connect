"""
In-memory implementation using HashMap (Python dict) for Event entities
"""

from typing import Optional, List, Dict
from datetime import datetime, timedelta
from src.repositories.event_repository import EventRepository, EventRegistrationRepository
from src.domain.event import Event, EventRegistration, EventStatus


class InMemoryEventRepository(EventRepository):
    """In-memory implementation of EventRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Event] = {}
    
    def save(self, entity: Event) -> None:
        self._storage[entity._event_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Event]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Event]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_organizer(self, organizer_id: str) -> List[Event]:
        return [event for event in self._storage.values() if event._organizer_id == organizer_id]
    
    def find_by_status(self, status: str) -> List[Event]:
        return [event for event in self._storage.values() if event._status.value == status]
    
    def find_published_events(self) -> List[Event]:
        return [event for event in self._storage.values() if event._status == EventStatus.PUBLISHED]
    
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Event]:
        return [event for event in self._storage.values() 
                if start_date <= event._start_time <= end_date]
    
    def find_upcoming_events(self, days: int) -> List[Event]:
        now = datetime.now()
        future = now + timedelta(days=days)
        return [event for event in self._storage.values() 
                if event._status == EventStatus.PUBLISHED and now <= event._start_time <= future]


class InMemoryEventRegistrationRepository(EventRegistrationRepository):
    """In-memory implementation of EventRegistrationRepository"""
    
    def __init__(self):
        self._storage: Dict[str, EventRegistration] = {}
    
    def save(self, entity: EventRegistration) -> None:
        self._storage[entity._registration_id] = entity
    
    def find_by_id(self, id: str) -> Optional[EventRegistration]:
        return self._storage.get(id)
    
    def find_all(self) -> List[EventRegistration]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_event(self, event_id: str) -> List[EventRegistration]:
        return [reg for reg in self._storage.values() if reg._event_id == event_id]
    
    def find_by_student(self, student_id: str) -> List[EventRegistration]:
        return [reg for reg in self._storage.values() if reg._student_id == student_id]
    
    def find_by_student_and_event(self, student_id: str, event_id: str) -> Optional[EventRegistration]:
        for reg in self._storage.values():
            if reg._student_id == student_id and reg._event_id == event_id:
                return reg
        return None
    
    def find_attendees(self, event_id: str) -> List[str]:
        return [reg._student_id for reg in self._storage.values() 
                if reg._event_id == event_id and reg._attended]