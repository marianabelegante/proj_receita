from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField(help_text="Liste os ingredientes separados por vírgulas.")
    instrucoes = models.TextField(help_text="Escreva as instruções passo a passo.")
    foto = models.ImageField(null=True, blank=True, verbose_name="Foto da Receita")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoria")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

class Comentario(models.Model):
    texto = models.TextField(verbose_name="Comentário")
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, verbose_name="Receita", related_name="comentarios")

    def __str__(self):
        return f"Comentário de {self.usuario} em {self.receita}"

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
