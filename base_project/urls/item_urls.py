from django.urls import path
from .. import views


# TODO: CHange to /project/all /item/create etc.
urlpatterns = [
    path('all/', views.ItemList.as_view()),
    path('update/<int:pk>/', views.ItemEdit.as_view()),
    path('create/', views.ItemCreate.as_view()),
    path('delete/<int:pk>/', views.ItemDelete.as_view()),
]
