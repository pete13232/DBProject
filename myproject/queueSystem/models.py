from django.db import models
from django.utils import timezone
from users.models import Member
from restaurants.models import Restaurant

import datetime

# Create your models here.
class Queue(models.Model):
    def genID():
        n = Queue.objects.count()
        if n == 0:
            return "Q001"
        else:
            return "Q" + str(n + 1).zfill(3)

    queueID = models.CharField(max_length=10, primary_key=True, default=genID)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    resID = models.ForeignKey(
        Restaurant, blank=True, null=True, on_delete=models.CASCADE
    )
    peopleNum = models.IntegerField(default=0)
    queueCreated = models.DateTimeField(auto_now_add=True)
    reserveDate = models.DateField(null=True, default=datetime.date.today)
    reserveTime = models.TimeField(null=True, default=timezone.now)
    queueType = (
        ("success", "success"),
        ("fail", "fail"),
        ("waiting", "waiting"),
        ("cancel", "cancel"),
        ("point", "point"),
    )
    queueIsSuccess = models.CharField(
        max_length=10, choices=queueType, default="waiting"
    )
    queueIsPass = models.BooleanField(default=False)

    class Meta:
        db_table = "queue"

    def __str__(self):
        return self.queueID


class Review(models.Model):
    def genID():
        n = Review.objects.count()
        if n == 0:
            return "RV001"
        else:
            return "RV" + str(n + 1).zfill(3)

    reviewID = models.CharField(max_length=10, primary_key=True, default=genID)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    detail = models.CharField(max_length=200)
    rating = models.FloatField(default=0)

    class Meta:
        db_table = "review"

    def __str__(self):
        return self.reviewID