from django.db import models
from django.contrib.postgres.fields import ArrayField
class Recipes(models.Model):
    name = models.CharField(max_length=200,null=False)
    ingredients = ArrayField(models.CharField(max_length=200), blank=False)
    instructions = ArrayField(models.CharField(max_length=200), blank=False)
    def __str__(self):
        return f'{self.name}'