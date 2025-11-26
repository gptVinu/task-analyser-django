from django.test import TestCase
from datetime import date, timedelta
from .scoring import calculate_score

class ScoringTest(TestCase):
    def test_overdue_task(self):
        task = {
            "title": "Test",
            "due_date": date.today() - timedelta(days=2),
            "estimated_hours": 2,
            "importance": 5,
            "dependencies": []
        }
        score = calculate_score(task)
        self.assertGreater(score, 20)

    def test_low_effort_high_score(self):
        t1 = {
            "title":"Quick",
            "due_date":date.today(),
            "estimated_hours":1,
            "importance":5,
            "dependencies":[]
        }
        t2 = {
            "title":"Slow",
            "due_date":date.today(),
            "estimated_hours":10,
            "importance":5,
            "dependencies":[]
        }
        self.assertGreater(calculate_score(t1), calculate_score(t2))
