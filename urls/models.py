from django.db import models

# Create your models here.

class User(models.Model):
    '''用户表'''
    username=models.CharField(max_length=50,verbose_name='用户账号')
    password=models.CharField(max_length=50,verbose_name='用户密码')
    isadmin=models.BooleanField(verbose_name='管理员身份')

class Urls(models.Model):
    '''链接地址表'''
    urlname=models.CharField(max_length=50,verbose_name='项目名称')
    urltype=models.CharField(max_length=50,verbose_name='类型')
    urltestenv=models.CharField(max_length=300,verbose_name='测试环境')
    urlformalenv=models.CharField(max_length=300,verbose_name='正式环境')
    uid=models.IntegerField(verbose_name='用户编号')