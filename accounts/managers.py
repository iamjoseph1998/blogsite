from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', False)

        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        if not extra_fields.setdefault('is_active'):
            raise ValueError('Superuser has to have is_active True')

        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.setdefault('is_superuser'):
            raise ValueError('Superuser has to have is_superuser True')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
