from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate

from django.contrib.auth.views import LoginView
# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, user)
            return redirect(reverse("home"))
        
    ctx = {"form":form}
    return render(request,"users/register.html",context=ctx)


class Login(LoginView):
    template_name = "users/login.html"
    next_page = reverse_lazy("home")

