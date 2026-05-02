"""
Singleton Pattern
Use Case: Database connection manager that should have only one instance
"""

import threading
from datetime import datetime
from typing import Optional, List, Dict, Any


class DatabaseConnection:
    """Thread-safe Singleton for database connection"""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._connection_string = "postgresql://localhost:5432/smartcampus"
        self._is_connected = False
        self._query_log = []
        self._initialized = True
    
    def connect(self) -> bool:
        """Establish database connection"""
        if not self._is_connected:
            self._is_connected = True
            self._log_query("CONNECTION ESTABLISHED")
        return self._is_connected
    
    def disconnect(self) -> bool:
        """Close database connection"""
        if self._is_connected:
            self._is_connected = False
            self._log_query("CONNECTION CLOSED")
        return True
    
    def execute_query(self, query: str, params: Optional[Dict] = None) -> List[Dict]:
        """Execute a database query"""
        if not self._is_connected:
            raise Exception("Database not connected. Call connect() first.")
        
        self._log_query(query)
        # Simulate query execution
        return [{"result": "success", "rows_affected": 1}]
    
    def _log_query(self, query: str):
        """Log executed query for audit"""
        self._query_log.append({
            "timestamp": datetime.now(),
            "query": query[:100] + "..." if len(query) > 100 else query
        })
    
    def get_query_log(self) -> List[Dict]:
        """Get audit log of executed queries"""
        return self._query_log.copy()
    
    @property
    def is_connected(self) -> bool:
        return self._is_connected


def get_db_connection() -> DatabaseConnection:
    """Convenience function to get the singleton instance"""
    return DatabaseConnection()