from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('upload/',views.upload,name='upload'),
    path('', views.posts, name='posts'),
    path('myPosts/', views.myPosts, name='myPosts'),
    path('<int:id>/', views.singlePost, name='singlePost')
]


    