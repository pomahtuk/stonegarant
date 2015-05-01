# # -*- coding: utf-8 -*-
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'email', 'memorial', 'user_name','user_phone','user_comment','status')
    search_fields = ['email', 'memorial', 'user_name','user_phone','user_comment','status']
    ordering = ('-pub_date',)
    list_filter = ['status'] 