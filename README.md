# NGO Website - Django Project

A comprehensive Django web application for managing NGO operations, including organizations, programs, volunteers, donations, and impact tracking.

## Features

- 🏢 **Organization Management** - Manage multiple NGO organizations with detailed profiles
- 🎯 **Program Tracking** - Track programs, budgets, beneficiaries, and timelines
- 👥 **Volunteer Management** - Connect and manage volunteers with their skills and availability
- 💰 **Donation System** - Track monetary and in-kind donations
- 📊 **Impact Metrics** - Measure and showcase the impact of programs
- 📅 **Event Management** - Organize and manage NGO events
- 🔌 **REST API** - Full REST API for all models using Django REST Framework
- 🎨 **Bootstrap UI** - Responsive web interface with Bootstrap 5

## Project Structure

```
ngo_project/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── ngo_project/              # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
├── core/                     # Core app with models
│   ├── models.py            # Database models
│   ├── views.py             # API views
│   ├── views_templates.py   # Template views
│   ├── serializers.py       # DRF serializers
│   ├── admin.py             # Django admin configuration
│   ├── urls.py              # App URLs
│   ├── apps.py
│   └── __init__.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── organizations.html
│   ├── programs.html
│   └── volunteers.html
├── static/                  # Static files (CSS, JS, images)
└── media/                   # User-uploaded files
```

## Models

### Organization
- Name, description, mission
- Contact information (email, phone, website)
- Location (address, city, country)
- Founded date
- Logo image

### Program
- Name, description, category
- Start date, end date
- Budget and target beneficiaries
- Status (active, completed, planned)
- Related organization

### Volunteer
- Personal information (name, email, phone)
- Skills and experience
- Availability status
- Linked to organization(s) and program(s)
- Join date

### Donation
- Donor information
- Donation type (monetary, in-kind, service)
- Amount and currency
- Related program and organization
- Receipt tracking

### Impact
- Program impact metrics
- People reached
- Lives changed
- Hours contributed
- Success rate and testimonials

### Event
- Event title, description
- Date, time, and location
- Capacity and registration count
- Related organization

## Installation

1. **Clone the repository:**
```bash
cd /Users/mac/Documents/3\ year/NGO
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

6. **Start the development server:**
```bash
python manage.py runserver
```

7. **Access the application:**
- Website: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- API: http://localhost:8000/api/

## API Endpoints

### Organizations
- `GET /api/organizations/` - List all organizations
- `GET /api/organizations/{id}/` - Get organization details
- `GET /api/organizations/{id}/programs/` - Get organization programs
- `GET /api/organizations/{id}/donations/` - Get organization donations
- `GET /api/organizations/{id}/volunteers/` - Get organization volunteers
- `POST /api/organizations/` - Create organization

### Programs
- `GET /api/programs/` - List all programs
- `GET /api/programs/{id}/` - Get program details
- `GET /api/programs/{id}/impact/` - Get program impact metrics
- `GET /api/programs/{id}/donations/` - Get program donations
- `POST /api/programs/` - Create program

### Volunteers
- `GET /api/volunteers/` - List all volunteers
- `GET /api/volunteers/active/` - List active volunteers
- `GET /api/volunteers/{id}/` - Get volunteer details
- `POST /api/volunteers/` - Create volunteer

### Donations
- `GET /api/donations/` - List all donations
- `GET /api/donations/statistics/` - Get donation statistics
- `GET /api/donations/{id}/` - Get donation details
- `POST /api/donations/` - Create donation

### Events
- `GET /api/events/` - List all events
- `GET /api/events/{id}/` - Get event details
- `POST /api/events/{id}/register/` - Register for event

### Impact
- `GET /api/impacts/` - List all impact records
- `GET /api/impacts/{id}/` - Get impact details

## Management Commands

Create sample data:
```bash
python manage.py shell
```

Then in the Python shell:
```python
from core.models import Organization
org = Organization.objects.create(
    name="Help Foundation",
    description="A nonprofit helping communities",
    mission="To improve lives in underserved communities",
    founded_date="2020-01-15",
    email="info@helpfound.org",
    phone="+1-555-1234",
    address="123 Main St",
    city="New York",
    country="USA"
)
```

## Admin Features

The Django admin panel (`/admin/`) provides:
- Full CRUD operations for all models
- Advanced filtering and search
- Bulk actions
- Custom list displays
- Related object editing

## Security Features

- CSRF protection
- SQL injection prevention via Django ORM
- Password hashing
- User authentication
- Admin authentication required

## Static Files

To collect static files for production:
```bash
python manage.py collectstatic
```

## Database

Default: SQLite (db.sqlite3)

For production, configure PostgreSQL in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ngo_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Future Enhancements

- [ ] User authentication and roles
- [ ] Advanced reporting and analytics
- [ ] Email notifications
- [ ] SMS alerts
- [ ] Mobile app
- [ ] Social media integration
- [ ] Online donation processing
- [ ] Impact visualization dashboards

## Support

For issues or questions, contact: support@ngoplatform.org

## License

MIT License - See LICENSE file for details
