# blog/apps.py
from django.apps import AppConfig  # 必须添加这行导入

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # 防止在开发服务器中运行两次
        import os
        if os.environ.get('RUN_MAIN') == 'true' or not os.environ.get('RUN_MAIN'):
            try:
                # 从项目根目录导入，确保路径正确
                import sys
                sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                from startup import create_initial_superuser
                create_initial_superuser()
            except ImportError as e:
                print(f'[AppConfig Ready] 导入启动脚本失败: {e}')
            except Exception as e:
                print(f'[AppConfig Ready] 创建用户出错: {e}')