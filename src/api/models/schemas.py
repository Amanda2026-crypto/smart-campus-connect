"""
Pydantic schemas for API request/response validation
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    STUDENT = "STUDENT"
    FACULTY = "FACULTY"
    ADMIN = "ADMIN"


# User schemas
class UserCreate(BaseModel):
    user_id: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    student_id: Optional[str] = None
    staff_id: Optional[str] = None
    department: str
    role: UserRole


class UserResponse(BaseModel):
    user_id: str
    email: str
    first_name: str
    last_name: str
    role: str
    is_active: bool


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    user_id: str
    email: str
    role: str
    first_name: str
    last_name: str


# Course schemas
class CourseCreate(BaseModel):
    course_id: str = Field(..., min_length=3, max_length=10)
    course_name: str
    credits: int = Field(..., ge=1, le=30)
    department: str
    faculty_id: str
    semester: str
    max_students: int = Field(default=50, ge=1, le=200)


class CourseResponse(BaseModel):
    course_id: str
    course_name: str
    credits: int
    department: str
    faculty_id: str
    semester: str
    max_students: int
    enrolled_count: int


class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    max_students: Optional[int] = Field(None, ge=1, le=200)


# Assignment schemas
class AssignmentCreate(BaseModel):
    assignment_id: str
    course_id: str
    title: str
    description: str
    due_date: datetime
    max_points: int = Field(..., ge=1, le=1000)


class AssignmentResponse(BaseModel):
    assignment_id: str
    course_id: str
    title: str
    description: str
    due_date: datetime
    max_points: int
    submission_count: int


class SubmissionCreate(BaseModel):
    submission_id: str
    assignment_id: str
    student_id: str
    file_url: str


class SubmissionResponse(BaseModel):
    submission_id: str
    assignment_id: str
    student_id: str
    file_url: str
    submitted_at: datetime
    is_late: bool
    score: Optional[int] = None
    feedback: Optional[str] = None


class GradeSubmission(BaseModel):
    score: int = Field(..., ge=0)
    feedback: str


# Booking schemas
class StudyRoomCreate(BaseModel):
    room_id: str
    building: str
    capacity: int = Field(..., ge=1, le=100)
    amenities: List[str] = []


class StudyRoomResponse(BaseModel):
    room_id: str
    building: str
    capacity: int
    amenities: List[str]
    is_available: bool


class BookingCreate(BaseModel):
    booking_id: str
    room_id: str
    student_id: str
    start_time: datetime
    end_time: datetime


class BookingResponse(BaseModel):
    booking_id: str
    room_id: str
    student_id: str
    start_time: datetime
    end_time: datetime
    status: str
    qr_code: Optional[str] = None


# Error response
class ErrorResponse(BaseModel):
    error: str
    message: str
    status_code: int