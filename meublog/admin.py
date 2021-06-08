from django.contrib import admin
from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug','autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ('status', '-publicado')

@admin.register(Comentario)
class ComentarioAdim(admin.ModelAdmin):
    list_display = ('post','nome', 'email', 'criado', 'ativo')
    list_filter = ('criado', 'ativo',)
    ordering = ('ativo', 'post', 'criado',)