from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pallavi(request):
   return HttpResponse('pallavi is a main thing in Music')

def hello(request):
    return HttpResponse('<h2> hello Mathew how are you </h2>')

def rudhresh(request):
    return HttpResponse('<h1><marquee> good morning my dear nephew </marquee></h1>')

def amaran(request):
    return HttpResponse('''
    <h1> Movie released on :31 Nov 2024</h1>
    <h1><i>hero:SK heroine:saipallavi</i></h1>
    <h1><b>Best movie</b></h1>
    <h1><img src='https://m.media-amazon.com/images/M/MV5BM2NlNWI0NDItYWM2MS00NjhhLTg4MTEtNzRjMjI4NzRkOTQ2XkEyXkFqcGc@._V1_QL75_UY281_CR18,0,500,281_.jpg'></h1>''')

