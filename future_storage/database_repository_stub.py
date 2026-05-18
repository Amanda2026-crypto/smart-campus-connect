"""
Stub implementation for future database storage backend.
This demonstrates how easy it is to add new storage backends.
"""

from typing import Optional, List, Dict
from src.repositories.user_repository import UserRepository
from src.domain.user import User


class DatabaseUserRepository(UserRepository):
    """
    Stub for future database implementation.
    When ready, this will connect to MySQL/PostgreSQL.
    """
    
    def __init__(self, connection_string: str):
        """
        Initialize database connection.
        
        Args:
            connection_string: Database connection string 
            (e.g., "postgresql://user:pass@localhost/db")
        """
        self._connection_string = connection_string
        self._connected = False
    
    def _connect(self):
        """Establish database connection (stub)"""
        self._connected = True
    
    def _disconnect(self):
        """Close database connection (stub)"""
        self._connected = False
    
    def save(self, entity: User) -> None:
        """Save user to database"""
        self._connect()
        # Future implementation:
        # INSERT INTO users (id, email, password_hash, first_name, last_name, role, created_at, is_active)
        # VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        self._disconnect()
    
    def find_by_id(self, id: str) -> Optional[User]:
        """Find user by ID from database"""
        self._connect()
        # Future implementation:
        # SELECT * FROM users WHERE id = %s
        self._disconnect()
        return None
    
    def find_all(self) -> List[User]:
        """Return all users from database"""
        self._connect()
        # Future implementation:
        # SELECT * FROM users
        self._disconnect()
        return []
    
    def delete(self, id: str) -> None:
        """Delete user from database"""
        self._connect()
        # Future implementation:
        # DELETE FROM users WHERE id = %s
        self._disconnect()
    
    def exists(self, id: str) -> bool:
        """Check if user exists in database"""
        self._connect()
        # Future implementation:
        # SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)
        self._disconnect()
        return False
    
    def count(self) -> int:
        """Return total number of users in database"""
        self._connect()
        # Future implementation:
        # SELECT COUNT(*) FROM users
        self._disconnect()
        return 0
    
    def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email from database"""
        self._connect()
        # Future implementation:
        # SELECT * FROM users WHERE email = %s
        self._disconnect()
        return None
    
    def find_by_role(self, role: str) -> List[User]:
        """Find users by role from database"""
        self._connect()
        # Future implementation:
        # SELECT * FROM users WHERE role = %s
        self._disconnect()
        return []
    
    def find_active_users(self) -> List[User]:
        """Find all active users from database"""
        self._connect()
        # Future implementation:
        # SELECT * FROM users WHERE is_active = true
        self._disconnect()
        return []