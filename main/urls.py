from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('credit_form/', views.credit_form, name='credit_form'),
    path('credit_result/', views.credit_result, name='credit_result'),
    path('info_without_insurance/', views.info_without_insurance, name='info_without_insurance'),
]
