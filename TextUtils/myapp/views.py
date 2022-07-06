from email.policy import default
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', default)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # Check which checkbox is ON
    if(removepunc == "on"):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removes New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removes Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charactercounter == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = (
                'No. of characters given in the text are : '+str(len(djtext)))
        params = {'purpose': 'Counts Characters', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on"):
        return HttpResponse("Please select atleast 1 operation")

    return render(request, 'analyze.html', params)
