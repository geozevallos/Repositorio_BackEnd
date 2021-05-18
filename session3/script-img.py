from PIL import Image
from PIL import ImageFilter

img = Image.open("gato.jpg")

filter1 = ImageFilter.EMBOSS
img2 = img.filter(filter1)

img2.save("filtro.jpg")