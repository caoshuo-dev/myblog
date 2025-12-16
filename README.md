# 个人博客系统

一个使用 Django 开发的全功能个人博客系统，包含清晰的前端界面和强大的后台管理。

## ✨ 主要功能
- **文章管理**：可以创建、编辑、删除文章，并对文章进行分类。
- **用户友好的界面**：包含文章列表首页、文章详情页和“关于我”页面。
- **后台管理**：使用 Django Admin 提供完整的内容管理功能。
- **响应式设计**：使用 Bootstrap 5 开发，适配电脑和手机端。
- **站点导航**：所有页面都有统一的导航栏。

## 🛠 技术栈
- **后端**：Python, Django
- **数据库**：SQLite (Django 默认数据库)
- **前端**：HTML, Django 模板语言, Bootstrap 5
- **版本控制**：Git

## 📁 项目结构
myblog/
├── blog/ # 博客主应用
│ ├── migrations/ # 数据库迁移文件
│ ├── templates/blog/ # HTML 模板文件
│ ├── init.py
│ ├── admin.py # 后台管理配置
│ ├── apps.py
│ ├── models.py # 数据模型 (文章 Post, 分类 Category)
│ ├── tests.py
│ ├── urls.py # 应用层路由配置
│ └── views.py # 视图函数
├── myblog/ # 项目配置文件
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py # 项目配置文件
│ ├── urls.py # 项目主路由配置
│ └── wsgi.py
├── templates/ # 全局模板目录
├── .gitignore
├── db.sqlite3 # 开发数据库 (如果使用 SQLite)
├── manage.py
└── README.md # 本文件

text

## 🚀 如何本地运行
1.  **克隆项目**
    ```bash
    git clone https://github.com/[你的GitHub用户名]/myblog.git
    cd myblog
    ```

2.  **安装依赖**
    ```bash
    pip install django
    ```

3.  **应用数据库迁移**
    ```bash
    python manage.py migrate
    ```
    （本项目使用Django默认的SQLite数据库，无需额外配置）

4.  **创建超级用户**
    ```bash
    python manage.py createsuperuser
    ```

5.  **运行开发服务器**
    ```bash
    python manage.py runserver
    ```

6.  **访问网站**
    - 前台博客：`http://127.0.0.1:8000`
    - 后台管理：`http://127.0.0.1:8000/admin`

## 🌐 在线访问
本项目已通过 [Vercel/Render/其他平台] 部署，可在线访问：
> [请在此处填写你的公网访问链接]

## 📝 后续计划
- [ ] 增加用户评论功能
- [ ] 集成 Redis 缓存以提升文章列表加载速度
- [ ] 实现文章全文搜索功能
- [ ] 编写单元测试

## 📄 许可证
本项目基于 MIT 许可证开源。