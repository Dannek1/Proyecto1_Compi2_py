from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    
def inicio(request):
    if(request.method=='POST'):
        return 
    else:
        return render(request, 'index.html')