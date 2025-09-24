import qrcode
from io import BytesIO
from django.shortcuts import render
from .forms import URLForm
from .models import URL
from django.core.files.base import ContentFile
import base64

def add_url(request):
    img_data = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            qr = qrcode.make(url)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            img_data = base64.b64encode(buffer.getvalue()).decode()

            # Save to database
            qr_instance = URL(url=url)
            qr_instance.image.save(f'{url[:20]}.png', ContentFile(buffer.getvalue()), save=True)
    else:
        form = URLForm()
    return render(request, 'add_url.html', {'form': form, 'img_data': img_data})

def delete_url(request, pk): ...

def url_library(request): ...
