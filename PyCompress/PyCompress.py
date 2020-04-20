"""
MIT license -- free to use as you want, cheers.
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import sys
import subprocess

sys.path.append(".")
import PyMenu

"""
Compression levels:

    0: default

    1: prepress

    2: printer

    3: ebook

    4: screen
"""

def compressPDF(fIn, fOut,compress_level=0):
    
    try:

            if compress_level == '1':
                compress_level = '/prepress'
            elif compress_level == '2':
                compress_level = '/printer'
            elif compress_level == '3':
                compress_level = '/ebook'
            elif compress_level == '4':
                compress_level = '/screen'
            else:
                compress_level = '/default'
            
            subprocess.call(['gswin64c', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',

                            '-dPDFSETTINGS=' + compress_level,

                            '-dNOPAUSE', '-dVERBOSE', '-dBATCH',

                            '-sOutputFile=' + fOut,

                             fIn]

            )
            return True
    except IOError:
        return False