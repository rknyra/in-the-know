from django.shortcuts import render, redirect
from .models import *
from .forms import *


#landing/index page

def index(request):
    
    return render(request,'index.html', locals())

#profilePage
def myProfile(request):
    userProfile = Profile.objects.all()

      
    return render(request, 'itk_pages/profile.html', locals())