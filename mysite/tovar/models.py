from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class tovarn(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    name = models.CharField(max_length=255)
    kod = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    tovarn = models.ForeignKey(tovarn, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

