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

from core.forms import RoomCleaningForm, ComplaintForm, medicalForm, LaundaryForm
from core.models import complains, roomRequest, medical, laundaryRequest
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


def complain_panel(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ComplaintForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()

            # sreturn render(request, )
            return HttpResponseRedirect("page-success-query.html")
            # process the data in form.cleaned_data as required
            # return HttpResponseRedirect('/thanks/')
    else:
        form = ComplaintForm()

    comps_hist = complains.objects.all().filter(user=request.user)
    return render(request, "complain_panel.html", {'complains': comps_hist, 'form': form})


def medicalReq(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = medicalForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()

            # sreturn render(request, )
            return HttpResponseRedirect("page-success-query.html")
            # process the data in form.cleaned_data as required
            # return HttpResponseRedirect('/thanks/')
    else:
        form = medicalForm()

    mdc = medical.objects.all().filter(user=request.user)
    return render(request, "medical.html", {'medical': mdc, 'form': form})


def room_req(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomCleaningForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()

            # sreturn render(request, )
            return HttpResponseRedirect("page-success-query.html")
            # process the data in form.cleaned_data as required
            # return HttpResponseRedirect('/thanks/')
    else:
        form = RoomCleaningForm()

    reqList = roomRequest.objects.all().filter(user=request.user)
    return render(request, "room_req.html", {'reqList': reqList, 'form': form})


def laundary(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LaundaryForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()

            # sreturn render(request, )
            return HttpResponseRedirect("page-success-query.html")
            # process the data in form.cleaned_data as required
            # return HttpResponseRedirect('/thanks/')
    else:
        form = LaundaryForm()

    la = laundaryRequest.objects.all().filter(user=request.user)
    return render(request, "laundary.html", {'laundary': la, 'form': form})
