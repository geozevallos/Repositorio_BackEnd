from django.forms import fields
from catalog.models import Author, Books
from django.shortcuts import redirect, render
from catalog.forms import BookForm
from catalog.forms import ModelBookForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


#Create your views here.

#View list
class AuthorsList(ListView):
    model = Author



#Vista para actualizar
class BookUpdate(UpdateView):
    model = Books
    fields = '__all__'


class BookCreate(CreateView):
    model = Books
    fields = '__all__'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'


def update_book(request, pk):
    if request.method == 'POST':
        
        data = request.POST
        author = Author.objects.get(pk=data['author'])
        book = Books.objects.get(pk=pk)
        book.title = data['title']
        book.author = author
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()
        return redirect('/catalog')
    else:
        book = Books.objects.get(pk=pk)
        form = ModelBookForm(book.__dict__)
        return render(request, 'catalog/new.html', {"form": form})


'''
def new_book(request):
    #Pasarle los datos del request
    # form = BookForm(request.POST)
    form = BookForm()
    return render(request, 'catalog/new.html', {"form": form})
'''


def new_book(request):
    #Si llegas a esta ruta mediante POST
    #DEntro del diccionari se almacenan
    if request.method == 'POST':
        #print(request.POST)
        data = request.POST
        book = Books()
        book.title = data['title']
        book.autor = data['autor']
        book.published_year = data['published_year']
        book.editorial = data['editorial']
        book.volume = data['volume']
        book.save()
        #Redireccionar luego de mandar. Esto es una respuesta 301
        return redirect('/catalog/')
    #Si llegas mediante GET
    else:
        form = ModelBookForm()
        return render(request, 'catalog/new.html', {"form": form})



def catalog_list(request):
    books = Books.objects.all()
    # books = Books.objects.filter(published_year__gt = 2018)
    # books = Books.objects.filter(title__contains = "feliz")
    return render(request, 'catalog/index.html', {'books': books})

# def catalog_list(request):
#     books = Books.objects.filter(title = "Un mundo Feliz")
#     return render(request, 'catalog/index.html', {'books': books})


def get_books_by_editorial(request, editorial):
    books = Books.objects.filter(editorial=editorial)

    #Esto es un parámetro
    year = request.GET.get("year")

    if year != None:
        books = books.filter(year=year)

    return render(request, 'catalog/index.html', {'books':books})