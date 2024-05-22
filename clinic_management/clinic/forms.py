from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Doctor, Patient

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class DoctorRegistrationForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    license_number = forms.CharField(max_length=20)
    license_expiry_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'specialization', 'phone', 'license_number', 'license_expiry_date')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor(user=user, specialization=self.cleaned_data['specialization'],
                        phone=self.cleaned_data['phone'], license_number=self.cleaned_data['license_number'],
                        license_expiry_date=self.cleaned_data['license_expiry_date'])
        if commit:
            doctor.save()
        return user

class PatientRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'full_name', 'date_of_birth', 'doctor')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient(user=user, full_name=self.cleaned_data['full_name'],
                          date_of_birth=self.cleaned_data['date_of_birth'],
                          doctor=self.cleaned_data['doctor'])
        if commit:
            patient.save()
        return user
