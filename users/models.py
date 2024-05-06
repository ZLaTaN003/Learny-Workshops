from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    about = models.CharField(max_length=400)
    goal_position = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to="profilepictures")
    education = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


    def __str__(self):
        return self.user.username
