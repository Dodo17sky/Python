import os
from PIL import Image

s = r"D:\Personal\Virusi_arme_si_otel\original"
d = r"D:\Personal\Virusi_arme_si_otel\small"

for i in range(10, 416, 2):
    dest = os.path.join(d, str(i) + '.jpg')
    sour = os.path.join(s, str(i) + '.jpg')

    im = Image.open(sour)
    im = im.resize((1376, 1032), Image.ANTIALIAS)
    im.save(dest, optimize=True, quality=95)
    print('image' , i, 'done')