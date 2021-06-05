from django import forms
from django.forms.fields import CharField
from django.forms.models import ModelForm
from catalog.models import Author, Books


#Formulario Generico
class BookForm(forms.Form):
    title = CharField(label='titulo')
    editorial = CharField(label='editorial')
    #autor = CharField(label='Autor')
    #Quiero q este campo sea un selecotor
    autor = forms.ModelChoiceField(queryset=Author.objects)
    year = forms.IntegerField(label = "año")
    volume = forms.IntegerField(label="volume")


#Formulario modelo
#Creando clase para formularios
class ModelBookForm(ModelForm):
    class Meta:
        #Este modelo va a usar como referencia
        model = Books

        #Q campos
       # fields = ['title', 'autor', 'editorial', 'published_year', 'volume']
        fields = ['title', 'editorial', 'author', 'published_year', 'volume']