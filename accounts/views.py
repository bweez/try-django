from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        # old example login form management
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     context = {'error': 'Invalid username or password.'}
        #     return render(request, 'accounts/login.html', context=context)
        
        if form.is_valid():
            user = form.get('user')
            login(request, user)
            return redirect('/')
    return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    context = {}
    return render(request, 'accounts/login.html', context=context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, 'accounts/register.html', context=context)
