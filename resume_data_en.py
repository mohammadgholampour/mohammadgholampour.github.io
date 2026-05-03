# resume_data_en.py
# English resume data — Mohammad Gholampour
# To update your resume, only edit this file

RESUME = {
    "name": "Mohammad Gholampour",
    "title": "Backend Developer",
    "subtitle": "Python · Django · FastAPI · PostgreSQL",
    "contact": {
        "phone": "+98 993 014 2744",
        "email": "m.gholampour2002@gmail.com",
        "linkedin": "linkedin.com/in/mohammad-gholampour",
    },

    # ─── Professional Summary ────────────────────────────────────────────────
    "summary": (
        "Backend Developer with 1+ year of production experience in logistics, "
        "healthcare, and international real estate CRM. "
        "Delivered 30+ API endpoints across 3 live projects at Dayamooz "
        "using Django, FastAPI, PostgreSQL, Celery, and Redis. "
        "Writes unit and integration tests (pytest), uses Docker for containerization, "
        "and collaborates closely with frontend teams to ship well-documented, "
        "reliable APIs."
    ),

    # ─── Key Achievements ────────────────────────────────────────────────────
    "achievements": [
        {
            "verb": "Designed and deployed",
            "kpi": "30+ REST API endpoints",
            "rest": "for a freight logistics admin panel (Truck) — sole backend developer",
        },
        {
            "verb": "Built",
            "kpi": "full CRM API layer",
            "rest": "for Lunaya, a Dubai real estate platform (listings, reservations, commissions)",
        },
        {
            "verb": "Contributed",
            "kpi": "60%+ of core APIs",
            "rest": "for the Gamify e-learning platform during internship",
        },
        {
            "verb": "Implemented",
            "kpi": "geospatial data processing",
            "rest": "with PostGIS for route and freight management in a logistics system",
        },
        {
            "verb": "Set up",
            "kpi": "Celery + Redis task queues",
            "rest": "for background jobs and periodic tasks in production",
        },
        {
            "verb": "Covered",
            "kpi": "business-critical endpoints",
            "rest": "with unit and integration tests using pytest",
        },
    ],

    # ─── Core Skills ─────────────────────────────────────────────────────────
    "skills": [
        {
            "label": "Languages",
            "value": "Python (Advanced)  ·  Java (Basic)",
        },
        {
            "label": "Frameworks",
            "value": "Django · Django REST Framework · FastAPI · Celery",
        },
        {
            "label": "Databases",
            "value": "PostgreSQL · PostGIS · MySQL · Redis",
        },
        {
            "label": "Testing",
            "value": "pytest · unittest  (unit & integration tests)",
        },
        {
            "label": "Tools",
            "value": "Docker · Docker Compose · Git · GitLab CI/CD · GitHub · Jira",
        },
        {
            "label": "Docs",
            "value": "OpenAPI / Swagger",
        },
        {
            "label": "Concepts",
            "value": "RESTful API Design · Clean Code · JWT / CSRF / XSS · Query Optimization",
        },
        {
            "label": "OS",
            "value": "Linux  (CLI & Development Environment)",
        },
    ],

    # ─── Work Experience ─────────────────────────────────────────────────────
    "experience": [
        {
            "role": "Backend Developer — Lunaya CRM",
            "company": "Dayamooz  |  Mashhad, Iran",
            "period": "Oct 2025 – Present  •  7 months",
            "bullets": [
                {
                    "verb": "Designed",
                    "rest": "and implemented the majority of API routes for a real estate CRM "
                            "managing property listings, unit reservations, and commission workflows in Dubai",
                },
                {
                    "verb": "Built",
                    "rest": "end-to-end modules for listing management, booking lifecycle, "
                            "and commission calculation using FastAPI",
                },
                {
                    "verb": "Integrated",
                    "rest": "Celery + Redis for background task processing and scheduled jobs",
                },
                {
                    "verb": "Collaborated",
                    "rest": "with a senior engineer on system architecture and the initial data import pipeline",
                },
            ],
            "stack": "FastAPI · Python · PostgreSQL · Redis · Celery",
        },
        {
            "role": "Backend Developer — Medlift",
            "company": "Dayamooz  |  Mashhad, Iran",
            "period": "Jul 2025 – Oct 2025  •  4 months",
            "bullets": [
                {
                    "verb": "Developed",
                    "rest": "REST API endpoints for a healthcare platform using FastAPI in an Agile environment",
                },
                {
                    "verb": "Designed",
                    "rest": "endpoints for medical data management and clinical workflow automation",
                },
                {
                    "verb": "Wrote",
                    "rest": "unit tests with pytest to cover business-critical endpoint logic",
                },
            ],
            "stack": "FastAPI · Python · PostgreSQL · pytest",
        },
        {
            "role": "Backend Developer — Truck (Load Truck Partial)",
            "company": "Dayamooz  |  Mashhad, Iran",
            "period": "Nov 2024 – Jul 2025  •  9 months",
            "bullets": [
                {
                    "verb": "Designed",
                    "rest": "and implemented 30+ REST API endpoints for the admin panel "
                            "of a freight logistics system using Django and DRF",
                },
                {
                    "verb": "Implemented",
                    "rest": "geospatial data processing with PostGIS and PostgreSQL "
                            "to manage routes, locations, and freight operations",
                },
                {
                    "verb": "Optimized",
                    "rest": "database queries and integrated new business logic to improve API stability",
                },
                {
                    "verb": "Set up",
                    "rest": "Celery + Redis for async task processing and periodic jobs",
                },
                {
                    "verb": "Used",
                    "rest": "GitLab CI/CD pipeline for deployments and tracked tasks in Jira",
                },
                {
                    "verb": "Collaborated",
                    "rest": "directly with the frontend team to ensure seamless API integration",
                },
            ],
            "stack": "Django · DRF · PostgreSQL · PostGIS · Redis · Celery · Docker · GitLab",
        },
        {
            "role": "Backend Developer Intern — Gamify",
            "company": "Dayamooz  |  Mashhad, Iran",
            "period": "Sep 2024 – Nov 2024  •  3 months",
            "bullets": [
                {
                    "verb": "Contributed",
                    "rest": "to 60%+ of the core API endpoints for the internal Gamify "
                            "e-learning platform using Django and DRF",
                },
                {
                    "verb": "Designed",
                    "rest": "MySQL database schema for user management and educational content",
                },
                {
                    "verb": "Documented",
                    "rest": "all APIs with OpenAPI/Swagger; produced clean, testable RESTful code",
                },
            ],
            "stack": "Django · DRF · MySQL · Swagger · Git",
        },
    ],

    # ─── Education ───────────────────────────────────────────────────────────
    "education": {
        "degree": "B.Sc. Computer Engineering",
        "university": "Khayyam University  |  Mashhad, Iran",
        "period": "2021 – 2025",
    },

    # ─── Training & Courses ──────────────────────────────────────────────────
    "courses": [
        {
            "name": "Code with Mosh (2024)",
            "topics": (
                "Django & REST Framework · SQL & Database Design · "
                "Docker & DevOps Fundamentals · Java · "
                "Design Patterns · Data Structures & Algorithms"
            ),
        },
    ],

    # ─── Languages ───────────────────────────────────────────────────────────
    "languages": [
        {
            "name": "Persian",
            "level": "Native",
        },
        {
            "name": "English",
            "level": (
                "Professional — technical documentation & work communication; "
                "ready to improve for international teams"
            ),
        },
    ],
}
