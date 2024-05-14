from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.Login.as_view(),name='login_url'),
    path('logout/',LogoutView.as_view(next_page=reverse_lazy("login_url")),name='logout_url'),
    path('profile',views.profile, name="profile"),
    path('contact/',views.contactus,name="contact")



]