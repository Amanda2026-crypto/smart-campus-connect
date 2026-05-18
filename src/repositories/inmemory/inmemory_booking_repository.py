"""
In-memory implementation using HashMap (Python dict) for Booking entities
"""

from typing import Optional, List, Dict
from datetime import datetime, timedelta
from src.repositories.booking_repository import StudyRoomRepository, BookingRepository
from src.domain.booking import StudyRoom, Booking, BookingStatus


class InMemoryStudyRoomRepository(StudyRoomRepository):
    """In-memory implementation of StudyRoomRepository"""
    
    def __init__(self):
        self._storage: Dict[str, StudyRoom] = {}
    
    def save(self, entity: StudyRoom) -> None:
        self._storage[entity._room_id] = entity
    
    def find_by_id(self, id: str) -> Optional[StudyRoom]:
        return self._storage.get(id)
    
    def find_all(self) -> List[StudyRoom]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_building(self, building: str) -> List[StudyRoom]:
        return [room for room in self._storage.values() if room._building == building]
    
    def find_by_capacity(self, min_capacity: int) -> List[StudyRoom]:
        return [room for room in self._storage.values() if room._capacity >= min_capacity]
    
    def find_available_rooms(self, start_time: datetime, end_time: datetime) -> List[StudyRoom]:
        return [room for room in self._storage.values() if room._is_available]


class InMemoryBookingRepository(BookingRepository):
    """In-memory implementation of BookingRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Booking] = {}
    
    def save(self, entity: Booking) -> None:
        self._storage[entity._booking_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Booking]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Booking]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_student(self, student_id: str) -> List[Booking]:
        return [booking for booking in self._storage.values() if booking._student_id == student_id]
    
    def find_by_room(self, room_id: str) -> List[Booking]:
        return [booking for booking in self._storage.values() if booking._room_id == room_id]
    
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Booking]:
        return [booking for booking in self._storage.values() 
                if start_date <= booking._start_time <= end_date]
    
    def find_active_bookings(self) -> List[Booking]:
        now = datetime.now()
        return [booking for booking in self._storage.values() 
                if booking._status == BookingStatus.CONFIRMED and booking._start_time <= now <= booking._end_time]
    
    def find_upcoming_bookings(self, student_id: str) -> List[Booking]:
        now = datetime.now()
        return [booking for booking in self._storage.values() 
                if booking._student_id == student_id and booking._start_time > now]