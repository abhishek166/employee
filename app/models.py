from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = PhoneNumberField(null=False,blank=False,unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name