import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

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
    if username is None or password is None:
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


# I guess I'd rather let Django handle this.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # PREDEPLOY: Add the correct redirect URL here.
            return redirect('http://127.0.0.1:8080/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def get_org_membership(request):
    if request.user.is_authenticated:
        orgs = []
        for org in request.user.org_joined.all():
            orgs.append(org.id)
        return JsonResponse({'orgs': orgs})
    else:
        return JsonResponse({'message': 'User is not logged in.'})


def set_org(request, **kwargs):
    if request.user.is_authenticated:
        request.user.current_org = kwargs['org_id']
        request.user.save()
        return JsonResponse({'message': 'Set user\'s current organization'})
    else:
        return JsonResponse({'message': 'User is not logged in.'})


# Create your views here.
