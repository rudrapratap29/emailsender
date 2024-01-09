from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def send(request):
    if request.method == 'POST':
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        # print(to,content)
        send_mail(
            # subject
            'texting',
            # msg
            content,
            # from email
            settings.EMAIL_HOST_USER,
            # rec list
            [to]

        )
        return HttpResponse('Email send successfully!!')
    return render(request,'index.html',{'title':'sendEmail'})



    # return render(request,'index.html',{'title':'sendEmail'})