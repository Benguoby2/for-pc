#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """
    Django 模型必须继承models.Model类
    Category只需要一个简单的分类名name就可以了
    CharField指定了分类名name的数据类型，CharField是字符型
    CharField的max_length指定最大长度
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签Tag继承models.Models
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章标签
    """
    title = models.CharField(max_length=70)
    #文章正文使用TextField，存储比较短的字符串可以使用CharField，但是对于文章而言使用TxtField
    body = models.TextField()

    #这两个列表示文章的创建时间和最后修改时间使用DatatimeField类
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要，可以没有文章摘要，但默认情况下CharField要求必须存入数据
    #指定Charfield的blank=True，参数之后可以允许空置
    excerpt = models.CharField(max_length=200, blank=True)

    #这是分类和标签，分类和标签模型已经在上面定义
    #将文章对应的数据库和分类、标签对应的数据库关联起来
    #规定一个文章只能对应一个分类，但是一个分类可以有多个文章，所以我们用ForeignKey,
    #即一对多的关系
    #一个文章可以有多个标签，一个标签下可以有多个文章所以我们是用ManyToManyField,表明多对多的关系
    #规定文章可以没有标签，因此指定blank=True
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    #文章作者，User是从django.contrib.auth.models导入的
    #django。contrib.auth是Django内置应用，用于网站用户的注册登录等流程，User是Django写好的用户模块
    #一个文章一个作者，但是一个作者可以写多个文章，一对多关系
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title