import numpy as np
import tensorflow as tf
from PIL import Image,ImageFile
from object_detection.utils import label_map_util
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True


class TFBrain:
    model_path = ''
    image = None
    box = (0, 0, 0, 0)    # (xmin,ymin,xmax,ymax)
    coords = (0, 0)       # Box's centre

    def __init__(self, image=None, model_path=''):
        # search for modelPath
        dirname = os.path.dirname(__file__)
        self.image = image
        if model_path == "":
            self.model_path = os.path.join(dirname, '../models/frozen_inference_graph.pb')
        else:
            self.model_path = model_path

    def find_waldo(self):
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.model_path, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        label_path = os.path.join(os.path.dirname(__file__), '../models/labels.txt')
        label_map = label_map_util.load_labelmap(label_path)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
        category_index = label_map_util.create_category_index(categories)

        with detection_graph.as_default():
            with tf.Session(graph=detection_graph) as sess:
                image_np = self.image.get_numpy_array()
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                # Actual detection.
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: np.expand_dims(image_np, axis=0)})

                if scores[0][0] < 0.1:
                    return False

                (width, height)=(self.image.get_width(), self.image.get_height())
                ymin = (boxes[0][0][0]*height)
                xmin = (boxes[0][0][1]*width)
                ymax = (boxes[0][0][2]*height)
                xmax = (boxes[0][0][3]*width)

                self.box = (xmin,ymin,xmax,ymax)
                self.coords = (xmin+((xmax-xmin)/2), height-ymin+((ymax-ymin)/2))
                return True

    def get_coords(self):
        return self.coords

    def get_box(self):
        return self.box
