from django.db import models
from permissions.models import Permissions

# Create your models here.
class UserRole(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permissions)