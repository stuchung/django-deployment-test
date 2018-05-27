from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('test/', views.test, name='test'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    #path('goodbye/', views.goodbye,name='goodbye'),
]
