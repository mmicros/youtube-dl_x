#!/usr/bin/python3
import sys
import subprocess

from bs4 import BeautifulSoup as bs

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject, SIGNAL
from ui_mainwindow import Ui_main

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
    url = window.ui._urls.topLevelItem(0).text(0)
    process = subprocess.Popen(['youtube-dl', '-x', '--no-playlist', '-o', 'songs/%(title)s.%(ext)s', str(url)], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    
    while True:
        output = process.stdout.readline()
        # print(output.strip())
        window.ui._lbProgress.setText(output)
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
    
        QObject.connect(self.ui._btnChooseFile, SIGNAL('clicked()'), selectBookmark )
        QObject.connect(self.ui._btnChooseFile, SIGNAL('clicked()'), download )
        

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    app.exec()


