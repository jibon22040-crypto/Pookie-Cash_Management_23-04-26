from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    
    def __str__(self):
        return self.user.username
    

class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    def __str__(self):
        return self.user.username



class AddCashModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    source = models.CharField(max_length=200,null=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


class ExpenseModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=255,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"