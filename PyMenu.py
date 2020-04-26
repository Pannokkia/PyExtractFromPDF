"""
MIT license -- free to use as you want, cheers.
"""

import PyExtract.PyExtract
import PyBookmarks.PyBookmarks
import PyCompress.PyCompress
import PyConvertToImage.PyConvertToImage
import PyRotatePage.PyRotatePage

from PyPDF2 import  PdfFileReader
import os, sys

def main():

    #Chiamo funzione per disegnare menu
    s = drawMenu()
    
    if s == '1':
     
        try:
               
            pages = []

            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks,inpPages = getSourceDestination(1)

            #Chiamo funzione per estrarre le pagine dal PDF
            res = PyExtract.PyExtract.extractPage(fIn, fOut, inpPages,1)
            
            #Pulisco pages
            pages.clear()
            
            if res:
                print (' File created correctly.')
                input(' Push button to continue ...')
                main()
                
        except Exception:
            print(" An error has occured!")
            input(' Push button to continue ...')
            main()
    
    elif s  == '2':
    
        try:
            
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks,pages = getSourceDestination()

            xString = input(' Text to search: ')
             
            if xString == '':
                print (' Empty string is not valid!')
                input(' Push button to continue ...')
                main()

            #Chiamo funzione per cercare all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.findInPdf(fIn, xString)
           
            if  len(pages) != 0:
                
                #Chiamo funzione per estrarre le pagine dove ho trovato il testo
                res = PyExtract.PyExtract.extractPage(fIn,fOut,pages,2)
                
                #Pulisco pages
                pages.clear()
                
                if res:
                    print (' File created correctly.')
                    input(' Push button to continue ...')
                    main()
            else:
                print ( 'No page was found containing the requested text.')
                input(' Push button to continue ...')
                drawMenu()
            
                
        except Exception:
            print(" An error has occured!")
            input(' Push button to continue ...')
            main()
    elif s  == '3':
        try:
            # even_odd_flag = 0 per estrarre pagine pari
            even_odd_flag = 0
            
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks,pages = getSourceDestination()

            #Chiamo funzione per per estrarre solo pagine pari all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.evenOddPages(fIn,even_odd_flag)
    
            #Chiamo funzione per estrarre le pagine pari
            res = PyExtract.PyExtract.extractPage(fIn,fOut,pages,3)
            
            #Pulisco pages
            pages.clear()
            
            if res:
                print (' File created correctly.')
                input(' Push button to continue ...')
                main()
        
        except Exception:
            print(" An error has occured!")
            input(' Push button to continue ...')
            main()
            
    elif s  == '4':
        
        try:
            # even_odd_flag = 1 per estrarre pagine dispari
            even_odd_flag = 1
            
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks, pages = getSourceDestination()

            #Chiamo funzione per per estrarre solo pagine pari all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.evenOddPages(fIn,even_odd_flag)
            
            #Chiamo funzione per estrarre le pagine dispari
            res = PyExtract.PyExtract.extractPage(fIn,fOut,pages,4)
            
            #Pulisco pages
            pages.clear()
            
            if res:
                print (' File created correctly.')
                input(' Push button to continue ...')
                main()
        
        except Exception:
                print(" An error has occured!")
                input(' Push button to continue ...')
                main()
    elif s  == '5':
        
        try:
            
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks,pages = getSourceDestination(5)


            res = PyBookmarks.PyBookmarks.addBookmarks(fIn,fOut,fBookmarks)
            
            if res:
                print (' File and bookmarks created correctly.')
                input(' Push button to continue ...')
                main()
            else:
                print (' An error has occurred!')
                input(' Push button to continue ...')
                main()
                
        except Exception:
                print(" An error has occured!")
                input(' Push button to continue ...')
                main()
                
    elif s  == '6':
        
        try:
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, compression_level,pages = getSourceDestination(6)

            res = PyCompress.PyCompress.compressPDF(fIn,fOut,compression_level)
            
            if res:
                print (' File created correctly.')
                input(' Push button to continue ...')
                main()
            else:
                print (' An error has occurred!')
                input(' Push button to continue ...')
                main()
        
        except Exception:
                print(" An error has occured!")
                input(' Push button to continue ...')
                main()
                
    elif s  == '7':
        
        try:
            #Chiedo all'utente PDF di origine e directory di destinazione file/files jpg
            fIn, outPathJPG = getSourceDestination(7)

            res = PyConvertToImage.PyConvertToImage.convertToImg(fIn,outPathJPG)
            
            if res:
                print (' Image file created correctly.')
                input(' Push button to continue ...')
                main()
            else:
                print (' An error has occurred!')
                input(' Push button to continue ...')
                main()
        
        except Exception:
                print(" An error has occured!")
                input(' Push button to continue ...')
                main()
    elif s  == '8':
        
        try:
            pages = []

            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, inpPages,angle = getSourceDestination(8)

            res = PyRotatePage.PyRotatePage.rotatePage(fIn,fOut,inpPages,angle)
            
            
            #Pulisco pages
            pages.clear()
            
            if res:
                print (' File created correctly.')
                input(' Push button to continue ...')
                main()
            else:
                print (' An error has occurred!')
                input(' Push button to continue ...')
                main()
        
        except IOError:
                print(" An error has occured!")
                input(' Push button to continue ...')
                main()
    else:
        print(" Bye!:-)")
        sys.exit(0)
        
def drawMenu():
    print('\n ::—–{ Menu }—-::')
    print('\n 1 - Extract page / pages from PDF')
    print(' 2 - Extract page / pages from PDF contain specific text')
    print(' 3 - Extract even pages from PDF')
    print(' 4 - Extract odd pages from PDF')
    print(' 5 - Add bookmarks from configuration file')
    print(' 6 - Reduce PDF size (using GS :-))')
    print(' 7 - Convert PDF to images (using GS :-))')
    print(' 8 - Rotate PDF page')
    print(' 0 - Quit')
    print('\n ::—–{ :-)) }—-::')
    s = (input('\n Seleziona una voce del menu: '))
    return s

#Funzione che richiede input all'utente
def getSourceDestination(s = 0):
    
        inpPDF = ''
        outPdf = ''
        fBookmarks = ''
        inpPages = ''
        fIn = ''
        fOut = ''
        outPathJPG = ''
        angle = ''
        pages = [] 
        
        #Pdf sorgente
        while inpPDF == '':
            inpPDF = input(' Source PDF: ').replace('\n','')
        
        if not os.path.isfile(inpPDF):
            print(' File not accessible!')
            input(' Push button to continue ...')
            main()
        
        if s == 5:
            fIn = PdfFileReader(open(inpPDF, 'rb')) # open input
        else:
            #Apro file in binary/lettura (PDF Origine)
            fIn = open(inpPDF, "br")
        
        
        if s == 7:
            while outPathJPG == '':
                outPathJPG = input(' Destination path image file: ').replace('\n','')
                
                if not os.path.isdir(outPathJPG):
                    os.mkdir(outPathJPG)
                
            return inpPDF,outPathJPG
        
        else:
            #Pdf destinazione
            while outPdf == '':
                outPdf = input(' Destination PDF: ').replace('\n','')
               
        
        if not os.path.isdir(os.path.dirname(os.path.abspath(outPdf))):
            print(' Path not accessible!')
            input(' Push button to continue ...')
            main()
        else:
            #Apro file in binary/scrittura (PDF destinazione)
            fOut = open(outPdf, "bw")
      
       
        #Gestione casi particolari
        #Se s = 8 chiedo angolo di rotazione        
        if s == 8:
            while angle == '':
                angle = input(' Rotation angle (90,180,270,360...): ').replace('\n','')

        #Se s = 1 oppure s = 8 chiedo numero di pagina / pagine da estrarre   
        if s == 1 or s == 8:
            try:
                
                if s == 1:
                    while inpPages == '':
                        inpPages = input(' Page/pages to extract (ex: 1/1,2,3/1-3): ').replace('\n','')
                else:
                    while inpPages == '':
                        inpPages = input(' Page to rotate: ').replace('\n','')
                    
                #Nel caso da input ricevo numero pagine tipo 1-3 allora cerco carattere '-' oppure ',' lo sostituisco con ' '
                if inpPages.find('-') == True:
                    inpPages = inpPages.replace('-',' ')
                    #Inserisco in una lista i valori letti da input e normalizzati
                    pageCounter = inpPages.split(' ')
                    #Creo un range con elementi inseriti nella lista precedentemente e ciclo per aggiungere a
                    #lista pages le pagine che devo estrarre (in python il primo indice )
                    for page in range(int(pageCounter[0]),int(pageCounter[1]) + 1):
                        pages.insert(page-1,page)
                else:
                    pages = inpPages.split(",")       

                if s  != 8:
                    return fIn, fOut,fBookmarks,pages
                else:
                    return fIn, fOut, pages, angle
                    
            except ValueError:
                print(" Invalid values ​​entered!")
                input(' Push button to continue ...')
                main()   
        elif s == 5:
            while fBookmarks == '':
                fb = input(' Bookmarks config file (.txt): ').replace('\n','')
                fBookmarks = open(fb, "r")
                return fIn, fOut,fBookmarks,''
        elif s == 6:
            try:
                compression_level = input(' Compression level (ex: 0,1,2,3,4): ').replace('\n','')
                return inpPDF, outPdf,compression_level,''
            except ValueError:
                print(" Invalid values ​​entered!")
                input(' Push button to continue ...')
                main() 
        else:
                return fIn, fOut,fBookmarks,''

if __name__ == "__main__":
    main()