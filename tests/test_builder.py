import unittest
from datetime import datetime, timedelta
from src.creational_patterns.builder import AssignmentBuilder, AssignmentDirector


class TestBuilder(unittest.TestCase):
    
    def test_build_complete_assignment(self):
        due_date = datetime.now() + timedelta(days=14)
        
        assignment = (AssignmentBuilder()
                      .set_assignment_id("ASSIGN_001")
                      .set_course_id("SE301")
                      .set_title("System Design")
                      .set_description("Design the system architecture")
                      .set_due_date(due_date)
                      .set_max_points(100)
                      .add_allowed_file_type(".pdf")
                      .add_attachment("instructions.pdf")
                      .set_as_group_assignment(True)
                      .build())
        
        self.assertEqual(assignment.assignment_id, "ASSIGN_001")
        self.assertEqual(assignment.course_id, "SE301")
        self.assertEqual(assignment.title, "System Design")
        self.assertEqual(assignment.max_points, 100)
        self.assertTrue(assignment.is_group_assignment)
    
    def test_missing_required_field(self):
        with self.assertRaises(ValueError):
            (AssignmentBuilder()
             .set_assignment_id("ASSIGN_001")
             .set_course_id("SE301")
             .set_title("Test")
             # Missing due_date
             .build())
    
    def test_past_due_date(self):
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            (AssignmentBuilder()
             .set_assignment_id("ASSIGN_001")
             .set_course_id("SE301")
             .set_title("Test")
             .set_due_date(past_date)
             .set_max_points(100)
             .build())
    
    def test_director_programming_assignment(self):
        builder = AssignmentBuilder()
        assignment = AssignmentDirector.create_programming_assignment(
            builder, "ASSIGN_002", "CS101"
        )
        
        self.assertEqual(assignment.title, "Programming Assignment")
        self.assertEqual(assignment.max_points, 100)
        self.assertIn(".py", assignment.allowed_file_types)
    
    def test_director_essay_assignment(self):
        builder = AssignmentBuilder()
        assignment = AssignmentDirector.create_essay_assignment(
            builder, "ASSIGN_003", "ENGLISH101"
        )
        
        self.assertEqual(assignment.title, "Essay Assignment")
        self.assertEqual(assignment.max_points, 50)
        self.assertIn(".pdf", assignment.allowed_file_types)
        self.assertIsNotNone(assignment.rubric)


if __name__ == '__main__':
    unittest.main()