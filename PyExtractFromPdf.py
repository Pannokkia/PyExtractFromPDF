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
        inpPDF = input('Indicare pdf di origine: ')
        inpPages = input('Indicare numero pagine/e da estrarre (es: 1/1,2,3/1-3): ')
        
        #Nel caso da input ricevo numero pagine tipo 1-3 allora cerco carattere '-' oppure ',' e lo sostituisco con ' '
        if inpPages.find('-') | inpPages.find(','):
            inpPages = inpPages.replace('-',' ').replace(',',' ') 
            #Inserisco in una lista i valori letti da input e normalizzati
            pageCounter = inpPages.split(' ')
        
        #Creo un tange con elementi inseriti nella lista precedentemente e ciclo per aggiungere a
        #lista pages le pagine che devo estrarre (in python il primo indice )
        for page in range(int(pageCounter[0]),int(pageCounter[-1]) + 1):
            pages.insert(page-1,page-1)

        f = open(inpPDF, "br")
        
        while outPdf == '':
            outPdf = input('Indicare pdf di destinazione: ').replace('\n','')
        
        fOut = open(outPdf, "bw")
        extractPage(f, fOut, pages)
        
    elif s  == '2':
        
        pages = []
        outPdf = ''
        inpPDF = input('Indicare pdf di origine: ')
        xString = input('Indicare testo da ricercare: ')
        f = open(inpPDF, "rb")
        #Chiamo funzione per cercare all'interno del PDF indicato da input
        pages = findInPdf(f, xString)
        
        if  len(pages) != 0:
            
            while outPdf == '':
                outPdf = input('Indicare pdf di destinazione: ').replace('\n','')
                 
            fOut = open(outPdf, "bw")
            #Chiamo funzione per estrarre le pagine dove ho trovato il testo
            extractPage(f,fOut,pages)
        else:
            print ('Non è stata trovata alcuna pagina contenete il testo richiesto')
            input()
            drawMenu()  
        
    else:
        exit()
    

# extract pages
def extractPage(f, fOut, pages):

    pdfOutput = PdfFileWriter()
    pdfInput = PdfFileReader(f)

    for i in pages:
        pdfOutput.addPage(pdfInput.getPage(i))

    pdfOutput.write(fOut)
    fOut.close()

def findInPdf(f, xString):
    
    pages = []
    pdfDoc = PdfFileReader(f)
    
    for i in range(0, pdfDoc.getNumPages()):
        
        content = ""
        content += pdfDoc.getPage(i).extractText()
        
        # content1 = content.encode('ascii', 'ignore').lower()
        # ResSearch = re.search(xString, content1)
        
        if re.search(xString,content):
           pages.append(i)
           print ('Testo trovato a pagine: ' + str(i))
           
    return pages

def drawMenu():
    print('\n ::—–{ Menu }—-::')
    print('\n1 - Estrai pagine da PDF')
    print('2 - Cerca testo in PDF ed estrai pagine')
    print('3 - Termina il programma.')
    print('\n ::—–{ :-)) }—-::')
    s = (input('\n Seleziona una voce del menu: '))
    return s

if __name__ == "__main__":
    main()
