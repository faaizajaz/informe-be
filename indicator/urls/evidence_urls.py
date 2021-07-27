from django.urls import path
from .. import views


urlpatterns = [
    path('view/<int:pk>/', views.IndicatorEvidenceDetail.as_view()),
    path('create/', views.IndicatorEvidenceCreate.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
