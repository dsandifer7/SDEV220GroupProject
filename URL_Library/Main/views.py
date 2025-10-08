from django.shortcuts import render,redirect
from .forms import URLForm
from Sign_up.models import UserContent, User
from .QRcode import generate_qr_code

def add_url(request):
    # access form data to generate qr code and save filepath to database
    if request.method == 'POST':
        libraryform = URLForm(request.POST)
        if libraryform.is_valid():
            object = libraryform.save(commit=False)
            user_id = request.session.get("user_id")    #using session to get the current user_id
            if user_id:
                object.user = User.objects.get(id=int(user_id))
                
            url = object.url 
            name = object.name
            object.image_path = generate_qr_code(url, name, '/media/qr_codes/')
            object.save()
            return redirect('/library')
    else:
        libraryform = URLForm()

    library = UserContent.objects.all() 
    return render(request, 'Library.html', {
        'libraryform':libraryform,
        'library': library,  
    })


def url_library(request):
    library = UserContent.objects.all()
    libraryform = URLForm()
    return render(request, 'Library.html', {
        'library': library,
        'libraryform': libraryform
    })
# send to personal view
def myurls_library(request):
    user_id = request.session.get('user_id')
    if user_id:
        library = UserContent.objects.filter(user=user_id)  #using the current user from the session with user_id to populate the page
    else:
        library = UserContent.objects.none()  # If no user is logged in, will show an empty list 
    
    libraryform = URLForm()
    return render(request, 'Library.html', {
        'library': library,
        'libraryform': libraryform
    })


# need a view to update
def update_url(request, pk):    #uses the primary key that gets made automajically when a new url is added to pull that specific record
    saved_url = UserContent.objects.get(id=pk)
    user_id = request.session.get('user_id')
    
    if not user_id or saved_url.user.id != int(user_id):         #only the user that created the url can edit it
        return redirect('/library')
     
    if request.method == 'POST':
        libraryform = URLForm(request.POST, instance=saved_url)    # this will prefill the form with the existing data from the database
        
        if libraryform.is_valid():
            object = libraryform.save(commit=False)
            url = object.url 
            name = object.name
            object.image_path = generate_qr_code(url, name, '/media/qr_codes/')
            object.save()
            return redirect('/library')
    else:
        libraryform = URLForm(instance=saved_url)

    if user_id:
        library = UserContent.objects.filter(user=int(user_id))  # Show only users URLs
    else:
        library = UserContent.objects.all()  # Show all URLs if not logged in
    
    return render(request, 'Library.html', {
        'libraryform': libraryform,
        'library': library,
        'edit_mode': True,
        'edit_id': pk,
    })


# need a view to delete
def delete_url(request, pk):    #uses the primary key to find the record to delete
    saved_url = UserContent.objects.get(id=pk)
    user_id = request.session.get('user_id')

    if not user_id or saved_url.user.id != int(user_id):         #only the user that created the url can delete it
        return redirect('/library')
    saved_url.delete()
    return redirect('/library')