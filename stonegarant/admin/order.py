# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget

class OrderPageForm(ModelForm):
    class Meta:
        widgets = {
            'user_comment': RedactorWidget(editor_options={'lang': 'ru'}),
            'notes': RedactorWidget(editor_options={'lang': 'ru'}),
        }

class OrderAdmin(admin.ModelAdmin):
    form = OrderPageForm
    list_display = ('pub_date', 'memorial', 'user_name', 'user_phone', 'user_email', 'user_comment', 'status', 'notes')
    search_fields = ['memorial', 'user_name', 'user_phone', 'user_email[jnz', 'user_comment', 'status']
    ordering = ('-pub_date',)
    list_filter = ['status']
    fieldsets = (
        (u'Основное', {
            'fields': (
                'order_number', 'order_pin', 'status', 'user_name', 'user_phone', 'user_email', 'user_comment'
            )
        }),
        (u'Детали заказа', {
            'fields': (
                'memorial', 'stella', 'cvetnik', 'podstavka', 'polirovka', 'total_price'
            )
        }),
        (u'Дополнительное', {
            'fields': (
                'pub_date', 'notes'
            )
        })
    )
