# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import ModelForm
from core.models import roomRequest, complains, medical, laundaryRequest


class RoomCleaningForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    roomNo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    PhoneNo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    TimeCleaning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = roomRequest
        fields = ('name', 'roomNo', 'PhoneNo', 'TimeCleaning')


class medicalForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    roomno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    phoneno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    problem = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = medical
        fields = ('name', 'roomno', 'phoneno', 'date', 'problem', 'time')


class ComplaintForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    roomno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    phoneno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    complaint = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = complains
        fields = ('name', 'roomno', 'phoneno', 'complaint')


class LaundaryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    roomno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    phoneno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = laundaryRequest
        fields = ('name', 'roomno', 'phoneno', 'time')
