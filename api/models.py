from django.db import models

# Create your models here.

class Users(models.Model):
  username = models.CharField(max_length=200)
  email = models.EmailField(max_length=254)
  password = models.CharField(max_length=50)
  # status = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.username