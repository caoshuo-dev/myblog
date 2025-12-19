"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

try:
    from startup import create_initial_superuser
    create_initial_superuser()
except ImportError:
    print("启动脚本导入失败，请检查 startup.py 文件。")
except Exception as e:
    print(f"启动时创建超级用户出错: {e}")

application = get_wsgi_application()
