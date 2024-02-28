from django.shortcuts import render
from django.urls import re_path
from basic_app.forms import UserProfileinfoForm,Userform

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
   return render(request,'basic_app/index.html',)


@login_required
def special(request):
   return HttpResponse('You are logged in!')

@login_required
def user_logout(request):
   logout(request)
   return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    
    if request.method == 'POST':
       
       user_form = Userform(data=request.POST)
       profile_form = UserProfileinfoForm(data=request.POST)
       
       if user_form.is_valid() and profile_form.is_valid():
          
          user = user_form.save()
          user.set_password(user.password)
          user.save()
          
          profile = profile_form.save(commit = False)
          profile.user = user
          
          if 'profile_pic' in request.FILES:
             profile.profile_pic = request.FILES['profile_pic']
             
          profile.save()
          
          registered=True
          
       else:
         print(user_form.errors,profile_form.errors)
         
    else:
       
       user_form = Userform()
       profile_form = UserProfileinfoForm()
       
    return render(request,'basic_app/register.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):
   
   if request.method == 'POST':
      
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(username= username, password=password)
      
      if user:
         if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
      
         else:
            return HttpResponse('Account is inactive')
      
      else:
         print('Someone tried a failed login attempt')
         print('username:{} password : {}'.format(username,password))
         return HttpResponse('Invalid credentials')
      
   else:
      return render(request,'basic_app/login.html')