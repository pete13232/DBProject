from re import split
from typing import Text
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    def genID():
        n = Category.objects.count()
        if n == 0:
            return "CT001"
        else:
            return "CT" + str(n + 1).zfill(3)

    categoryID = models.CharField(max_length=10, primary_key=True, default=genID)
    categoryName = models.CharField(max_length=20)
    minuteWait = models.IntegerField()

    def __str__(self):
        return self.categoryID

    def fullCate(self):
        list_string = self.categoryName.split(" ")
        string = "_".join(list_string)
        return string


class Company(models.Model):
    class Meta:
        db_table = "company"

    def genID():
        n = Company.objects.count()
        if n == 0:
            return "C001"
        else:
            return "C" + str(n + 1).zfill(3)

    companyID = models.CharField(max_length=10, primary_key=True, default=genID)
    companyName = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    subDistrict = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    profilePic = models.ImageField(upload_to="static/images/", blank=True, null=True)
    coverPic = models.ImageField(upload_to="static/images/", blank=True, null=True)

    def __str__(self):
        return self.companyID


class Restaurant(models.Model):
    class Meta:
        db_table = "Restaurant"

    def genID():
        n = Restaurant.objects.count()
        if n == 0:
            return "R001"
        else:
            return "R" + str(n + 1).zfill(3)

    resID = models.CharField(max_length=10, primary_key=True, default=genID)
    companyID = models.ForeignKey(
        Company, blank=True, null=True, on_delete=models.SET_NULL
    )
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    resName = models.CharField(max_length=30)
    open = models.TimeField()
    close = models.TimeField()
    address = models.CharField(max_length=20)
    subDistrict = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    ig = models.CharField(max_length=50, null=True)
    fb = models.CharField(max_length=50, null=True)
    mapLon = models.CharField(max_length=10, default=0)
    mapLAT = models.CharField(max_length=10, default=0)
    profilePic = models.ImageField(upload_to="static/images/", blank=True, null=True)
    coverPic = models.ImageField(upload_to="static/images/", blank=True, null=True)

    def __str__(self):
        return self.resID

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

    def fullPhone(self):
        return self.tel[0:3] + "-" + self.tel[3:6] + "-" + self.tel[6:10]

    def location(self):
        return self.mapLon + "," + self.mapLAT


class Menu(models.Model):
    class Meta:
        db_table = "menu"

    def genID():
        n = Menu.objects.count()
        if n == 0:
            return "MU001"
        else:
            return "MU" + str(n + 1).zfill(3)

    menuID = models.CharField(max_length=15, primary_key=True, default=genID)
    resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menuName = models.CharField(max_length=20)
    description = models.TextField(null=True)
    price = models.FloatField()
    avaliable = models.BooleanField()
    picture = models.ImageField(upload_to="static/images/", blank=True, null=True)

    def __str__(self):
        return self.menuID
