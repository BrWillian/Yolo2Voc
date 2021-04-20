import Yolo2Voc


annotation_path = "~/Pictures/yolo-labels" #where are the dataset annotations.
source = "Personal Dataset" #contains base dataset name.
output = "~/Pictures/voc-labels" #where it will be saved to new annotations.
    
Yolo2Voc.convert(annotations_path=annotation_path, source=source, output=output)

#Get version on Yolo2Voc
print(Yolo2Voc.__version__)

#Get Author Name
print(Yolo2Voc.__author__)

#Get Author Contact
print(Yolo2Voc.__email__)