from django.urls import path
from .views import UsuarioView

urlpatterns = [
        path('user/<str:user>,<str:password>', UsuarioView.getUser, name='obtenerUsuarioLogin'),
        path('user/', UsuarioView.getUsers, name='obtenerUsuarios'),
        path('user/<int:id>', UsuarioView.updateUser, name='actualizarUsuario'),
        path('user/', UsuarioView.dispatch, name='actualizarUsuario'),
        path('view/', UsuarioView.getPageNormal, name='vistaPaginaNormal'),
    ]


