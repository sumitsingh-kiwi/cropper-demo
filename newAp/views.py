from django.shortcuts import render
from django.shortcuts import render
# Create your views here.


def demo(request):
    return render(request, template_name='index.html', context={})