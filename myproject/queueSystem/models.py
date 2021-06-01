from django.db import models
from users.models import Member
from restaurants.models import Restaurant

# Create your models here.
class Queue(models.Model):
    queueID = models.CharField(max_length=10, primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    resID = models.ForeignKey(
        Restaurant, blank=True, null=True, on_delete=models.CASCADE
    )
    peopleNum = models.IntegerField(default=0)
    queueCreated = models.DateTimeField(auto_now_add=True)
    reserveTime = models.DateTimeField(blank=True, null=True)
    queueType = (
        ("S", "Success"),
        ("F", "Fail"),
        ("C", "Cancel"),
        ("P", "Point"),
    )
    queueIsSuccess = models.CharField(max_length=10, choices=queueType)
    queueIsCome = models.BooleanField()

    class Meta:
        db_table = "queue"

    def __str__(self):
        return self.queueID


class Review(models.Model):
    reviewID = models.CharField(max_length=10, primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    detail = models.CharField(max_length=200)
    rating = models.FloatField(default=0)

    class Meta:
        db_table = "review"

    def __str__(self):
        return self.reviewID