from django.urls import path
from .. import views


urlpatterns = [
    path('all/', views.ItemList.as_view()),
    path('update/<int:pk>/', views.ItemEdit.as_view()),
    path('create/', views.ItemCreate.as_view()),
    path('delete/<int:pk>/', views.ItemDelete.as_view()),
]
