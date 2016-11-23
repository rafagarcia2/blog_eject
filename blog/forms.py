#-*- coding: utf-8 -*-
from django import forms
from .models import Email
from django.core.mail import send_mail
from django.conf import settings

class LeadForm(forms.Form):
   name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Seu nome'}))
   email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'seu.email.aqui@porfavor.com'}))
   email.clean('email@example.com')

   def save_contact(self):
        email = Email(nome=self.cleaned_data['name'], email=self.cleaned_data['email'])
        email.save()

   def __str__(self):
        return self.name

class MailForm(forms.Form):
    assunto = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Assunto do E-mail'}))
    mensagem = forms.CharField(widget=forms.Textarea)

    def my_send_mail(self):
        context = {
            'assunto': self.cleaned_data['assunto'],
            'mensagem': self.cleaned_data['mensagem'],
        }
        users = Email.objects.all()
        for user in users:
            send_mail(context['assunto'], context['mensagem'],
            settings.DEFAULT_FROM_EMAIL, [user.email])