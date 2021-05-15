from django.shortcuts import render, redirect

from .forms import RegistrForm

def registr(request):
    data = {}

    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = 'Success'
            return redirect('../')
    else:
        form = RegistrForm()
        data['form'] = form
        return render(request, 'registr/registr.html', data)