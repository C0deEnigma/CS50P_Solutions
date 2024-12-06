import sys
from PIL import Image, ImageOps
if len(sys.argv)>3:
    sys.exit('Too many command-line arguments')
if len(sys.argv)<3:
    sys.exit('Too few command-line arguments')
if sys.argv[1].split('.')[-1] not in ['jpg', 'jpeg', 'png']:
    sys.exit('Invalid input')
if sys.argv[1].split('.')[-1] not in ['jpg', 'jpeg', 'png']:
    sys.exit('Invalid output')
if sys.argv[1].split('.')[-1]!=sys.argv[2].split('.')[-1]:
    sys.exit('Input and output have different extensions')
try:
    with Image.open (sys.argv[1]) as i1:
        with Image.open ('shirt.png') as original:
            size = original.size
            photo=ImageOps.fit(i1, size)
            photo.paste(original, original)
            photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit('Input does not exist')

