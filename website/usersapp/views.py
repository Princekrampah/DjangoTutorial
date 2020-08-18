from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserInfoUpdateForm, ProfileUpdateForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Hello {username}, your account has been created! You can now login.")
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'usersapp/registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        userUpdateForm = UserInfoUpdateForm(
            request.POST, instance=request.user)
        profileUpdateForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        userUpdateForm = UserInfoUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userUpdateForm': userUpdateForm,
        'profileUpdateForm': profileUpdateForm
    }
    return render(request, 'usersapp/profile.html', context)
