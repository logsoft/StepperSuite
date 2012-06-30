# -*- coding: utf-8 -*-

"""
Module implementing PointsEdit.
"""

from PyQt4.QtGui import QFrame
from PyQt4.QtCore import pyqtSignature
import csv

from ui_points import Ui_Frame
from model import PointsModel

class PointsEdit(QFrame, Ui_Frame):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QFrame.__init__(self, parent)
        self.setupUi(self)

        self.tableWidget_points.setRowCount(3)
        self.pointsdata = []

        self.header = [ 'p' , 't' , 'PosX' , 'PosY' , 'PosZ', 'ZoomCmd' ]
        self.tableWidget_points.setHorizontalHeaderLabels(self.header)



    def loaddata(self, filename):
        try:
            with open(filename, 'rb') as file:
                csvread = csv.reader(file, delimiter='\t',
                                     quotechar='"',  quoting = csv.QUOTE_ALL)
                for row in csvread:
                    self.pointsdata.append(row)

        except:
            pass
        self.tableWidget_points.clear()
        self.tableWidget_points.setSortingEnabled(False)
        self.tableWidget_points.setRowCount(len(self.pointsdata))
        self.tableWidget_points.setColumnCount(len(self.header))
        self.tableWidget_points.setHorizontalHeaderLabels(self.header)

#        self.tableWidget_points.setModel(self.pointsdata)



    @pyqtSignature("")
    def on_pushButton_teachNew_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_teachInsert_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_deleteRow_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_moveTo_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_testcycle_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
