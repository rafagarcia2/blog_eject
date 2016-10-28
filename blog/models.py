from django.db import models
from django import forms
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField('Nome da categoria',max_length=100)
    def __str__(self):
        return self.nome  
        

class Editor(models.Model):
    nome = models.CharField('Nome e Sobrenome do Editor',max_length=100)
    facebooklink = models.CharField('Link do Facebook pessoal', max_length=200, null=True, blank=True)
      
    def __str__(self):
        return self.nome  
        

class Post(models.Model):
    editor = models.ManyToManyField(Editor)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100,null=True, blank=True)
    capa = models.ImageField('Foto da capa', upload_to='img/', default='static/img/logo.svg')
    nivel = models.PositiveSmallIntegerField(default=1,null=True)
    categoria = models.ForeignKey(Categoria, null=True)
    text1 = models.TextField()
    picture1 = models.ImageField(upload_to='img/', blank=True)
    picturefigcaption1 = models.CharField('Figcaption',max_length=200, default="Direitos reservados")
    text2 = models.TextField(blank=True)
    picture2 = models.ImageField(upload_to='img/', blank=True)
    picturefigcaption2 = models.CharField('Figcaption',max_length=200, default="Direitos reservados")
    text3 = models.TextField(blank=True)
    picture3 = models.ImageField(upload_to='img/',blank=True)
    picturefigcaption3 = models.CharField('Figcaption',max_length=200, default="Direitos reservados")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title