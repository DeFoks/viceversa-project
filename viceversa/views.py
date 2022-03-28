from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('This is about page')

def home(request):
   ## text_get = ReversStr(request.GET['TextReverse2'])
    if str(request).find('TextReverse2') == -1:
        text_get = ''
    else:
        text_get = ReversStr(request.GET['TextReverse2'])        
    print(request)
    if text_get == '':
        text_get = ""
    return render(request, 'home.html',{'TextReverse3':text_get})

def reverse(request):
    text_get = ReversStr(request.GET['TextReverse'])

    return render(request, 'reverse.html', {'TextReverse':text_get})

def ReversStr(StrForReverse):

    return StrForReverse[::-1]