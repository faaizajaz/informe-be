from django.urls import path

from . import views

urlpatterns = [
    path('csrf/', views.get_csrf, name='user-csrf'),
    path('login/', views.login_view, name='user-login'),
    path('logout/', views.logout_view, name='user-logout'),
    path('session/', views.session_view, name='user-session'),
    path('whoami/', views.whoami_view, name='user-whoami'),
]
