from catalog.models import Books
from django.shortcuts import render

#Create your views here.
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