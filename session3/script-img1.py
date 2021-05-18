from PIL import Image
from PIL import ImageEnhance


img = Image.open("gato.jpg")
applier = ImageEnhance.Brightness(img)
img2 = applier.enhance(5)
applier2 = ImageEnhance.Contrast(img2)
img3 = applier2.enhance(6)

img3.save('output.jpg')