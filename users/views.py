from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileEdit
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.views.generic import DetailView
from .models import Profile

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



def profile(request):
    user = request.user
    user_profile = user.profile

    form_initial_data = {"first":user.first_name,
                         "last":user.last_name,
                         "email":user.email,
                         "about":user_profile.about,
                         "goal":user_profile.goal_position,
                         "pfp":user_profile.profile_img,
                         "education":user_profile.education,
                         }

    if request.method == "POST":
        form = ProfileEdit(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print("baliid")
            if form.cleaned_data["pfp"]:
                user_profile.profile_img  = form.cleaned_data["pfp"]
                user_profile.save()

            user.first_name = form.cleaned_data["first"]
            user.last_name = form.cleaned_data["last"]
            user.email = form.cleaned_data["email"]
            user.save()

            user_profile.about = form.cleaned_data["about"]
            user_profile.goal_position = form.cleaned_data["goal"]
            user_profile.education = form.cleaned_data["education"]
            user_profile.save()
        else:
            print(form.errors)
    else:
        form = ProfileEdit(initial=form_initial_data)



    ctx = {"user_profile":user_profile,"form":form}
    return render(request,"users/profile.html",context=ctx)