from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('user_register/', views.register, name='user_register'),
    path('login/', views.user_login, name='login'),
    path('startup_profile/', views.startup_profile, name='reg_form_login'),
    path('startup_profile/profile', views.startup_profile_pro, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blocksingle'),
    path('logout/', views.logout_view, name='logout'),
]
