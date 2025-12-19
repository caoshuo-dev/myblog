from django.urls import path
from . import views  # 从当前目录导入views模块
from .views import create_admin_view

urlpatterns = [
    # 当用户访问 ‘blog/’ 这个路径时，调用 views.py 中的 post_list 函数来处理
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
]
