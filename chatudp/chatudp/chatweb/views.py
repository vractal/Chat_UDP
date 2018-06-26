from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from ..core.models import *
# Create your views here.

def room_view(request, room):

    try:
        room = Room.objects.get(room_name=room)
    except:
        return HttpResponseNotFound(request)


    if request.method == "POST":
        text = request.POST.get("message-to-send")
        message = SentTextMessage.objects.create(text=text, room=room, is_sent=True)
        return redirect('room-view',room=room)


    participants = Participant.objects.all()
    messages = SentTextMessage.objects.all().order_by('-datetime')
    return render(request,template_name="room_view.html",context={"participants": participants,
                                                                  "messages": messages,
                                                                  "room":room})

