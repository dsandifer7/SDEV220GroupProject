import qrcode
url='https://docs.google.com/document/u/0/'
name= "Google Docs"
location= 'URL_Library/media/qr_codes/'

def generate_qr_code(url, name, size=10, border_size=4, color1 = 'black', color2= 'white'):
    qr=qrcode.QRCode(
        version=1,
        box_size=size,
        border = border_size
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color= color1, back_color= color2)  # qrcode.image.pil.PilImage
    file_path=f'{location}{name}.png'
    img.save(file_path)
    return file_path

#generate_qr_code(url,name,5,2,'brown','tan')
#https://copilot.microsoft.com/shares/mYq2DsqmQw77ZwwDdtLgP
