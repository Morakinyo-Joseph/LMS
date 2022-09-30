from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # books
    path('book', views.book_list, name="book_list"),
    path('book/create/', views.book_create, name="book_create"),
    path('book/<int:pk>', views.book_detail, name="book_detail"),
    path('book/<int:pk>/update', views.book_update, name="book_update"),
    path('book/<int:pk>/delete', views.book_delete, name="book_delete"),

    # membership
    path('member', views.member_list, name="member_list"),
    path('member/create', views.member_create, name="member_create"),
    path('member/<int:pk>', views.member_detail, name="member_detail"),

    # borrow a book
    path('member/<int:pk>/borrow', views.book_borrow, name="book_borrow"),

    # notification
    path('notification', views.notification, name="notification"),

    # profile
    path('profile', views.profile, name="profile"),
    path('profile/members', views.profile_member, name="profile_member"),
    path('profile/books', views.profile_book, name="profile_book"),
    path('profile/delete', views.profile_library_delete, name="profile_delete"),
    path('profile/change_password', views.profile_password_change, name="profile_password_change"),

]
