from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User


#landing/index page
def index(request):
    
    return render(request,'index.html', locals())


#profilePage
def myProfile(request):
    userProfile = Profile.objects.all()

    return render(request, 'itk_pages/profile.html', locals())


#updateProfile
def updateProfile(request):
    my_prof = Profile.objects.get(user=request.user)
        
    if request.method == 'POST':
        updateProf = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if updateProf.is_valid():
            updateProf.save()
              
        return redirect('my_profile')
    else:
        updateProf = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'itk_pages/update_profile.html', locals())


#share a notice
def shareNotice(request):
    form = ShareNoticeForm()
    
    if request.method == 'POST':
        form = ShareNoticeForm(request.POST,request.FILES)
        user = request.user.id
        
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user
            announcement.save()
        return redirect('view_notices')
    else:
        form = ShareNoticeForm()
        return render(request, 'itk_pages/share_notice.html', locals())
    

#view notices/alerts/announcements
def viewNotices(request):
    notices=Notice.objects.all()
    
    return render(request,'itk_pages/notices.html', locals())