from django.urls import path
from .. import views


# TODO: CHange to /project/all /item/create etc.
urlpatterns = [
    path('all/', views.ProjectList.as_view()),
    path('view/<int:pk>/', views.ProjectDetail.as_view()),
    path('create/', views.ProjectCreate.as_view()),
    path('update/<int:pk>/', views.ProjectEdit.as_view()),
]
