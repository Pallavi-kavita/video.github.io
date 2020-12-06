from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,InfoProfile
# Create your views here.

def video(request):
    obj = Item.objects.all()
    return render(request,'video.html',{'obj' :obj} )

def register(request):
    if request.method == "POST":
       profile_form=ProfileForm(data=request.POST)
       info_form = InfoProfile(data=request.POST)        
       if profile_form.is_valid():
           user=profile_form.save()
           user.set_password(user.password)
           user.save()
           profile=info_form.save(commmit=False)
           profile.user=user
           profile.save()
        
        
    else:
        profile_form = ProfileForm(data=request.POST)
        info_form = InfoProfile(data=request.POST)
    return render(request,'reg.html',{'profile_form':profile_form,'info_form':info_form})