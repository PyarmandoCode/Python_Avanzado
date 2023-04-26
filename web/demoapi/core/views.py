from django.shortcuts import render
import requests


def index(request):
    template_name="index.html"
    response=requests.get("https://api.escuelajs.co/api/v1/categories")
    categorias = response.json
    context = {
        "categorias":categorias
    }
    return render(request,template_name,context)




