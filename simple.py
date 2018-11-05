import pyqrcode

from pyzbar.pyzbar import decode
from PIL import Image


data = 'sure this works'

# Encode data to QR code and save file as PNG
qr = pyqrcode.create(data)
qr.png('my_qr.png', scale=6)

# Decode data from QR code from PNG file
result = decode(Image.open('./my_qr.png'))
print(result)

