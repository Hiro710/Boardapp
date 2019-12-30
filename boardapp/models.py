from django.db import models

"""
  title タイトル
  content 内容
  author 投稿者
  images 投稿画像
  good いいね
  read 既読
  readtext 既読ボタンを一人につき1回に制限する(今回は既読ボタンを押したユーザーの名前が入る)
"""

class BoardModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=100)
  images = models.ImageField(upload_to='')
  good = models.IntegerField(null=True, blank=True, default=0)
  read = models.IntegerField(null=True, blank=True, default=0)
  readtext = models.CharField(max_length=500, null=True, blank=True, default='default')