from django.shortcuts import render
from .models import Noticia

def noticia(request):
    misNoticias=Noticia.objects.all()
    return render(request,"foro/foro.html",{'misNoticias':misNoticias})
