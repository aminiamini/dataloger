from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='datachart-index'),
    path('postplain/', views.get_data)
]
