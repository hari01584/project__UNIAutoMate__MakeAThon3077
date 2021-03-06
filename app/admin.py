# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import complains, roomRequest, notifications, medical, laundaryRequest
from django.contrib import messages
import datetime

def accept(modeladmin, request, queryset):
    for i in list(queryset):
        n = notifications()
        n.forUser = i.user
        n.title = i.type
        n.message = "Your Request For %s Has Been Accepted!" % (i.type,)
        n.time = datetime.datetime.now().strftime("%I:%M %p on %B %d, %Y")
        n.save()
        i.delete()
    messages.add_message(request, messages.INFO, 'Okay! Following request have been accepted!')

accept.short_description = "Accept the Selected Orders"


def decline(modeladmin, request, queryset):
    for i in list(queryset):
        n = notifications()
        n.forUser = i.user
        n.title = i.type
        n.message = "Your Request For %s Has Been Declined :((" % (i.type,)
        n.time = datetime.datetime.now().strftime("%I:%M %p on %B %d, %Y")
        n.save()
        i.delete()
    messages.add_message(request, messages.INFO, 'The selected requests are declined!!')

decline.short_description = "Decline the Selected Orders"



@admin.register(roomRequest)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "roomNo", "PhoneNo", "TimeCleaning")
    actions = [accept,decline]

@admin.register(complains)
class ComplainsAdmin(admin.ModelAdmin):
    list_display = ("name", "roomno", "phoneno", "complaint")
    actions = [accept,decline]

@admin.register(medical)
class MedicalAdmin(admin.ModelAdmin):
    list_display = ("name", "roomno", "phoneno", "date", "problem", "time")
    actions = [accept,decline]


@admin.register(laundaryRequest)
class LaundaryAdmin(admin.ModelAdmin):
    list_display = ("name", "roomno", "phoneno", "time")
    actions = [accept,decline]

admin.site.site_header = "UAutoMate Admin Console"
#admin.site.unregister(Group)
