from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

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
