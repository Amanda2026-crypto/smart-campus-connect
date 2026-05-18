"""
Assignment API routes
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from src.api.models.schemas import (
    AssignmentCreate, AssignmentResponse, SubmissionCreate,
    SubmissionResponse, GradeSubmission
)
from src.services.assignment_service import AssignmentService

router = APIRouter(prefix="/api/assignments", tags=["Assignments"])
assignment_service = AssignmentService()


@router.post("/", response_model=AssignmentResponse, status_code=status.HTTP_201_CREATED)
async def create_assignment(assignment_data: AssignmentCreate):
    """Create a new assignment"""
    try:
        assignment = assignment_service.create_assignment(
            assignment_data.assignment_id, assignment_data.course_id,
            assignment_data.title, assignment_data.description,
            assignment_data.due_date, assignment_data.max_points
        )
        return AssignmentResponse(
            assignment_id=assignment._assignment_id,
            course_id=assignment._course_id,
            title=assignment._title,
            description=assignment._description,
            due_date=assignment._due_date,
            max_points=assignment._max_points,
            submission_count=len(assignment._submissions)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{assignment_id}", response_model=AssignmentResponse)
async def get_assignment(assignment_id: str):
    """Get assignment by ID"""
    assignment = assignment_service.get_assignment_by_id(assignment_id)
    if not assignment:
        raise HTTPException(status_code=404, detail=f"Assignment with ID {assignment_id} not found")
    
    return AssignmentResponse(
        assignment_id=assignment._assignment_id,
        course_id=assignment._course_id,
        title=assignment._title,
        description=assignment._description,
        due_date=assignment._due_date,
        max_points=assignment._max_points,
        submission_count=len(assignment._submissions)
    )


@router.get("/", response_model=List[AssignmentResponse])
async def get_assignments(course_id: str = None, upcoming_days: int = None):
    """Get assignments, optionally filtered by course or upcoming"""
    if course_id:
        assignments = assignment_service.get_assignments_by_course(course_id)
    elif upcoming_days:
        assignments = assignment_service.get_upcoming_assignments(upcoming_days)
    else:
        assignments = assignment_service.get_all_assignments()
    
    return [
        AssignmentResponse(
            assignment_id=a._assignment_id,
            course_id=a._course_id,
            title=a._title,
            description=a._description,
            due_date=a._due_date,
            max_points=a._max_points,
            submission_count=len(a._submissions)
        ) for a in assignments
    ]


@router.post("/{assignment_id}/submit", response_model=SubmissionResponse, status_code=status.HTTP_201_CREATED)
async def submit_assignment(assignment_id: str, submission_data: SubmissionCreate):
    """Submit an assignment"""
    try:
        submission = assignment_service.submit_assignment(
            submission_data.submission_id, assignment_id,
            submission_data.student_id, submission_data.file_url
        )
        return SubmissionResponse(
            submission_id=submission._submission_id,
            assignment_id=submission._assignment_id,
            student_id=submission._student_id,
            file_url=submission._file_url,
            submitted_at=submission._submitted_at,
            is_late=submission._is_late,
            score=submission._score,
            feedback=submission._feedback
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/submissions/{submission_id}/grade", response_model=SubmissionResponse)
async def grade_submission(submission_id: str, grade_data: GradeSubmission):
    """Grade a submission"""
    try:
        submission = assignment_service.grade_submission(
            submission_id, grade_data.score, grade_data.feedback
        )
        return SubmissionResponse(
            submission_id=submission._submission_id,
            assignment_id=submission._assignment_id,
            student_id=submission._student_id,
            file_url=submission._file_url,
            submitted_at=submission._submitted_at,
            is_late=submission._is_late,
            score=submission._score,
            feedback=submission._feedback
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/submissions/ungraded", response_model=List[SubmissionResponse])
async def get_ungraded_submissions():
    """Get all ungraded submissions"""
    submissions = assignment_service.get_ungraded_submissions()
    return [
        SubmissionResponse(
            submission_id=s._submission_id,
            assignment_id=s._assignment_id,
            student_id=s._student_id,
            file_url=s._file_url,
            submitted_at=s._submitted_at,
            is_late=s._is_late,
            score=s._score,
            feedback=s._feedback
        ) for s in submissions
    ]