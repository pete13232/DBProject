from django.utils.translation import gettext_lazy as _
from django.db import models
from restaurants.models import Restaurant, Company
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Member(AbstractUser):
    class Meta:
        db_table = "member"

    def genID():
        n = Member.objects.count()
        if n == 0:
            return "M001"
        else:
            return "M" + str(n + 1).zfill(3)

    companyID = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.SET_NULL
    )

    resID = models.ForeignKey(
        Restaurant, null=True, blank=True, on_delete=models.SET_NULL
    )
    username = None
    first_name = None
    last_name = None
    ROLE = (
        ("admin", "admin"),
        ("executive", "executive"),
        ("manager", "manager"),
        ("staff", "staff"),
        ("member", "member"),
    )
    role = models.CharField(max_length=10, choices=ROLE, default="member")
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
    profile = ProcessedImageField(
        upload_to="static/images/%Y/%m/%d",
        format="PNG",
        options={"quality": 60},
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


class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars")
    avatar_thumbnail = ProcessedImageField(
        upload_to="avatars",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
