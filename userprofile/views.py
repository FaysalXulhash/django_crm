from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.create(user=user)
            userprofile.save()
            return redirect('user-login')
    form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'userprofile/signup.html', context)