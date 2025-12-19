# startup.py
import os
from django.contrib.auth import get_user_model

def create_initial_superuser():
    User = get_user_model()
    # 从环境变量读取，没设置就用默认值（务必改默认密码）
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'cs.040222')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'[启动脚本] 超级用户 "{username}" 创建成功。')
    else:
        print(f'[启动脚本] 超级用户 "{username}" 已存在。')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
    import django
    django.setup()
    create_initial_superuser()