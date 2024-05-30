from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def register(request):
    if request.method =='POST':
        email = request.POST.get('email')
        username = email.split('@')[0]
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        if password == confirm_password:
            user = User.objects.create_user(username=username,email=email,password=password)
            send_mail(
                'Succes Signup',
                f'Your username is :{username}\n your password is: {password} \n ',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect('accounts:login')
            
        else : 
            return HttpResponse('Invalid Password')


    return render(request,'accounts/register.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('home')

    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def forget_password(request):
    if request.method =="POST":
        email = request.POST.get('email')
    
        new_password = User.objects.make_random_password()
        user = User.objects.filter(email=email).first()
        user.set_password(new_password)
        user.save
        send_mail(
                'Reset Password',
                f' your permnant password is: {new_password} \n ',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        return redirect('accounts:reset_password')

    return render(request,'accounts/forget_password.html')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            raise 'Invalid Password'
        user = get_object_or_404(User,email=email)
        user.set_password(new_password)
        user.save()
        # user_exist = User.objects.filter(email=email).first()
        # if user_exist:
        #     user = User.objects.get(email=email)
        #     user.set_password(new_password)
        #     user.save()

    return render(request,'accounts/reste_password.html')