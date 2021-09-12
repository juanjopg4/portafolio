from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):

    if request.method=='POST':

        subject=request.POST['asunto']

        message= 'Nombre: ' + request.POST['nombre'] + '\n' + 'Email: ' + request.POST['email'] + '\n' + 'Mensaje: ' + request.POST['mensaje']

        email_from=settings.EMAIL_HOST_USER

        recipient_list=['juanjopg4@gmail.com']

        send_mail(subject,message,email_from,recipient_list)

    return render(request,'index.html')
