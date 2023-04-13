from django.contrib import admin

# Register your models here.

from .models import Risco, DonoControle, Controle, PlanoAcao

admin.site.register(Risco)
admin.site.register(DonoControle)
admin.site.register(Controle)
admin.site.register(PlanoAcao)