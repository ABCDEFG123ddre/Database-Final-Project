from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField('id', primary_key=True, null=False, default='')
    user_name = models.CharField('name', max_length=30, null=False, default='')
    password = models.CharField('password', max_length=30, null=False, default='')

    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_id = models.IntegerField('id', primary_key=True)
    price = models.IntegerField('price', null=False, default='')
    brand = models.CharField('brand', max_length=30, null=False, default='')
    original_info = models.CharField(max_length=200)

    def __str__(self):
        return self.product_id

class SSD(models.Model):
    product_id = models.IntegerField('id', primary_key=True)
    ssd_type = models.CharField(max_length=50, default='')
    capacity = models.CharField(null=False, default='', max_length=50)
    read_speed = models.IntegerField()
    write_speed = models.IntegerField()
    warranty = models.CharField()

    def __str__(self):
        return self.product_id

class HDD(models.Model):
    product_id = models.IntegerField('id', primary_key=True)
    hdd_type = models.CharField(max_length=50, default='')
    series = models.CharField(max_length=100)
    capacity = models.CharField(null=False, default='', max_length=50)
    memory = models.IntegerField()
    model = models.CharField(max_length=100)
    RPM = models.IntegerField()
    warranty = models.IntegerField()

    def __str__(self):
        return self.product_id

class RAM(models.Model):
    product_id = models.IntegerField('id', primary_key=True)
    ram_type = models.CharField(max_length=50, default='')
    ddr_gen = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    capacity = models.CharField(null=False, default='', max_length=50)
    clock_rate = models.IntegerField()
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id
