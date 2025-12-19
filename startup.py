# startup.py
import os
import time
from django.db import connections
from django.db.utils import OperationalError
from django.contrib.auth import get_user_model


def create_initial_superuser():
    """安全地创建初始超级用户，确保数据库已就绪"""
    max_retries = 5
    for i in range(max_retries):
        try:
            # 1. 检查数据库连接
            db_conn = connections['default']
            db_conn.cursor()

            # 2. 从环境变量读取凭证，使用安全的默认值
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
            # !!! 重要：请将下一行引号内的默认密码改为一个你自己的强密码 !!!
            default_password = 'cs.040222'  # ← 修改这里
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', default_password)
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

            User = get_user_model()

            # 3. 检查并创建用户
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                print(f'[启动脚本] 成功创建超级用户: {username}')
                return True
            else:
                print(f'[启动脚本] 用户已存在: {username}')
                return True

        except OperationalError as e:
            # 数据库未就绪，等待后重试
            wait_time = 2 * (i + 1)
            print(f'[启动脚本] 数据库未就绪 (尝试 {i + 1}/{max_retries})，等待 {wait_time}秒... 错误: {e}')
            time.sleep(wait_time)
        except Exception as e:
            # 捕获其他所有错误并打印
            print(f'[启动脚本] 创建用户时发生未知错误: {e}')
            import traceback
            traceback.print_exc()  # 打印完整错误堆栈
            return False

    print(f'[启动脚本] 错误: 在 {max_retries} 次重试后仍无法连接数据库')
    return False


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
    import django

    django.setup()
    create_initial_superuser()