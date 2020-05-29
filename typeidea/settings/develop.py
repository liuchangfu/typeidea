# -*- coding:utf-8 -*-
# @Time : 2020/5/29 8:49
# @Author : Administrator
# @File : develop.py
# @Software: PyCharm
# @Motto: good good study,day day up.

from .base import *  # NOQA


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
