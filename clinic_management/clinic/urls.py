from django.contrib import admin
from django.urls import path
from clinic import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
