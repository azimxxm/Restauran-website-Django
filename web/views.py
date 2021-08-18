from django.shortcuts import redirect, render
from .models import *
from .forms import *
def home(request):
    piza = Pizza.objects.all()
    salad = Salad.objects.all()
    noodle = Noodle.objects.all()
    famous = Famous.objects.all()
    person = Person.objects.all()
    hostory = History.objects.all()
    banner = Banner.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        'piza':piza,
        'salad':salad,
        'noodle':noodle,
        'famous':famous,
        'person':person,
        'hostory':hostory,
        'banner':banner,
        'form':form,
    }
    return render(request, 'web/base.html', context)


def about(request):
    context = {
    }
    return render(request, 'web/about.html', context)

def contact(request):
    context = {
    }
    return render(request, 'web/contct.html', context)