from django.urls import path
from usuario import views


urlpatterns = [
    path('cadastro/', views.UsuarioCreateView.as_view(),
         name='cadusuario'),
    path('login/', views.LoginUserView.as_view(), name='loginuser'),
]