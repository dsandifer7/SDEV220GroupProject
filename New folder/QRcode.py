import qrcode
import os
from django.conf import settings
# url='https://docs.google.com/document/u/0/'
# name= "Google Docs"
# location= 'URL_Library/media/qr_codes/'

def generate_qr_code(url, name, size=6, border_size= 4, color1 = 'black', color2= 'white'):
    qr_code_dir = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
    os.makedirs(qr_code_dir, exist_ok=True)
    qr=qrcode.QRCode(
        version=1,
        box_size=size,
        border = border_size
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color = color1, back_color= color2)  # qrcode.image.pil.PilImage
    file_name = f'{name}.png'
    full_path = os.path.join(qr_code_dir, file_name)
    img.save(full_path)
    
    # Return relative path (for database and URLs)
    return f'qr_codes/{file_name}'

#generate_qr_code('https://github.com/Maggiekocon/Django-Project', 'Github','URL_Library/media/qr_codes/')
#https://copilot.microsoft.com/shares/mYq2DsqmQw77ZwwDdtLgP
