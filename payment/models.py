from django.db import models
from datetime import date
# Create your models here.
class PaidUser(models.Model):
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    expiry_date = models.DateField(default=date(2019,5,5))

class payment(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)