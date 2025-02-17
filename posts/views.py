from django.shortcuts import render, redirect, get_object_or_404
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

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
    
        else:
            messages.info(request, "Credential invalid!")
            return redirect('login')
    
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def delete(request):
    user = request.user
    user.delete()
    return redirect('/')

def article_page(request, id):
    article = get_object_or_404(Post, id=id)
    return render(request, 'article_page.html', {'article' : article})
