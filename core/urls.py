from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.IndexView.as_view(), name="home"),
    path('posts/',views.PostsView.as_view(), name="post"),
    path('<slug:slug>/', views.SingleView.as_view(), name="single")
]