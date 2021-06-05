from django.db import models

# Create your models here.

#La clase autor
class Author(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    nationality = models.CharField(max_length=50)
    genere = models.CharField(max_length=15)
    
    def __str__(self):
       return f"{self.last_name}, {self.first_name}"

# Creando la clase Books
class Books(models.Model):
    title = models.CharField(max_length=45)
    #autor = models.CharField(max_length=45)
    published_year = models.IntegerField()
    editorial = models.CharField(max_length=25)
    volume = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    #Creando ruta absoluta
    def get_absolute_url(self):
        return "/catalog/"
