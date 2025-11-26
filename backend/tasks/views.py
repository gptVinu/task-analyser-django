from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .scoring import calculate_score, explain_score
from datetime import date
from .models import Task

@api_view(["POST"])
def analyze_tasks(request):
    serializer = TaskSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    tasks = serializer.validated_data

    for task in tasks:
        task["score"] = calculate_score(task)
        task["explanation"] = explain_score(task)

    tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)

    return Response(tasks)


# @api_view(["GET"])
# def suggest_tasks(request):
#     return Response({
#         "error": "Send tasks using POST /api/tasks/analyze first."
#     })

@api_view(["GET"])
def suggest_tasks(request):
    # Example tasks (replace with actual database query if needed)
    tasks = [
        {
            "title": "Task 1",
            "due_date": date.today(),
            "estimated_hours": 2,
            "importance": 8,
            "dependencies": []
        },
        {
            "title": "Task 2",
            "due_date": date.today(),
            "estimated_hours": 5,
            "importance": 6,
            "dependencies": []
        },
        {
            "title": "Task 3",
            "due_date": date.today(),
            "estimated_hours": 1,
            "importance": 9,
            "dependencies": []
        },
        {
            "title": "Task 4",
            "due_date": date.today(),
            "estimated_hours": 3,
            "importance": 7,
            "dependencies": []
        }
    ]

    # Calculate scores and explanations
    for task in tasks:
        task["score"] = calculate_score(task)
        task["explanation"] = explain_score(task)

    # Sort tasks by score in descending order
    tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)

    # Return the top 3 tasks
    return Response(tasks[:3])
