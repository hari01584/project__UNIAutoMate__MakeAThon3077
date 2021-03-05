# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse

from core.models import complains


def complain_panel(request):
    cmps = complains(
      name = "HSSKSK", hostel = "Hostel M",
      time = "7:15 AM",
   )

    cmps.save()

    return render(request, "complain_panel.html")
