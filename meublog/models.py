from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublicadosManager(models.Manager):

    def get_queryset(self):
        return super(PublicadosManager, self). \
            get_queryset().filter(status='publicado')


class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    objects = models.Manager()  # este é o gerenciador padrão
    publicados = PublicadosManager()  # Nosso gerenciador personalizado

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    corpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meublog_posts')
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')

    class Meta:
        ordering = ('-publicado',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    corpo = models.TextField('Comentário')
    criado = models.DateTimeField('Data da criação',
                                  auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=False)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return 'Comentário de: ' + self.nome