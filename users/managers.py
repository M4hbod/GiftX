from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class CustomUsermanager(BaseUserManager):
    @transaction.atomic
    def create_user(self, email: str, phone_number: str, password: str, is_superuser: bool = False):
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, phone_number: str, password: str):
        return self.create_user(email=email, phone_number=phone_number, password=password, is_superuser=True)
