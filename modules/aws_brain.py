from PIL import Image
import boto3
import os

try:
    from modules.aws_conf import *
except:
    raise Exception("No AWS credentials")

def _get_matches(source_binary, target_binary):
    client = None

    try:
        client = boto3.client('rekognition')
    except:
        try: 
            client = boto3.client('rekognition', region_name=AWS_REGION, aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)
        except:
            raise Exception("AWS couldnt be reached")

    response = client.compare_faces(SourceImage={ 'Bytes': source_binary, }, TargetImage={ 'Bytes': target_binary, })
    
    return response


def find_face(source, target):
    response = _get_matches(open(source, 'rb').read(), open(target, 'rb').read())

    try:
        face = response["FaceMatches"][0]["Face"]["BoundingBox"]
    except:
        raise Exception("No matches")

    (width, height) = (Image.open(target).width, Image.open(target).height)

    box = round(face["Left"] * width), round(face["Top"] * height), round((face["Left"] * width) + (face["Width"] * width)), round((face["Top"] * height) + (face["Height"] * height))

    return box

