from django.urls import path
from myTrain import views

app_name = "myTrain"

urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', views.log_in, name = 'login'),
    path('register/', views.register, name = 'register')
]