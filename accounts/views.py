from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method =='POST':
        email = request.POST.get('email')
        username = email.split('@')[0]
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        if password == confirm_password:
            user = User.objects.create_user(username=username,email=email,password=password)
            
        else : 
            return HttpResponse('Invalid Password')


    return render(request,'accounts/register.html')