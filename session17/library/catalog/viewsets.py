from catalog.serializers import BookSerializer
from rest_framework import viewsets
from catalog.models import Books

#TRansforma esto a JSON mediante este serializador
class BooksViewSet(viewsets.ModelViewSet):
        queryset = Books.objects.all()
        serializer_class = BookSerializer