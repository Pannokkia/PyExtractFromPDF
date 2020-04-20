from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

sys.path.append(".")
import PyMenu


# Funzione per estrarre le pagine dal PDF di origine
def addBookmarks(fIn,fOut,fBookmarks):

    try:
        line = ''

        pdfOutput = PdfFileWriter()
    
        #Prendo nome file input
        #fName = fIn.name 
        #fIn.close()
        
        #f = PdfFileReader(open(fInName, 'rb')) # open input
        
        #Leggo file di configurazione Bookmarks
        line = fBookmarks.readlines()
        l = 0
        i = 0;
       
        while i < fIn.getNumPages():
            while l < len(line):
                values =  line[l].split(',')
                if (int(values[0]) - 1) == i:
                    pdfOutput.addPage(fIn.getPage(i)) # aggiungo pagina a file di destinazione
                    pdfOutput.addBookmark(str(values[1]).replace('\n',''),(int(values[0]) - 1))
                    print ('Bookmark added to the page: ' + str(i))
                    i += 1
                    break
                else:
                    pdfOutput.addPage(fIn.getPage(i)) # aggiungo pagina a file di destinazione    
                    i += 1
            l += 1
            pdfOutput.addPage(fIn.getPage(i)) # aggiungo pagina a file di destinazione  
            i += 1  

        
        pdfOutput.write(fOut)
        fOut.close()
        fBookmarks.close()
        return True
    
    except IOError:
        print(" An error has occured!")
        input()
        PyMenu.drawMenu()