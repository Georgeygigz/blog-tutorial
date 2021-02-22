
from django.urls import path
from .views import RegistrationApiView

urlpatterns = [
    path('signup/', RegistrationApiView.as_view(), name='user-registration'),
]