from django.db import models
from django.core.validators import URLValidator, MinValueValidator
from django.utils import timezone

class Organization(models.Model):
    """NGO Organization model"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    mission = models.TextField()
    founded_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name


class Program(models.Model):
    """NGO Programs/Initiatives"""
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('health', 'Health'),
        ('environment', 'Environment'),
        ('poverty', 'Poverty Alleviation'),
        ('disaster', 'Disaster Relief'),
        ('community', 'Community Development'),
        ('other', 'Other'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    target_beneficiaries = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('completed', 'Completed'), ('planned', 'Planned')],
        default='active'
    )
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    """Volunteer information"""
    SKILL_CHOICES = [
        ('teaching', 'Teaching'),
        ('medical', 'Medical'),
        ('engineering', 'Engineering'),
        ('it', 'IT/Technology'),
        ('management', 'Project Management'),
        ('marketing', 'Marketing'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='volunteers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=20, choices=SKILL_CHOICES)
    experience_years = models.IntegerField(validators=[MinValueValidator(0)])
    availability = models.CharField(
        max_length=20,
        choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('weekend', 'Weekend Only')],
        default='part_time'
    )
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True, related_name='volunteers')
    programs = models.ManyToManyField(Program, related_name='volunteers', blank=True)
    joined_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Donation(models.Model):
    """Donation tracking"""
    DONATION_TYPE = [
        ('monetary', 'Monetary'),
        ('in_kind', 'In-Kind'),
        ('service', 'Service'),
    ]
    
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField(blank=True)
    donor_phone = models.CharField(max_length=20, blank=True)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, default='USD')
    description = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True, related_name='donations')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='donations')
    donation_date = models.DateField(auto_now_add=True)
    receipt_issued = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-donation_date']

    def __str__(self):
        return f"{self.donor_name} - {self.amount} {self.currency}"


class Impact(models.Model):
    """Track NGO impact metrics"""
    program = models.OneToOneField(Program, on_delete=models.CASCADE, related_name='impact')
    people_reached = models.IntegerField(validators=[MinValueValidator(0)])
    lives_changed = models.IntegerField(validators=[MinValueValidator(0)])
    hours_contributed = models.IntegerField(validators=[MinValueValidator(0)])
    success_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MinValueValidator(100)])
    testimonials = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Impact Metrics'

    def __str__(self):
        return f"Impact - {self.program.name}"


class Event(models.Model):
    """NGO Events and activities"""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=300)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    registered_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.title
