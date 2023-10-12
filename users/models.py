from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email = email
            #이메일 형식 받는 것 밑에 참고
            #email=self.normalize_email(email), 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    nickname = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
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
    fullname = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    job = models.CharField(max_length=50)
    religion = models.CharField(choices=ReligionChoices.choices, max_length=10)
    my_character = models.TextField()
    purpose_to_join = models.CharField(max_length=100)
    like = models.ManyToManyField(User, related_name='like_profiles')

    def __str__(self):
        return str(self.user)