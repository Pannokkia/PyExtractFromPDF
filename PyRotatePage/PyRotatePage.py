"""
MIT license -- free to use as you want, cheers.
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
sys.path.append(".")
import PyMenu

def rotatePage(fIn, fOut, pages,angle=90):
    
    pdfOutput = PdfFileWriter()
    pdfInput = PdfFileReader(fIn)
    pages_list_int = []
    
    
    try:
        #Converto da str ad int la lista
        pages_list_int = [int(i) for i in pages] 
        
        if len(pages_list_int) != 0: 
            i = 0    
            #Se pages contiene una sequenza consecutiva di numeri tipo 1,2,3,4,5,6 entro nel
            #primo if
            list(range(min(pages_list_int), max(pages_list_int)+1))
            res = sorted(pages_list_int)
            
            if res != True:
                for p in range(0,pdfInput.getNumPages()):
                    if p == pages_list_int[i] - 1:
                        pdfOutput.addPage(pdfInput.getPage(p).rotateCounterClockwise(int(angle)))
                        i += 1
                        
                        if i >= len(pages_list_int):
                            i = 0
                            continue
                    else:  
                        pdfOutput.addPage(pdfInput.getPage(p))       
            else:
                for v in pages_list_int:
                    for p in range(0,pdfInput.getNumPages()):
                        if p == v - 1:
                            pdfOutput.addPage(pdfInput.getPage(p).rotateCounterClockwise(int(angle)))
                            v = v + 1
                            if v >= len(pages_list_int):
                                v = 0
                                continue
                            
                        else:       
                            pdfOutput.addPage(pdfInput.getPage(p))
                    
        else:
            print(" Page not found!")
            input()
            PyMenu.drawMenu()
        
        pdfOutput.write(fOut)
        
        fIn.close()
        fOut.close()
        return True
    
    except Exception:
        print (' An error has occurred!')
        input(' Push button to continue ...')
        PyMenu.drawMenu()
