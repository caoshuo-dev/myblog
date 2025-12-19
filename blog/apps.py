from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # 防止在开发服务器中运行两次
        import os
        if os.environ.get('RUN_MAIN') == 'true' or not os.environ.get('RUN_MAIN'):
            try:
                from .startup import create_initial_superuser
                create_initial_superuser()
            except ImportError as e:
                print(f'[AppConfig Ready] 导入启动脚本失败: {e}')
            except Exception as e:
                print(f'[AppConfig Ready] 创建用户出错: {e}')