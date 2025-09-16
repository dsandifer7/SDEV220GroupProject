import qrcode
img = qrcode.make('https://www.allrecipes.com/recipe/9959/marshmallow-treats/')
type(img)  # qrcode.image.pil.PilImage
img.save("Rice Krispie.jpg")