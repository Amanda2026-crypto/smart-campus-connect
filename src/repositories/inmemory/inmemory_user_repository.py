"""
In-memory implementation using HashMap (Python dict) for User entities
"""

from typing import Optional, List, Dict
from src.repositories.user_repository import UserRepository, StudentRepository, FacultyRepository, AdminRepository
from src.domain.user import User, Student, Faculty, Admin


class InMemoryUserRepository(UserRepository):
    """In-memory implementation of UserRepository using dictionary storage"""
    
    def __init__(self):
        self._storage: Dict[str, User] = {}
    
    def save(self, entity: User) -> None:
        self._storage[entity.user_id] = entity
    
    def find_by_id(self, id: str) -> Optional[User]:
        return self._storage.get(id)
    
    def find_all(self) -> List[User]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_email(self, email: str) -> Optional[User]:
        for user in self._storage.values():
            if user.email == email:
                return user
        return None
    
    def find_by_role(self, role: str) -> List[User]:
        return [user for user in self._storage.values() if user._role.value == role]
    
    def find_active_users(self) -> List[User]:
        return [user for user in self._storage.values() if user.is_active]


class InMemoryStudentRepository(StudentRepository):
    """In-memory implementation of StudentRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Student] = {}
    
    def save(self, entity: Student) -> None:
        self._storage[entity.user_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Student]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Student]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_student_id(self, student_id: str) -> Optional[Student]:
        for student in self._storage.values():
            if student.student_id == student_id:
                return student
        return None
    
    def find_by_department(self, department: str) -> List[Student]:
        return [student for student in self._storage.values() if student._department == department]
    
    def find_enrolled_courses(self, student_id: str) -> List[str]:
        return []


class InMemoryFacultyRepository(FacultyRepository):
    """In-memory implementation of FacultyRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Faculty] = {}
    
    def save(self, entity: Faculty) -> None:
        self._storage[entity.user_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Faculty]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Faculty]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_staff_id(self, staff_id: str) -> Optional[Faculty]:
        for faculty in self._storage.values():
            if faculty._staff_id == staff_id:
                return faculty
        return None
    
    def find_by_department(self, department: str) -> List[Faculty]:
        return [faculty for faculty in self._storage.values() if faculty._department == department]
    
    def find_teaching_courses(self, faculty_id: str) -> List[str]:
        return []


class InMemoryAdminRepository(AdminRepository):
    """In-memory implementation of AdminRepository"""
    
    def __init__(self):
        self._storage: Dict[str, Admin] = {}
    
    def save(self, entity: Admin) -> None:
        self._storage[entity.user_id] = entity
    
    def find_by_id(self, id: str) -> Optional[Admin]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Admin]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: str) -> bool:
        return id in self._storage
    
    def count(self) -> int:
        return len(self._storage)
    
    def find_by_staff_id(self, staff_id: str) -> Optional[Admin]:
        for admin in self._storage.values():
            if admin._staff_id == staff_id:
                return admin
        return None
    
    def find_by_admin_role(self, admin_role: str) -> List[Admin]:
        return [admin for admin in self._storage.values() if admin._admin_role == admin_role]