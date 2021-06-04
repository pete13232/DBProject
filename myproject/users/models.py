from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from restaurants.models import Restaurant
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

from .managers import CustomUserManager

# Create your models here.
class Role(Group):
    class Meta:
        proxy = True
        app_label = "auth"
        verbose_name = _("Role")


class Member(AbstractUser):
    class Meta:
        db_table = "member"

    def genID():
        n = Member.objects.count()
        if n == 0:
            return "M001"
        else:
            return "M" + str(n + 1).zfill(3)

    roleID = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)
    resID = models.ForeignKey(
        Restaurant, null=True, blank=True, on_delete=models.SET_NULL
    )
    username = None
    first_name = None
    last_name = None
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    tel = models.CharField(max_length=10)
    dob = models.DateField(null=True)
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    picture = models.ImageField(
        upload_to="static/images/", default="static/images/defaultProfile.png"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def fullName(self):
        return self.fName + " " + self.lName

    def fullPhone(self):
        return self.tel[0:3] + "-" + self.tel[3:6] + "-" + self.tel[6:10]

    def showGender(self):
        if self.gender == "M":
            return "Male"
        elif self.gender == "F":
            return "Female"
        else:
            return "Other"
