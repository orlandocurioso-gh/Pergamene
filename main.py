import os
import Moduli
import datetime
import win32api

#routine spostamento file stampati e cancellazione directory

oggi=datetime.date.today()
anno=str(oggi).split('-')[0]
mese=str(oggi).split('-')[1]
giorno=str(oggi).split('-')[2]
data=str(giorno+'/'+mese+'/'+anno)
os.system('cls')
intestazioneXL='matricola,nomeCognome,dataNascita,luogoNascita,provincia,facolta,abilitazione,classeLaurea,lode,rettrice,firmaRettrice,preside,firmaPreside,dg,firmaDg,protocollo,dataLaurea,dataConsegna,numeroDiploma,formLaurea\n'
fInDesign=open('C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\filePergameneInDesign\\fileInDesign.csv','a')
fLista=open('C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\filePergameneInDesign\\fileLista.txt','a')
fInDesign.write(intestazioneXL)
fLista.write('Elenco diplomi stampati il '+data+'\n\n')
files=os.listdir('C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\filePergameneDaLavorare')
for elemento in files:
    with open('C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\filePergameneDaLavorare\\'+elemento,'r') as file:
        contenuto=file.readlines()
        listaPulita=Moduli.cancellaTestaLista(contenuto)#cancella intestazione DB
        for elemento in listaPulita:  
            listaFinale=Moduli.scomponi(elemento)
            listaFinale=Moduli.pulisciFileFinale(listaFinale)
            listaFinale=Moduli.controlloProvincia(listaFinale)
            listaFinale=Moduli.controlloAbilitazione(listaFinale)
            listaFinale=Moduli.controlloClasseLaurea(listaFinale)
            listaFinale=Moduli.controlloLode(listaFinale)
            pergamenaOggetto=Moduli.pergamena(listaFinale)
            riga=pergamenaOggetto.stampaDatiPergamena()
            fLista.write(riga+'\n')
            listaFinale.pop(len(listaFinale)-1)
            stringaPergamena=','.join(listaFinale)
            fInDesign.write(stringaPergamena)
            Moduli.creaCamicia(pergamenaOggetto)
fLista.write('\nTotale: '+str(len(listaPulita)))
fInDesign.close()
fLista.close()
percorsoStampa='C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\filePergameneInDesign\\'
file='fileLista.txt'
#Moduli.stampaFile(percorsoStampa,file)