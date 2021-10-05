from django.shortcuts import render,redirect
from django.contrib import messages
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        image = request.FILES.get('image')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        print(image)
        if password_1 == password_2:
            try:
                user = User.objects.create(username = username)
                user.set_password(password_1)
                user.save()
                profile = Profile.objects.create(user = user, nickname=nickname,image=image)
                user = authenticate(username=username,password = password_1)
                login(request,user)
                return redirect('index')
            except:
                messages.error(request,'NOT CORRECT VALUE')
        else:
            messages.error(request,'NOT CORRECT PASSWORD')
    return render(request,'users/register.html')

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
        except:
            messages.error(request, 'NOT CORRECT LOGIN OR PASSWORD')
    return render(request,'users/login.html')

def profile(request,id):
    profiles = Profile.objects.get(user__id =id)
    return render(request, 'users/profile.html', {'profiles':profiles})