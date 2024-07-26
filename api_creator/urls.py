from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAPIView.as_view(), name='create_api'),
    path('', views.api_list, name='api_list'),
    path('<int:api_id>/data/', views.api_data_list, name='api_data_list'),
    path('<int:api_id>/data/add/', views.add_data, name='add_data'),
]
