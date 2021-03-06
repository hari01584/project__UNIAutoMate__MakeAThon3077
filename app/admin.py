# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from core.models import complains, roomRequest

admin.site.register(complains)
admin.site.register(roomRequest)
# Register your models here.
