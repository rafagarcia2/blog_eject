from django.contrib import admin
from .models import Post, Editor, Categoria
from django.db import models
from django.forms import CheckboxSelectMultiple


class ArtigoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Post,ArtigoAdmin)
admin.site.register(Editor)
admin.site.register(Categoria)