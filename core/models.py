from django.db import models
from django.contrib.auth.models import User


class complains(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    roomno = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=50)
    complaint = models.CharField(max_length=500)

    type = models.CharField(max_length=10, default='Complains', editable=False)

    class Meta:
        db_table = "complains"


class medical(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    roomno = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    problem = models.CharField(max_length=500)
    time = models.CharField(max_length=50)

    type = models.CharField(max_length=10, default='Medical', editable=False)

    class Meta:
        db_table = "medical"


class roomRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    roomNo = models.CharField(max_length=50)
    PhoneNo = models.CharField(max_length=50)
    TimeCleaning = models.CharField(max_length=50)

    type = models.CharField(
        max_length=15, default='Room Request', editable=False)

    class Meta:
        db_table = "roomRequest"


class laundaryRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    roomno = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    type = models.CharField(max_length=15, default='Laundary', editable=False)

    class Meta:
        db_table = "laundary"


class notifications(models.Model):
    forUser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    time = models.CharField(max_length=50)

    class Meta:
        db_table = "notifications"
