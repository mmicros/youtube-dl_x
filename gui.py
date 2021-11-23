#!/usr/bin/python3
import sys
import subprocess

from bs4 import BeautifulSoup as bs

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject, SIGNAL, Signal, Slot, QProcess, QByteArray
from ui_mainwindow import Ui_main

@Slot(str)
def updateProgress(message):
    window.ui._lbUpdate.setText(message)


def selectBookmark():
    filename = QFileDialog.getOpenFileName(window, "Select Bookmark", "", "(*.html)")
    print("filename :"+str(filename[0]))

    with open(str(filename[0])) as f: #we should pass the bookmark file as argument
        soup = bs(f, 'html.parser')
	
    for i in soup.find_all('h3'): # the music file we will use this header
        if(i.string == "music"): # we should pass the folder name as argument
            tag = i
            while(tag.next_element and tag.next_element.name!='h3'):
                #if element is a tag, that has an 'href' attr and that attr is a youtube link
                if(tag.name and 'href' in tag.attrs and "youtube" in tag['href']):
                    url = QTreeWidgetItem([ str(tag['href']), tag.string ])
                    window.ui._urls.addTopLevelItem(url)
                    #print(tag['href'] + " || " + tag.string)
                    
                tag = tag.next_element


            
def download():
    def updateProg():
        message = proc.readAllStandardOutput().data().decode() 
        print(message)
        window.ui._lbUpdate.setText(message.strip())
        
        try:
            idx = message.index('%')
            pcnt = round(float(message[12:idx]))
            print(f"percentage:{round(float(pcnt))}")
            window.ui._prBar.setValue(pcnt)
        except (IndexError,ValueError):
            pass

    url = window.ui._urls.topLevelItem(0).text(0)    

    program = 'youtube-dl'
    args = ['-x', '--no-playlist', '-o', 'songs/%(title)s.%(ext)s', str(url)]
    proc = QProcess(window)
    proc.readyReadStandardOutput.connect(updateProg)
    proc.start(program,args)


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
    
        QObject.connect(self.ui._btnChooseFile, SIGNAL('clicked()'), selectBookmark )
        QObject.connect(self.ui._btnDownload, SIGNAL('clicked()'), download )
        

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    app.exec()


