#!/usr/bin/env python3

import boto3
import json
import os
from PIL import Image


class _config:
    def __init__(self):
        
        self.region = str()
        self.aws_key_id = str()
        self.aws_secret = str()


def _get_matches(source_bin, target_bin):

    client = None

    try:
        client = boto3.client('rekognition')
    except:
        try:
            conf = _config()
            conf.__dict__ = json.load(open("..\\..\\config.json", 'r'))
            client = boto3.client('rekognition', region_name=conf.region, aws_access_key_id=conf.aws_key_id, aws_secret_access_key=conf.aws_secret)
        except:
            print("no aws credentials found")
            os.sys.exit()

    response = client.compare_faces(SourceImage={ 'Bytes': source_bin, }, TargetImage={ 'Bytes': target_bin, })

    return response


def get_position(source, target):

    source_bin = open(source, 'rb').read()
    target_bin = open(target, 'rb').read()

    response = _get_matches(source_bin, target_bin)

    try:
        face = response["FaceMatches"][0]["Face"]["BoundingBox"]
    except:
        print("no matches")
        os.sys.exit()

    px_width, px_height = Image.open(target).size

    return px_width * face["Left"], px_height * face["Top"], (px_width * face["Left"]) + (px_width * face["Width"]), (px_height * face["Top"]) + (px_height * face["Height"])
