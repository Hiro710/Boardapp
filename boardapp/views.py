from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import BoardModel


def signupfunc(request):
  if request.method == "POST":
    username2 = request.POST['username']
    password2 = request.POST['password']
    # 例外処理
    # try: 入力されたユーザー名が既に作られている場合はユーザー登録画面に遷移してエラーメッセージを表示する
    try:
        User.objects.get(username=username2)
        return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})
    # except: 入力されたユーザー名が既に作られていない場合はそのままDBに登録される
    except:
        user = User.objects.create_user(username2, '', password2)
        return render(request, 'signup.html', {'some':100})
  # コンテキスト{}でモデルを指定して欲しいデータを持ってくる
  return render(request, 'signup.html', {'some':100})

def loginfunc(request):
  if request.method == "POST":
    username2 = request.POST['username']
    password2 = request.POST['password']
    user = authenticate(request, username=username2, password=password2)
    # ユーザーがいる場合のそのユーザーのログイン処理をする
    if user is not None:
      login(request, user)
      return redirect('signup')
    else:
    # ユーザーがいなかった場合の処理(ログインできなかったらログインページに戻る)
      return redirect('login')
  # if文のPOSTに当てはまらない時の処理
  return render(request, 'login.html')

def listfunc(request):
  # objects_listにBoardModel内の全てのデータを格納する
  object_list = BoardModel.objects.all()
  # コンテキストでobject_listを使い回す
  return render(request, 'list.html', {'object_list':object_list})
