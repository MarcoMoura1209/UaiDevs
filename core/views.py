from django.shortcuts import render, redirect
from .forms import Form
from django_ratelimit.decorators import ratelimit
# Create your views here.


@ratelimit(key='ip', rate='10/h', method='POST', block=True)
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
