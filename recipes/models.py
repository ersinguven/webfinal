from django.db import models
from users.models import CustomUser
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.




class Recipe(models.Model):
    name = models.CharField(max_length=32)
    cuisine = models.CharField(max_length=16)
    difficulty = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    pub_date = models.DateField('date published')
    publisher = CustomUser()
    comments = ArrayField(
        ArrayField(
                models.CharField(max_length=255,blank=True),
        )
    )
    image = models.ImageField(upload_to='gallery')
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    price = models.IntegerField()
    instructions = models.CharField(max_length=2048)
    video = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    img = models.ImageField()


class ingredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)

    name = models.CharField(max_length=16)
    img = models.ImageField(blank=True)
    origin = models.CharField(max_length=16,blank=True)
    information = models.CharField(max_length=255,blank=True)
    amount = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class equipment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)
    price_range = models.CharField(max_length=16)
    desc = models.CharField(max_length=255)