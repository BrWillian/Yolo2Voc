import os
from PIL import Image
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET



class Yolo2Voc(object):
    def __init__(self, class_file, annotations_path, **kwargs):
        self.class_file = class_file
        self.annotations_path = annotations_path
        self.annotation_files = []
        self.__readAnnotations()


    def __readAnnotations(self):
        try:
            for root, dirs, files in os.walk(self.annotations_path):
                for file in files:
                    print(file)
        except NameError:
            raise