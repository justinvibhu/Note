from django.shortcuts import render, redirect
from .models import Destination
from  django.contrib.auth.models import User,auth
# Create your views here.



def index(request):
    dest = Destination.objects.all()

    return render(request,'index.html',{'dest':dest})

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']

        user = User.objects.create_user(
        username = username,
        first_name = first_name,
        last_name = last_name,
        email = email,
        password = password1
         )
        user.save()
        return redirect('login')

    else:
       return render(request,'signup.html')

def login(request):

    if request.method == 'POST':
        username=request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            url = "/home/{}".format(username)
            return redirect(url)
        else:
            return redirect('/login')
    else:
       return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')