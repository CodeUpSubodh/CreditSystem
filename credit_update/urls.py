from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.credit_score_form, name='credit_score_form'),
    path('result/<int:score>/', views.credit_score_result, name='credit_score_result'),
]
