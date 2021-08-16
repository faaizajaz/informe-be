from django.urls import path

from .. import views

urlpatterns = [
    path('allorgprojects/', views.OrgAllProjects.as_view()),
    path('create/', views.OrgCreate.as_view()),
    path('updateowner/<int:pk>/', views.OrgOwnerEdit.as_view()),
    path('updatemember/<int:pk>/', views.OrgMemberEdit.as_view()),
]
