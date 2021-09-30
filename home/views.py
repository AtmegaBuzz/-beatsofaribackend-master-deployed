from django.contrib import messages
from django.contrib.messages.api import error
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Beat,ArijitAddress,Contact
from .serializer import GetBeatsSerializer
from .form import ContactForm
# Create your views here.

def index(request):
    return render(request,"index.html")



def contact(request):
    
    contact_data_owner = ArijitAddress.objects.get(id=1)

    context = {
        "contact":contact_data_owner
    }
    if request.method=="POST":
            
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        myform = ContactForm(request,first_name,last_name,email,phone,message)

        if(myform.is_valid()):
            myform.save()
        

        return render(request,"contact.html",context)

    return render(request,"contact.html",context)


def error_page_404(request,exception):

    return render(request,"404.html")


# api views

class BeatsApiView(ListAPIView):
    queryset = Beat.objects.all()
    serializer_class = GetBeatsSerializer


class BeatsOnlyApiView(ListAPIView):
    queryset = Beat.objects.filter(mediaType="BEAT")
    serializer_class = GetBeatsSerializer


class PlaybackOnlyApiView(ListAPIView):
    queryset = Beat.objects.filter(mediaType="PLAYBACK")
    serializer_class = GetBeatsSerializer