from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-message/', views.send_telegram_message, name='send_telegram_message'),
]
