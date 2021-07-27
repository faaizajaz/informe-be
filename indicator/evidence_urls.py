from django.urls import path, include
from . import views


# TODO: CHange to /project/all /item/create etc.
urlpatterns = [
    path('view/<int:pk>/', views.IndicatorEvidenceDetail.as_view()),
    path('create/', views.IndicatorEvidenceCreate.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
