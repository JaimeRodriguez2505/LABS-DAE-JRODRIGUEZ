from django.urls import path
from . import views

urlpatterns = [
    path('suma/<int:num1>/<int:num2>/', views.suma, name='suma'),
    path('resta/<int:num1>/<int:num2>/', views.resta, name='resta'),
    path('multiplicar/<int:num1>/<int:num2>/', views.multiplicacion, name='multiplicacion'),
    path('division/<int:num1>/<int:num2>/', views.divition,name = 'divition'),
    path('potencia/<int:num1>/<int:num2>/', views.potencia,name = 'potencia'),
]
