from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from usuario.forms import UsuarioCreationForm


class UsuarioCreateView(CreateView):
    template_name = 'usuario/cadusuario.html'
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('loginuser')

    def form_valid(self, form):
        form.cleaned_data
        usuario = form.save(commit=False)
        usuario.is_staff = True
        grupo = get_object_or_404(Group, name='usuario')
        usuario.save()
        usuario.groups.add(grupo)
        messages.success(self.request, f"Usuário Cadastrado!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Usuário não pôde ser cadastrado!")
        return super().form_invalid(form)


class LoginUserView(FormView):
    template_name = 'usuario/login.html'
    model = User
    form_class = AuthenticationForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        user = form.cleaned_data['username']
        senha = form.cleaned_data['password']
        usuario = authenticate(self.request, username=user, password=senha)
        if usuario is not None:
            login(self.request, usuario)
            return redirect(self.success_url)
        else:
            messages.error(self.request, "Usuário ou senha inválida")
            return self.form_invalid(form)


