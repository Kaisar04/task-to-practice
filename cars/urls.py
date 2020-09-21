from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('car-list/', views.CarList.as_view()),
    path('car-detail/<str:pk>/', views.CarDetail.as_view()),
]