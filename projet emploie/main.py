from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
import os
def affich_click():
    try:
        i=0
        f=open(w.year.currentText()+".txt","r")
        rows = w.emploie.rowCount()
        cols = w.emploie.columnCount()
        # Iterate through the table to read data
        r=f.readlines()
        for row in range(rows):
            for col in range(cols):
                item = r[i].rstrip()
                w.emploie.setItem(row, col, QTableWidgetItem(item))
                i+=1
        f.close()
    except:
        pass
def sauv_click():
    try:
        f=open(w.year.currentText()+".txt","w")
        rows = w.emploie.rowCount()
        cols = w.emploie.columnCount()
        # Iterate through the table to read data
        for row in range(rows):
            for col in range(cols):
                item = w.emploie.item(row, col)
                cell_data = item.text()
                f.write(cell_data+"\n")
        f.close()
    except:
        pass
def ajouter_click():
    if w.nouv.text()!="":
        fo=open("options.txt","a")
        w.year.addItem(w.nouv.text())
        fo.write(w.nouv.text()+"\n")
        fo.close()
        ff=open(w.nouv.text()+".txt","w")
        ff.close()
        w.nouv.setText("")
def effacer_click():
    index = w.year.findText(w.year.currentText())  # Find the index of the item by its text
    if index != -1 and w.year.currentText()!="Selectionner":
        with open("options.txt", "r") as fo:
            lines = fo.readlines()
        with open("options.txt", "w") as fo:
            for line in lines:
                if line.strip("\n") != w.year.currentText():
                    fo.write(line)
        try:
            os.remove(w.year.currentText()+".txt")
            w.year.removeItem(index)
            fo.close()
        except:
            pass
def vider_click():
    w.emploie.clearContents()


app = QApplication([])
w = loadUi ("interface.ui")
fo=open("options.txt","r")
r=fo.readlines()
for i in r:
    w.year.addItem(i.rstrip())
    fo.close()
w.show()
w.affich.clicked.connect ( affich_click )
w.sauv.clicked.connect ( sauv_click )
w.ajouter.clicked.connect ( ajouter_click )
w.effacer.clicked.connect ( effacer_click )
w.vider.clicked.connect ( vider_click )
app.exec_()
