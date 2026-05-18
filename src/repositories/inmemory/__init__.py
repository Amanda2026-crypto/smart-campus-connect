# In-memory repository implementations
from src.repositories.inmemory.inmemory_user_repository import (
    InMemoryUserRepository,
    InMemoryStudentRepository,
    InMemoryFacultyRepository,
    InMemoryAdminRepository
)
from src.repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository
from src.repositories.inmemory.inmemory_assignment_repository import (
    InMemoryAssignmentRepository,
    InMemorySubmissionRepository
)
from src.repositories.inmemory.inmemory_booking_repository import (
    InMemoryStudyRoomRepository,
    InMemoryBookingRepository
)
from src.repositories.inmemory.inmemory_event_repository import (
    InMemoryEventRepository,
    InMemoryEventRegistrationRepository
)