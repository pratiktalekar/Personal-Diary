from django.shortcuts import render

def index(request):
    return render(request, 'entries/index.html')

def add_entry(request):
    return render(request, 'entries/add_entry.html')