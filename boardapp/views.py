from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


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

# ログイン
def loginfunc(request):
  if request.method == "POST":
    username2 = request.POST['username']
    password2 = request.POST['password']
    user = authenticate(request, username=username2, password=password2)
    # ユーザーがいる場合のそのユーザーのログイン処理をする
    if user is not None:
      login(request, user)
      return redirect('list')
    else:
      # ユーザーがいなかった場合の処理(ログインできなかったらログインページに戻る)
      return redirect('login')
  # if文のPOSTに当てはまらない時の処理
  return render(request, 'login.html')

# ログインしているかどうかの処理(前処理、railsのbefore_actionに近いイメージ)
# 認証で閲覧制限をかけている
@login_required
def listfunc(request):
  # objects_listにBoardModel内の全てのデータを格納する
  object_list = BoardModel.objects.all()
  # コンテキストでobject_listを使い回す
  return render(request, 'list.html', {'object_list':object_list})

# ログアウト
def logoutfunc(request):
  logout(request)
  # ログアウトしたらログイン画面に遷移させる
  return redirect('login')

# 個別投稿
# 個別データの指定のため必ずpkを引数にする
def detailfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  return render(request, 'detail.html', {'object':object})

# いいね機能
# 個別データにいいねするので必ずpkを引数にする
def goodfunc(request, pk):
  post = BoardModel.objects.get(pk=pk)
  # models.py(BoardModel)のpostオブジェクト内のgoodフィールドを持ってくる
  # post.goodに1を足す
  post.good += 1
  post.save()
  return redirect('list')

# 既読機能
# 個別データに既読するので必ずpkを引数にする
def readfunc(request, pk):
  post_user = BoardModel.objects.get(pk=pk)
  # ログインしているユーザーのユーザー名を持ってくる(まだ既読ボタンを押していないユーザー)
  no_post_user = request.user.get_username()
  # post_user内にno_post_user内のユーザー名が入っている場合(ユーザー名が一致した場合)
  # true listへリダイレクトさせる
  if no_post_user in post_user.readtext:
    return redirect('list')
  else:
    post_user.read += 1 
    # ボタンが押されたらpost_userにボタンを押したno_post_userの情報を格納する
    post_user.readtext = post_user.readtext + ' ' + no_post_user
    post_user.save()
    return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')