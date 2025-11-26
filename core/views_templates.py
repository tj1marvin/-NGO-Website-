from django.shortcuts import render
from .models import Organization, Program, Volunteer


def index(request):
    return render(request, 'home.html')


def organizations_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations.html', {'organizations': organizations})


def programs_list(request):
    programs = Program.objects.all()
    return render(request, 'programs.html', {'programs': programs})


def volunteers_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers.html', {'volunteers': volunteers})
def donate(request):
    return render(request, 'donate.html')
