
.. _examples:

========
Examples
========

.. _Annotation:

Transform Yolo annotation to PascalVOC
--------------------------------------

The following examples show how to transform the dataset annotation

.. code:: python

    #import the yolo2voc
    import Yolo2Voc

    # setting args

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


This example will print:

.. code-block:: console

    Loading your dataset....
    100%|███████████████████████████████| 16/16 [00:00<?, ? file/s]

    Please wait for all labels to be processed....
    100%|███████████████████████████████| 8/8 [00:00<00:00, 21.39 label/s]

    1.0.3
    
    Willian Antunes
    
    wiliam-m-@hotmail.com