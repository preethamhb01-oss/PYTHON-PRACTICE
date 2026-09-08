import qrcode
img = qrcode.make("https://github.com/preethamhb01-oss/PYTHON-PRACTICE")
img.save("github.png")
print("QR IS GENERATED")


