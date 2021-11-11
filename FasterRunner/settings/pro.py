# !/usr/bin/python3
# -*- coding: utf-8 -*-

from dotenv import load_dotenv, find_dotenv
from os import environ
from .base import *
import os

DEBUG = False

# RabbitMQ和MySQL配置相关的设置
if find_dotenv():
    load_dotenv(find_dotenv())
    # RabbitMQ 账号密码
    MQ_USER = environ.get('FASTER_MQ_USER')
    MQ_PASSWORD = environ.get('FASTER_MQ_PASSWORD')
    # 数据库账号密码
    FASTER_HOST = environ.get('FASTER_HOST')
    DB_NAME = environ.get('FASTER_DB_NAME')
    DB_USER = environ.get('FASTER_DB_USERNAME')
    DB_PASSWORD = environ.get('FASTER_DB_PASSWORD')
    PLATFORM_NAME = environ.get('PLATFORM_NAME')
    if PLATFORM_NAME:
        IM_REPORT_SETTING.update({'platform_name': PLATFORM_NAME})

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '47.113.177.159',
        'NAME': 'db_faster',  # 新建数据库名
        'USER': 'faster',  # 数据库登录名
        'PASSWORD': 'faster2019',  # 数据库登录密码
        'OPTIONS': {'charset': 'utf8mb4'},
        'TEST': {
            # 'MIRROR': 'default',  # 单元测试时,使用default的配置
            # 'DEPENDENCIES': ['default']
        }
    }
}

MQ_USER='username'
MQ_PASSWORD='password'
FASTER_HOST='47.113.177.159'
BROKER_URL = f'amqp://{MQ_USER}:{MQ_PASSWORD}@{FASTER_HOST}:5672//'

# 用来直接url访问
#STATIC_URL = '/static/'

# 部署的时候执行python manage.py collectstatic，django会把所有App下的static文件都复制到STATIC_ROOT文件夹下
STATIC_ROOT=os.path.join(BASE_DIR, 'static')

# 开发者模式中使用访问静态文
# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#)
