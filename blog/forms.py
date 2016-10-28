#-*- coding: utf-8 -*-
from django import forms

class LeadForm(forms.Form):
   name = forms.CharField(max_length = 100)
   email = forms.EmailField()
   email.clean('email@example.com')

   def __str__(self):
        return self.name