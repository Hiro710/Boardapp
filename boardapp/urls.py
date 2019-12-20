from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc

urlpatterns = [
    # アプリへの繋ぎこみ
    # functionbasedviewで呼び出している
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
]
