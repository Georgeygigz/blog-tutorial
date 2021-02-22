
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.response import Response


from .serializers import RegistrationSerializer, User


class RegistrationApiView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        user_data = request.data

        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save

        return_message = {
            "message": "Registration successful",
            "data": serializer.data
        }

        return Response(return_message, status=status.HTTP_201_CREATED)