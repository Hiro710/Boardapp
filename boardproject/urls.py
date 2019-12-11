from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # アプリへの繋ぎこみ
    path('', include('boardapp.urls')),
]
