from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        allow_null=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message= "Email already exist.",
            )
        ],
        error_messages={
            'required': "This field is required.",
        }
    )

    password = serializers.RegexField(
        regex=("^(?=.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*"),
        min_length=8,
        max_length=30,
        required=True,
        allow_null=False,
        write_only=True,
        error_messages={
            'required': "This field is required.",
            'min_length': "{} must be at least {} characters long.".format("Password", "8"),
            'max_length': 'Password cannot be more than 30 characters',
            'invalid': "Password must have at least a number, and a least an uppercase and a lowercase letter.",
        }
    )

    username = serializers.RegexField(
        regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
        allow_null=False,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message= "Username already exist.",
            )
        ],
        error_messages={
            'required': "This field is required.",
            'invalid': "Username cannot have spaces or special characters."
        }
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'id', 'password']

    @classmethod
    def create(self, data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**data)