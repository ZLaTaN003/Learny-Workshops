from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here
class WorkshopCategory(models.Model):
    name = models.CharField(max_length=200)
    workshopcategoryslug = models.SlugField()

    class Meta:
        verbose_name_plural = "WorkshopCategories"

    def save(self,*args, **kwargs):
        self.workshopcategoryslug = slugify(self.name)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

class Instructor(models.Model):#
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length=120)
    shortdescription = models.CharField(max_length=400)
    description = models.TextField(max_length=2000)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="workshopimages",default="defaultw")#
    students_in_workshop = models.IntegerField() #
    workshopcategory = models.ForeignKey(WorkshopCategory, on_delete=models.CASCADE) #r
    difficulty_choices = models.TextChoices("difficulty_choices","Easy Intermediate Difficult")
    difficulty = models.CharField(choices=difficulty_choices,max_length=50)
    paid = models.BooleanField(default=False)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)#r
    workshopslug = models.SlugField()
    price = models.IntegerField()


    def save(self, *args, **kwargs):
        self.workshopslug = slugify(self.name)

        super().save(*args, **kwargs)



    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)#r
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)#r


    def __str__(self):
        return f"{self.student} joined {self.workshop}"



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
