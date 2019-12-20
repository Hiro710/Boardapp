from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc

urlpatterns = [
    # アプリへの繋ぎこみ
    # functionbasedviewで呼び出している
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    # 個別投稿は必ず<int:pk>を入れる
    path('detail/<int:pk>', detailfunc, name='detail'),
    # いいね機能のURL
    path('good/<int:pk>', goodfunc, name='good'),
]
