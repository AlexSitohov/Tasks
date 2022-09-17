from django.urls import path

from main.views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', create_view, name='create'),
    path('update/<int:id>', update_view, name='update'),
    path('delete/<int:id>', delete_view, name='delete'),
    path('create_account/', create_account_view, name='create_account'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('self_tasks/', self_tasks_view, name='self_tasks')

]
