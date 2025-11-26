from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from core.models import Organization, Program, Volunteer, Donation, Impact, Event


class OrganizationTestCase(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(
            name="Test NGO",
            description="Test Description",
            mission="Test Mission",
            founded_date="2020-01-01",
            email="test@ngo.org",
            phone="+1-555-0000",
            address="123 Test St",
            city="Test City",
            country="Test Country"
        )

    def test_organization_creation(self):
        self.assertEqual(self.org.name, "Test NGO")
        self.assertEqual(self.org.email, "test@ngo.org")

    def test_organization_string_representation(self):
        self.assertEqual(str(self.org), "Test NGO")


class ProgramTestCase(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(
            name="Test NGO",
            description="Test Description",
            mission="Test Mission",
            founded_date="2020-01-01",
            email="test@ngo.org",
            phone="+1-555-0000",
            address="123 Test St",
            city="Test City",
            country="Test Country"
        )
        self.program = Program.objects.create(
            organization=self.org,
            name="Test Program",
            description="Test Program Description",
            category="education",
            start_date="2023-01-01",
            budget=100000,
            target_beneficiaries=1000,
            status="active"
        )

    def test_program_creation(self):
        self.assertEqual(self.program.name, "Test Program")
        self.assertEqual(self.program.organization, self.org)

    def test_program_string_representation(self):
        self.assertEqual(str(self.program), "Test Program")


class VolunteerTestCase(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(
            name="Test NGO",
            description="Test Description",
            mission="Test Mission",
            founded_date="2020-01-01",
            email="test@ngo.org",
            phone="+1-555-0000",
            address="123 Test St",
            city="Test City",
            country="Test Country"
        )
        self.volunteer = Volunteer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="+1-555-1234",
            skills="teaching",
            experience_years=5,
            organization=self.org
        )

    def test_volunteer_creation(self):
        self.assertEqual(self.volunteer.first_name, "John")
        self.assertEqual(self.volunteer.email, "john@example.com")

    def test_volunteer_string_representation(self):
        self.assertEqual(str(self.volunteer), "John Doe")


class DonationTestCase(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(
            name="Test NGO",
            description="Test Description",
            mission="Test Mission",
            founded_date="2020-01-01",
            email="test@ngo.org",
            phone="+1-555-0000",
            address="123 Test St",
            city="Test City",
            country="Test Country"
        )
        self.donation = Donation.objects.create(
            donor_name="Test Donor",
            donor_email="donor@example.com",
            donation_type="monetary",
            amount=5000,
            description="Test Donation",
            organization=self.org
        )

    def test_donation_creation(self):
        self.assertEqual(self.donation.donor_name, "Test Donor")
        self.assertEqual(self.donation.amount, 5000)

    def test_donation_string_representation(self):
        self.assertEqual(str(self.donation), "Test Donor - 5000 USD")


class EventTestCase(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(
            name="Test NGO",
            description="Test Description",
            mission="Test Mission",
            founded_date="2020-01-01",
            email="test@ngo.org",
            phone="+1-555-0000",
            address="123 Test St",
            city="Test City",
            country="Test Country"
        )
        self.event = Event.objects.create(
            organization=self.org,
            title="Test Event",
            description="Test Event Description",
            event_date=timezone.now() + timedelta(days=30),
            location="Test Location",
            capacity=100
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, "Test Event")
        self.assertEqual(self.event.capacity, 100)

    def test_event_string_representation(self):
        self.assertEqual(str(self.event), "Test Event")
