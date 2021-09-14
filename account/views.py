import json

from account.serializers import UserRegisterSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework import generics

from .models import CustomUser


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

    # By default, imagefield.url returns a relative url, so we need to build
    # an absolute url to avoid hardcoding anything
    profile_picture_url = request.user.profile_picture.url
    absolute_profile_picture_url = request.build_absolute_uri(profile_picture_url)

    # If ever there was a reason to use a CBV...
    current_user = {
        'id': request.user.id,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'profile_picture': absolute_profile_picture_url,
    }
    return JsonResponse({'isAuthenticated': True, 'currentUser': current_user})


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
            orgs.append({'id': org.id, 'name': org.name})
        return JsonResponse({'orgs': orgs})
    else:
        return JsonResponse({'message': 'User is not logged in.'})


def set_org(request, **kwargs):
    if request.user.is_authenticated:
        request.user.current_org = kwargs['org_id']
        request.user.save()
        return JsonResponse(
            {
                'message': 'Current organization has been set',
                'org': request.user.current_org,
            }
        )
    else:
        return JsonResponse({'message': 'User is not logged in.'})


def get_current_org(request):
    if request.user.is_authenticated:
        if request.user.current_org:
            # TODO: This only gives the org ID. Should also return the org name
            return JsonResponse(
                {
                    'message': 'Current organization id has been returned',
                    'org': request.user.current_org,
                }
            )
        else:
            return JsonResponse({'message': 'No current organization set'})
    else:
        return JsonResponse({'message': 'User is not logged in.'})
