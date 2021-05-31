from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate, logout


# Create your views here.
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('index')

    return render(request,'registration/signup.html',{
        'form':form
    })

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    return render(request,'registration/login.html')   

def logout_view(request):
    logout(request)
    return render(request,'registration/login.html')
    
