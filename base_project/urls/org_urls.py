from django.urls import path

from .. import views

urlpatterns = [
    path('allorgprojects/', views.OrgAllProjects.as_view()),
    path('allorgmembers/', views.OrgAllMembers.as_view()),
    path('allorgowners/', views.OrgAllOwners.as_view()),
    path('create/', views.OrgCreate.as_view()),
    path('updateowner/<int:pk>/', views.OrgOwnerEdit.as_view()),
]
