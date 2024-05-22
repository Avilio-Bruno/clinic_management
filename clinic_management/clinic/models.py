from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='clinic_user_groups',  # Изменено здесь
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='clinic_user_permissions',  # И здесь
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    license_expiry_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name
