"""Yolo2Voc: Transform archives Yolo to PascalVOC annotation.
    Copyright (c) 2021-2021 Yolo2Voc contributors
    Permission is Hereby Granted, Free Of Charge, To Any Person Obtaining A Copy
    OF THIS SOFTWARE AND ASSOCIATED Documentation Files (The "Software"), To Deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
    Copies of the Software, and to PER PER PERPOSS TO WHOM THE SOFTWARE IS
    SO Furnished to Subject to The Following Conditions:
    The above Copyright Notice and this Permission Notice Shall Be included in
    All copies or substantial portions of the software.
    The Software Is Provided "AS IS", Without Warranty Of Any Kind, Express OR
    Implied, including but not limited to the warranties of merchantability,
    Fitness is the private purpose and noninfringement. In the Event Shall The
    Authors or Copyright Holders Be Liabe for Any Claim, Damages or Other
    Liability, whether in An Action of Contract, Tort or Otherwise, Arising From,
    Out of or in connection with the software or the use or other dealings in
    The Software.
"""

from . import convert

convert = convert.Yolo2Voc

VERSION = (1, 0, 2, None)
if VERSION[3] is not None:
    VERSION_STRING = "%d.%d.%d_%s" % VERSION
else:
    VERSION_STRING = "%d.%d.%d" % VERSION[:3]

def get_client_info():
    """Get client info."""
    version = VERSION
    if VERSION[3] is None:
        version = VERSION[:3]
    return ".".join(map(str, version))

__version__ = get_client_info()
__author__ = "Willian Antunes"
__copyright__ = "Copyright 2021, Yolo2Voc contributors"
__credits__ = "Willian Antunes"
__license__ = "GPL"
__maintainer__ = "Willian Antunes"
__email__ = "willianantuness@outlook.com.br"
__status__ = "Production"