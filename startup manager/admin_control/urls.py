from django.urls import path
from admin_control import views

urlpatterns = [
    path('admin-control/', views.display_data, name='admin-control'),
]