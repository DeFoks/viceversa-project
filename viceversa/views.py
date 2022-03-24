from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('This is about page')

def home(request):

    return render(request, 'home.html')

def reverse(request):
    text_get = ReversStr(request.GET['TextReverse'])

    return render(request, 'reverse.html', {'TextReverse':text_get})

def ReversStr(StrForReverse):

    return StrForReverse[::-1]