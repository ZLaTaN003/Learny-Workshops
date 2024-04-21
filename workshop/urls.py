from django.urls import path
from . import views

urlpatterns = [
    path('workshop_detail/<slug:slugworkshop>/',views.workshop_detail,name='workshop_detail'),
    path('related_workshops/<slug:slugworkshop>/',views.related_workshops,name='related_workshops'), # this allow me to sort by related category in all_categories
    path('category/',views.category,name="category"),
    path('category/<slug:slugworkshopcategory>/',views.category_details,name='category_details') ,
]