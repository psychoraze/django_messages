from django.shortcuts import render
from .models import Street
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    info = request.GET.get("info", "just info")
    response = HttpResponse(f"it is infromation : {info}")
    response.set_cookie("info", info)
    messages.add_message(request, messages.INFO, f"message : {info}")
    messages.add_message(request, messages.ERROR, f"message ERROR : {info}")
    messages.add_message(request, messages.SUCCESS, f"message SUCCESS : {info}")
    return render(request, "index.html")
