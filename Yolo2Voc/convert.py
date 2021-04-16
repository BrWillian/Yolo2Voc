import os
from PIL import Image
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
from pathlib import Path
from errno import ENOENT



class Yolo2Voc(object):
    def __init__(self, annotations_path, **kwargs):
        self.__annotations_path = annotations_path
        self.__annotation_files = []
        self.__image_files = []

        #kwargs
        self.__source = kwargs['source']

        #call functions
        self.__readFiles()
        self.__createFile()        

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
        try:
            class_map = open(self.__annotations_path+"/"+"classes.txt").read().strip().split('\n')
        except:
            raise IOError(ENOENT, 'No such classes file in', self.__annotations_path)
        
        for image in self.__image_files:
            image_file = Path(self.__annotations_path+"/"+image)
            relative_annotation = image.split(".")[0]
            annotation_file = Path(self.__annotations_path+"/"+relative_annotation+".txt")
            if relative_annotation in self.__annotation_files:
                im = Image.open(image_file)
                img_shape = (*im.size, len(im.mode))
                w, h, c = img_shape
                with open(annotation_file, "r") as file:
                    lines = file.readlines()
                    voc_labels = []
                    for line in lines:
                        annotation = dict()
                        line = line.strip()
                        data = line.split()
                        bbox_width = float(data[3]) * w
                        bbox_height = float(data[4]) * h
                        center_x = float(data[1]) * w
                        center_y = float(data[2]) * h
                        voc_labels.append({
                            'classe': class_map[int(data[0])],
                            'boxes': {
                                'x': int(center_x - (bbox_width / 2)),
                                'y': int(center_y - (bbox_height / 2)),
                                'w': int(center_x + (bbox_width / 2)),
                                'h': int(center_y + (bbox_height / 2))
                            }
                        })
                       
                    self.__createObjectAnnotation(image, img_shape, voc_labels)
                        
    def __createObjectAnnotation(self, file, img_shape, objects, **kwargs):
        root = ET.Element("annotation")
        ET.SubElement(root, "folder").text = str(Path(self.__annotations_path))
        ET.SubElement(root, "filename").text = file
        ET.SubElement(root, "path").text = str(Path(self.__annotations_path + "\\" + file))

        source = ET.SubElement(root, "source")
        ET.SubElement(source, "database").text = "None" if not self.__source else self.__source

        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(img_shape[0])
        ET.SubElement(size, "height").text = str(img_shape[1])
        ET.SubElement(size, "depth").text = str(img_shape[2])

        for object in objects:
            obj = ET.SubElement(root, "object")
            ET.SubElement(obj, "name").text = object['classe']
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = str(0)
            ET.SubElement(obj, "difficult").text = str(0)
            bbox = ET.SubElement(obj, "bndbox")
            ET.SubElement(bbox, "xmin").text = str(object['boxes']['x'])
            ET.SubElement(bbox, "ymin").text = str(object['boxes']['y'])
            ET.SubElement(bbox, "xmax").text = str(object['boxes']['w'])
            ET.SubElement(bbox, "ymax").text = str(object['boxes']['h'])
        

        print(ET.tostring(root))
