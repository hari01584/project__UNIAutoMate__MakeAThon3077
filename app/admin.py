# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from core.models import complains, roomRequest

admin.site.register(complains)

@admin.register(roomRequest)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "roomNo", "PhoneNo", "TimeCleaning")
# Register your models here.

admin.site.site_header = "UAutoMate Admin Console"
