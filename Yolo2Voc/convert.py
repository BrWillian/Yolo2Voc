import os
from PIL import Image
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
from pathlib import Path



class Yolo2Voc(object):
    def __init__(self, class_file, annotations_path, **kwargs):
        self.class_file = class_file
        self.annotations_path = annotations_path
        self.annotation_files = []
        self.__readFiles()

        #kwargs
        self.source = kwargs['source']

        print(self.source)

        xml = self.__createRoot('image.png', img_shape = (100, 100, 3), source="teste")
        print(ET.tostring(xml))


    def __readFiles(self):
        try:
            for root, dirs, files in os.walk(self.annotations_path):
                for file in files:
                    if file.endswith('txt'):
                        print(file)
        except NameError:
            raise

    def __createRoot(self, file, img_shape, **kwargs):
        root = ET.Element("annotations")
        ET.SubElement(root, "folder").text = str(Path(self.annotations_path))
        ET.SubElement(root, "filename").text = file
        ET.SubElement(root, "path").text = str(Path(self.annotations_path + "\\" + file))

        source = ET.SubElement(root, "source")
        ET.SubElement(source, "database").text = "None" if kwargs['source'] else kwargs['source']

        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(img_shape[0])
        ET.SubElement(size, "height").text = str(img_shape[1])
        ET.SubElement(size, "depth").text = str(img_shape[2])

        return root