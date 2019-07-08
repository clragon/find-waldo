import urllib
import os


def take_photo(file, address, port=8080):
    request = None
    try:
        request = urllib.request.urlopen("http://{}:{}/photoaf.jpg".format(str(address), str(port)), timeout=10000)
    except:
        raise Exception("Camera not reachable")
        os.sys.exit()  
    with open(file, 'wb') as f:
        try:
            f.write(request.read())
        except:
            print("error")

    return file
