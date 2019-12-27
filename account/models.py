from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    user_type = models.CharField(max_length=30)
    class Meta:
        db_table='account'


class Notifications(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=250,default=" ")
    message = models.CharField(max_length=250,default=" ")
    url = models.CharField(max_length=100,default="home")
    date = models.DateTimeField(auto_now=True)

    def notify(user,title,message,url):
        n = Notifications()
        n.user = user
        n.title =title
        n.message = message
        n.url = url
        n.save()


    class Meta:
        db_table='notifications'