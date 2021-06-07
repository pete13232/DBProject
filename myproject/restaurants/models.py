from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "Category"

    def genID():
        n = Category.objects.count()
        if n == 0:
            return "CT001"
        else:
            return "CT" + str(n + 1).zfill(3)

    def __str__(self):
        return self.categoryID

    def fullCate(self):
        list_string = self.categoryName.split(" ")
        string = "_".join(list_string)
        return string

    categoryID = models.CharField(max_length=10, primary_key=True, default=genID)
    categoryName = models.CharField(max_length=20)
    minuteWait = models.IntegerField()


class Company(models.Model):
    class Meta:
        db_table = "Company"

    def genID():
        n = Company.objects.count()
        if n == 0:
            return "C001"
        else:
            return "C" + str(n + 1).zfill(3)

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

    def __str__(self):
        return self.companyID

    companyID = models.CharField(max_length=10, primary_key=True, default=genID)
    companyName = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    subDistrict = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    profilePic = ProcessedImageField(
        null=True,
        upload_to="static/images/%Y/%m/%d",
        format="PNG",
        options={"quality": 60},
    )
    success = models.BooleanField(default=False, null=True)


class Restaurant(models.Model):
    class Meta:
        db_table = "Restaurant"

    def genID():
        n = Restaurant.objects.count()
        if n == 0:
            return "R001"
        else:
            return "R" + str(n + 1).zfill(3)

    def getProfilePic(self):
        if self.profilePic:
            return self.profilePic.url
        return (
            "https://ui-avatars.com/api/?name="
            + self.resName
            + "&color=7F9CF5&background=EBF4FF"
        )

    def getCoverPic(self):
        if self.coverPic:
            return self.coverPic.url
        return (
            "https://ui-avatars.com/api/?name="
            + self.resName
            + "&color=7F9CF5&background=EBF4FF"
        )

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
    profilePic = ProcessedImageField(
        null=True,
        upload_to="static/images/%Y/%m/%d",
        format="PNG",
        options={"quality": 60},
    )
    coverPic = ProcessedImageField(
        null=True,
        upload_to="static/images/%Y/%m/%d",
        format="PNG",
        options={"quality": 60},
    )
    success = models.BooleanField(default=False, null=True)


class Menu(models.Model):
    class Meta:
        db_table = "menu"

    def genID():
        n = Menu.objects.count()
        if n == 0:
            return "MU001"
        else:
            return "MU" + str(n + 1).zfill(3)

    def getProfilePic(self):
        if self.profilePic:
            return self.profilePic.url
        return (
            "https://ui-avatars.com/api/?name="
            + self.menuName
            + "&color=7F9CF5&background=EBF4FF"
        )

    def __str__(self):
        return self.menuID

    menuID = models.CharField(max_length=15, primary_key=True, default=genID)
    resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menuName = models.CharField(max_length=20)
    description = models.TextField(null=True)
    price = models.FloatField()
    avaliable = models.BooleanField()
    profilePic = ProcessedImageField(
        null=True,
        upload_to="static/images/%Y/%m/%d",
        format="PNG",
        options={"quality": 60},
    )