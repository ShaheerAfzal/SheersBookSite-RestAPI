#from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .emails import *
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = (
            User.objects.filter(email=username).first()
            or User.objects.filter(username=username).first()
        )

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        else:
            raise serializers.ValidationError(
                "No active account found with the given credentials"
            )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =[ 
        "email",
        "password",
        "is_verified",
        #"first_name", "last_name"
                
        ]
    def create(self, validated_data):
        user = User.objects.create(
            #username=validated_data["username"],
            email=validated_data["email"],
            #first_name=validated_data["first_name"],
            #last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        # def post(self, request):
        #     try:
        #         data = request.data
        #         serializer = UserSerializer(data=data)
        #         if serializer.is_valid():
        #             # Assuming send_otp_via_email is a function to send the OTP
                # return Response({
                #         'status': status.HTTP_200_OK,
                #         'message': "Registeration succesful, check email for verification otp",
                #     })
            # except Exception as e:
            #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user.save()
        send_otp_via_email(validated_data['email'])  
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            #"username", 
            "email", 
            #"first_name", "last_name",
            "password")
        extra_kwargs = {
            "password": {"write_only": True},
            #"username": {"read_only": True},
            "email": {"read_only": True},
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "is_verified",
        ]