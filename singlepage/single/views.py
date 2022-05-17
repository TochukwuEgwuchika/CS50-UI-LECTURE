from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'single/single.html')
    

def section(request, page):
    texts = ['Section1', 'Section2', 'Section3']
    text = texts[int(page-1)]

    return HttpResponse(text)
    

