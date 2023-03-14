from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Roles, Profile
from django.shortcuts import get_object_or_404

# Create your views here.



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            user=authenticate(request,username=uname,password=pass1)
            login(request,user)
            return redirect('completeProfile')

    return render (request,'accounts/signup.html')

def completeProfile(request):
    if request.user.is_authenticated:
        
        if request.method=='POST':
            user = request.user
            profile = get_object_or_404(Profile,user=user.pk)
            profile.name = request.POST.get('fullname')
            profile.phone = request.POST.get('phone')
            profile.zip = request.POST.get('zip')
            profile.address = request.POST.get('address')
            profile.state =request.POST.get('state')
            profile.country = request.POST.get('country')
            profile.profile_image = request.POST.get('profile_image')
            profile.bio = request.POST.get('bio')
            profile.roles = request.POST.get('roles')
            profile.save()
            return redirect('completeProfile')
        
        roles = Roles.objects.all().values()
        context ={'roles': roles}
        print(context)
        return render (request,'accounts/completeProfile.html', context=context)
    else:
        return redirect('LoginPage')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'accounts/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

