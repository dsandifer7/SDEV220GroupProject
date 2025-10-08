import qrcode
from django.shortcuts import render,redirect
from .forms import URLForm
from Sign_up.models import UserContent
from .QRcode import generate_qr_code

def add_url(request):
    # access form data to generate qr code and save filepath to database
    libraryform = URLForm()
    if request.method == 'POST':
        libraryform = URLForm(request.POST)
        if libraryform.is_valid():
            #object.user = request.user  # comment if you want to test without user login
            url = object.url 
            name = object.name
            object.image_path = generate_qr_code(url, name)
            object.save()
            return redirect('/library')
        else:
            libraryform = URLForm()

    library = UserContent.objects.all() 
    return render(request, 'Library.html', {
        'libraryform':libraryform,
        'library': library,  
    })

# This function is not needed anymore
def url_library(request):
    library = UserContent.objects.all()
    libraryform = URLForm()
    return render(request, 'Library.html', {
        'library': library,
        'libraryform': libraryform
    })
# send to personal view
def myurls_library(request):
    #library = UserContent.objects.filter(user = '3') # replace 3 with curent user id
    libraryform = URLForm()
    return render(request, 'Library.html', {
        'library': library,
        'libraryform': libraryform
    })


# need a view to update

# need a view to delete