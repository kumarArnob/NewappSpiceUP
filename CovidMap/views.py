from django.shortcuts import render , HttpResponse
import requests 
from django.contrib import messages
from CovidMap.models import Contact

def index(request):

    #clsmessages.success(request ,"HI")
    return render(request,'index.html')


def about(request):
    return render(request,'about.html') 


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        contact = Contact(name=name , phone=phone ,email = email ,desc =desc)
        contact.save()
        messages.success(request, 'We will contact soon .')


    return render(request ,'contact.html')


# Create your views here.
def api(request):
    data = requests.get('https://api.covid19api.com/countries').json()
    return render(request,'api.html',{'response':data})

