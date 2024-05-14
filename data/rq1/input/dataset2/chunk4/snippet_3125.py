#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#views.py



from django.shortcuts import render
from django.http import Http404, JsonResponse
#from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticatedOrReadOnly,IsAuthenticated, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from myapp.renderers import UserRenderer
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from myapp.models import Airport, Flight, User, Passenger, Booking
from myapp.serializers import *
from myapp.permissions import IsOwnerOrAdmin
from rest_framework import viewsets



def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }



# Create your views here.

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrtieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    








class FlightListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    permission_classes= [DjangoModelPermissions]


class FlightRetrtieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class AirportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class AirportRetrtieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer





class PassengerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerRetrtieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer



class BookingRetrtieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



class BookViewSet(viewsets.ModelViewSet):
    
    # queryset = Book.objects.all()
    serializer_class = BookingSerializer
    # print(serializer_class)
    def get_queryset(self):
        book = Booking.objects.all()
        return book 

    def create(self, request, *args, **kwargs):
        data = request.data

        user = User.objects.get(id=data["user"])
        flightdetails = Flight.objects.get(id=data["flights"])
        # bookingdetails = Booking.objects.get(no_of_passengers=data["no_of_passengers"])

        
        new_book = Booking.objects.create(
            booking_number= data["booking_number"],
            no_of_passengers= data["no_of_passengers"],
            user=user,
            flights=flightdetails,
        )
        new_book.save()
        for passenger in data["passenger"]:
            passenger_book= Passenger.objects.create(
                user = user,
                name= passenger["name"],
                contact_number = passenger["contact_number"],
                email = passenger["email"],
                gender = passenger["gender"],
                age = passenger["age"]

            )
            new_book.passenger.add(passenger_book)

            if flightdetails.available_seats < len(data["passenger"]):
                return Response({"data": "No seats available", "status": status.HTTP_400_BAD_REQUEST})
            update_seats = flightdetails.available_seats - data["no_of_passengers"]
            flightdetails.available_seats = update_seats
            flightdetails.save()
            serializers = BookingSerializer(new_book)
            return Response({"data": serializers.data, "status": status.HTTP_201_CREATED})