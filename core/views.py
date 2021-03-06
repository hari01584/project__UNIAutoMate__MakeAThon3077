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

from core.forms import RoomCleaningForm
from core.models import complains, roomRequest


def complain_panel(request):
    comps_hist = complains.objects.all()
    return render(request, "complain_panel.html",{'complains': comps_hist})

def room_req(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomCleaningForm(request.POST)
        print("ASADWDWDD")
        if form.is_valid():
            print("1453453")
            form.save()
            print("7989877")

            # process the data in form.cleaned_data as required
            #return HttpResponseRedirect('/thanks/')
    else:
        form = RoomCleaningForm()


    reqList = roomRequest.objects.all()
    return render(request, "room_req.html", {'reqList': reqList, 'form': form})
