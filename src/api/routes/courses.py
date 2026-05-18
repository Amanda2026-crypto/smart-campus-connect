"""
Course API routes
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from src.api.models.schemas import (
    CourseCreate, CourseResponse, CourseUpdate, ErrorResponse
)
from src.services.course_service import CourseService

router = APIRouter(prefix="/api/courses", tags=["Courses"])
course_service = CourseService()


@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course_data: CourseCreate):
    """Create a new course"""
    try:
        course = course_service.create_course(
            course_data.course_id, course_data.course_name, course_data.credits,
            course_data.department, course_data.faculty_id, course_data.semester,
            course_data.max_students
        )
        return CourseResponse(
            course_id=course.course_id,
            course_name=course._course_name,
            credits=course._credits,
            department=course._department,
            faculty_id=course._faculty_id,
            semester=course._semester,
            max_students=course._max_students,
            enrolled_count=len(course._enrolled_students)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{course_id}", response_model=CourseResponse)
async def get_course(course_id: str):
    """Get course by ID"""
    course = course_service.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found")
    
    return CourseResponse(
        course_id=course.course_id,
        course_name=course._course_name,
        credits=course._credits,
        department=course._department,
        faculty_id=course._faculty_id,
        semester=course._semester,
        max_students=course._max_students,
        enrolled_count=len(course._enrolled_students)
    )


@router.get("/", response_model=List[CourseResponse])
async def get_all_courses(department: str = None, faculty_id: str = None):
    """Get all courses, optionally filtered by department or faculty"""
    if department:
        courses = course_service.get_courses_by_department(department)
    elif faculty_id:
        courses = course_service.get_courses_by_faculty(faculty_id)
    else:
        courses = course_service.get_all_courses()
    
    return [
        CourseResponse(
            course_id=c.course_id,
            course_name=c._course_name,
            credits=c._credits,
            department=c._department,
            faculty_id=c._faculty_id,
            semester=c._semester,
            max_students=c._max_students,
            enrolled_count=len(c._enrolled_students)
        ) for c in courses
    ]


@router.put("/{course_id}", response_model=CourseResponse)
async def update_course(course_id: str, update_data: CourseUpdate):
    """Update a course"""
    try:
        course = course_service.update_course(course_id, **update_data.dict(exclude_unset=True))
        return CourseResponse(
            course_id=course.course_id,
            course_name=course._course_name,
            credits=course._credits,
            department=course._department,
            faculty_id=course._faculty_id,
            semester=course._semester,
            max_students=course._max_students,
            enrolled_count=len(course._enrolled_students)
        )
    except ValueError as e:
        raise HTTPException(status_code=400 if "not found" not in str(e) else 404, detail=str(e))


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: str):
    """Delete a course"""
    try:
        course_service.delete_course(course_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{course_id}/enroll/{student_id}", response_model=CourseResponse)
async def enroll_student(course_id: str, student_id: str):
    """Enroll a student in a course"""
    try:
        course = course_service.enroll_student(course_id, student_id)
        return CourseResponse(
            course_id=course.course_id,
            course_name=course._course_name,
            credits=course._credits,
            department=course._department,
            faculty_id=course._faculty_id,
            semester=course._semester,
            max_students=course._max_students,
            enrolled_count=len(course._enrolled_students)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))