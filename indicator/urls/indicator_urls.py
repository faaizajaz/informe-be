from django.urls import path
from .. import views


# TODO: CHange to /project/all /item/create etc.
urlpatterns = [
    path('view/<int:pk>/', views.IndicatorDetail.as_view()),
    path('create/', views.IndicatorCreate.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
