from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from products.models import Product

# class UserCreate(models.Model):
#     user=models.CharField(User,on_delete=models.CASCADE)
#     image=models.ImageField(upload_to='accouts/media/')

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"


