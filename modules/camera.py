import urllib
import os


def take_photo(file, address, port=8080):

    try:
        urllib.request.urlretrieve("http://{}:{}/photoaf.jpg".format(str(address), str(port)), filename=file)
    except:
        raise Exception("Camera not reachable")
        os.sys.exit()

    return file
