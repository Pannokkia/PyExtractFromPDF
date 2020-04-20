"""
MIT license -- free to use as you want, cheers.
"""

import PyExtract.PyExtract
import PyBookmarks.PyBookmarks
import PyCompress.PyCompress
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
    else:
        print(" Bye!:-)")
        exit()
        
def drawMenu():
    print('\n ::—–{ Menu }—-::')
    print('\n 1 - Extract page / pages from PDF')
    print(' 2 - Extract page / pages from PDF contain specific text')
    print(' 3 - Extract even pages from PDF')
    print(' 4 - Extract odd pages from PDF')
    print(' 5 - Add bookmarks from configuration file')
    print(' 6 - Reduce PDF size (using GS :-))')
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
        
        #Pdf destinazione
        while outPdf == '':
            outPdf = input(' Destination PDF: ').replace('\n','')
 
        if not os.path.isdir(os.path.dirname(os.path.abspath(outPdf))):
            print(' Path not accessible!')
            input(' Push button to continue ...')
            main()
        
        #Apro file in binary/scrittura (PDF destinazione)
        fOut = open(outPdf, "bw")

       
        #Gestione casi particolari
        if s == 1:
            try:    
                while inpPages == '':
                    inpPages = input(' Page/pages to extract (ex: 1/1,2,3/1-3): ').replace('\n','')
                    
                #Nel caso da input ricevo numero pagine tipo 1-3 allora cerco carattere '-' oppure ',' e lo sostituisco con ' '
                if inpPages.find('-') | inpPages.find(','):
                    inpPages = inpPages.replace('-',' ').replace(',',' ') 
                    #Inserisco in una lista i valori letti da input e normalizzati
                    pageCounter = inpPages.split(' ')
                
                #Creo un range con elementi inseriti nella lista precedentemente e ciclo per aggiungere a
                #lista pages le pagine che devo estrarre (in python il primo indice )
                for page in range(int(pageCounter[0]),int(pageCounter[-1]) + 1):
                    pages.insert(page-1,page-1)
                
                return fIn, fOut,fBookmarks,pages
                    
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