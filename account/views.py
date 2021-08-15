import json

from account.serializers import UserRegisterSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework import generics

from .models import CustomUser


# TODO: Add view to set user current_org
def get_csrf(request) -> JsonResponse:
    """Returns a CSRF token on GET

    Args:
        request (request): Request. Not much more to say

    Returns:
        JsonResponse: An object containing which contains:
            "detail" (String): A status message,
            "X-CSRFToken" (String): The CSRF token for the current session
    """
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


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


def get_org_membership(request):
    if request.user.is_authenticated:
        orgs = []
        for org in request.user.org_joined.all():
            orgs.append({'name': org.name})
        return JsonResponse({'orgs': orgs})
    else:
        return JsonResponse({'message': 'User is not logged in.'})


def set_org(request, **kwargs):
    if request.user.is_authenticated:
        request.user.current_org = kwargs['org_id']
        request.user.save()
        return JsonResponse({'message': 'Current organization has been set'})
    else:
        return JsonResponse({'message': 'User is not logged in.'})


# Create your views here.
