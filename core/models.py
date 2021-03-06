from django.db import models
from django.contrib.auth.models import User

class complains(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name= models.CharField(max_length = 50)
   hostel = models.CharField(max_length = 50)
   time = models.CharField(max_length = 50)

   class Meta:
      db_table = "complains"


class roomRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length = 50)
    roomNo= models.CharField(max_length = 50)
    PhoneNo= models.CharField(max_length = 50)
    TimeCleaning= models.CharField(max_length = 50)

    class Meta:
        db_table = "roomRequest"
