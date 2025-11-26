from rest_framework import serializers
from .models import Organization, Program, Volunteer, Donation, Impact, Event


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'mission', 'founded_date', 'email', 
                 'phone', 'website', 'address', 'city', 'country', 'created_at']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'organization', 'name', 'description', 'category', 'start_date',
                 'end_date', 'budget', 'target_beneficiaries', 'status', 'created_at']


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'skills',
                 'experience_years', 'availability', 'organization', 'is_active', 'joined_date']


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donor_name', 'donor_email', 'donation_type', 'amount',
                 'currency', 'program', 'organization', 'donation_date', 'receipt_issued']


class ImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impact
        fields = ['id', 'program', 'people_reached', 'lives_changed', 
                 'hours_contributed', 'success_rate', 'created_at']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'organization', 'title', 'description', 'event_date',
                 'location', 'capacity', 'registered_count', 'created_at']
