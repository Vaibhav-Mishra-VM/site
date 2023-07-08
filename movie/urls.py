from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('movies',views.movies),
    path('series',views.series),
    path('login',views.login),
    path('logout',views.logout),
    path('create_account',views.create_account),
    path('categories',views.categories),
    path('categories/<str:cat>',views.categories_specific),
    path('upload',views.upload),
    path('upload_se',views.upload_se),
    path('play/<int:url>',views.play),
    path('play_se/<str:name>',views.play_ser)
]
