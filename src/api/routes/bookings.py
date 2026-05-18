"""
Booking API routes
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime
from src.api.models.schemas import (
    StudyRoomCreate, StudyRoomResponse, BookingCreate, BookingResponse
)
from src.services.booking_service import BookingService

router = APIRouter(prefix="/api/bookings", tags=["Bookings"])
booking_service = BookingService()


@router.post("/rooms", response_model=StudyRoomResponse, status_code=status.HTTP_201_CREATED)
async def create_study_room(room_data: StudyRoomCreate):
    """Create a new study room"""
    try:
        room = booking_service.create_study_room(
            room_data.room_id, room_data.building,
            room_data.capacity, room_data.amenities
        )
        return StudyRoomResponse(
            room_id=room._room_id,
            building=room._building,
            capacity=room._capacity,
            amenities=room._amenities,
            is_available=room._is_available
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/rooms", response_model=List[StudyRoomResponse])
async def get_all_study_rooms(building: str = None):
    """Get all study rooms, optionally filtered by building"""
    if building:
        rooms = booking_service.get_study_rooms_by_building(building)
    else:
        rooms = booking_service.get_all_study_rooms()
    
    return [
        StudyRoomResponse(
            room_id=r._room_id,
            building=r._building,
            capacity=r._capacity,
            amenities=r._amenities,
            is_available=r._is_available
        ) for r in rooms
    ]


@router.get("/rooms/available")
async def get_available_rooms(start_time: datetime, end_time: datetime):
    """Get available rooms for a time slot"""
    try:
        rooms = booking_service.get_available_rooms(start_time, end_time)
        return [
            StudyRoomResponse(
                room_id=r._room_id,
                building=r._building,
                capacity=r._capacity,
                amenities=r._amenities,
                is_available=r._is_available
            ) for r in rooms
        ]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(booking_data: BookingCreate):
    """Create a new booking"""
    try:
        booking = booking_service.create_booking(
            booking_data.booking_id, booking_data.room_id,
            booking_data.student_id, booking_data.start_time,
            booking_data.end_time
        )
        return BookingResponse(
            booking_id=booking._booking_id,
            room_id=booking._room_id,
            student_id=booking._student_id,
            start_time=booking._start_time,
            end_time=booking._end_time,
            status=booking._status.value,
            qr_code=booking._qr_code
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: str):
    """Get booking by ID"""
    booking = booking_service.get_booking_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail=f"Booking with ID {booking_id} not found")
    
    return BookingResponse(
        booking_id=booking._booking_id,
        room_id=booking._room_id,
        student_id=booking._student_id,
        start_time=booking._start_time,
        end_time=booking._end_time,
        status=booking._status.value,
        qr_code=booking._qr_code
    )


@router.get("/student/{student_id}", response_model=List[BookingResponse])
async def get_student_bookings(student_id: str):
    """Get all bookings for a student"""
    bookings = booking_service.get_bookings_by_student(student_id)
    return [
        BookingResponse(
            booking_id=b._booking_id,
            room_id=b._room_id,
            student_id=b._student_id,
            start_time=b._start_time,
            end_time=b._end_time,
            status=b._status.value,
            qr_code=b._qr_code
        ) for b in bookings
    ]


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_booking(booking_id: str):
    """Cancel a booking"""
    try:
        booking_service.cancel_booking(booking_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))