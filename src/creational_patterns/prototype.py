"""
Prototype Pattern
Use Case: Cloning existing Notification templates
"""

import copy
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any


class Prototype(ABC):
    """Abstract prototype"""
    
    @abstractmethod
    def clone(self):
        pass


class NotificationTemplate(Prototype):
    """Notification template that can be cloned"""
    
    def __init__(self, template_id: str, title: str, body: str, 
                 notification_type: str, priority: str = "normal"):
        self.template_id = template_id
        self.title = title
        self.body = body
        self.notification_type = notification_type
        self.priority = priority
        self.placeholders = {}
        self.created_at = datetime.now()
    
    def add_placeholder(self, key: str, value: Any):
        """Add a placeholder value to fill in the template"""
        self.placeholders[key] = value
        return self
    
    def render(self) -> Dict[str, str]:
        """Render the notification with placeholders filled"""
        rendered_title = self.title
        rendered_body = self.body
        for key, value in self.placeholders.items():
            rendered_title = rendered_title.replace(f"{{{{{key}}}}}", str(value))
            rendered_body = rendered_body.replace(f"{{{{{key}}}}}", str(value))
        return {
            "title": rendered_title,
            "body": rendered_body,
            "type": self.notification_type,
            "priority": self.priority
        }
    
    def clone(self):
        """Create a deep copy of the template"""
        return copy.deepcopy(self)


class NotificationTemplateCache:
    """Cache for storing and retrieving notification templates"""
    
    _templates = {}
    
    @classmethod
    def load_templates(cls):
        """Pre-load some templates"""
        # Grade posted template
        grade_template = NotificationTemplate(
            "GRADE_TMPL", "Grade Posted", 
            "Your grade for {{course_name}} has been posted. Score: {{score}}/{{max_points}}",
            "academic", "high"
        )
        cls._templates["grade"] = grade_template
        
        # Event reminder template
        event_template = NotificationTemplate(
            "EVENT_TMPL", "Event Reminder",
            "Reminder: {{event_name}} starts in {{hours}} hours at {{location}}",
            "event", "normal"
        )
        cls._templates["event"] = event_template
        
        # Low balance template
        balance_template = NotificationTemplate(
            "BALANCE_TMPL", "Low Balance Alert",
            "Your meal plan balance is low. Remaining swipes: {{remaining_swipes}}",
            "warning", "high"
        )
        cls._templates["balance"] = balance_template
    
    @classmethod
    def get_template(cls, template_key: str) -> NotificationTemplate:
        """Get a clone of the requested template"""
        if template_key not in cls._templates:
            raise ValueError(f"Template not found: {template_key}")
        return cls._templates[template_key].clone()