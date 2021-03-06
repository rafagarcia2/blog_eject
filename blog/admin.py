from django.contrib import admin
from .models import Post, Editor, Categoria, Email, EnviarEmail
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.core.mail import send_mail
from django.conf import settings


class ArtigoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class EnvioEmailAdmin(admin.ModelAdmin):
    list_display = ['assunto', 'texto']

    def save_model(self, request, obj, form, change):
        context = {
            'assunto': obj.assunto,
            'texto': obj.texto,
        }
        users = Email.objects.all()
        for user in users:
            send_mail(context['assunto'], context['texto'],
            settings.DEFAULT_FROM_EMAIL, [user.email])
            

admin.site.register(Post,ArtigoAdmin)
admin.site.register(Editor)
admin.site.register(Categoria)
admin.site.register(Email)
admin.site.register(EnviarEmail, EnvioEmailAdmin)