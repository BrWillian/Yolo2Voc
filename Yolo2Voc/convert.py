import os
from PIL import Image
from lxml.etree import Element
from lxml.etree import SubElement
from lxml.etree import tostring
from pathlib import Path
from errno import ENOENT, EIO
from tqdm import tqdm
from defusedxml import ElementTree as etree

etree.Element = _ElementType = Element
etree.SubElement = SubElement
etree.tostring = tostring

class Yolo2Voc(object):
    def __init__(self, annotations_path, **kwargs):
        """A python class to convert YOLO into Pascal VOC 2012 format. It generates xml annotation file in PASCAL VOC format for Object Detection."""
        self.__annotations_path = annotations_path
        self.__annotation_files = []
        self.__image_files = []
        self.__source = kwargs['source']
        self.__output = kwargs['output']
        self.__readFiles()
        self.__createFile()

    def __readFiles(self):
        """Function to read dataset annotation, and create list of images with location."""
        try:
            print('Loading your dataset....')
            for _, _, files in os.walk(self.__annotations_path):
                for file in tqdm(files, unit=' file', ncols=74):
                    if file.endswith('txt'):
                        self.__annotation_files.append(file.split(".")[0])
                    else:
                        self.__image_files.append(file)
        except NameError:
            raise

    def __createFile(self):
        """Function to convert yolo annotation for PascalVOC format."""
        try:
            class_map = open(self.__annotations_path+"/"+"classes.txt").read().strip().split('\n')
        except:
            raise IOError(ENOENT, 'No such classes file in', self.__annotations_path)

        print('\nPlease wait for all labels to be processed....')
        for image in tqdm(self.__image_files, unit=' label', ncols=70):
            image_file = Path(self.__annotations_path+"/"+image)
            relative_annotation = image.split(".")[0]
            annotation_file = Path(self.__annotations_path+"/"+relative_annotation+".txt")
            if relative_annotation in self.__annotation_files:
                im = Image.open(image_file)
                img_shape = (*im.size, len(im.mode))
                w, h, _ = img_shape
                with open(annotation_file, "r") as file:
                    lines = file.readlines()
                    voc_labels = []
                    for line in lines:
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

                    self.__writeXml(self.__createObjectAnnotation(image, img_shape, voc_labels), relative_annotation, self.__output)

    def __createObjectAnnotation(self, file, img_shape, objects, **kwargs):
        """Function for modeling xml annotation on PascalVOC format."""
        root = Element("annotation")
        SubElement(root, "folder").text = str(self.__annotations_path.split("/")[-1])
        SubElement(root, "filename").text = file
        SubElement(root, "path").text = str(Path(self.__annotations_path + "/" + file))
        source = SubElement(root, "source")
        SubElement(source, "database").text = "None" if not self.__source else self.__source
        size = SubElement(root, "size")
        SubElement(size, "width").text = str(img_shape[0])
        SubElement(size, "height").text = str(img_shape[1])
        SubElement(size, "depth").text = str(img_shape[2])

        for objectLabeled in objects:
            obj = SubElement(root, "object")
            SubElement(obj, "name").text = objectLabeled['classe']
            SubElement(obj, "pose").text = "Unspecified"
            SubElement(obj, "truncated").text = str(0)
            SubElement(obj, "difficult").text = str(0)
            bbox = SubElement(obj, "bndbox")
            SubElement(bbox, "xmin").text = str(objectLabeled['boxes']['x'])
            SubElement(bbox, "ymin").text = str(objectLabeled['boxes']['y'])
            SubElement(bbox, "xmax").text = str(objectLabeled['boxes']['w'])
            SubElement(bbox, "ymax").text = str(objectLabeled['boxes']['h'])

        return tostring(root, pretty_print=True)

    def __writeXml(self, objectXml, file_name, output_path):
        """Function for write xml object annotation."""
        output_path = './output' if not self.__output else self.__output

        if output_path == './output':
            try:
                os.mkdir('./output')
            except:
                raise IOError(EIO, 'It is not possible to create the directory: ', './output')

        with open(output_path+'/'+file_name+'.xml', 'wb') as xmlObject:
            xmlObject.write(objectXml)
