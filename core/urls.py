from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('receita/<int:pk>/', views.ReceitaDetailView.as_view(), name='receita_detail'),
    path('comentario/<int:receita_id>/', views.CriarComentarioView.as_view(), name='criar_comentario'),
]
