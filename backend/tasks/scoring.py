from datetime import date

def urgency_weight(due_date):
    days = (due_date - date.today()).days
    if days < 0:
        return 25  # overdue
    return max(0, 25 - days)  # the sooner, the higher

def importance_weight(importance):
    return importance * 3

def effort_weight(hours):
    if hours <= 0:
        return 10
    return 10 / hours  # quick wins

def dependency_weight(deps):
    return len(deps) * 5

def calculate_score(task):
    return round(
        urgency_weight(task["due_date"]) +
        importance_weight(task["importance"]) +
        effort_weight(task["estimated_hours"]) +
        dependency_weight(task.get("dependencies", [])),
        2
    )

def explain_score(task):
    return f"Urgency, Importance & Effort considered"
