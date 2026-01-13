from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def paginicial():
    template = loader.get_template('html/loguin.html')
    return HttpResponse(template.render())