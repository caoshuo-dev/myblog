from django.db import models

# Create your models here.
from django.db import models


# 分类模型
class Category(models.Model):
    # 分类名称，CharField是字符字段，max_length指定最大长度
    name = models.CharField(max_length=100)

    def __str__(self):
        # 这个函数决定了在后台或其他地方显示此对象时，显示什么内容
        return self.name


# 文章模型
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=200)
    # 文章正文，TextField用于存储长文本
    content = models.TextField()
    # 文章创建时间，auto_now_add=True表示在对象创建时自动设置为当前时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 文章更新时间，auto_now=True表示在每次保存对象时自动更新为当前时间
    modified_time = models.DateTimeField(auto_now=True)
    # 文章分类，ForeignKey表示“外键”，建立与Category模型的多对一关系
    # on_delete=models.CASCADE 表示如果关联的分类被删除，此文章也会被级联删除
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
