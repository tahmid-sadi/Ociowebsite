from django.db import models


class Product(models.Model):
    chair_model_no = models.CharField(max_length=255)
    features = models.CharField(max_length=600)
    color_combination = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    url_image = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    image_url = models.CharField(max_length=2083)

