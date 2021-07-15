from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('allprojects/', views.ProjectList.as_view()),
    path('viewproject/<int:pk>/', views.ProjectDetail.as_view()),
    path('createproject/', views.ProjectCreate.as_view()),
    path('updateproject/<int:pk>/', views.ProjectEdit.as_view()),
    path('allitems/', views.ItemList.as_view()),
    path('updateitem/<int:pk>/', views.ItemEdit.as_view()),
    path('createitem/', views.ItemCreate.as_view()),
    path('deleteitem/<int:pk>/', views.ItemDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
