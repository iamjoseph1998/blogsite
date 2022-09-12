from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .managers import UserManager

class User(AbstractUser):

    username = is_staff = None

    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    mobile = models.CharField(max_length=10, unique=True, null=True, blank=True)
    intro = models.CharField(max_length=1024, blank=True, null=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    @property
    def is_staff(self):
        return self.is_superuser
