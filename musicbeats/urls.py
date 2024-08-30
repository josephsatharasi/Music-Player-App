from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs, name=('songs')),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('Watchlater', views.Watchlater, name='Watchlater'),

]