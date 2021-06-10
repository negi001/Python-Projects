# import modules
import os
import eel
import pyqrcode
import png

# get the current dir
currnet_dir = os.getcwd()

# initialize eel
eel.init(currnet_dir)

# qrcode
@eel.expose
def qrcode_generator(url):
    # Generate the QRcode
    url = pyqrcode.create(url)
    # create and save the png file name
    img = url.png('myqr.png', scale=6)
    return img


# start the eel windows
eel.start("index.html", size=(1000, 600))
