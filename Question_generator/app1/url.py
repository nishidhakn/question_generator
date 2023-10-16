from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.func1),
    path('view/',views.func2),
    path('paper/',views.func3,name='paper')
]