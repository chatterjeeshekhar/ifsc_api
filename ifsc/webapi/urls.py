from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ifsc/', views.ifsc, name='ifsc'),
    path('bank/', views.bank, name='bank'),
    path('state/', views.state, name='state'),
    path('district/', views.district, name='district')
]
