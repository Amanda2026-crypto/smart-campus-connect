"""
User API routes
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
import re
from src.api.models.schemas import (
    UserCreate, UserResponse, LoginRequest, LoginResponse, ErrorResponse
)
from src.services.user_service import UserService

router = APIRouter(prefix="/api/users", tags=["Users"])
user_service = UserService()


def validate_user_registration(user_data: UserCreate):
    """Validate user registration input data"""
    
    # Validate user_id
    if not user_data.user_id or not user_data.user_id.strip():
        raise HTTPException(status_code=400, detail="User ID cannot be empty")
    
    # Validate password
    if not user_data.password or len(user_data.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    
    if not any(c.isdigit() for c in user_data.password):
        raise HTTPException(status_code=400, detail="Password must contain at least one number")
    
    if not any(c.isalpha() for c in user_data.password):
        raise HTTPException(status_code=400, detail="Password must contain at least one letter")
    
    # Validate first name
    if not user_data.first_name or not user_data.first_name.strip():
        raise HTTPException(status_code=400, detail="First name cannot be empty")
    
    if len(user_data.first_name) > 50:
        raise HTTPException(status_code=400, detail="First name cannot exceed 50 characters")
    
    # Validate last name
    if not user_data.last_name or not user_data.last_name.strip():
        raise HTTPException(status_code=400, detail="Last name cannot be empty")
    
    if len(user_data.last_name) > 50:
        raise HTTPException(status_code=400, detail="Last name cannot exceed 50 characters")
    
    # Validate department
    if not user_data.department or not user_data.department.strip():
        raise HTTPException(status_code=400, detail="Department cannot be empty")
    
    return True


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate):
    """Register a new user (student, faculty, or admin)"""
    
    # Validate input before processing
    validate_user_registration(user_data)
    
    try:
        if user_data.role == "STUDENT":
            if not user_data.student_id:
                raise HTTPException(status_code=400, detail="student_id required for STUDENT role")
            user = user_service.register_student(
                user_data.user_id, user_data.email, user_data.password,
                user_data.first_name, user_data.last_name,
                user_data.student_id, user_data.department
            )
        elif user_data.role == "FACULTY":
            if not user_data.staff_id:
                raise HTTPException(status_code=400, detail="staff_id required for FACULTY role")
            user = user_service.register_faculty(
                user_data.user_id, user_data.email, user_data.password,
                user_data.first_name, user_data.last_name,
                user_data.staff_id, user_data.department
            )
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported role: {user_data.role}")
        
        return UserResponse(
            user_id=user.user_id,
            email=user.email,
            first_name=user._first_name,
            last_name=user._last_name,
            role=user._role.value,
            is_active=user.is_active
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    """Authenticate a user"""
    try:
        result = user_service.login(login_data.email, login_data.password)
        return LoginResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    """Get user by ID"""
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    return UserResponse(
        user_id=user.user_id,
        email=user.email,
        first_name=user._first_name,
        last_name=user._last_name,
        role=user._role.value,
        is_active=user.is_active
    )


@router.get("/", response_model=List[UserResponse])
async def get_all_users():
    """Get all users"""
    users = user_service.get_all_users()
    return [
        UserResponse(
            user_id=u.user_id,
            email=u.email,
            first_name=u._first_name,
            last_name=u._last_name,
            role=u._role.value,
            is_active=u.is_active
        ) for u in users
    ]


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    """Delete a user"""
    try:
        user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{user_id}/deactivate", response_model=UserResponse)
async def deactivate_user(user_id: str):
    """Deactivate a user account"""
    try:
        user_service.deactivate_user(user_id)
        user = user_service.get_user_by_id(user_id)
        return UserResponse(
            user_id=user.user_id,
            email=user.email,
            first_name=user._first_name,
            last_name=user._last_name,
            role=user._role.value,
            is_active=user.is_active
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))