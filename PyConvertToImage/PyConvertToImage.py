"""
MIT license -- free to use as you want, cheers.
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import sys
import subprocess

sys.path.append(".")
import PyMenu


def convertToImg(fIn, outPathJPG):
    
    try:

        subprocess.call(['gswin64c ', '-sDEVICE=pngalpha',
                        ' -density 1200x1200 -resize 25%',
                        ' -transparent black -background tranparent',
                        ' -dBATCH',
                        ' -dNOPAUSE',
                        ' -dVERBOSE',
                        ' -sOutputFile=' + outPathJPG + '\Pic-%d.png',fIn])
        
        return True
        
    except IOError:
        return False