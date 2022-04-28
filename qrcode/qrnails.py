import qrcode

img = qrcode.make("https://www.instagram.com/maarcarballonails/")

img.save("myQR.jpg")