import pyqrcode

url = input("enter url to generate qr:  \n")

QR = pyqrcode.create(url)

QR.png("webqr.png",scale=8)