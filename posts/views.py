from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list': post_list})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not the same")
            return redirect('register')

    else:
        return render(request, 'register.html')