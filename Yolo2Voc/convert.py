import os
from PIL import Image
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
from pathlib import Path



class Yolo2Voc(object):
    def __init__(self, class_file, annotations_path, **kwargs):
        self.__class_file = class_file
        self.__annotations_path = annotations_path
        self.__annotation_files = []
        self.__image_files = []


        self.__readFiles()
        self.__createFile()

        #kwargs
        self.source = kwargs['source']

        #print(self.__image_files)

        xml = self.__createObjectAnnotation('image.png', img_shape = (100, 100, 3), source="teste", objects=None)
        #print(ET.tostring(xml))


    def __readFiles(self):
        try:
            for root, dirs, files in os.walk(self.__annotations_path):
                for file in files:
                    if file.endswith('txt'):
                        self.__annotation_files.append(file.split(".")[0])
                    else:
                        self.__image_files.append(file)              
        except NameError:
            raise

    def __createFile(self):
        for image in self.__image_files:
            image_file = Path(self.__annotations_path+"/"+image)
            relative_annotation = image.split(".")[0]
            annotation_file = Path(self.__annotations_path+"/"+relative_annotation+".txt")
            if relative_annotation in self.__annotation_files:
                im = Image.open(image_file)
                img_shape = (*im.size, len(im.mode))
                with open(annotation_file, "r") as file:
                    line = file.readlines()
                    print(line)
                
                

    def __createObjectAnnotation(self, file, img_shape, objects, **kwargs):
        root = ET.Element("annotations")
        ET.SubElement(root, "folder").text = str(Path(self.__annotations_path))
        ET.SubElement(root, "filename").text = file
        ET.SubElement(root, "path").text = str(Path(self.__annotations_path + "\\" + file))

        source = ET.SubElement(root, "source")
        ET.SubElement(source, "database").text = "None" if kwargs['source'] else kwargs['source']

        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(img_shape[0])
        ET.SubElement(size, "height").text = str(img_shape[1])
        ET.SubElement(size, "depth").text = str(img_shape[2])
        
        return root