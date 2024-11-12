from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')  
    context = {'form': form}
    return render(request, 'auth_app/signup.html', context)

def login_view(request):
    context={}
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('employee_list')   
        return render(request, 'auth_app/login.html', {'error': 'Invalid username or password'})
    return render(request, 'auth_app/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('signin_url')