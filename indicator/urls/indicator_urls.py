from django.urls import path

from .. import views

urlpatterns = [
    path('view/<int:pk>/', views.IndicatorDetail.as_view()),
    path('create/', views.IndicatorCreate.as_view()),
    path('delete/<int:pk>', views.IndicatorDelete.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
