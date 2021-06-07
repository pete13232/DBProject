from django.db import models
from django.utils import timezone
from users.models import Member
from restaurants.models import Restaurant


# Create your models here.
class Queue(models.Model):
    class Meta:
        db_table = "Queue"

    def genID():
        n = Queue.objects.count()
        if n == 0:
            return "Q001"
        else:
            return "Q" + str(n + 1).zfill(3)

    def __str__(self):
        return self.queueID

    queueID = models.CharField(max_length=10, primary_key=True, default=genID)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    resID = models.ForeignKey(
        Restaurant, blank=True, null=True, on_delete=models.CASCADE
    )
    peopleNum = models.IntegerField(default=0)
    queueCreated = models.DateTimeField(auto_now_add=True)
    reserveDateTime = models.DateTimeField(null=True, default=timezone.now)
    TYPE = (
        ("success", "success"),
        ("fail", "fail"),
        ("calling", "calling"),
        ("waiting", "waiting"),
        ("cancel", "cancel"),
        ("point", "point"),
    )
    status = models.CharField(max_length=10, choices=TYPE, default="waiting")
    queueIsPass = models.BooleanField(default=False)
    point = models.IntegerField(default = 0)


class Review(models.Model):
    class Meta:
        db_table = "Review"

    def genID():
        n = Review.objects.count()
        if n == 0:
            return "RV001"
        else:
            return "RV" + str(n + 1).zfill(3)

    def __str__(self):
        return self.reviewID

    reviewID = models.CharField(max_length=10, primary_key=True, default=genID)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    detail = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    dateCreated = models.DateTimeField(auto_now_add=True)
