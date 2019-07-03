import urllib
import os


def take_photo(address, port=8080):
    file = "docs/photo/webcam.jpg"

    try:
        urllib.request.urlretrieve("http://{}:{}/photoaf.jpg".format(str(address), str(port)), filename=file)
    except:
        raise Exception("Camera not reachable")
        os.sys.exit()

    return file
