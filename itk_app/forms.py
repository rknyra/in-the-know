from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['hood_name','location','population']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['prof_pic','bio']
        
        
class SubmitBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['bsns_name','bsns_email']

class ShareNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['user']