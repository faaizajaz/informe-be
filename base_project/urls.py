from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('all/', views.ProjectList.as_view()),
    path('key/<int:pk>/', views.ProjectDetail.as_view()),
    path('keyview/<int:pk>/', views.ProjectDetailNested.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
