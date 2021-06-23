from django.shortcuts import render, HttpResponse
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%c", localtime())
    }
    return render(request,'index.html', context)

# Create your views here.
