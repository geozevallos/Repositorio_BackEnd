from django.db import models

# Create your models here.

# Creando la clase Books
class Books(models.Model):
    title = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    published_year = models.IntegerField()
    editorial = models.CharField(max_length=25)
    volume = models.IntegerField()

    def __str__(self):
        return self.title