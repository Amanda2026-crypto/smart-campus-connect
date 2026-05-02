import unittest
from src.creational_patterns.prototype import NotificationTemplateCache


class TestPrototype(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        NotificationTemplateCache.load_templates()
    
    def test_clone_template(self):
        original = NotificationTemplateCache.get_template("grade")
        clone = original.clone()
        
        # Should be different objects
        self.assertIsNot(original, clone)
        # Should have same attributes
        self.assertEqual(original.template_id, clone.template_id)
        self.assertEqual(original.title, clone.title)
    
    def test_render_with_placeholders(self):
        template = NotificationTemplateCache.get_template("grade")
        template.add_placeholder("course_name", "Software Engineering")
        template.add_placeholder("score", "85")
        template.add_placeholder("max_points", "100")
        
        rendered = template.render()
        
        self.assertEqual(rendered["title"], "Grade Posted")
        self.assertIn("Software Engineering", rendered["body"])
        self.assertIn("85", rendered["body"])
    
    def test_clone_independence(self):
        original = NotificationTemplateCache.get_template("event")
        original.add_placeholder("event_name", "Career Fair")
        
        clone = original.clone()
        clone.add_placeholder("event_name", "Hackathon")
        
        original_rendered = original.render()
        clone_rendered = clone.render()
        
        self.assertIn("Career Fair", original_rendered["body"])
        self.assertIn("Hackathon", clone_rendered["body"])
    
    def test_template_not_found(self):
        with self.assertRaises(ValueError):
            NotificationTemplateCache.get_template("nonexistent")


if __name__ == '__main__':
    unittest.main()