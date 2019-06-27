import numpy as np
import tensorflow as tf
from PIL import Image,ImageFile
from object_detection.utils import label_map_util
import os


ImageFile.LOAD_TRUNCATED_IMAGES = True


def _get_numpy_array(image_binary):
    (im_width, im_height) = (image.width, image.height)
    image_np = np.array(image.getdata())
    reshaped = image_np.reshape((im_height, im_width, 3))
    result = reshaped.astype(np.uint8)
    return result


def find_waldo(image):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(os.path.join(os.path.dirname(__file__), '../models/frozen_inference_graph.pb'), 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    label_path = os.path.join(os.path.dirname(__file__), '../models/labels.txt')
    label_map = label_map_util.load_labelmap(label_path)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    with detection_graph.as_default():
        with tf.Session(graph = detection_graph) as sess:
            image_np = _get_numpy_array(open(image, 'rb').read())
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
                raise Exception("No Matches")

            (width, height) = (image.width, image.height)

            box = round(boxes[0][0][1] * width), round(boxes[0][0][0] * height), round(boxes[0][0][3] * width), round(boxes[0][0][2] * height)

            return box

