from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, phone_number):

        if not email:
            raise ValueError('email must be set')
        if not password:
            raise ValueError('password must be set')
        if not phone_number:
            raise ValueError('phone number must be set')

        user = self.model(email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, phone_number):

        user = self.create_user(email, password, phone_number)
        user.is_admin = True
        user.save(using=self._db)
        return user

