from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    )
from django.contrib.auth.forms import (
    UserChangeForm,
    PasswordChangeForm
    )
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# @login_required
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    else:
        form = RegistrationForm()
        args = { 'form' : form }
        return render(request, 'accounts/reg_form.html', args)

@login_required
def profile(request):
    args = {'user' : request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form' : form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change_password')
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form' : form}
        return render(request, 'accounts/change_password.html', args)

# def pagina_artist(request):






# Create your views here.
