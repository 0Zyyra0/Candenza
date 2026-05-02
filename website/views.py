from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request,'index.html')


