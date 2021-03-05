from django.db import models

class complains(models.Model):

   name= models.CharField(max_length = 50)
   hostel = models.CharField(max_length = 50)
   time = models.CharField(max_length = 50)

   class Meta:
      db_table = "complains"
