import qrcode

img2 = qrcode.make("https://chat.whatsapp.com/KBlCBOVXsv22639q9hklbX")
img2.save("whatsapp.png")
print("QR2 is generated ")