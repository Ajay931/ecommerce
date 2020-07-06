from django.urls import path
from . import views

urlpatterns = [
    path('',views.disp,name='disp'),
    path('buy',views.buy,name='buy')
] 
