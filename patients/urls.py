# patients/urls.py
from django.urls import path

from . import views
from .views import create_patient, create_medical_record, patient_list, patient_detail, home, delete_medical_record, \
    view_patient_hash_chain

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_patient, name='create_patient'),
    path('<int:patient_id>/', patient_detail, name='patient_detail'),
    path('<int:patient_id>/record/create/', create_medical_record, name='create_medical_record'),
    path('list/', patient_list, name='patient_list'),  # Add this line
    path('<int:patient_id>/record/delete/<int:record_id>/', delete_medical_record, name='delete_medical_record'),
    path('patient/<int:pk>/hash_chain/', view_patient_hash_chain, name='view_patient_hash_chain'),
    path('patients/', views.patient_list, name='patient_list'),

]
