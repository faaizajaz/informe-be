from django.urls import path

from .. import views

urlpatterns = [
    path('all/', views.ProjectList.as_view()),
    path('view/<int:pk>/', views.ProjectDetail.as_view()),
    path('create/', views.ProjectCreate.as_view()),
    path('update/<int:pk>/', views.ProjectEdit.as_view()),
    path('updateowner/<int:pk>/', views.ProjectOwnerEdit.as_view()),
    path('updatereporter/<int:pk>/', views.ProjectReporterEdit.as_view()),
]
