from django.urls import path
from .views import signupfunc, loginfunc

urlpatterns = [
    # アプリへの繋ぎこみ
    # functionbasedviewで呼び出している
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
]
