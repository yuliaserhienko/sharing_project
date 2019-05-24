from django.urls import reverse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from main.forms import AuthorizationForm


def main_page(request):
    form = AuthorizationForm(request.POST or None)
    if form.is_valid():
        user = authenticate(**form.cleaned_data)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'main/index.html', {'form': form, 'error': 'User not found'})
    return render(request, 'main/index.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_page'))
