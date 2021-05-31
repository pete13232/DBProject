from typing import Text
from django.db import models

# Create your models here.
class Category(models.Model):
    categoryID = models.CharField(max_length=10, primary_key=True)
    categoryName = models.CharField(max_length=20)
    minuteWait = models.IntegerField()

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryID


class Company(models.Model):
    companyID = models.CharField(max_length=10, primary_key=True)
    categoryNameTH = models.CharField(max_length=30)
    categoryNameEN = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    subDistrict = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    picture = models.URLField(max_length=200, blank=True)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.companyID


class Restaurant(models.Model):
    resID = models.CharField(max_length=10, primary_key=True)
    companyID = models.ForeignKey(
        Company, blank=True, null=True, on_delete=models.SET_NULL
    )
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    resNameTH = models.CharField(max_length=30)
    resNameEN = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    subDistrict = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    picture = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "Restaurant"

    def __str__(self):
        return self.resID


class Menu(models.Model):
    menuID = models.CharField(max_length=15, primary_key=True)
    resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menuNameTH = models.CharField(max_length=20)
    menuNameEN = models.CharField(max_length=20)
    description = models.TextField(null=True)
    price = models.FloatField()
    avaliable = models.BooleanField()
    picture = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "menu"

    def __str__(self):
        return self.menuID
