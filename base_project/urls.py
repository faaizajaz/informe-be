from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # TODO: Add delete views for all
    # Project URLS
    path('allprojects/', views.ProjectList.as_view()),
    path('viewproject/<int:pk>/', views.ProjectDetail.as_view()),
    path('createproject/', views.ProjectCreate.as_view()),
    path('allitems/', views.ItemList.as_view()),
    # path('editproject/<int:pk>/', views.ProjectEdit.as_view()),
    # # Impact URLs
    # path('createimpact/', views.ImpactCreate.as_view()),
    # path('editimpact/<int:pk>/', views.ImpactEdit.as_view()),
    # path('deleteimpact/<int:pk>/', views.ImpactDelete.as_view()),
    # # Outcome URLS
    # path('createoutcome/', views.OutcomeCreate.as_view()),
    # path('editoutcome/<int:pk>/', views.OutcomeEdit.as_view()),
    # # Output URLS
    # path('createoutput/', views.OutputCreate.as_view()),
    # path('editoutput/<int:pk>/', views.OutputEdit.as_view()),
    # path('deleteoutput/<int:pk>/', views.OutputDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
