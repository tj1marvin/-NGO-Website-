from django.contrib import admin
from .models import Organization, Program, Volunteer, Donation, Impact, Event

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'city', 'created_at']
    search_fields = ['name', 'email', 'city']
    list_filter = ['created_at', 'country']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'category', 'status', 'start_date']
    search_fields = ['name', 'organization__name']
    list_filter = ['category', 'status', 'start_date']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'skills', 'organization', 'is_active']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['skills', 'availability', 'is_active', 'joined_date']
    filter_horizontal = ['programs']


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'amount', 'currency', 'donation_type', 'organization', 'donation_date']
    search_fields = ['donor_name', 'donor_email']
    list_filter = ['donation_type', 'donation_date', 'receipt_issued']
    readonly_fields = ['created_at']


@admin.register(Impact)
class ImpactAdmin(admin.ModelAdmin):
    list_display = ['program', 'people_reached', 'lives_changed', 'hours_contributed']
    search_fields = ['program__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'event_date', 'location', 'capacity']
    search_fields = ['title', 'organization__name']
    list_filter = ['event_date', 'organization']
    readonly_fields = ['created_at', 'updated_at']
