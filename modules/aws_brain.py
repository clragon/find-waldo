import boto3
import os


class AWSBrain:

    def find_face(self, source, target):
        x_start, y_start, x_end, y_end = self._get_position(open(source, 'rb').read(), open(target, 'rb').read())
        return x_start, y_start, x_end, y_end
    

    def get_position(self, source_binary, target_binary):
        response = self._get_matches(source_binary, target_binary)

        try:
            face = response["FaceMatches"][0]["Face"]["BoundingBox"]
        except:
            raise Exception("No matches")
            os.sys.exit()

        (px_width, px_height) = self.target.get_size()

        return px_width * face["Left"], px_height * face["Top"], (px_width * face["Left"]) + (px_width * face["Width"]), (px_height * face["Top"]) + (px_height * face["Height"])


    def get_matches(self, source_binary, target_binary):
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

