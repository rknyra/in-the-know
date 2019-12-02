from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField
from pyuploadcare.dj.models import ImageField

#Neighborhood Model
class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    # admin = models.ForeignKey(Admin,on_delete=models.CASCADE) to add this later
    
    
    def __str__(self):
        return str(self.neighborhood)
    
    def save_neighborhood(self):
        self.save()


#User/Profile Model
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop="", null=True)
    bio = models.CharField(max_length = 250, null=True)
    email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
    
    def save_profile(self):
        self.save()
   
    @classmethod
    def profile(cls):
        profile = cls.objects.filter(id=Profile.id)
        return profile

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()


#Business Model
class Business(models.Model):
    bsns_name = models.CharField(max_length=250)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    bsns_email = models.EmailField()
    
    def __str__(self):
        return str(self.bsns_name)
    
    def save_business(self):
        self.save()