from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

def HomeView(request):
    return HttpResponseRedirect('/blog')
