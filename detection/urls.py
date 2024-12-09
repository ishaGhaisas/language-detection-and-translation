from django.urls import path
from . import views

urlpatterns = [
    path('', views.detection, name='detect'),
    # path('translate/', views.translate, name='translate'),
]