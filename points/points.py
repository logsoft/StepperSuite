# -*- coding: utf-8 -*-

"""
Module implementing PointsEdit.
"""
from PyQt4 import QtCore
from PyQt4.QtGui import QFrame, QTableWidgetItem
from PyQt4.QtCore import pyqtSignature
import csv
from Ui_points import Ui_Frame


class PointsEdit(QFrame, Ui_Frame):
    """
    Class documentation goes here.
    """
    drive_msg  = QtCore.pyqtSignal(list)
    control_msg = QtCore.pyqtSignal(str)
    points_msg =  QtCore.pyqtSignal(list)

    def __init__(self, parent = None):
        """
        Constructor
        """
        QFrame.__init__(self, parent)
        self.setupUi(self)

        self.header = [ 'point' , 'time' , 'pos X' , 'pos Y' , 'pos Z', 'LancCmd' ]
        self._init_table()

        #last known positions
        self.posx = '0'
        self.posy = '0'
        self.posz = '0'
        #drive msg slot
        self.drive_msg.connect(self._driveupdate)


    def _driveupdate(self,msg):
        if msg[0] == 'W' or msg[0] == 'L':              #pos
            if msg[1]  == 'X': self.posx = msg[2]
            if msg[1]  == 'Y': self.posy = msg[2]
            if msg[1]  == 'Z': self.posz = msg[2]


    def _init_table(self):
        self.tableWidget_points.clear()     #clear table
        self.tableWidget_points.setRowCount(0)
        self.tableWidget_points.setColumnCount(len(self.header))
        self.tableWidget_points.setHorizontalHeaderLabels(self.header)
        self.tableWidget_points.setSortingEnabled(False)
        #self.tableWidget_points.resizeRowsToContents()


    def _renumber(self):
        for r in range(0,self.tableWidget_points.rowCount()):
            item = QTableWidgetItem(str(r + 1))
            self.tableWidget_points.setItem(r, 0, item)


    def loadfile(self, filename):
        try:
            with open(filename, 'rb') as file:
                csvread = csv.reader(file, delimiter='\t',
                                     quotechar='"',  quoting = csv.QUOTE_ALL)
                pointsdata = []
                for row in csvread:         #get data in
                    pointsdata.append(row)

                self._init_table()

                for row, rdata in enumerate(pointsdata):    #fill table with data
                    self.tableWidget_points.insertRow( self.tableWidget_points.rowCount())
                    for cell, data in enumerate(rdata):
                        self.tableWidget_points.setItem(row, cell, QTableWidgetItem(data))
                self._renumber()
                self.label_filename.setText(filename)
        except:
            pass

    def savefile(self,filename):
        try:
            with open(filename, 'wb') as file:
                csvwrite = csv.writer(file, delimiter='\t',
                                      quotechar='"',  quoting = csv.QUOTE_ALL)
                rows = []

                for r in range(0,self.tableWidget_points.rowCount()):
                    rows.append([])
                    for c in range(0,self.tableWidget_points.columnCount()):
                        item = self.tableWidget_points.item(r,c)
                        stri = str(item.data(0).toString())
                        rows[r].append(stri)

                for row in rows:
                    print row
                    csvwrite.writerow(row)

                self.label_filename.setText(filename)

        except:
            pass


    @pyqtSignature("")
    def on_pushButton_teachNew_released(self):
        """
        Slot documentation goes here.
        """
        lastrow = self.tableWidget_points.rowCount()
        self.tableWidget_points.insertRow(lastrow)
        self.tableWidget_points.setItem(lastrow, 0, QTableWidgetItem(str(lastrow + 1))) #point number
        self.tableWidget_points.setItem(lastrow, 1, QTableWidgetItem('0'))              # time
        self.tableWidget_points.setItem(lastrow, 2, QTableWidgetItem(self.posx))        #position x
        self.tableWidget_points.setItem(lastrow, 3, QTableWidgetItem(self.posy))        #position y
        self.tableWidget_points.setItem(lastrow, 4, QTableWidgetItem(self.posz))        #position z
        self.tableWidget_points.setItem(lastrow, 5, QTableWidgetItem('-1'))             #lanc command

    @pyqtSignature("")
    def on_pushButton_teachInsert_released(self):
        """
        Slot documentation goes here.
        """
        rowselected = self.tableWidget_points.currentRow()
        print rowselected
        self.tableWidget_points.insertRow(rowselected)
        self.tableWidget_points.setItem(rowselected, 1, QTableWidgetItem('0') )         #time
        self.tableWidget_points.setItem(rowselected, 2, QTableWidgetItem(self.posx))    #position x
        self.tableWidget_points.setItem(rowselected, 3, QTableWidgetItem(self.posy))    #position y
        self.tableWidget_points.setItem(rowselected, 4, QTableWidgetItem(self.posz))    #position z
        self.tableWidget_points.setItem(rowselected, 5, QTableWidgetItem('-1'))         #lanc command
        self._renumber()


    @pyqtSignature("")
    def on_pushButton_deleteRow_released(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget_points.currentRow()
        self.tableWidget_points.removeRow(row)
        self._renumber()


    @pyqtSignature("")
    def on_pushButton_moveTo_released(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget_points.currentRow()
        #item = self.tableWidget_points.item(row,2).data(0).toString()
        pos  = str(self.tableWidget_points.item(row,2).data(0).toString())
        #pos = str(item.data(0).toString())
        self.control_msg.emit( 'P X '+ pos +  ' ' + str(2000))
        item = self.tableWidget_points.item(row,3)
        pos = str(item.data(0).toString())
        self.control_msg.emit( 'P Y '+ pos +  ' ' + str(2000))
        item = self.tableWidget_points.item(row,4)
        pos = str(item.data(0).toString())
        self.control_msg.emit( 'P Z '+ pos +  ' ' + str(2000))


    @pyqtSignature("")
    def on_pushButton_testcycle_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


    @pyqtSignature("int, int")
    def on_tableWidget_points_cellChanged(self, row, column):
        """
        Slot documentation goes here.
        """
        rows = []

        for r in range(0,self.tableWidget_points.rowCount()):
            rows.append([])
            for c in range(0,self.tableWidget_points.columnCount()):
                item = self.tableWidget_points.item(r,c)
                if item is not None:
                    stri = str(item.data(0).toString())
                    rows[r].append(stri)
                else:
                    rows[r].append(None)

        if not None in rows:
            self.points_msg.emit(rows)

