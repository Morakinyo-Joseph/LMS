from django.shortcuts import render, redirect
from .forms import AccountCreationForm
from .models import User, Library
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from core.models import Library, Notification

# Create your views here.


def landing_page(request):
    return render(request, 'account/landing_page.html')


def signing_up(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect("core:book_list")
        
    form = AccountCreationForm()

    if request.method == "POST":
        form = AccountCreationForm(request.POST)

        if request.POST.get("submit"):
            if form.is_valid():
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                password2 = form.cleaned_data["password2"]
                library_name = request.POST["library_name"]
                username = first_name + "-" + last_name

                if request.POST.get("accept_condition"):
                    print("The toggle button worked")

                    if Library.objects.filter(name=library_name).exists():
                        messages.info(request, "Library account with this library name already exists")
                        return redirect("account:signup")

                    elif User.objects.filter(email=email).exists():
                        messages.info(request, "Email address already being used!")
                        return redirect("account:signup")

                    elif library_name == "":
                        messages.info(request, "Library name cannot be empty")
                        return redirect("account:signup")

                    elif first_name == "":
                        messages.info(request, "First name cannot be empty")
                        return redirect("account:signup")

                    elif last_name == "":
                        messages.info(request, "Last Name cannot be empty")
                        return redirect("account:signup")

                    elif email == "":
                        messages.info(request, "Email address already Empty")
                        return redirect("account:signup")

                    elif password == "" or password2 == "":
                        messages.info(request, "Passwords cannot be empty")
                        return redirect("account:signup")
                        
                    elif len(password) < 8:
                        messages.info(request, "Passwords should be more than eight characters")
                        return redirect("account:signup")

                    elif password == password2:
                        print(f"The passwords are a match: {password}")

                        owner = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                         email=email, password=password)
                        owner.save

                        new_library = Library.objects.create(owner=owner, name=library_name)
                        new_library.save()

                        notification_heading = "Account Creation"
                        notification_message = f"Account for '{library_name}' created successfully"
                        alert = Notification.objects.create(library_name=new_library, heading=notification_heading,
                                                            message=notification_message)
                        alert.save()

                        return redirect("account:login")
                    else:
                        messages.info(request, "Passwords do not match!")
                        return redirect("account:signup")
                else:
                    messages.info(request, "Oops, you forgot to accept Terms&Conditons")
                    return redirect("account:signup")

    return render(request, "account/signup.html", {"form": form})


def logging_in(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect("core:book_list")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            potential_user = User.objects.get(email=email)
            kinetic_user = potential_user.username

            if potential_user.check_password(password):
                print(password)
                
                logged_user = authenticate(username=kinetic_user, password=password)
                login(request, logged_user)
                messages.success(request, f"Logged in as {email}")
                return redirect("core:book_list")
            else:
                messages.info(request, "Email/Password doesn't exist")
                return redirect("accounts:login")
        else:
            messages.info(request, "Email/Password doesn't exist")
            return redirect("account:login")

    return render(request, "account/login.html")


def logging_out(request):
    logout(request)
    return redirect("account:login")


def terms_and_conditions(request):
    return render(request, "account/terms&conditions.html")