from django.urls import path
from . import views

urlpatterns = [
    path('<str:domain>/', views.lookup, name='lookup'),
]

