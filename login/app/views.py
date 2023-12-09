from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('app:homepage')
        else:
            messages.info(request,'Invalid user')
            return redirect('app:login')
    else:    
        return render(request,'login.html')
def send_otp(email,otp):
    subject="OTP Verification"
    message=f'Your OTP for registration is:{otp}'
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email'] 
        password=request.POST['pass1']
        password2=request.POST['pass2']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already taken")
            return redirect('app:registration')
        otp_number=random.randint(1000,9999)
        otp=str(otp_number)
        send_otp(email,otp)
        request.session['username']=username
        request.session['email']=email
        request.session['password']=password
        request.session['otp']=otp
        return HttpResponseRedirect(reverse('app:otp',args=[otp,username,password,email]))
        else:    
            return render(request,'register.html')
def otp(request,otp,username,password,email):
    return render(request,'otp.html')
def homepage(request):
    return HttpResponse('HomePage')