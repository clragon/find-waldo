import boto3
import os


class AWSBrain:

    @staticmethod
    def _get_matches(source_binary, target_binary):
        client = None

        try:
            client = boto3.client('rekognition')
        except:
            try:
                from aws_conf import *
            except:
                raise Exception("No AWS credentials")
                os.sys.exit()
            try: 
                client = boto3.client('rekognition', region_name=AWS_REGION, aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)
            except:
                raise Exception("AWS couldnt be reached")
                os.sys.exit()

        response = client.compare_faces(SourceImage={ 'Bytes': source_binary, }, TargetImage={ 'Bytes': target_binary, })
        return response

    @staticmethod
    def find_face(source, target):
        response = _get_matches(open(source, 'rb').read(), open(target, 'rb').read())

        try:
            face = response["FaceMatches"][0]["Face"]["BoundingBox"]
        except:
            raise Exception("No matches")
            os.sys.exit()

        (width, height) = (target.width, target.height)

        return face["Left"] * width, face["Top"] * height, (face["Left"] * width) + (face["Width"] * width), (face["Top"] * height) + (face["Height"] * height)

