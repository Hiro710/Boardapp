from django.urls import path
from .views import signupfunc

urlpatterns = [
    # アプリへの繋ぎこみ
    # functionbasedviewで呼び出している
    path('signup/', signupfunc),
]
