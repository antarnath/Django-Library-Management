from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from .context_processors import SESSION

# Create your models here.

class Student(AbstractBaseUser):
    first_name      = models.CharField(max_length=255, blank=True, null=True)
    last_name       = models.CharField(max_length=255, blank=True, null=True)
    username        = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    student_id      = models.IntegerField(unique=True, null=True)
    department_name = models.CharField(max_length=255,blank=True,null=True)
    phone_number    = models.CharField(max_length=15, blank=True, null=True)
    session         = models.CharField(max_length=255, choices=SESSION)
    
    
    data_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    
    objects = UserManager()
    
    def full_name(self):
        return f'{self.full_name} {self.last_name}'
    
    def get_email(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True