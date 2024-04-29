from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Customer_profile')
    phone=models.IntegerField()
   
    def __str__(self) -> str:
        return self.user.username