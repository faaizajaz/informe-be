import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import RegisterForm


def get_csrf(request):
    csrf_token = get_token(request)
    response = JsonResponse({'detail': 'CSRF cookie set', 'X-CSRFToken': csrf_token})
    return response


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    # ALERT: All 403 responses do not pass the 'detail' to frontend for some reason
    if len(username) == 0 or len(password) == 0:
        return JsonResponse(
            data={'detail': 'Please provide username and password.'}, status=403
        )

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=403)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=403)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'username': request.user.username})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # PREDEPLOY: Add the correct login redirect URL here.
            return redirect('SOME_ROUTE')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Create your views here.
