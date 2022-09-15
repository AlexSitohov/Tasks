from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', create_view, name='create'),
    path('update/<int:id>', update_view, name='update'),
    path('update_done/<int:id>', update_done_view, name='update_done'),
    path('delete/<int:id>', delete_view, name='delete'),
    path('<str:user>', personal_area_view, name='personal_area'),
    path('create_account/', create_account_view,name='create_account')

]
