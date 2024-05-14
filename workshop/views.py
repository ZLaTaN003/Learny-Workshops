from django.shortcuts import render,get_object_or_404,redirect
from .models import Workshop,WorkshopCategory,Enrollment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

''''
Took down

def all_workshops(request):
    all_workshops = Workshop.objects.all()
    ctx = {"all_workshops":all_workshops}
    return render(request,"workshop/all_workshops.html",context=ctx)'''
@login_required
def workshop_detail(request,slugworkshop):
    user  = request.user
    workshop = Workshop.objects.get(workshopslug=slugworkshop)
    enrolled = Enrollment.objects.filter(student=user, workshop=workshop).exists()
    if request.method == "POST":
        if not enrolled:
            Enrollment.objects.create(student=user,workshop=workshop)
            workshop.students_in_workshop += 1
            workshop.save()
            return redirect(reverse("workshop_detail", args=[slugworkshop]))

        else:
            enrollment_to_delete = Enrollment.objects.get(student=user, workshop=workshop)
            enrollment_to_delete.delete()
            workshop.students_in_workshop -= 1
            workshop.save()
            return redirect(reverse("workshop_detail", args=[slugworkshop]))



    skills = workshop.skills_you_learn.splitlines() 
    new_skills = []
    for skill in skills:
        if skill:
            new_skills.append(skill)


    print(skills)
    ctx = {"workshop":workshop,"enroll":enrolled,"skills":new_skills}
    return render(request,"workshop/workshop_detail.html",context=ctx)

"""
def related_workshops(request,slugworkshop):
    
    workshop_selected = Workshop.objects.get(workshopslug=slugworkshop)
    category_of_workshop = workshop_selected.workshopcategory
    workshops_of_category = Workshop.objects.filter(workshopcategory=category_of_workshop)
    ctx = {"all_workshops":workshops_of_category}
    return render(request,"workshop/all_workshops.html",context=ctx)
"""
def category_details(request,slugworkshopcategory):
    """
    this view helps me to dynamically update the category page with the selected  instance of category model which is related to workshop
    implementation of category feature with a model for category (WorkshopCategory)
    """
    categories = WorkshopCategory.objects.all()
    difficulty_levels = Workshop.objects.order_by().values_list('difficulty', flat=True).distinct()# or Workshop.difficulty_choices.choices

    category = WorkshopCategory.objects.get(workshopcategoryslug=slugworkshopcategory)
    workshops = category.workshop_set.all()
    ctx = {"all_workshops":workshops,"categories":categories,"difficulty":difficulty_levels,"category_slug":slugworkshopcategory}
    return render(request,"workshop/workshop_category.html",context=ctx)

def category(request):
    """
    Category feature implemented through get requests where  the fields on the model Workshop is used as a get req query param
    """
    difficulty_levels = Workshop.objects.order_by().values_list('difficulty', flat=True).distinct()# or Workshop.difficulty_choices.choices
    categories = WorkshopCategory.objects.all()
    workshops = Workshop.objects.all()

    category = request.GET.get("category") #hidden input field which i get from category_details
    if category:
        category_selected = WorkshopCategory.objects.get(workshopcategoryslug=category) 
        workshops = category_selected.workshop_set.all()
  
    difficulty = request.GET.get("difficulty")
    if difficulty:
        workshops = workshops.filter(difficulty=difficulty.title())
    paid_or_free = request.GET.get("paid") 
    if paid_or_free == "paid":
        workshops = workshops.filter(paid=True)
    elif paid_or_free == "free":
        workshops = workshops.filter(paid=False)
  
    ctx = {"categories":categories,"all_workshops":workshops,"difficulty":difficulty_levels,"category_slug":category}
    return render(request,"workshop/workshop_category.html",context=ctx)


def search(request):
    course = request.GET.get("course")
    workshops = None
    print(course)
    if course:
        workshops = Workshop.objects.filter(name__icontains = course)
    ctx = {"workshops":workshops}
    return render(request,"workshop/searchresult.html",context=ctx)
    