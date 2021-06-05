from catalog.models import Author, Books
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'view_author', 'editorial', 'price_in_usd')

    list_filter = ('editorial', 'author')

    # Crear una vista, campo para 
    def view_author(self, obj):
        if(obj.author != None):
            link = f"<a href='/admin/catalog/author/{obj.author.id}/change/'>{obj.author}</a>"
            return format_html(link)
        else:
            return "-"


    def price_in_usd(self, obj):
        if obj.price == None:
            f_price = 0.0
        else:
            f_price = float(obj.price)
        return f"$ {f_price}"

admin.site.register(Books, BookAdmin)


class AutorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AutorAdmin)