from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('questions/', views.questions, name='questions'),
    path('tags/', views.tags, name='tags'),
    path('users/', views.users, name='users'),

    path('questions/<str:id>', views.discuss_room, name='discuss_room'),

    path('create_discuss/', views.create_discuss, name='create_discuss'),

    path('getTag/', views.get_quantity_of_tags),
    path('delete/<str:id>', views.delete_tag)
]
