#Source: https://stackoverflow.com/questions/72095878/typeerror-create-superuser-missing-2-required-positional-arguments
from django.contrib.auth.base_user import BaseUserManager

class UserManger(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name or last_name:
            raise ValueError("Users must have a first and last name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(user.password)
        #user.is_staff = True
        user.is_superuser = True
        #user.is_admin = True
        user.save(using=self._db)
        return user