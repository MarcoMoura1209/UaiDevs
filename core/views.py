from django.shortcuts import render, redirect
from .forms import Form
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = Form()

    return render(request, 'core/pages/home.html', context={
        'form': form,
    })
