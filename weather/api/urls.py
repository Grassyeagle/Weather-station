from django.urls import path
from . import views

urlpatterns = [
    path('',views.TemperatureList.as_view()),
    path('<int:pk>/', views.TemperatureDetail.as_view()),
    path('H/',views.HList.as_view()),
    path('H/<int:pk>/', views.HDetail.as_view()),
    path('P/',views.BpList.as_view()),
    path('P/<int:pk>/', views.BpDetail.as_view())
] 

