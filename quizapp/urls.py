from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('quiz',views.homepage, name='quiz'),
    path('result',views.result)
    
] 