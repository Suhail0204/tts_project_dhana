from django.shortcuts import render

from tts_file import ttsmodel


from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def tts_view(request):
    if request.method == "POST":
        text = request.POST['text']
        
        ttsmodel(text)
       

    return render(request,'tts.html')

def stt_view(request):
    return render(request,'stt.html')