from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable': 'this is sent!'
    }
    messages.success(request, "This is a test mesage!")
    return render(request, 'index.html', context)
    # return HttpResponse("this is a homepage!")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is a about page!")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is a services page!")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your form has been submitted.")

    return render(request, 'contact.html')
    # return HttpResponse("this is a contact page!")