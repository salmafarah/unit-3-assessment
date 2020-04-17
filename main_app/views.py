from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.

def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'list': widgets, 'widget_form': widget_form})

def add(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')

def delete(req, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('index')