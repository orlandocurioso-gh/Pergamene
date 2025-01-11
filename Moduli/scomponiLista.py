def scomponi(stringa):
    listaNuova=stringa.split('^')
    i=0
    while i<=len(listaNuova)-1:
        if listaNuova[i]=='':
            listaNuova.pop(i)
            i=i-1
        i=i+1
    return listaNuova