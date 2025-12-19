# blog/middleware.py
import os
from django.utils.deprecation import MiddlewareMixin


class StartupMiddleware(MiddlewareMixin):
    """在第一个请求时确保超级用户存在"""

    def __init__(self, get_response):
        self.get_response = get_response
        self._initialized = False

    def __call__(self, request):
        # 仅在第一个请求时执行一次
        if not self._initialized:
            self._initialized = True
            try:
                # 动态导入，避免循环依赖
                from startup import create_initial_superuser
                print('[启动中间件] 正在尝试创建超级用户...')
                create_initial_superuser()
            except Exception as e:
                print(f'[启动中间件] 初始化失败: {e}')

        return self.get_response(request)