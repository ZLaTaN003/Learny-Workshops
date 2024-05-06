from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    about = models.CharField(max_length=400)
    goal_position = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to="profilepictures")
    education = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username
