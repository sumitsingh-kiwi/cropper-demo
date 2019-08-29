from django.shortcuts import render, redirect
from rest_framework.views import APIView
import random
from django.core.files import File

# Create your views here.
from newAp.models import Attachment

import base64

def demo(request):
    return render(request, template_name='index.html', context={})


class upload(APIView):
    def post(self, request):
        files = eval(request.POST['upload_file'])
        for obj in files:
            imgdata = base64.b64decode(obj['image'][22:])
            filename = str(random.randint(10, 9999999)) + '.jpg'  # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                f.write(imgdata)
            with open(filename, 'rb') as f:
                Attachment.objects.create(document=File(f))
        return redirect('/index.html')
