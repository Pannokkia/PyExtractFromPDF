from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import os
import re

def main():

    #Chiamo funzione per disegnare menu
    s = drawMenu()
    
    if s == '1':
        
        pages = []
        outPdf = ''
        
        #Parametri di input
        inpPDF = input('Source PDF: ')
        
        try:
            #Apro file in binary/lettura (PDF Origine)
            f = open(inpPDF, "br")
      
        
            inpPages = input('Page/pages to extract (ex: 1/1,2,3/1-3): ')
            
            #Nel caso da input ricevo numero pagine tipo 1-3 allora cerco carattere '-' oppure ',' e lo sostituisco con ' '
            if inpPages.find('-') | inpPages.find(','):
                inpPages = inpPages.replace('-',' ').replace(',',' ') 
                #Inserisco in una lista i valori letti da input e normalizzati
                pageCounter = inpPages.split(' ')
            
            #Creo un tange con elementi inseriti nella lista precedentemente e ciclo per aggiungere a
            #lista pages le pagine che devo estrarre (in python il primo indice )
            for page in range(int(pageCounter[0]),int(pageCounter[-1]) + 1):
                pages.insert(page-1,page-1)

            
            while outPdf == '':
                outPdf = input('Destination PDF: ').replace('\n','')
            
            #Apro file in binary/scrittura (PDF destinazione)
            fOut = open(outPdf, "bw")

            res = extractPage(f, fOut, pages)
            
            if res:
                print ('File created correctly.')
                input()
                main()
                
        except IOError:
            print("File not accessible!")
            input()
            main()
        
    elif s  == '2':
        
        pages = []
        outPdf = ''
        inpPDF = input('Source PDF: ')
        xString = input('Text to search: ')
        
        try:
            #Apro file in binary/lettura (PDF Origine)
            f = open(inpPDF, "rb")
            #Chiamo funzione per cercare all'interno del PDF indicato da input
            pages = findInPdf(f, xString)
        
            if  len(pages) != 0:
                
                while outPdf == '':
                    outPdf = input('Indicare pdf di destinazione: ').replace('\n','')
                
                fOut = open(outPdf, "bw")
                #Chiamo funzione per estrarre le pagine dove ho trovato il testo
                res = extractPage(f,fOut,pages)
                
                if res:
                    print ('File created correctly.')
                    input()
                    main()
            else:
                print ('No page was found containing the requested text.')
                input()
                drawMenu()
                
        except IOError:
            print("File not accessible!")
            input()
            main()
        except Exception:
            print("An error has occured!")
            input()
            main()
    elif s  == '3':
        main()
    elif s  == '4':
        main()
    else:
        print("Bye!:-)")
        exit()

# extract pages
def extractPage(f, fOut, pages):

    try:
        
        pdfOutput = PdfFileWriter()
        pdfInput = PdfFileReader(f)

        for i in pages:
            pdfOutput.addPage(pdfInput.getPage(i))

        pdfOutput.write(fOut)
        fOut.close()
        f.close()
        return True
    
    except Exception:
        print("An error has occured!")
        input()
        main()

def findInPdf(f, xString):
    
    pages = []
    pdfDoc = PdfFileReader(f)
    
    try:
        
        for i in range(0, pdfDoc.getNumPages()):
            
            content = ""
            content += pdfDoc.getPage(i).extractText()
            
            # content1 = content.encode('ascii', 'ignore').lower()
            # ResSearch = re.search(xString, content1)
            
            if re.search(xString,content):
                pages.append(i)
                print ('Testo trovato a pagine: ' + str(i))
            
        return pages
    
    except Exception:
        print("An error has occured!")
        input()
        main()

def drawMenu():
    print('\n ::—–{ Menu }—-::')
    print('\n1 - Extract page / pages from PDF')
    print('2 - Extract page / pages from PDF contain specific text')
    print('3 - Extract even pages from PDF')
    print('4 - Extract even pages from PDF')
    print('5 - Search for text and extract pages')
    print('0 - Quit')
    print('\n ::—–{ :-)) }—-::')
    s = (input('\n Seleziona una voce del menu: '))
    return s

if __name__ == "__main__":
    main()
