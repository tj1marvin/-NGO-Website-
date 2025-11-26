# 🎯 NGO Website - Visual Quick Reference

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   NGO Website Architecture                   │
└─────────────────────────────────────────────────────────────┘

┌────────────────────┐
│   Client/Browser   │
└────────────┬───────┘
             │
        ┌────▼────────────────────────┐
        │   Web Server (Nginx)        │
        │   - Reverse Proxy           │
        │   - Static Files            │
        └────┬───────────────────────┘
             │
   ┌─────────┼─────────┐
   │         │         │
┌──▼──────┬──▼──┐  ┌──▼──────────────┐
│ REST    │ Web │  │ Admin Panel     │
│ API     │ App │  │ (Django Admin)  │
└────┬────┴─┬──┘  └──┬───────────────┘
     │      │        │
     └──────┼────────┘
            │
     ┌──────▼─────────────────────┐
     │  Django Application Layer   │
     │  ┌──────────────────────┐  │
     │  │ Models (6 Models)    │  │
     │  ├──────────────────────┤  │
     │  │ Organization         │  │
     │  │ Program              │  │
     │  │ Volunteer            │  │
     │  │ Donation             │  │
     │  │ Impact               │  │
     │  │ Event                │  │
     │  └──────────────────────┘  │
     └──────┬──────────────────────┘
            │
     ┌──────▼──────────────┐
     │   Database Layer    │
     │ ┌────────────────┐  │
     │ │  SQLite (Dev)  │  │
     │ │  PostgreSQL(Pro)  │
     │ └────────────────┘  │
     └─────────────────────┘
```

---

## 🗂️ File Organization

```
NGO/
├── 📖 Documentation/
│   ├── START_HERE.md ⭐ (Read First!)
│   ├── README.md
│   ├── QUICKSTART.md (5 min guide)
│   ├── COMPLETE_GUIDE.md
│   ├── DEPLOYMENT.md
│   ├── SETUP_CHECKLIST.md
│   ├── PROJECT_SUMMARY.md
│   └── FILES_CREATED.md
│
├── 🐍 Django Project/
│   ├── manage.py (Main management)
│   ├── requirements.txt (Dependencies)
│   │
│   ├── ngo_project/ (Project Settings)
│   │   ├── settings.py ⭐ (Configuration)
│   │   ├── urls.py (Main Routes)
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   └── __init__.py
│   │
│   ├── core/ (Main Application)
│   │   ├── models.py ⭐ (6 Database Models)
│   │   ├── views.py (REST API Views)
│   │   ├── views_templates.py (Web Views)
│   │   ├── serializers.py (API Serializers)
│   │   ├── admin.py (Admin Configuration)
│   │   ├── urls.py (App Routes)
│   │   ├── apps.py
│   │   ├── tests.py (Unit Tests)
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_data.py (Data Script)
│   │   └── __init__.py
│   │
│   ├── templates/ (HTML Templates)
│   │   ├── base.html (Base Template)
│   │   ├── home.html (Homepage)
│   │   ├── organizations.html
│   │   ├── programs.html
│   │   └── volunteers.html
│   │
│   ├── static/ (CSS, JS, Images)
│   ├── media/ (User Uploads)
│   └── db.sqlite3 (Database - Created)
│
├── 🐳 Docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── nginx.conf
│
├── 🔧 Configuration/
│   ├── .env.example (Environment Template)
│   ├── .gitignore (Git Ignore)
│   └── setup.sh (Setup Script)
│
└── 📝 Utilities/
    └── init_sample_data.py (Load Sample Data)
```

---

## 🔄 Data Flow Diagram

```
User Request
    ↓
┌───────────────────┐
│  Web Server       │
│  (Browser/API)    │
└────────┬──────────┘
         ↓
┌──────────────────────────┐
│  Django URL Router       │
│  (ngo_project/urls.py)   │
└────────┬─────────────────┘
         ↓
    ┌────┴─────┐
    │           │
    ▼           ▼
┌─────────┐  ┌──────────────────┐
│ REST    │  │ Template Views   │
│ API     │  │ (Web Pages)      │
│ Views   │  │                  │
└────┬────┘  └────┬─────────────┘
     │            │
     └──────┬─────┘
            ▼
     ┌────────────────┐
     │ Serializers &  │
     │ View Logic     │
     └────┬───────────┘
          ▼
     ┌────────────────┐
     │ Database       │
     │ Models (ORM)   │
     └────┬───────────┘
          ▼
     ┌────────────────┐
     │ SQLite/Postgres│
     └────────────────┘
```

---

## 📊 Database Schema (Simplified)

```
Organization
├── id (PK)
├── name
├── email
├── phone
├── city, country
└── timestamps

    ├──► Program
    │    ├── id (PK)
    │    ├── name
    │    ├── budget
    │    ├── status
    │    └── organization (FK)
    │        │
    │        ├──► Impact (1:1)
    │        │    ├── people_reached
    │        │    ├── lives_changed
    │        │    └── success_rate
    │        │
    │        └──► Donation (1:M)
    │             ├── amount
    │             ├── donor_name
    │             └── organization (FK)
    │
    ├──► Volunteer (1:M)
    │    ├── name, email
    │    ├── skills
    │    └── programs (M:M)
    │
    ├──► Donation (1:M)
    │    └── [See above]
    │
    └──► Event (1:M)
         ├── title
         ├── event_date
         └── capacity
```

---

## 🔌 API Endpoints Summary

```
┌─────────────────────────────────────────┐
│          REST API Endpoints             │
├─────────────────────────────────────────┤

ORGANIZATIONS
  GET  /api/organizations/
  POST /api/organizations/
  GET  /api/organizations/{id}/
  PUT  /api/organizations/{id}/
  DELETE /api/organizations/{id}/

PROGRAMS
  GET  /api/programs/
  POST /api/programs/
  GET  /api/programs/{id}/impact/

VOLUNTEERS
  GET  /api/volunteers/
  GET  /api/volunteers/active/

DONATIONS
  GET  /api/donations/statistics/

EVENTS
  POST /api/events/{id}/register/

└─────────────────────────────────────────┘
```

---

## 🎨 Web Pages

```
┌─────────────────────────────────────┐
│   Navigation Bar (Bootstrap 5)       │
│  NGO Platform | Org | Programs | ... │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│ Home   │ │  Org   │ │Program │
│ Page   │ │ List   │ │  List  │
└────────┘ └────────┘ └────────┘
    │          │          │
    └──────────┼──────────┘
               │
        ┌──────▼──────┐
        │ Footer with │
        │  Links      │
        └─────────────┘
```

---

## ⚙️ Setup Workflow

```
START
  ↓
Install Dependencies
  pip install -r requirements.txt
  ↓
Run Migrations
  python manage.py migrate
  ↓
Create Admin Account
  python manage.py createsuperuser
  ↓
(Optional) Load Sample Data
  python init_sample_data.py
  ↓
Start Development Server
  python manage.py runserver
  ↓
Visit http://localhost:8000/
  ↓
READY TO USE ✅
```

---

## 🐳 Docker Setup Workflow

```
START
  ↓
Build & Start Services
  docker-compose up -d
  ↓
Run Migrations
  docker-compose exec web python manage.py migrate
  ↓
Create Superuser
  docker-compose exec web python manage.py createsuperuser
  ↓
Access Application
  http://localhost:80/
  ↓
RUNNING IN DOCKER ✅
```

---

## 📈 Model Relationships

```
Organization (1)
    │
    ├─── (1:M) ──→ Program (1)
    │                  │
    │                  ├─── (1:1) ──→ Impact
    │                  │
    │                  ├─── (1:M) ──→ Donation
    │                  │
    │                  └─── (M:M) ──→ Volunteer
    │
    ├─── (1:M) ──→ Volunteer
    │
    ├─── (1:M) ──→ Donation
    │
    └─── (1:M) ──→ Event
```

---

## 🔐 Security Layers

```
┌──────────────────────────────────────┐
│      Application Security            │
├──────────────────────────────────────┤
│  1. CSRF Protection                  │
│  2. SQL Injection Prevention (ORM)   │
│  3. Password Hashing                 │
│  4. Admin Authentication             │
│  5. Environment Variables            │
│  6. HTTPS/SSL Ready                  │
│  7. XSS Protection                   │
│  8. Debug Mode Control               │
└──────────────────────────────────────┘
```

---

## 📱 Responsive Design

```
Desktop (≥992px)          Tablet (768-991px)    Mobile (<768px)
┌──────────────┐          ┌──────────────┐      ┌──────────┐
│ Logo | Menu  │          │ Logo | Menu  │      │ Logo ☰   │
├──────────────┤          ├──────────────┤      ├──────────┤
│              │          │              │      │          │
│  3-Col Grid  │          │  2-Col Grid  │      │ 1-Col    │
│              │          │              │      │ Stack    │
├──────────────┤          ├──────────────┤      ├──────────┤
│              │          │              │      │          │
│  Footer      │          │  Footer      │      │ Footer   │
└──────────────┘          └──────────────┘      └──────────┘
```

---

## 🔄 Admin Panel Flow

```
Login (admin/)
    ↓
Dashboard
    ├─→ Organizations
    │   ├─ List
    │   ├─ Add New
    │   ├─ Edit
    │   └─ Delete
    │
    ├─→ Programs
    │   ├─ List
    │   ├─ Add New
    │   ├─ Edit
    │   └─ Delete
    │
    ├─→ Volunteers
    │   └─ [Same operations]
    │
    ├─→ Donations
    │   └─ [Same operations]
    │
    ├─→ Events
    │   └─ [Same operations]
    │
    └─→ Impact Metrics
        └─ [Same operations]
```

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Install Deps | `pip install -r requirements.txt` |
| Migrate DB | `python manage.py migrate` |
| Create Admin | `python manage.py createsuperuser` |
| Load Data | `python init_sample_data.py` |
| Run Server | `python manage.py runserver` |
| Run Tests | `python manage.py test core` |
| Shell | `python manage.py shell` |
| Docker Start | `docker-compose up -d` |
| Docker Stop | `docker-compose down` |
| Backup DB | `python manage.py dumpdata > backup.json` |

---

## 🌐 Access Points

```
┌─────────────────────────────────────────┐
│        Application Access Points        │
├─────────────────────────────────────────┤
│                                         │
│  🏠 Website                             │
│     http://localhost:8000/              │
│                                         │
│  🔐 Admin Panel                         │
│     http://localhost:8000/admin/        │
│                                         │
│  🔌 API Root                            │
│     http://localhost:8000/api/          │
│                                         │
│  📊 Organizations API                   │
│     http://localhost:8000/api/          │
│     organizations/                      │
│                                         │
│  📄 Organizations Page                  │
│     http://localhost:8000/organizations/│
│                                         │
│  📝 Programs Page                       │
│     http://localhost:8000/programs/     │
│                                         │
│  👥 Volunteers Page                     │
│     http://localhost:8000/volunteers/   │
│                                         │
└─────────────────────────────────────────┘
```

---

## 📌 Key Concepts

```
Model → Database table
Serializer → Convert model to/from JSON
View → Handle requests and return responses
URL → Route request to correct view
Template → HTML page (for web)
Admin → Django admin interface
API → RESTful endpoints
```

---

## ✅ Final Checklist

```
□ Dependencies installed
□ Migrations run
□ Admin user created
□ Sample data loaded (optional)
□ Development server started
□ Admin panel accessible
□ API endpoints accessible
□ Web pages loading
□ Database working
□ Ready for customization
```

---

## 🎉 You're All Set!

Everything is organized and ready. Start with **START_HERE.md** and follow the quick start guide!

**Happy coding!** 🚀

---

*Last Updated: November 15, 2025*
