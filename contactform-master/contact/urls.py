from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.index, name='contact'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('warning/<int:user_id>/', views.send_warning, name='warning'),
    path('warningsent/', views.warning_sent, name='warningsent'),
    path('ban_user/<int:user_id>/', views.ban_user, name='ban_user'),
    path('ban_admin/<int:user_id>/', views.ban_admin, name='ban_admin'),
    ]

