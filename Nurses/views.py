from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm, UserAdminCreationForm
# Create your views here.
from django.contrib import messages


User = get_user_model()
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
            "form": form
        }
    if form.is_valid():
        email = form.cleaned_data["email"]
        next_ = request.META.get('HTTP_REFERER', "/")
        password = form.cleaned_data["password"]
        if request.method =='POST':
            form = LoginForm(request.POST or None)


        print("FORM", form)        
        print("\n", next_)

        user = authenticate(request, username=email, password=password)
        print("USER:",user)
        if user is not None:
            login(request, user)
            if is_safe_url(next_, request.get_host()) and "login" not in next_:
                return redirect(next_)
            else:
                return redirect("/")
        else:
            messages.error(request,'Username or Password not correct')
            print("Failed!")

    return render(request, "Nurses/Login.html", context)


def registration_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        form.save()
        next_ = request.META.get('HTTP_REFERER', "/")
        try:
            next_ = next_.split("next=")[1]
        except IndexError:
            next_ = "/"

        print("\n\nNEXT", next_)
        return redirect(next_)
        

    return render(request, "Nurses/Sign-Up.html", context)
