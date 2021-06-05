"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from catalog import views, viewsets
from rest_framework import routers

#Creando como restframework
router = routers.DefaultRouter()
router.register(r'books', viewsets.BooksViewSet)


urlpatterns = [

    #Carga el router
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),




    #Rutas genericas
    # path('books', views.BookCreate.as_view()),
     #ruta de actualización
    # path('book/<pk>/', views.BookUpdate.as_view()),
    
    path('authors', views.AuthorCreate.as_view()),

    path('authors/list', views.AuthorsList.as_view()),

       path('catalog/books', views.new_book),
    #Otra manera
    path('catalog/book/<pk>/update', views.new_book),
    re_path(r'^catalog[\/]{0,1}$', views.catalog_list),
   
   
    path('admin/', admin.site.urls),
    

    
    re_path(r'catalog\/(?P<editorial>[a-zA-Z]+)', views.get_books_by_editorial)
    # path('catalog/<editorial>/books', views.get_books_by_editorial)
]
