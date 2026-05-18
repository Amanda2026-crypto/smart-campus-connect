import unittest
import threading
from src.creational_patterns.singleton import DatabaseConnection, get_db_connection


class TestSingleton(unittest.TestCase):
    
    def test_same_instance(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        
        self.assertIs(db1, db2)
    
    def test_get_db_connection(self):
        db1 = get_db_connection()
        db2 = get_db_connection()
        
        self.assertIs(db1, db2)
    
    def test_thread_safety(self):
        instances = []
        
        def create_instance():
            instances.append(DatabaseConnection())
        
        threads = []
        for _ in range(10):
            t = threading.Thread(target=create_instance)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        # All instances should be the same
        first_instance = instances[0]
        for instance in instances:
            self.assertIs(first_instance, instance)
    
    def test_connection_lifecycle(self):
        db = DatabaseConnection()
        
        self.assertFalse(db.is_connected)
        
        db.connect()
        self.assertTrue(db.is_connected)
        
        result = db.execute_query("SELECT * FROM users")
        self.assertEqual(len(result), 1)
        
        db.disconnect()
        self.assertFalse(db.is_connected)
    
    def test_query_logging(self):
        db = DatabaseConnection()
        db.connect()
        
        db.execute_query("SELECT * FROM courses")
        db.execute_query("INSERT INTO enrollments VALUES ('1', '2')")
        
        log = db.get_query_log()
        self.assertGreaterEqual(len(log), 2)
    
    def test_execute_without_connection(self):
        db = DatabaseConnection()
        # Ensure disconnected
        db.disconnect()
        
        with self.assertRaises(Exception):
            db.execute_query("SELECT * FROM users")


if __name__ == '__main__':
    unittest.main()