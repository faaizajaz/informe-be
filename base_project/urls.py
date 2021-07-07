from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('all/', views.ProjectList.as_view()),
    path('view/<int:pk>/', views.ProjectDetail.as_view()),
    path('addimpact/', views.ImpactDetail.as_view()),
    path('editimpact/<int:pk>', views.ImpactEdit.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
