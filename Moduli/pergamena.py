class pergamena:
    def __init__(self,lista):
        #print (lista)
        self.matricola=lista[0]
        self.nomeCognome=lista[1]
        self.dataNascita=lista[2]
        self.luogoNascita=lista[3]
        self.provincia=lista[4]
        self.facolta=lista[5].upper()
        self.abilitazione=lista[6]
        self.classeLaurea=lista[7]
        self.lode=lista[8]
        self.rettrice=lista[9]
        self.firmaRettrice=lista[10]
        self.preside=lista[11]
        self.firmaPreside=lista[12]
        self.dg=lista[13]
        self.firmaDg=lista[14]
        self.protocollo=lista[15]
        self.dataLaurea=lista[16]
        self.dataConsegna=lista[17]
        self.numeroDiploma=lista[18]
        self.formLaurea=lista[19]
        self.sesso=lista[len(lista)-1]

    def stampaDatiPergamena(self):
        riga=self.matricola+' '+self.nomeCognome+'                      '+self.facolta
        return riga
        #rigaCsv=self.matricola+','+self.nomeCognome+','+self.facolta
        #return rigaCsv
        