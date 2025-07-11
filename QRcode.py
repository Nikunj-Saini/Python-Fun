# import qrcode
# myqr = qrcode.make("https://www.linkedin.com/in/nikunj-saini")
# myqr.save("myqr.png")

import qrcode
features = qrcode.QRCode(version = 1,box_size=20,border = 2)
features.add_data = qrcode.make("https://www.linkedin.com/in/nikunj-saini")
features.make(fit=True)
new_image = features.make_image( fill='pink',back_color="white")
new_image.save('qrcode4.png')