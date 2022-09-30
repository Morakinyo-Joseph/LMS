from django import forms
from .models import Book, Membership, BorrowedBook


class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "location",
            "quantity",
            "cover",
        )

class MembershipCreationForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = (
            "name",
            "email",
            "phone_number",
            "home_address",
        )

class BookBorrowingForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = {
            "book",
        }
