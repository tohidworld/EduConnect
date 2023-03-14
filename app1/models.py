from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # Produce a signal if there is any database action.

# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    profile_image = models.ImageField(upload_to='pictures/%Y/%m/%d/' , max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True) 
    roles = models.CharField(max_length=255, blank=True, default='Individual',null=True)
    def __str__(self):
        return "{0}".format(self.user.email)
    
# When any User instance created, Profile object instance is created automatically linked by User 
@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)
    else:
        instance.profile.save()
