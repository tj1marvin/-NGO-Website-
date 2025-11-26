"""
Fixtures for seeding initial data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from core.models import Organization, Program, Volunteer, Donation, Impact, Event


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        # Create Organizations
        org1 = Organization.objects.create(
            name="Charity Foundation",
            description="A community-focused charity providing health, education and emergency support.",
            mission="Deliver sustainable programs that improve lives and strengthen communities.",
            founded_date="2010-04-12",
            email="info@charityfoundation.org",
            phone="+1-555-0101",
            website="https://charityfoundation.org",
            address="123 Charity Way",
            city="San Francisco",
            country="USA"
        )

        org2 = Organization.objects.create(
            name="Charity Foundation - Education Wing",
            description="Focused on learning, scholarships and school support for children.",
            mission="Expand access to quality education for underprivileged children.",
            founded_date="2016-09-01",
            email="education@charityfoundation.org",
            phone="+1-555-0102",
            website="https://charityfoundation.org/education",
            address="200 Learning Blvd",
            city="Los Angeles",
            country="USA"
        )

        # Create Programs
        prog1 = Program.objects.create(
            organization=org1,
            name="Community Support Program",
            description="Health camps, food distribution and emergency relief in vulnerable neighborhoods.",
            category="health",
            start_date="2024-01-01",
            end_date="2025-12-31",
            budget=75000,
            target_beneficiaries=15000,
            status="active"
        )

        prog2 = Program.objects.create(
            organization=org2,
            name="Education Outreach",
            description="After-school tutoring, scholarships and school supplies for children.",
            category="education",
            start_date="2024-03-01",
            budget=25000,
            target_beneficiaries=2000,
            status="active"
        )

        prog3 = Program.objects.create(
            organization=org1,
            name="Volunteer Mobilization",
            description="Recruiting and training volunteers for local program delivery.",
            category="community",
            start_date="2024-05-01",
            budget=5000,
            target_beneficiaries=500,
            status="active"
        )

        # Create Volunteers
        vol1 = Volunteer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@volunteer.org",
            phone="+1-555-1001",
            bio="Passionate about community health and outreach.",
            skills="medical",
            experience_years=5,
            availability="part_time",
            organization=org1,
            is_active=True
        )
        vol1.programs.add(prog1)

        vol2 = Volunteer.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@volunteer.org",
            phone="+1-555-1002",
            bio="Experienced tutor and youth mentor.",
            skills="teaching",
            experience_years=3,
            availability="full_time",
            organization=org2,
            is_active=True
        )
        vol2.programs.add(prog2)

        # Create Donations
        Donation.objects.create(
            donor_name="Alice Johnson",
            donor_email="alice@example.com",
            donation_type="monetary",
            amount=5000,
            currency="USD",
            description="Support for mobile clinics",
            program=prog1,
            organization=org1,
            receipt_issued=True
        )

        Donation.objects.create(
            donor_name="Bob Wilson",
            donor_email="bob@example.com",
            donation_type="in_kind",
            amount=2000,
            currency="USD",
            description="Medical supplies donation",
            organization=org1
        )

        # Create Impact
        Impact.objects.create(
            program=prog1,
            people_reached=25000,
            lives_changed=5000,
            hours_contributed=10000,
            success_rate=92.5,
            testimonials="This program saved lives in our community."
        )

        # Create Events
        Event.objects.create(
            organization=org1,
            title="Health Awareness Campaign",
            description="Community health education and screening",
            event_date=timezone.now() + timedelta(days=30),
            location="Community Center, San Francisco",
            capacity=200,
            registered_count=120
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
