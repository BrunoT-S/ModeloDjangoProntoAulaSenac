from django.urls import path
from . import views 

urlpatterns = [

    path('',views.main,name='main'),
    path('cadastrar', views.cadastro, name='cadastro'),
    path('vizulaizacao',views.visualizar, name='ver'),
    path('Update/<str:pk>',views.Update, name='Update'),
    path('Deletar/<str:pk>',views.Delete, name='Delete'),

]
