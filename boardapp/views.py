from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
  user2 = User.objects.get(username='user')
  print(user2.email)
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, '', password)
    return render(request, 'signup.html', {'some':100})
  # コンテキスト{}でモデルを指定して欲しいデータを持ってくる
  return render(request, 'signup.html', {'some':100})