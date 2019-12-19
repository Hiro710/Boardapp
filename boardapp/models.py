from django.db import models

"""
  title タイトル
  content 内容
  author 投稿者
  images 投稿画像
  good いいね
  read 既読
  readtext 既読ボタンを一人につき1回に制限する
"""

class BoardModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=100)
  images = models.ImageField(upload_to='')
  good = models.IntegerField()
  read = models.IntegerField()
  readtext = models.CharField(max_length=500)