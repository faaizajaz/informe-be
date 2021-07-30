from django.urls import path

from .. import views

urlpatterns = [
    path('all/', views.OrgList.as_view()),
    path('allorgprojects/', views.OrgAllProjects.as_view()),
    path('create/', views.OrgCreate.as_view()),
    path('updateowner/<int:pk>/', views.OrgOwnerEdit.as_view()),
]
