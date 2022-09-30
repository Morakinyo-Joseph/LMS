from django.contrib import admin
from .models import Book, BorrowedBook, Membership, BookAmount

# Register your models here.

admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Membership)
admin.site.register(BookAmount)

