import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# 删除已存在的admin（如果有）
User.objects.filter(username='admin').delete()

# 创建新超级用户
try:
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='cs.040222'
    )
    print(f'✅ 用户创建成功: {user.username}')
    print(f'   是超级用户: {user.is_superuser}')
    print(f'   是staff: {user.is_staff}')
except Exception as e:
    print(f'❌ 创建失败: {e}')