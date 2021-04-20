.. image:: https://readthedocs.org/projects/yolo2voc/badge/?version=latest
    :target: https://yolo2voc.readthedocs.io/
    :alt: Documentation Status

.. image:: https://app.codacy.com/project/badge/Grade/b5cbcb07687648fe8f77027f4438aceb
    :target: https://www.codacy.com/gh/BrWillian/Yolo2Voc/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BrWillian/Yolo2Voc&amp;utm_campaign=Badge_Grade


Yolo2Voc
=============

.. contents:: Table of Contents
   :local:

Requirements
-------------

* Python -- one of the following:

  - CPython : 3.6 and newer
  - Pillow : Latest 8.x version
  - lxml : Latest 4.x version
  - tqdm : Latest 4.x version
  - defusedxml : Latest 0.x version

Installation
------------

Package is uploaded on `PyPI <https://pypi.org/project/yolo2voc>`_.

You can install it with pip::

    $ python3 -m pip install yolo2voc


Examples
------------

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

Documentation
-------------

Documentation is available online: https://yolo2voc.readthedocs.io/

License
-------

Yolo2Voc is released under the MIT License. See LICENSE for more information.
