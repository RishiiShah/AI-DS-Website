from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('activate/<uidb64>/<token>/',views.activateEmail, name='activate'), 
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('syllabus/', views.syllabus, name="syllabus"),
    path('chapter/', views.chapter, name="chapter"),
    path('content/', views.content, name="content"),
    path('contact-us/', views.contact, name="contact"),
    
    path('chat-room/', views.chatroom, name="chat-room"),
    
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('update-message/<str:pk>/', views.updateMessage, name="update-message"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
