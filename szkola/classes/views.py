from django.shortcuts import render
from .models import Class

def classes_list(request):
    classes = Class.objects.all()
    return render(request, 'classes/classes_list.html', {'classes': classes})

