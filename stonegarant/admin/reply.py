# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms #зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('reply', 'person')
    search_fields = ['reply', 'person']
    ordering = ('-person',)

    class Form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'reply': RedactorWidget(editor_options={'lang': 'ru'}),
            }