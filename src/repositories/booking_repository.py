"""
Entity-specific repository interfaces for Booking domain
"""

from abc import abstractmethod
from typing import Optional, List
from datetime import datetime
from src.repositories.repository_interface import Repository
from src.domain.booking import Booking, StudyRoom


class StudyRoomRepository(Repository[StudyRoom, str]):
    """Repository for StudyRoom entities"""
    
    @abstractmethod
    def find_by_building(self, building: str) -> List[StudyRoom]:
        """Find rooms by building name"""
        pass
    
    @abstractmethod
    def find_by_capacity(self, min_capacity: int) -> List[StudyRoom]:
        """Find rooms with at least min_capacity"""
        pass
    
    @abstractmethod
    def find_available_rooms(self, start_time: datetime, end_time: datetime) -> List[StudyRoom]:
        """Find rooms available during a time slot"""
        pass


class BookingRepository(Repository[Booking, str]):
    """Repository for Booking entities"""
    
    @abstractmethod
    def find_by_student(self, student_id: str) -> List[Booking]:
        """Find all bookings made by a student"""
        pass
    
    @abstractmethod
    def find_by_room(self, room_id: str) -> List[Booking]:
        """Find all bookings for a specific room"""
        pass
    
    @abstractmethod
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Booking]:
        """Find bookings within a date range"""
        pass
    
    @abstractmethod
    def find_active_bookings(self) -> List[Booking]:
        """Find currently active (confirmed and in progress) bookings"""
        pass
    
    @abstractmethod
    def find_upcoming_bookings(self, student_id: str) -> List[Booking]:
        """Find a student's upcoming bookings"""
        pass