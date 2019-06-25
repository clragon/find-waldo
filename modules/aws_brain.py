#!/usr/bin/env python3

import boto3
import json
import os


class _config:
    def __init__(self):
        self.region = str()
        self.aws_key_id = str()
        self.aws_secret = str()


class AWSBrain:
    source = None
    target = None
    coords = (0, 0)
    box = (0, 0, 0, 0)

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def find_face(self):

        x_start, y_start, x_end, y_end = self._get_position(self.source.get_binary(), self.target.get_binary())
        self.coords = (x_start, y_start)
        self.box = (x_start, y_start, x_end, y_end)
        print("{} {} {} {}".format(x_start, y_start, x_end, y_end))
        return True

    def get_coords(self):
        return self.coords

    def get_box(self):
        return self.box

    def _get_matches(self, source_binary, target_binary):
        client = None

        try:
            client = boto3.client('rekognition')
        except:
            try:
                conf = _config()
                conf.__dict__ = json.load(open("config.json", 'r'))
                client = boto3.client('rekognition', region_name=conf.region, aws_access_key_id=conf.aws_key_id, aws_secret_access_key=conf.aws_secret)
            except:
                raise Exception("No AWS credentials")
                os.sys.exit()

        response = client.compare_faces(SourceImage={ 'Bytes': source_binary, }, TargetImage={ 'Bytes': target_binary, })
        return response

    def _get_position(self, source_binary, target_binary):
        response = self._get_matches(source_binary, target_binary)

        try:
            face = response["FaceMatches"][0]["Face"]["BoundingBox"]
        except:
            raise Exception("No matches")
            os.sys.exit()

        (px_width, px_height) = self.target.get_size()

        return px_width * face["Left"], px_height * face["Top"], (px_width * face["Left"]) + (px_width * face["Width"]), (px_height * face["Top"]) + (px_height * face["Height"])