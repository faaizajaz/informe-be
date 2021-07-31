from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.SendOrgInvitation.as_view(), name="send-invitation"),
    path('handle/<uuid:uid>/', views.handle_org_invitation, name="handle-invitation"),
]
