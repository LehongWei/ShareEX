from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    '''
    小程序用户信息
    '''
    GEN = ((0,"女"), (1, "男"), (2, "未知"))
    nickname = models.CharField(max_length=30, null=False, blank=False, verbose_name='微信昵称')
    gender = models.IntegerField(choices=GEN, null=False, blank=False, default=2, verbose_name='性别')
    college = models.CharField(max_length=30, null=False, blank=False, verbose_name='大学名称')
    grade = models.CharField(max_length=30, null=False, blank=False, verbose_name='所学专业')
    interest = models.CharField(max_length=50, null=False, blank=False, verbose_name='兴趣爱好')
    specialization = models.CharField(max_length=30, null=False, blank=False, verbose_name='特长')
    qq = models.CharField(max_length=12, null=False, blank=False, verbose_name='qq号')
    wx = models.CharField(max_length=30, null=False, blank=False, verbose_name='微信号')
    email = models.CharField(max_length=30, null=False, blank=False, verbose_name='邮箱 ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='微信昵称')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Group(models.Model):
    '''
    用户所创建的组
    '''
    user = models.ForeignKey(User, null=False, blank=False, verbose_name='创建者')
    name = models.CharField(max_length=15, null=False, blank=False, verbose_name='小组名称')
    short_description = models.CharField(max_length=60, null=False, blank=False, verbose_name='小组简介')
    max_number = models.SmallIntegerField(default=10, null=False, blank=False, verbose_name='小组最大成员数')
    now_number = models.SmallIntegerField(default=0, null=False, blank=False, verbose_name='小组现有成员数')
    demand = models.CharField(max_length=60, null=True, blank=True, verbose_name='加组要求')
    aim = models.CharField(max_length=100, null=False, blank=False, verbose_name='小组目标')
    show_1 = models.CharField(max_length=30, null=False, blank=False, verbose_name='成果描述')
    pic_1 = models.ImageField(upload_to="", null=True, blank=True, verbose_name="成果图1")
    pic_2 = models.ImageField(upload_to="", null=True, blank=True, verbose_name="成果图1")
    pic_3 = models.ImageField(upload_to="", null=True, blank=True, verbose_name="成果图3")
    created = models.DateTimeField(auto_now_add=True, verbose_name='微信昵称')

    class Meta:
        verbose_name = '小组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MyGroup(models.Model):
    '''
    我加入的小组
    '''
    user = models.ForeignKey(User, null=False, blank=False, verbose_name="用户名")
    group = models.ForeignKey(Group, null=False, blank=False, verbose_name="小组名")
    created = models.DateTimeField(auto_now_add=True, verbose_name='微信昵称')

    class Meta:
        verbose_name = '我加入的小组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group.name


class Letter(models.Model):
    '''
    加组申请
    '''
    IS_REPLAIED= ((0, "未回复"), (1, "已同意"), (2, "已拒绝"))
    user = models.ForeignKey(User, null=False, blank=False, verbose_name="用户名")
    group = models.ForeignKey(Group, null=False, blank=False, verbose_name="小组名")
    content = models.CharField(max_length=60, null=False, blank=False, verbose_name="申请说明")
    status = models.IntegerField(choices=IS_REPLAIED, null=False, blank=False, verbose_name="申请说明")
    refused = models.CharField(max_length=60, null=True, blank=True, verbose_name="拒绝原因")
    created = models.DateTimeField(auto_now_add=True, verbose_name='微信昵称')

    class Meta:
        verbose_name = '加组申请'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nickname


class Focus(models.Model):
    '''
    我的收藏
    '''
    user = models.ForeignKey(User, null=False, blank=False, verbose_name="用户名")
    group = models.ForeignKey(Group, null=False, blank=False, verbose_name="小组名")
    created = models.DateTimeField(auto_now_add=True, verbose_name='微信昵称')

    class Meta:
        verbose_name = '我的关注'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group.name


class Remark(models.Model):
    '''
    小组评论
    '''
    user = models.ForeignKey(User, null=False, blank=False, verbose_name="用户名")
    group = models.ForeignKey(Group, null=False, blank=False, verbose_name="小组名")
    created = models.DateTimeField(auto_now_add=True, verbose_name='微信昵称')