from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import os, sys
        # 将项目根目录添加到Python路径
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        try:
            from startup import create_initial_superuser  # 注意：去掉了前面的 '.'
            #create_initial_superuser()
        except ImportError as e:
            print(f'[AppConfig Ready] 导入启动脚本失败: {e}')
        except Exception as e:
            print(f'[AppConfig Ready] 创建用户出错: {e}')