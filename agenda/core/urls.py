from django.urls import path
from .views import create_contato
from .views import read_contato
from .views import update_contato
from .views import delete_contato
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('create', create_contato, name='create_contato'),
    path('lista', read_contato, name='read_contato'),
    path('update/<int:id>', update_contato, name='update_contato'),
    path('delete/<int:id>', delete_contato, name='delete_contato'),
]