from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("", views.landing_page, name="landing_page"),

    path("signup", views.signing_up, name="signup"),
    path("login", views.logging_in, name="login"),
    path("logout", views.logging_out, name="logout"),

    path("terms&conditions", views.terms_and_conditions, name="t&c")
]
