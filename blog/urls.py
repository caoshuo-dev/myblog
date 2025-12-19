from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('test/', views.test_view, name='test'),
    path('check-admin/', views.check_admin, name='check_admin'),
]
