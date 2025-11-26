# Smart Task Analyzer

A web-based tool that intelligently prioritizes your tasks based on importance, due dates, estimated hours, and dependencies. Built with Django and vanilla JavaScript.

## Features

- Add tasks individually or bulk import via JSON
- Smart priority scoring with detailed explanations
- Support for task dependencies
- Clean, responsive interface

## Tech Stack

**Backend**: Django 5.2, Python 3.13 | **Frontend**: HTML5, CSS3, JavaScript | **Package Manager**: pipenv

## Quick Start

### Backend
```bash
cd backend
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver 9000
```

### Frontend
Open `frontend/index.html` in your browser or run:
```bash
cd frontend
python -m http.server 8000
```

## Usage

**Add Tasks**: Fill the form or paste JSON in bulk input area
**Analyze**: Click "Analyze Tasks" to get prioritized results
**Suggested Tasks**: Click "Get Suggested Tasks" (dummy data currently)

### JSON Format Example
```json
[
  {
    "title": "Complete report",
    "due_date": "2024-01-15",
    "estimated_hours": 5.0,
    "importance": 9,
    "dependencies": []
  }
]
```

## API Endpoints

- `POST /api/tasks/analyze/` - Analyze and prioritize tasks
- `GET /api/tasks/suggest/` - Get suggested tasks (in development)

## Scoring Logic

**Priority Score** = (Importance × 40%) + (Urgency × 35%) + (Efficiency × 25%) - Dependency Penalty

### Components

**Importance (40%)**: User rating 1-10
**Urgency (35%)**: Days until due (≤0 days = 10, ≤3 days = 8, ≤7 days = 6, else decreasing)
**Efficiency (25%)**: Hours needed (≤1hr = 10, ≤3hrs = 7, ≤8hrs = 4, else 2)
**Dependency Penalty**: -1.0 per incomplete dependency

### Score Ranges
- **9-10**: Critical - Start now
- **7-9**: High - Today/tomorrow
- **5-7**: Medium - This week
- **3-5**: Low - When time permits
- **0-3**: Lowest - Delegate/defer

### Example
Task: "Complete project report" | Importance: 9 | Due: 2 days | Hours: 3 | Dependencies: None
```
Score = (9×0.4) + (8×0.35) + (7×0.25) + 0 = 8.15 (High Priority)
```

## Troubleshooting

**Port in use**: Change port with `runserver 8000` and update `script.js`
**CORS errors**: Ensure backend is running on correct port
**Connection failed**: Check backend is running at `http://127.0.0.1:9000`

## Notes

- Suggested tasks feature uses dummy data (database integration pending)
- Task persistence requires backend database setup







