from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserOurRegistration
from .models import Profile
from django.views.generic import ListView, UpdateView

def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Пользователь {username} был успешно создан. Теперь вы можете войти в личный кабинет.')
            return redirect('auth')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html',
                  {'form': form})
class ProfileView(ListView):
    model = Profile
    template_name = 'users/profile.html'
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['img']
    template_name = 'users/profile_update.html'
    success_url = '/profile'

