from django.contrib import admin
from .models import Chave

class detChave(admin.ModelAdmin):
    list_display = ('id','nome','usuario_nome','usuario_edv', 'status')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 5


admin.site.register(Chave)