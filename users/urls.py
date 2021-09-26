from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.auth, name='auth'),
    path('reg', views.reg, name='reg'),
    path('recover_pass', views.recover_pass, name='recover_pass'),
]
