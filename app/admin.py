from django.contrib import admin
from .models import *

class detUsuarios(admin.ModelAdmin):        #quais são os dados que e para mostrar na tela de admin
    list_display = ('id','nome', 'email', 'fone', 'ativo')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detCategoria(admin.ModelAdmin):        #quais são os dados que e para mostrar na tela de admin
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detFilmes(admin.ModelAdmin):        #quais são os dados que e para mostrar na tela de admin
    list_display = ('id','nome','categoria')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detAssinatura(admin.ModelAdmin):        #quais são os dados que e para mostrar na tela de admin
    list_display = ('id','nome','valor')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detFavoritos(admin.ModelAdmin):        #quais são os dados que e para mostrar na tela de admin
    list_display = ('id','filme_id','users_id')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria, detCategoria)
admin.site.register(Filmes, detFilmes)
admin.site.register(Assinatura, detAssinatura)
admin.site.register(Favoritos, detFavoritos)
admin.site.register(Usuarios, detUsuarios)