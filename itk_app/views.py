from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User


#landing/index page
def index(request):
    health_centers=HealthCenter.objects.all()
    police_stations=Police.objects.all()
    
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

#neighborhoods/join a neighborhood
def neighborhood(request):
    neighborhoods=Neighborhood.objects.all()
    form = AddNeighborhoodForm()
    
    return render(request,'itk_pages/neighborhoods.html', locals())


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


#view businesses
def business(request):
    businesses=Business.objects.all()
    form = AddBusinessForm()
    
    return render(request,'itk_pages/businesses.html', locals())


#add a business
def addBusiness (request):
    form = AddBusinessForm()
    
    if request.method == 'POST':
        form = AddBusinessForm(request.POST,request.FILES)
        user = request.user.id
        
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.save()
        return redirect('view_businesses')
    else:
        form = AddBusinessForm()
        return render(request, 'itk_pages/businesses.html', locals())

#search businesses
def searchBusiness(request):

    if 'search' in request.GET and request.GET["search"]:
    
        search_term = request.GET.get("search")
        searched_businesses = Business.objects.filter(bsns_name__icontains=search_term)
        message = f"{search_term}"
        
        return render(request, 'itk_pages/search_results.html', locals())
    
    else:
        
        message = "you haven't searched for any business"  
        return render(request, 'itk_pages/search_results.html', locals())
    

#view health centers
def healthCenters(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood,pk=neighborhood_id)
    health_centers = HealthCenter.objects.filter(neighborhood=neighborhood)
    
    return render(request,'itk_pages/health_centers.html', locals())


#view police stations
def policeStations(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood,pk=neighborhood_id)
    police_stations = Police.objects.filter(neighborhood=neighborhood)
    
    return render(request,'itk_pages/police_stations.html', locals())