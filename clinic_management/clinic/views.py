from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PatientRegistrationForm, DoctorRegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_doctor:
                return redirect('doctor_dashboard')
            elif user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('patient_dashboard')
        else:
            return render(request, 'clinic/login.html', {'error': 'Invalid username or password'})
    return render(request, 'clinic/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'clinic/register_patient.html', {'form': form})

@login_required
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'clinic/register_doctor.html', {'form': form})

@login_required
def patient_dashboard(request):
    return render(request, 'clinic/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'clinic/doctor_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'clinic/admin_dashboard.html')

def home(request):
    return render(request, 'clinic/home.html')
