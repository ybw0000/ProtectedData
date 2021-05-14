from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponseRedirect

# def index(request):
#     return render(request, 'main/index.html')

def index(request):
    error = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = True
    else:
        form = ContactForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'main/index.html', data)