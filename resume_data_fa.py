# resume_data_fa.py
# فایل داده رزومه فارسی — محمد غلامپور
# برای آپدیت رزومه فقط همین فایل رو ویرایش کن

RESUME = {
    "name": "محمد غلامپور",
    "title": "توسعه‌دهنده بک‌اند",
    "subtitle_en": "Python · Django · FastAPI · PostgreSQL",
    "contact": {
        "phone": "09930142744",
        "email": "m.gholampour2002@gmail.com",
        "linkedin": "linkedin.com/in/mohammad-gholampour",
    },

    # ─── خلاصه حرفه‌ای ──────────────────────────────────────────────────────
    "summary": {
        "text": (
            "توسعه‌دهنده بک‌اند با بیش از یک سال تجربه عملی در Dayamooz، "
            "در سه پروژه تولیدی در حوزه‌های لجستیک، پزشکی و CRM املاک بین‌المللی. "
            "با Django و FastAPI به‌صورت حرفه‌ای کار کرده‌ام. "
            "بیش از ۳۰ endpoint تولیدی طراحی و پیاده‌سازی کرده‌ام — "
            "از سامانه لجستیکی با داده مکانی (PostGIS) تا سیستم رزرو و کمیسیون "
            "واحدهای ملکی در دبی. "
            "به کد تمیز، تست‌نویسی (pytest) و بهینه‌سازی کوئری متعهد هستم."
        ),
    },

    # ─── دستاوردهای کلیدی ───────────────────────────────────────────────────
    "achievements": [
        {
            "verb": "طراحی و استقرار",
            "kpi": "بیش از ۳۰ endpoint تولیدی",
            "rest": "برای پنل مدیریتی سامانه لجستیکی (Truck) — توسعه‌دهنده اصلی بک‌اند",
        },
        {
            "verb": "پیاده‌سازی",
            "kpi": "لایه کامل API یک CRM",
            "rest": "برای پلتفرم املاک Lunaya در دبی — لیستینگ، رزرو و کمیسیون",
        },
        {
            "verb": "توسعه",
            "kpi": "۶۰٪+ از APIهای اصلی",
            "rest": "پلتفرم آموزشی Gamify در دوره کارآموزی",
        },
        {
            "verb": "پیاده‌سازی",
            "kpi": "پردازش داده مکانی با PostGIS",
            "rest": "برای مدیریت مسیر و بار در سامانه لجستیکی",
        },
        {
            "verb": "راه‌اندازی",
            "kpi": "Celery + Redis",
            "rest": "برای مدیریت task queue و periodic tasks در محیط production",
        },
        {
            "verb": "پوشش",
            "kpi": "endpoint‌های حیاتی",
            "rest": "با unit test و integration test با pytest",
        },
    ],

    # ─── مهارت‌های کلیدی ────────────────────────────────────────────────────
    "skills": [
        {
            "label": "زبان‌ها",
            "value": "Python (Advanced)  ·  Java (Basic)",
        },
        {
            "label": "فریم‌ورک‌ها",
            "value": "Django · Django REST Framework · FastAPI · Celery",
        },
        {
            "label": "پایگاه داده",
            "value": "PostgreSQL · PostGIS · MySQL · Redis",
        },
        {
            "label": "تست‌نویسی",
            "value": "pytest · unittest  (unit & integration tests)",
        },
        {
            "label": "ابزارها",
            "value": "Docker · Docker Compose · Git · GitLab CI/CD · GitHub · Jira",
        },
        {
            "label": "مستندسازی",
            "value": "OpenAPI / Swagger",
        },
        {
            "label": "مفاهیم تخصصی",
            "value": "RESTful API Design · Clean Code · JWT / CSRF / XSS · Query Optimization",
        },
        {
            "label": "سیستم‌عامل",
            "value": "Linux  (CLI & Development Environment)",
        },
    ],

    # ─── سوابق شغلی ─────────────────────────────────────────────────────────
    "experience": [
        {
            "role_fa": "توسعه‌دهنده بک‌اند  |  پروژه Lunaya",
            "company_en": "Dayamooz — مشهد",
            "period_fa": "آبان ۱۴۰۴ – اکنون  •  ۷ ماه",
            "bullets": [
                "طراحی و پیاده‌سازی اکثر route‌های سیستم CRM مدیریت واحدهای ملکی در دبی با FastAPI",
                "توسعه ماژول‌های لیستینگ، رزرو واحدها و محاسبه کمیسیون با منطق تجاری پیچیده",
                "یکپارچه‌سازی Celery + Redis برای پردازش background tasks و scheduled jobs",
                "همکاری با ارشد تیم برای معماری پایه سیستم و اجرای data import اولیه",
                "پوشش طیف کامل API از احراز هویت تا گزارش‌گیری در یک CRM یکپارچه",
            ],
            "stack": "FastAPI · Python · PostgreSQL · Redis · Celery",
        },
        {
            "role_fa": "توسعه‌دهنده بک‌اند  |  پروژه Medlift",
            "company_en": "Dayamooz — مشهد",
            "period_fa": "تیر ۱۴۰۴ – آبان ۱۴۰۴  •  ۴ ماه",
            "bullets": [
                "توسعه endpoint‌های پلتفرم پزشکی با FastAPI در محیط Agile",
                "طراحی endpoint‌های مدیریت داده‌های پزشکی و جریان‌های کاری بالینی",
                "نوشتن unit test با pytest برای پوشش منطق تجاری endpoint‌های حیاتی",
            ],
            "stack": "FastAPI · Python · PostgreSQL · pytest",
        },
        {
            "role_fa": "توسعه‌دهنده بک‌اند  |  پروژه Truck",
            "company_en": "Dayamooz — مشهد",
            "period_fa": "آبان ۱۴۰۳ – تیر ۱۴۰۴  •  ۹ ماه",
            "bullets": [
                "طراحی و پیاده‌سازی بیش از ۳۰ endpoint برای پنل مدیریتی سامانه لجستیکی با Django و DRF",
                "پیاده‌سازی پردازش داده مکانی با PostGIS و PostgreSQL برای مدیریت مسیر و بار",
                "بهینه‌سازی کوئری‌های پایگاه داده و یکپارچه‌سازی منطق تجاری جدید",
                "راه‌اندازی Celery + Redis برای پردازش async tasks و periodic jobs",
                "استفاده از GitLab CI/CD pipeline برای استقرار و پیگیری وظایف با Jira",
                "همکاری مستقیم با تیم فرانت‌اند برای یکپارچگی بدون خطای API",
            ],
            "stack": "Django · DRF · PostgreSQL · PostGIS · Redis · Celery · Docker · GitLab",
        },
        {
            "role_fa": "کارآموز بک‌اند  |  پروژه Gamify",
            "company_en": "Dayamooz — مشهد",
            "period_fa": "شهریور ۱۴۰۳ – آبان ۱۴۰۳  •  ۳ ماه",
            "bullets": [
                "مشارکت در توسعه ۶۰٪+ از APIهای اصلی پلتفرم Gamify با Django و DRF",
                "طراحی اسکیمای MySQL برای مدیریت کاربران و محتوای آموزشی",
                "مستندسازی کامل APIها با OpenAPI/Swagger و تولید کد تمیز RESTful",
            ],
            "stack": "Django · DRF · MySQL · Swagger · Git",
        },
    ],

    # ─── سوابق تحصیلی ───────────────────────────────────────────────────────
    "education": {
        "degree_fa": "کارشناسی مهندسی کامپیوتر",
        "university_fa": "دانشگاه خاوران  |  مشهد",
        "period": "۱۴۰۰ – ۱۴۰۴",
    },

    # ─── دوره‌های آموزشی ─────────────────────────────────────────────────────
    "courses": [
        {
            "name": "Code with Mosh (2024)",
            "topics": (
                "Django & REST Framework · SQL & Database Design · "
                "Docker & DevOps · Java · Design Patterns · "
                "Data Structures & Algorithms"
            ),
        },
    ],

    # ─── زبان‌ها ─────────────────────────────────────────────────────────────
    "languages": [
        {"name": "فارسی",    "level": "زبان مادری"},
        {"name": "انگلیسی", "level": "تسلط کافی برای مستندات فنی و ارتباطات کاری — آماده ارتقاء"},
    ],
}
