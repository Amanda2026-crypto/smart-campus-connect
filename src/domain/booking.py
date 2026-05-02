from datetime import datetime
from enum import Enum


class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


class StudyRoom:
    """Study room entity"""
    
    def __init__(self, room_id: str, building: str, capacity: int, amenities: list):
        self._room_id = room_id
        self._building = building
        self._capacity = capacity
        self._amenities = amenities
        self._is_available = True
    
    def check_availability(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if room is available for given time slot"""
        # Simplified availability check
        return self._is_available
    
    def release_room(self, booking_id: str) -> bool:
        """Release room after booking"""
        self._is_available = True
        return True


class Booking:
    """Booking entity"""
    
    def __init__(self, booking_id: str, room_id: str, student_id: str,
                 start_time: datetime, end_time: datetime):
        self._booking_id = booking_id
        self._room_id = room_id
        self._student_id = student_id
        self._start_time = start_time
        self._end_time = end_time
        self._status = BookingStatus.PENDING
        self._qr_code = None
    
    def confirm(self) -> bool:
        """Confirm the booking"""
        self._status = BookingStatus.CONFIRMED
        self._qr_code = f"QR_{self._booking_id}"
        return True
    
    def cancel(self) -> bool:
        """Cancel the booking"""
        self._status = BookingStatus.CANCELLED
        return True