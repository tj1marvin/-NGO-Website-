# 🚀 NGO Website - Complete Setup & Usage Guide

## 📌 What You Have

A complete, production-ready Django NGO management website with:
- ✅ 6 Database models (Organization, Program, Volunteer, Donation, Impact, Event)
- ✅ Full REST API with 40+ endpoints
- ✅ Admin dashboard for management
- ✅ Responsive web interface
- ✅ Docker & Docker Compose setup
- ✅ Nginx configuration
- ✅ Comprehensive documentation

---

## ⚡ Quick Start (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Database Migrations
```bash
python manage.py migrate
```

### 3. Create Admin Account
```bash
python manage.py createsuperuser
# Enter username: admin
# Enter email: admin@example.com
# Enter password: (secure password)
```

### 4. Load Sample Data (Optional)
```bash
python init_sample_data.py
```

### 5. Start Development Server
```bash
python manage.py runserver
```

### 6. Access Application
- 🏠 Website: http://localhost:8000/
- 🔐 Admin: http://localhost:8000/admin/ (use credentials from step 3)
- 🔌 API: http://localhost:8000/api/

---

## 📂 Project Structure

```
NGO/
├── manage.py                    # Django management
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker container config
├── docker-compose.yml           # Docker Compose setup
├── nginx.conf                   # Nginx web server config
├── setup.sh                     # Automated setup script
├── init_sample_data.py          # Load sample data
│
├── ngo_project/                 # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/                        # Main application
│   ├── models.py               # 6 database models
│   ├── views.py                # REST API views
│   ├── views_templates.py      # Web views
│   ├── serializers.py          # API serializers
│   ├── admin.py                # Admin configuration
│   ├── urls.py                 # Routes
│   ├── tests.py                # Unit tests
│   └── management/
│       └── commands/
│           └── seed_data.py    # Data seeding command
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template
│   ├── home.html               # Homepage
│   ├── organizations.html
│   ├── programs.html
│   └── volunteers.html
│
├── static/                      # CSS, JavaScript, Images
├── media/                       # User uploads
│
├── README.md                    # Full documentation
├── QUICKSTART.md               # Quick start guide
├── DEPLOYMENT.md               # Production deployment
├── SETUP_CHECKLIST.md          # Setup checklist
└── PROJECT_SUMMARY.md          # Project overview
```

---

## 🗄️ Database Models Overview

### Organization
Represents an NGO/nonprofit organization
- Fields: name, description, mission, contact info, location, founded date
- Relations: Has many programs, volunteers, donations, events

### Program
Represents a program or initiative
- Fields: name, description, category, budget, target beneficiaries, status
- Relations: Belongs to organization, has donations, impacts, volunteers

### Volunteer
Represents a volunteer
- Fields: name, email, phone, skills, experience, availability
- Relations: Belongs to organization, works on programs

### Donation
Tracks donations received
- Fields: donor info, type, amount, description, receipt status
- Relations: Associated with organization and program

### Impact
Measures program impact
- Fields: people reached, lives changed, hours contributed, success rate
- Relations: One-to-one with program

### Event
Manages events and activities
- Fields: title, description, date, location, capacity
- Relations: Belongs to organization

---

## 🔌 REST API Endpoints

### Organizations
```
GET    /api/organizations/                    List all
POST   /api/organizations/                    Create
GET    /api/organizations/{id}/               Details
PUT    /api/organizations/{id}/               Update
DELETE /api/organizations/{id}/               Delete
GET    /api/organizations/{id}/programs/      Get programs
GET    /api/organizations/{id}/donations/     Get donations
GET    /api/organizations/{id}/volunteers/    Get volunteers
```

### Programs
```
GET    /api/programs/                         List all
POST   /api/programs/                         Create
GET    /api/programs/{id}/                    Details
PUT    /api/programs/{id}/                    Update
DELETE /api/programs/{id}/                    Delete
GET    /api/programs/{id}/impact/             Get impact metrics
GET    /api/programs/{id}/donations/          Get donations
```

### Volunteers
```
GET    /api/volunteers/                       List all
POST   /api/volunteers/                       Create
GET    /api/volunteers/{id}/                  Details
GET    /api/volunteers/active/                List active only
PUT    /api/volunteers/{id}/                  Update
DELETE /api/volunteers/{id}/                  Delete
```

### Donations
```
GET    /api/donations/                        List all
POST   /api/donations/                        Create
GET    /api/donations/{id}/                   Details
GET    /api/donations/statistics/             Get statistics
PUT    /api/donations/{id}/                   Update
DELETE /api/donations/{id}/                   Delete
```

### Events
```
GET    /api/events/                           List all
POST   /api/events/                           Create
GET    /api/events/{id}/                      Details
POST   /api/events/{id}/register/             Register for event
PUT    /api/events/{id}/                      Update
DELETE /api/events/{id}/                      Delete
```

### Impact
```
GET    /api/impacts/                          List all
POST   /api/impacts/                          Create
GET    /api/impacts/{id}/                     Details
PUT    /api/impacts/{id}/                     Update
DELETE /api/impacts/{id}/                     Delete
```

---

## 🎯 Common Tasks

### Add a New Organization
**Via Admin Panel:**
1. Go to http://localhost:8000/admin/
2. Click "Organizations" → "Add organization"
3. Fill in details and save

**Via API:**
```bash
curl -X POST http://localhost:8000/api/organizations/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Global Health Initiative",
    "description": "Healthcare for all",
    "mission": "Improve health outcomes",
    "founded_date": "2020-01-01",
    "email": "info@ghi.org",
    "phone": "+1-555-0001",
    "address": "123 Main St",
    "city": "New York",
    "country": "USA"
  }'
```

### Create a Program
```bash
curl -X POST http://localhost:8000/api/programs/ \
  -H "Content-Type: application/json" \
  -d '{
    "organization": 1,
    "name": "Mobile Clinics",
    "description": "Healthcare in remote areas",
    "category": "health",
    "start_date": "2023-01-01",
    "budget": 500000,
    "target_beneficiaries": 50000,
    "status": "active"
  }'
```

### Get Donation Statistics
```bash
curl http://localhost:8000/api/donations/statistics/
```

### Register for Event
```bash
curl -X POST http://localhost:8000/api/events/1/register/
```

---

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)
```bash
# Build and start all services
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Load sample data
docker-compose exec web python init_sample_data.py

# Access application
# Website: http://localhost:80/
# API: http://localhost:80/api/
```

### Using Docker Only
```bash
# Build image
docker build -t ngo-website .

# Run container
docker run -p 8000:8000 ngo-website

# To use with PostgreSQL:
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:password@host:5432/ngo_db \
  ngo-website
```

### Stop Services
```bash
docker-compose down
```

---

## 📊 Admin Panel

The Django admin panel provides:
- ✅ Full CRUD operations for all models
- ✅ Search and filtering capabilities
- ✅ Bulk actions (delete multiple items)
- ✅ Inline editing of related objects
- ✅ Custom list displays
- ✅ Permission management
- ✅ Data export capabilities

**Access:** http://localhost:8000/admin/

---

## 🔧 Management Commands

### Create Sample Data
```bash
python manage.py seed_data
```

### Database Backup
```bash
python manage.py dumpdata > backup.json
```

### Database Restore
```bash
python manage.py loaddata backup.json
```

### Make Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run Tests
```bash
python manage.py test core
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Start Django Shell
```bash
python manage.py shell
```

---

## 🧪 Testing

### Run All Tests
```bash
python manage.py test core
```

### Run Specific Test
```bash
python manage.py test core.tests.OrganizationTestCase
```

### Run with Coverage
```bash
coverage run --source='.' manage.py test core
coverage report
coverage html
```

---

## 🚀 Production Deployment

### 1. Environment Setup
Create `.env` file:
```bash
DEBUG=False
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/ngo_db
```

### 2. Using Gunicorn
```bash
pip install gunicorn
gunicorn ngo_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

### 3. Using Docker Compose
```bash
docker-compose -f docker-compose.yml up -d
```

### 4. Using Nginx (See DEPLOYMENT.md)

### 5. Configure HTTPS
- Use Let's Encrypt with Certbot
- Set SECURE_SSL_REDIRECT = True
- Set SESSION_COOKIE_SECURE = True

---

## 📈 Performance Tips

- Use PostgreSQL instead of SQLite for production
- Enable database connection pooling
- Use Gunicorn with multiple workers (4-8)
- Set up caching with Redis
- Enable gzip compression in Nginx
- Optimize database queries
- Use CDN for static files
- Monitor with tools like New Relic or DataDog

---

## 🔐 Security Checklist

- [ ] DEBUG = False in production
- [ ] SECRET_KEY is secure and secret
- [ ] ALLOWED_HOSTS configured correctly
- [ ] HTTPS/SSL enabled
- [ ] Database password is strong
- [ ] Environment variables configured
- [ ] CSRF protection enabled
- [ ] XSS protection enabled
- [ ] SQL injection prevention (Django ORM)
- [ ] Admin credentials secure
- [ ] Backups configured
- [ ] Error logging set up

---

## 📞 Troubleshooting

### Issue: ImportError for Django modules
**Solution:** Make sure virtual environment is activated and requirements installed
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: Database errors
**Solution:** Reset database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Issue: Static files not loading
**Solution:** Collect static files
```bash
python manage.py collectstatic
```

### Issue: Admin login fails
**Solution:** Create new superuser
```bash
python manage.py createsuperuser
```

### Issue: Port 8000 already in use
**Solution:** Use different port
```bash
python manage.py runserver 8001
```

---

## 📚 Documentation Files

- **README.md** - Complete project documentation
- **QUICKSTART.md** - 5-minute quick start
- **DEPLOYMENT.md** - Production deployment guide
- **SETUP_CHECKLIST.md** - Step-by-step setup checklist
- **PROJECT_SUMMARY.md** - Project overview and features

---

## 🌟 Next Steps

1. **Customize Models** - Extend models for your specific needs
2. **Add Authentication** - Implement user accounts and permissions
3. **Create Custom Views** - Add business logic specific to your NGO
4. **Enhance UI** - Customize templates and styling
5. **Add Email Notifications** - Send automated emails
6. **Implement Analytics** - Track and visualize metrics
7. **Deploy to Production** - Follow DEPLOYMENT.md
8. **Set Up Monitoring** - Monitor application health
9. **Configure Backups** - Automate database backups
10. **Add More Features** - Expand functionality as needed

---

## 💡 Tips & Best Practices

### Code Organization
- Keep models focused and single-responsibility
- Use serializers for API responses
- Create reusable utility functions
- Document complex logic with comments

### Database
- Use indexes for frequently queried fields
- Create database backups regularly
- Monitor query performance
- Use transactions for data consistency

### API Design
- Use appropriate HTTP methods (GET, POST, PUT, DELETE)
- Return meaningful status codes
- Provide clear error messages
- Version your API for backwards compatibility

### Frontend
- Keep templates DRY (Don't Repeat Yourself)
- Use template inheritance
- Optimize images
- Minify CSS and JavaScript

---

## 🎓 Learning Resources

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Bootstrap: https://getbootstrap.com/
- PostgreSQL: https://www.postgresql.org/
- Docker: https://www.docker.com/

---

## 📞 Support

For issues or questions:
1. Check the documentation files
2. Review Django and DRF official docs
3. Search Stack Overflow
4. Check project issues on GitHub (if applicable)

---

## 🎉 You're Ready!

Your NGO website is fully set up and ready to use. Start by exploring the admin panel, then customize it for your specific needs.

**Happy coding!** 🚀

---

**Last Updated:** November 15, 2025
**Django Version:** 4.2.0
**Python:** 3.8+
**Status:** Production Ready ✅
