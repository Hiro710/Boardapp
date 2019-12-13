from django.shortcuts import render

def signupfunc(request):
  if request.method == "POST":
    print('this is post method')
  else:
    print('this is not post method')
  # コンテキスト{}でモデルを指定して欲しいデータを持ってくる
  return render(request, 'signup.html', {'some':100})