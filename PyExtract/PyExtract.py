"""
MIT license -- free to use as you want, cheers.
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import os
import re 
import sys

sys.path.append(".")
import PyMenu

# Funzione per estrarre le pagine dal PDF di origine
def extractPage(f, fOut, pages,s):

    try:
        
        
        pdfOutput = PdfFileWriter()
        pdfInput = PdfFileReader(f)

        for i in pages:
            pdfOutput.addPage(pdfInput.getPage(int(i)-1))

        pdfOutput.write(fOut)
        
        if s != 5:
            fOut.close()
            
        f.close()
        return True
    
    except Exception:
        print(" An error has occured!")
        input()
        PyMenu.drawMenu()


def extractPage2(fIn, pages, xString):
    
  
        pdfOutput = PdfFileWriter()
        pdfInput = PdfFileReader(fIn)
        
        fhOut = open('output/' + str(xString).upper().replace(' ','_') + '.pdf','bw+')
        
        for i in pages:
            pdfOutput.addPage(pdfInput.getPage(i))
        
        pdfOutput.write(fhOut)
        fhOut.close()

        return True
  
        
#Funzione ricerca testo in file PDF
def findInPdf(f, xString):
    
    pages = []
    pdfDoc = PdfFileReader(f)
    xString = xString.replace('\n','')
    try:
        
        for i in range(0, pdfDoc.getNumPages()):
            
            content = ""
            content += pdfDoc.getPage(i).extractText()
            
            #content1 = content.encode('ascii', 'ignore').lower()
            #ResSearch = re.search(xString, content1)
            
            if re.search(xString,content,re.IGNORECASE):
                pages.append(i)
                print (' Found text on page: ' + str(i))
        
        return pages
    
    except Exception:
        print(" An error has occured!")
        input()
        PyMenu.drawMenu()

#Funzione per estrapolare pagine pari/dispari da PDF
def evenOddPages(f,even_odd_flag):
    
    pages = []
    pdfDoc = PdfFileReader(f)
    
    try:
        
        for i in range(0, pdfDoc.getNumPages()):
            
            #Se numero pagina / 2 restituisce resto 0 allora pagina è pari
            if even_odd_flag == 0:
                if i % 2 == 0:    
                    content = ""
                    content += pdfDoc.getPage(i).extractText()   
                    pages.append(i)
                    print (' Added page: ' + str(i))
            else:
                if i % 2 != 0:    
                    content = ""
                    content += pdfDoc.getPage(i).extractText()   
                    pages.append(i)
                    print (' Added page: ' + str(i))
        return pages
         
    except Exception:
        print(" An error has occured!")
        input()
        PyMenu.drawMenu()  


