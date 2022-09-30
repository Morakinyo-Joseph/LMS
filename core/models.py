from django.db import models
from datetime import datetime
from account.models import Library

# Create your models here.


class Membership(models.Model):
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    home_address = models.CharField(max_length=2000)
    date_joined = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


# including books
class Book(models.Model):
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    quantity = models.PositiveIntegerField(default=0)
    cover = models.ImageField()

    def __str__(self):
        return self.title


class BookAmount(models.Model):
    book = models.ForeignKey(Book, related_name="quantity_serial", on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return self.serial_number


# Borrowing books
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, related_name="borrowed_book", on_delete=models.CASCADE)
    book_serial = models.ForeignKey(BookAmount, related_name="borrowed_book_serial", on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(Membership, related_name="borrowed_book_name", on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(default=datetime.now)
    date_to_be_returned = models.DateField(null=True, blank=True)


class Notification(models.Model):
    library_name = models.ForeignKey(Library, related_name="notification", on_delete=models.CASCADE)
    heading = models.CharField(max_length=250)
    message = models.CharField(max_length=5000)

    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.account.username