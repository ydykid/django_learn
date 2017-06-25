from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import AddForm

def index(request):
    return render(request, 'learn/index.html')

# add get
def add_get_show(request):
    return render(request, 'learn/add_get.html')

def add_get(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    return HttpResponse(str(int(a)+int(b)))

# add form
def add_form(request):
    if request.method == "POST" :
        form = AddForm(request.POST)
        if form.is_valid() :
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(a+b))
    else :
        form = AddForm()
    return render(request, "learn/form.html", {'title':'add','form':form})

# send Email
def send_email_show(request):
    return render(request, 'learn/send_email.html')

def send_email(request):
    to_email = request.GET.get('email')
    subject = request.GET.get('subject')
    context = request.GET.get('context')
    print("%s|%s|%s"%\
    (str(to_email),str(subject),str(context)))
    send_mail(subject,context,'ydy201@qq.com',[to_email],fail_silently=False)
    return render(request, 'learn/send_email.html',{'info':'ok'})
