from rest_framework import viewsets
from django.shortcuts import render
from .models import Activity, Accommodation, Destination
from .serializers import ActivitySerializer, AccommodationSerializer, DestinationSerializer


def index(request):
    destinations = Destination.objects.all()
    return render(request, 'index.html', {'destinations': destinations})


class TripOptionsViewSet(viewsets.ViewSet):
    def create(self, request):
        destination_id = request.data.get('destination')
        activities = Activity.objects.filter(DestinationID=destination_id)
        accommodations = Accommodation.objects.filter(DestinationID=destination_id)
        destinations = Destination.objects.filter(DestinationID=destination_id).values('City', 'Country', 'Region', 'Description').first()
        destination_serializer = DestinationSerializer(data=destinations)  # Serialize destination data
        print(request.POST)
        # Check if the serializer data is valid before accessing .data
        if destination_serializer.is_valid():
            destination_data = destination_serializer.data
        else:
            # Handle the case where data is not valid
            destination_data = None
      
        
        activities_serializer = ActivitySerializer(activities, many=True)
        accommodations_serializer = AccommodationSerializer(accommodations, many=True)
        return render(request, "trip_options.html", {'activities': activities_serializer.data,'accommodations': accommodations_serializer.data, 'destinations': destination_data})