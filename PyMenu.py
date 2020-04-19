import PyExtract.PyExtract

def main():

    #Chiamo funzione per disegnare menu
    s = drawMenu()
    
    if s == '1':
     
        try:
               
            pages = []

            #Chiedo all'utente PDF di origine e PDF di destinazione
            fIn, fOut = getSourceDestination()

            inpPages = input(' Page/pages to extract (ex: 1/1,2,3/1-3): ')
            
            #Nel caso da input ricevo numero pagine tipo 1-3 allora cerco carattere '-' oppure ',' e lo sostituisco con ' '
            if inpPages.find('-') | inpPages.find(','):
                inpPages = inpPages.replace('-',' ').replace(',',' ') 
                #Inserisco in una lista i valori letti da input e normalizzati
                pageCounter = inpPages.split(' ')
            
            #Creo un tange con elementi inseriti nella lista precedentemente e ciclo per aggiungere a
            #lista pages le pagine che devo estrarre (in python il primo indice )
            for page in range(int(pageCounter[0]),int(pageCounter[-1]) + 1):
                pages.insert(page-1,page-1)

            res = PyExtract.PyExtract.extractPage(fIn, fOut, pages)
            
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
            fIn, fOut = getSourceDestination()

            xString = input(' Text to search: ')
             
            if xString == '':
                print (' Empty string is not valid!')
                input()
                main()

            #Chiamo funzione per cercare all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.findInPdf(fIn, xString)
        
            if  len(pages) != 0:
                
                #Chiamo funzione per estrarre le pagine dove ho trovato il testo
                res = PyExtract.PyExtract.extractPage(fIn,fOut,pages)
                
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
            fIn, fOut = getSourceDestination()

            #Chiamo funzione per per estrarre solo pagine pari all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.evenOddPages(fIn,even_odd_flag)
            

            #Chiamo funzione per estrarre le pagine pari
            res = PyExtract.PyExtract.extractPage(fIn,fOut,pages)
            
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
            fIn, fOut = getSourceDestination()

            #Chiamo funzione per per estrarre solo pagine pari all'interno del PDF indicato da input
            pages = PyExtract.PyExtract.evenOddPages(fIn,even_odd_flag)
            
            #Chiamo funzione per estrarre le pagine pari
            res = PyExtract.PyExtract.extractPage(fIn,fOut,pages)
            
            if res:
                print (' File created correctly.')
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
    print(' 5 - Search for text and extract pages')
    print(' 0 - Quit')
    print('\n ::—–{ :-)) }—-::')
    s = (input('\n Seleziona una voce del menu: '))
    return s
def getSourceDestination():
    
        inpPDF = ''
        outPdf = ''
        
        #Pdf sorgente
        while inpPDF == '':
            inpPDF = input(' Source PDF: ').replace('\n','')
        
        #Pdf destinazione
        while outPdf == '':
            outPdf = input(' Destination PDF: ').replace('\n','')
        
        #Apro file in binary/lettura (PDF Origine)
        fIn = open(inpPDF, "br")
        
        #Apro file in binary/scrittura (PDF destinazione)
        fOut = open(outPdf, "bw")
        
        return fIn, fOut
        
      
        
if __name__ == "__main__":
    main()