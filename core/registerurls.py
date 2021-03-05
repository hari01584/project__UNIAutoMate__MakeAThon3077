# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .views import complain_panel
from django.urls import path, include  # add this

urlpatterns = [
    path('complain_panel', complain_panel),
]
