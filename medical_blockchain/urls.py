# medical_blockchain/urls.py
from django.contrib import admin
from django.urls import path, include
from patients.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),  # Includes URLs from the patients app
    path('', home, name='home'),  # Route the root URL to the home view
]
