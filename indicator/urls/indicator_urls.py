from django.urls import path, include
from .. import views
from rest_framework.urlpatterns import format_suffix_patterns

# TODO: CHange to /project/all /item/create etc.
urlpatterns = [
    path('view/<int:pk>/', views.IndicatorDetail.as_view()),
    path('create/', views.IndicatorCreate.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
