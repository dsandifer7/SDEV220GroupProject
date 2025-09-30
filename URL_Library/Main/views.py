import qrcode
from django.shortcuts import render,redirect
from .forms import URLForm
from .models import URL
from .QRcode import generate_qr_code

def add_url(request):
    # access form data to generate qr code and save filepath to database
    libraryform = URLForm
    if request.method == 'POST':
        libraryform = URLForm(request.Post)
        if libraryform.is_valid():
            objects = URLForm.save(commit=False)
            url = object.url 
            name = object.name
            object.file_path = generate_qr_code(url, name,'URL_Library/media/qr_codes/')
            object.save()
            libraryform.save()
            return redirect("url_library")
        else:
            libraryform = URLForm()
    return render(request )


#def delete_url(request, pk): ...

def url_library(request):
    library = URL.objects.all()
    return render(request, 'Library.html',{'library':library})
