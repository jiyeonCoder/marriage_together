from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
    

class Profile(models.Model):
    class ReligionChoices(models.TextChoices):
        PROTESTANTISM = '개신교'
        BUDDHISM = '불교'
        CATHOLICISM = '천주교'
        OTHERS = '기타'
        NO_RELIGION = '종교 없음'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='profile/%Y/%m/')
    introduce_me = models.TextField()
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    job = models.CharField(max_length=50)
    religion = models.CharField(choices=ReligionChoices.choices, max_length=10)
    my_character = models.TextField()
    purpose_to_join = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)