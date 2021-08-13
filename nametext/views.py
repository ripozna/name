from .models import Info
from django.shortcuts import render

def name(request):
    name = Info.objects.all()
    return render(request, "name.html", {"name":name})

