from django.db import models
class advisor(models.Model):
    name = models.CharField(max_length=100)
    password = models.IntegerField()

class users4(models.Model):
    userid=models.IntegerField(primary_key=True)
    data = models.FileField()
    name=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contactno=models.IntegerField()
    country=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    password = models.IntegerField()
    date = models.CharField(max_length=20)
class dress(models.Model):
    dressid= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    price = models.IntegerField()
    data=models.FileField()
class book10(models.Model):
    usr = models.IntegerField()
    date = models.CharField(max_length=20)
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    status = models.IntegerField(default=0)


class feedback1(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)

