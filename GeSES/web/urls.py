from django.urls import path
from . import views
urlpatterns = [

    path('', views.web, name='web'),
    path('espacios/', views.espacios, name='espacios'),
    path('simulacion/', views.simulacion, name='simulacion'),

]