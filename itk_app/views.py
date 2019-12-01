from django.shortcuts import render


#landing/index page

def index(request):
    
    return render(request,'index.html', locals())