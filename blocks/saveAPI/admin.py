from django.contrib import admin
from saveAPI.models import Gallery, StateSave, BookCategory, Book
from django.forms import TextInput, Textarea
from django.db import models


@admin.register(StateSave)
class UserDiagrams(admin.ModelAdmin):
    list_display = ('name', 'base64_image',
                    'save_time', 'create_time')
    list_filter = ('save_id',)


@admin.register(Gallery)
class GalleryDiagrams(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'description', 'shared')
    list_filter = ('save_time',)
    search_fields = ('name', 'description')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 50})},
    }


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'category')
    search_fields = ('book_name', 'category__category_name')
    list_filter = ('category',)

