"""
Database initialization script
Run this after setup to populate the database with sample data
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ngo_project.settings')
django.setup()

from core.models import Organization, Program, Volunteer, Donation, Impact, Event
from django.utils import timezone
from datetime import timedelta

def create_sample_data():
    print("Creating sample organizations...")
    
    # Organization 1
    org1 = Organization.objects.create(
        name="Global Health Initiative",
        description="Providing healthcare to underserved communities across the globe",
        mission="To improve health outcomes in developing countries",
        founded_date="2015-03-10",
        email="info@ghi.org",
        phone="+1-555-0001",
        website="https://example.com/ghi",
        address="456 Health Ave",
        city="San Francisco",
        country="USA"
    )
    print(f"✓ Created: {org1.name}")
    
    # Organization 2
    org2 = Organization.objects.create(
        name="Education For All",
        description="Making quality education accessible to every child",
        mission="Ensure every child has access to quality education",
        founded_date="2018-06-15",
        email="contact@efa.org",
        phone="+1-555-0002",
        website="https://example.com/efa",
        address="789 Education St",
        city="Los Angeles",
        country="USA"
    )
    print(f"✓ Created: {org2.name}")
    
    print("\nCreating sample programs...")
    
    # Program 1
    prog1 = Program.objects.create(
        organization=org1,
        name="Mobile Health Clinics",
        description="Bringing healthcare to remote areas through mobile clinics",
        category="health",
        start_date="2023-01-01",
        end_date="2024-12-31",
        budget=500000,
        target_beneficiaries=50000,
        status="active"
    )
    print(f"✓ Created: {prog1.name}")
    
    # Program 2
    prog2 = Program.objects.create(
        organization=org2,
        name="Scholarship Program",
        description="Providing scholarships to underprivileged students",
        category="education",
        start_date="2023-06-01",
        budget=300000,
        target_beneficiaries=1000,
        status="active"
    )
    print(f"✓ Created: {prog2.name}")
    
    print("\nCreating sample volunteers...")
    
    # Volunteer 1
    vol1 = Volunteer.objects.create(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        phone="+1-555-1001",
        bio="Passionate about healthcare with 5 years of experience",
        skills="medical",
        experience_years=5,
        availability="part_time",
        organization=org1,
        is_active=True
    )
    vol1.programs.add(prog1)
    print(f"✓ Created: {vol1.first_name} {vol1.last_name}")
    
    # Volunteer 2
    vol2 = Volunteer.objects.create(
        first_name="Jane",
        last_name="Smith",
        email="jane@example.com",
        phone="+1-555-1002",
        bio="Education enthusiast with teaching experience",
        skills="teaching",
        experience_years=3,
        availability="full_time",
        organization=org2,
        is_active=True
    )
    vol2.programs.add(prog2)
    print(f"✓ Created: {vol2.first_name} {vol2.last_name}")
    
    print("\nCreating sample donations...")
    
    # Donation 1
    don1 = Donation.objects.create(
        donor_name="Alice Johnson",
        donor_email="alice@example.com",
        donation_type="monetary",
        amount=5000,
        currency="USD",
        description="Support for mobile health clinics",
        program=prog1,
        organization=org1,
        receipt_issued=True
    )
    print(f"✓ Created donation: ${don1.amount}")
    
    # Donation 2
    don2 = Donation.objects.create(
        donor_name="Bob Wilson",
        donor_email="bob@example.com",
        donation_type="in_kind",
        amount=2000,
        currency="USD",
        description="Medical supplies donation",
        organization=org1,
        is_anonymous=False
    )
    print(f"✓ Created donation: ${don2.amount}")
    
    print("\nCreating sample impact metrics...")
    
    # Impact 1
    impact1 = Impact.objects.create(
        program=prog1,
        people_reached=25000,
        lives_changed=5000,
        hours_contributed=10000,
        success_rate=92.5,
        testimonials="This program saved lives in our community. Many people received care who otherwise wouldn't have access."
    )
    print(f"✓ Created impact metrics for: {prog1.name}")
    
    print("\nCreating sample events...")
    
    # Event 1
    event1 = Event.objects.create(
        organization=org1,
        title="Health Awareness Campaign 2025",
        description="Community health education and free screening",
        event_date=timezone.now() + timedelta(days=30),
        location="Community Center, San Francisco",
        capacity=200,
        registered_count=120
    )
    print(f"✓ Created event: {event1.title}")
    
    # Event 2
    event2 = Event.objects.create(
        organization=org2,
        title="Scholarship Awards Ceremony",
        description="Annual ceremony to award scholarships to deserving students",
        event_date=timezone.now() + timedelta(days=60),
        location="Grand Ballroom, Los Angeles",
        capacity=150,
        registered_count=80
    )
    print(f"✓ Created event: {event2.title}")
    
    print("\n✅ Sample data created successfully!")
    print("\nAccess your data:")
    print("- Admin: http://localhost:8000/admin/")
    print("- API: http://localhost:8000/api/")
    print("- Organizations: http://localhost:8000/organizations/")
    print("- Programs: http://localhost:8000/programs/")
    print("- Volunteers: http://localhost:8000/volunteers/")

if __name__ == "__main__":
    create_sample_data()
