"""
Booking Service - Business logic for study room booking operations
"""

import logging

logger = logging.getLogger(__name__)


from typing import Optional, List
from datetime import datetime, timedelta
from src.domain.booking import StudyRoom, Booking
from src.repositories.booking_repository import StudyRoomRepository, BookingRepository
from src.factories.repository_factory import RepositoryFactory


class BookingService:
    """Service for booking-related business logic"""
    
    def __init__(self, storage_type: str = "MEMORY"):
        self.study_room_repo = RepositoryFactory.get_study_room_repository(storage_type)
        self.booking_repo = RepositoryFactory.get_booking_repository(storage_type)
    
    def create_study_room(self, room_id: str, building: str, capacity: int, amenities: list) -> StudyRoom:
        """Create a new study room"""
        if self.study_room_repo.exists(room_id):
            raise ValueError(f"Room with ID {room_id} already exists")
        
        room = StudyRoom(room_id, building, capacity, amenities)
        self.study_room_repo.save(room)
        return room
    
    def get_study_room_by_id(self, room_id: str) -> Optional[StudyRoom]:
        """Get study room by ID"""
        return self.study_room_repo.find_by_id(room_id)
    
    def get_all_study_rooms(self) -> List[StudyRoom]:
        """Get all study rooms"""
        return self.study_room_repo.find_all()
    
    def get_available_rooms(self, start_time: datetime, end_time: datetime) -> List[StudyRoom]:
        """Get available rooms for a time slot"""
        # Business rule: Booking duration cannot exceed 3 hours
        duration = end_time - start_time
        if duration > timedelta(hours=3):
            raise ValueError("Booking cannot exceed 3 hours")
        
        return self.study_room_repo.find_available_rooms(start_time, end_time)
    
    def create_booking(self
        logger.info(f"Creating booking"), booking_id: str, room_id: str, student_id: str,
                       start_time: datetime, end_time: datetime) -> Booking:
        """Create a new booking"""
        # Business rule: Check room exists
        room = self.study_room_repo.find_by_id(room_id)
        if not room:
            raise ValueError(f"Room with ID {room_id} not found")
        
        # Business rule: Check availability
        available_rooms = self.get_available_rooms(start_time, end_time)
        if room not in available_rooms:
            raise ValueError(f"Room {room_id} is not available at the requested time")
        
        # Business rule: Check if student has conflicting bookings
        existing_bookings = self.booking_repo.find_by_student(student_id)
        for booking in existing_bookings:
            if booking._status.value == "CONFIRMED":
                if (start_time < booking._end_time and end_time > booking._start_time):
                    raise ValueError("Student has a conflicting booking")
        
        booking = Booking(booking_id, room_id, student_id, start_time, end_time)
        booking.confirm()
        self.booking_repo.save(booking)
        return booking
    
    def get_booking_by_id(self, booking_id: str) -> Optional[Booking]:
        """Get booking by ID"""
        return self.booking_repo.find_by_id(booking_id)
    
    def get_bookings_by_student(self, student_id: str) -> List[Booking]:
        """Get all bookings by a student"""
        return self.booking_repo.find_by_student(student_id)
    
    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel a booking"""
        booking = self.booking_repo.find_by_id(booking_id)
        if not booking:
            raise ValueError(f"Booking with ID {booking_id} not found")
        
        # Business rule: Cancellation must be at least 1 hour before start
        if booking._start_time - datetime.now() < timedelta(hours=1):
            raise ValueError("Bookings can only be cancelled at least 1 hour before start time")
        
        booking.cancel()
        self.booking_repo.save(booking)
        return True