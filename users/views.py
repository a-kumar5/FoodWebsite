from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_http_methods


# Create your views here.


@require_http_methods(["GET", "POST"])
def register(request: HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('food:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})