import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from .managers import CustomUsermanager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=11, validators=[RegexValidator(r"^09\d{9}$")])
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]
    objects = CustomUsermanager()

    def __str__(self):
        return f"<User {self.id}>"

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
