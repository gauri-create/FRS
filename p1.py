# import libraries
import cv2
import face_recognition
import os
import numpy as np
#Load images and encode faces
def load_images_from_folder(folder):
    images = []
    labels = []
    for subdir in os.listdir(folder):
        subdir_path = os.path.join(folder, subdir)
        if os.path.isdir(subdir_path):
            for filename in os.listdir(subdir_path):
                img_path = os.path.join(subdir_path, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    images.append(img)
                    labels.append(subdir)
    return images, labels
data_dir = 'Data'
known_images, known_labels = load_images_from_folder(data_dir)