from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(null=True)




def __str__(self):
    return self.name
