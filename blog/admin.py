from django.contrib import admin
# 从当前目录的 models.py 文件中，导入我们定义的模型类
from .models import Category, Post

# 将模型注册到后台管理站点
admin.site.register(Category)
admin.site.register(Post)
