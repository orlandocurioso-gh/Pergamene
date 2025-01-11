import win32api

def stampaFileRegistro(percorso,nomeFile):
    filedastampare=percorso+nomeFile
    win32api.ShellExecute(0,"print",filedastampare,None,".",0)