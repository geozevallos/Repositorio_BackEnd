from django.db.models import fields
from rest_framework import serializers
from catalog.models import Author, Books




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "nationality", "genere"]

#Definir mi serializador
#Cuando consultes como json, muestra etos campos del modelo
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
                model = Books
                fields = ['title', 'editorial', 'published_year', 'volume', "author"]