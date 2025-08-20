
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.welcome, name='base'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('private_gallery/', views.private_gallery, name='private_gallery'),
    path('public_gallery/', views.public_gallery, name='public_gallery'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),
    path('logout/', views.logout_view, name='logout'),
    path('comment/<int:photo_id>/', views.comment, name='comment'),  
    path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
    path('welcome/', views.welcome, name='welcome'),
]
