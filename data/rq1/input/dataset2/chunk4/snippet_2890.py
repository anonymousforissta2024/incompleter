#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#serializers.py


from rest_framework import serializers
from myapp.models import Airport, Flight, User, Passenger, Booking 


class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email','name','contact_number','gender','address','state','city','country','pincode','dob','password', 'password2']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']

# class UserProfileSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = '__all__'



class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False)
    class Meta:
        model= Passenger
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields = '__all__'


    