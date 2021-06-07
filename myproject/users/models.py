from django.db.models.query import NamedValuesListIterable
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
        db_table = "Member"

    def genID():
        n = Member.objects.count()
        if n == 0:
            return "M001"
        else:
            return "M" + str(n + 1).zfill(3)

    def fullName(self):
        return self.fName + " " + self.lName

    def __str__(self):
        return self.email

    def fullPhone(self):
        return self.tel[0:3] + "-" + self.tel[3:6] + "-" + self.tel[6:10]

    def getProfilePic(self):
        if self.profilePic:
            return self.profilePic.url
        return (
            "https://ui-avatars.com/api/?name="
            + self.fullName()
            + "&color=7F9CF5&background=EBF4FF"
        )

    def fullAddress(self):
        return (
            self.address
            + " "
            + self.subDistrict
            + " "
            + self.district
            + " "
            + self.province
            + " "
            + self.postalCode
        )

    memberID = models.CharField(max_length=50, primary_key=True, default=genID)
    resID = models.ForeignKey(
        Restaurant, null=True, blank=True, on_delete=models.SET_NULL
    )
    companyID = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.SET_NULL
    )
    username = None
    first_name = None
    last_name = None
    groups = None
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
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True)

    profilePic = ProcessedImageField(
        null=True,
        upload_to="static/images/%Y/%m/%d",
        format="PNG",
        options={"quality": 60},
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
