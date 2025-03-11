from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Ride
from django.contrib.auth.models import User

# Fix: Re-add map_view function
def map_view(request):
    return render(request, 'rides/map.html')

@csrf_exempt
def create_ride(request):
    if request.method == "POST":
        try:
            # Print the raw request body for debugging
            print("Raw request body:", request.body)

            data = json.loads(request.body)  # Read JSON request body

            # Print parsed JSON data
            print("Parsed data:", data)

            # Ensure all required fields exist
            if not all(k in data for k in ('pickup_lat', 'pickup_lng', 'dropoff_lat', 'dropoff_lng')):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            user = User.objects.first()  # Temporarily assign first user
            ride = Ride.objects.create(
                passenger=user,
                pickup_lat=data['pickup_lat'],
                pickup_lng=data['pickup_lng'],
                dropoff_lat=data['dropoff_lat'],
                dropoff_lng=data['dropoff_lng'],
            )

            print("Ride created successfully:", ride.id)
            return JsonResponse({"message": "Ride created successfully!", "ride_id": ride.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

