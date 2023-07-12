import sys, os, csv, os.path
from color_scheduler_ui import Ui_Scheduler
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget, 
    QTableWidgetItem, QVBoxLayout, QHeaderView
)


# Performs all permanent code-based UI changes
def ui_changes(self):
    self.ui.lblColorSeq.setStyleSheet("color: gray;")
    self.ui.lblTruck.setStyleSheet("color: gray;")

    self.ui.tblOutput.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)      
    self.ui.tblOutput.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    

# Prompts the user to choose a csv file
def callback():
    filename = askopenfilename()
    ext = os.path.splitext(filename)[1]

    if (ext != ".csv"):
        filename = 'ERR'
    return filename

def file_open(self, filename):
    return open(filename, 'r')

def file_read(self, handler):
    return handler.readlines()



