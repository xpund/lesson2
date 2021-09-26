from django.urls import path
from . import views

# Типа я умею делать комментарии к своему коду
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'), # Главаня страница
    path('about', views.about, name='about'), # Страница обо мне
    path('create', views.create_task, name='create'), # Страница для создания задачи
]
