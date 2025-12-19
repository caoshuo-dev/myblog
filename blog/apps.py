# blog/apps.py
from django.apps import AppConfig  # 必须添加这行导入

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # 仅导入，但不立即执行
        pass