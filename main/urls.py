from django.urls import path

from main.views import *

urlpatterns = [
    # Главная страница, личные таски, создание таска, редактирование таска, удаление таска.
    path('', main_view, name='main'),
    path('self_tasks/', self_tasks_view, name='self_tasks'),
    path('create/', create_task_view, name='create'),
    path('update/<int:id>', update_task_view, name='update'),
    path('delete/<int:id>', delete_task_view, name='delete'),
    # Регистрация, логин, логаут.
    path('register_account/', register_account_view, name='register_account'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
