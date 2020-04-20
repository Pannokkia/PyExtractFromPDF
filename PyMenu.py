import PyExtract.PyExtract
import PyBookmarks.PyBookmarks
from PyPDF2 import  PdfFileReader

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
                input()
                main()
                
        except IOError:
            print(' File not accessible!')
            input()
            main()
    
    elif s  == '2':
    
        try:
            
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks,pages = getSourceDestination()

            xString = input(' Text to search: ')
             
            if xString == '':
                print (' Empty string is not valid!')
                input()
                main()

            #Chiamo funzione per cercare all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.findInPdf(fIn, xString)
        
            if  len(pages) != 0:
                
                #Chiamo funzione per estrarre le pagine dove ho trovato il testo
                res = PyExtract.PyExtract.extractPage(fIn,fOut,pages,2)
                
                if res:
                    print (' File created correctly.')
                    input()
                    main()
            else:
                print ( 'No page was found containing the requested text.')
                input()
                drawMenu()
                
        except IOError:
            print(" File not accessible!")
            input()
            main()
        except Exception:
            print(" An error has occured!")
            input()
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
                input()
                main()
        except IOError:
            print(' File not accessible!')
            input()
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
                input()
                main()
        except IOError:
            print(" File not accessible!")
            input()
            main()
            
    elif s  == '5':
        
        try:
            
            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut, fBookmarks,pages = getSourceDestination(5)


            res = PyBookmarks.PyBookmarks.addBookmarks(fIn,fOut,fBookmarks)
            
            if res:
                print (' File and bookmarks created correctly.')
                input()
                main()
                
        except IOError:
            print(" File not accessible!")
            input()
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
        
        pages = [] 
        
        #Pdf sorgente
        while inpPDF == '':
            inpPDF = input(' Source PDF: ').replace('\n','')
        
        #Pdf destinazione
        while outPdf == '':
            outPdf = input(' Destination PDF: ').replace('\n','')
        
 
       
        
        if s == 5:
            fIn = PdfFileReader(open(inpPDF, 'rb')) # open input
        else:
             #Apro file in binary/lettura (PDF Origine)
            fIn = open(inpPDF, "br")
            
        #Apro file in binary/scrittura (PDF destinazione)
        fOut = open(outPdf, "bw")
        
        if s == 1:        
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
                
        if s == 5:
            while fBookmarks == '':
                fb = input(' Bookmarks config file: ').replace('\n','')
                fBookmarks = open(fb, "r")
               
        return fIn, fOut,fBookmarks,pages
        
      
        
if __name__ == "__main__":
    main()