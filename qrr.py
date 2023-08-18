import pyqrcode
import png
from pyqrcode import QRCode

val = str(input("Enter URL : "))
print(val)
buss = pyqrcode.create(val)
buss.png('inputqr2.png',scale=8)