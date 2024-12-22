from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Receita, Comentario
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from core.forms import ComentarioForm

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Receita.objects.all()
    context_object_name = 'receitas'

class ReceitaDetailView(DetailView):
    template_name = 'receita_detail.html'
    model = Receita
    context_object_name = 'receita'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        receita = self.get_object()
        context['ingredientes'] = [ingrediente.strip() for ingrediente in receita.ingredientes.split(',')]
        context['comentarios'] = receita.comentarios.all()
        context['comentario_form'] = ComentarioForm()
        return context

class CriarComentarioView(LoginRequiredMixin, FormView):
    form_class = ComentarioForm
    template_name = 'receita_detail.html'

    def form_valid(self, form):
        receita_id = self.kwargs.get('receita_id')
        receita = get_object_or_404(Receita, pk=receita_id)
        form.instance.usuario = self.request.user
        form.instance.receita = receita
        form.save()
        return redirect('core:receita_detail', pk=receita_id)

    def form_invalid(self, form):
        return HttpResponseForbidden("Dados inválidos!")
