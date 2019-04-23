from keras.layers import Input
from keras.models import Model
from keras.optimizers import RMSprop
import numpy as np
from PIL import Image
from scipy.misc import imresize

from tiramisu import create_tiramisu
from brain_config import MU, STD, ROBOT_IMG_SIZE


def load_image(pil_img, img_sz=None):
    if img_sz:
        return np.array(pil_img.resize(img_sz, Image.NEAREST))
    else:
        return np.array(pil_img)


def img_resize(img):
    h, w, _ = img.shape
    nvpanels = h // 224
    nhpanels = w // 224
    new_h, new_w = h, w
    if nvpanels * 224 != h:
        new_h = (nvpanels + 1) * 224
    if nhpanels * 224 != w:
        new_w = (nhpanels + 1) * 224
    if new_h == h and new_w == w:
        return (img / 255. - MU) / STD
    else:
        return (imresize(img, (new_h, new_w)) / 255. - MU) / STD


def split_panels(img):
    h, w, _ = img.shape
    num_vert_panels = h // 224
    num_hor_panels = w // 224
    panels = []
    for i in range(num_vert_panels):
        for j in range(num_hor_panels):
            panels.append(img[i * 224:(i + 1) * 224, j * 224:(j + 1) * 224])
    return np.stack(panels)


def combine_panels(img, panels):
    h, w, _ = img.shape
    num_vert_panels = h // 224
    num_hor_panels = w // 224
    total = []
    p = 0
    for i in range(num_vert_panels):
        row = []
        for j in range(num_hor_panels):
            row.append(panels[p])
            p += 1
        total.append(np.concatenate(row, axis=1))
    return np.concatenate(total, axis=0)


def prediction_mask(img, target):
    layer1 = Image.fromarray(((img * STD + MU) * 255).astype('uint8'))
    layer2 = Image.fromarray(
        np.concatenate(
            4 * [np.expand_dims((225 * (1 - target)).astype('uint8'), axis=-1)],
            axis=-1))
    result = Image.new("RGBA", layer1.size)
    result = Image.alpha_composite(result, layer1.convert('RGBA'))
    return Image.alpha_composite(result, layer2)


def reshape_pred(pred): return pred.reshape(224, 224, 2)[:, :, 1]


def localize_waldo(pixel_probs, confidence=0.7):
    """
    Find Waldo pixel coordinates
    :param pixel_probs:
    :param confidence:
    :return: y and x coordinate if Waldo was found, None otherwise
    """
    r = np.nonzero(pixel_probs > 0.7)
    if len(r) < 2:
        # Confidence is too low, Waldo was not found
        return None

    i_s, j_s = r
    mean_i = np.mean(i_s)
    mean_j = np.mean(j_s)
    print("Found at x: {}/{}, y: {}/{}".format(mean_j, pixel_probs.shape[1], mean_i, pixel_probs.shape[0]))
    return int(round(mean_i)), int(round(mean_j))


class Brain(object):
    """
    Encapsulates ML model that is used to find Waldo on input images.
    """
    def __init__(self, train_model=False, trained_model_path=None):
        """

        :param train_model: True iff model should be trained from scratch
        :param trained_model_path: path to trained model file
        """
        self.trained_model_path = trained_model_path

        self.input_shape = (224, 224, 3)
        self.model = self.build_model()

        if train_model:
            self.train()
        elif trained_model_path is None:
            exit('Path to trained model is required to load pretrained model!')
        else:
            self.load_pretrained_model()

    def build_model(self):
        """
        Build inference network.
        :return: Keras model
        """
        img_input = Input(shape=self.input_shape)
        x = create_tiramisu(2, img_input, nb_layers_per_block=[4, 5, 7, 10, 12, 15], p=0.2, wd=1e-4)
        model = Model(img_input, x)

        model.compile(loss='categorical_crossentropy',
                      optimizer=RMSprop(1e-3),
                      metrics=["accuracy"],
                      sample_weight_mode='temporal')

        return model

    def train(self):
        """
        Train model from scratch.
        """
        pass

    def load_pretrained_model(self):
        """
        Load pretrained model file.
        """
        self.model.load_weights(self.trained_model_path)

    def find_waldo(self, robot_image):
        """
        Find Waldo on image taken by roboter.
        :param robot_image: should be of custom image wrapper
        :return: (x, y) coordinates in mm if Waldo was found, None otherwise
        """
        img = robot_image.get_pixel_values()
        img_w_mm, img_h_mm = robot_image.get_size_in_mm()
        img_size = ROBOT_IMG_SIZE  # TODO: need to fine-tune this to suitable waldo scale
        pixel_probs = self.predict_pixel_probabilities(Image.fromarray(img), img_size)
        r = localize_waldo(pixel_probs)
        out_width, out_height = pixel_probs.shape[1], pixel_probs.shape[0]

        if r is None:
            return r

        pixel_y, pixel_x = r
        # Convert to distance
        rel_x, rel_y = pixel_x / out_width, pixel_y / out_height
        return rel_x * img_w_mm, rel_y * img_h_mm

    def predict_pixel_probabilities(self, img, img_size):
        full_img = load_image(img, img_size)
        full_img_r, full_pred = self.waldo_predict(full_img)
        return full_pred

    def waldo_predict(self, img):
        rimg = img_resize(img)
        panels = split_panels(rimg)
        pred_panels = self.model.predict(panels, batch_size=6)
        pred_panels = np.stack([reshape_pred(pred) for pred in pred_panels])
        return rimg, combine_panels(rimg, pred_panels)
