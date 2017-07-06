import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

# This is needed to display the images.
# %matplotlib inline
ROOT = '/Users/Pani/Documents/MakersAcademy/show-and-tell/object_detect/'
sys.path.append(ROOT + '/models')

from object_detection.utils import label_map_util

from object_detection.utils import visualization_utils as vis_util

MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = ROOT + MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = ROOT + MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(ROOT + 'models/object_detection/data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

class ObjectDetector(object):
    def __init__(self):
        self.download_model()
        self.load_model()

    def download_model(self):
        if os.path.exists(MODEL_FILE):
            print('model has already been downloaded')
            return
        opener = urllib.request.URLopener()
        opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
        tar_file = tarfile.open(MODEL_FILE)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'frozen_inference_graph.pb' in file_name:
                tar_file.extract(file, os.getcwd())

    def load_model(self):
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(categories)

    def load_image_into_numpy_array(self, image):
      (im_width, im_height) = image.size
      return np.array(image.getdata()).reshape(
          (im_height, im_width, 3)).astype(np.uint8)

    def detect(self, image_np):
        # Size, in inches, of the output images.
        IMAGE_SIZE = (12, 8)

        with self.detection_graph.as_default():
            with tf.Session(graph=self.detection_graph) as sess:
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
                # Each box represents a part of the image where a particular object was detected.
                boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
                # Each score represent how level of confidence for each of the objects.
                # Score is shown on the result image, together with the class label.
                scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
                classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
                # Actual detection.
                (boxes, scores, classes, num_detections) = sess.run(
                  [boxes, scores, classes, num_detections],
                  feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.
                vis_util.visualize_boxes_and_labels_on_image_array(
                  image_np,
                  np.squeeze(boxes),
                  np.squeeze(classes).astype(np.int32),
                  np.squeeze(scores),
                  self.category_index,
                  use_normalized_coordinates=True,
                  line_thickness=8)
                # plt.figure(figsize=IMAGE_SIZE)
                # plt.imshow(image_np)
                # plt.show()
                object_array = []
                for element in classes[scores > 0.7]:
                    object_array.append(str(self.category_index[element]['name']))
                return object_array, image_np

class FakeObjectDetector(object):

    def __init__(self):
        pass

    def download_model(self):
        pass

    def load_model(self):
        pass

    def load_image_into_numpy_array(self, image):
        pass

    def detect(self, image_np):
        return ['apple']

def main():
    # from object_detect import ObjectDetector
    # test_image_path = '/Users/Pani/Downloads/airplane.jpg'
    test_image_path = '/Users/Pani/Downloads/fruits.jpeg'
    object_detector = ObjectDetector()
    # load a test image
    image = Image.open(test_image_path)
    image_np = object_detector.load_image_into_numpy_array(image)
    object_detector.detect(image_np)

if __name__ == '__main__':
    main()
