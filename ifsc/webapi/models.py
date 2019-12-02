from django.db import models


class ifscsearch(models.Model):
    ifsc = models.CharField(max_length=30)
    bank_id = models.CharField(max_length=3)
    branch = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    def __str__(self):
        return self.bank_name
