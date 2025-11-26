from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Organization, Program, Volunteer, Donation, Impact, Event
from .serializers import (
    OrganizationSerializer, ProgramSerializer, VolunteerSerializer,
    DonationSerializer, ImpactSerializer, EventSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(detail=True, methods=['get'])
    def programs(self, request, pk=None):
        organization = self.get_object()
        programs = organization.programs.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def donations(self, request, pk=None):
        organization = self.get_object()
        donations = organization.donations.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def volunteers(self, request, pk=None):
        organization = self.get_object()
        volunteers = organization.volunteers.all()
        serializer = VolunteerSerializer(volunteers, many=True)
        return Response(serializer.data)


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    @action(detail=True, methods=['get'])
    def impact(self, request, pk=None):
        program = self.get_object()
        try:
            impact = program.impact
            serializer = ImpactSerializer(impact)
            return Response(serializer.data)
        except Impact.DoesNotExist:
            return Response({'detail': 'No impact data available'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def donations(self, request, pk=None):
        program = self.get_object()
        donations = program.donations.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

    @action(detail=False, methods=['get'])
    def active(self, request):
        volunteers = Volunteer.objects.filter(is_active=True)
        serializer = self.get_serializer(volunteers, many=True)
        return Response(serializer.data)


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        from django.db.models import Sum
        total_donations = Donation.objects.aggregate(total=Sum('amount'))
        count = Donation.objects.count()
        return Response({
            'total_amount': total_donations['total'],
            'donation_count': count
        })


class ImpactViewSet(viewsets.ModelViewSet):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        event = self.get_object()
        if event.registered_count < event.capacity:
            event.registered_count += 1
            event.save()
            return Response({'status': 'registered successfully'})
        return Response({'error': 'Event is at full capacity'}, status=status.HTTP_400_BAD_REQUEST)
