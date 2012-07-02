# -*- coding: utf-8 -*-

"""
Module implementing ComFrame.
"""
from PyQt4 import QtCore
from PyQt4.QtGui import QFrame
from PyQt4.QtCore import pyqtSignature
from ui_comframe import Ui_frame

import comthread

class ComFrame(QFrame, Ui_frame):
    """
    Class documentation goes here.
    """

    portstatus = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        """
        Constructor
        """
        QFrame.__init__(self, parent)
        self.setupUi(self)

        #get the ports
        self.ports = comthread.scanports()
        self.comboBox_com_ports.addItems(self.ports)

        #get a com port
        self.com = comthread.ComThread(self)
        #self.com.serial_arg['port'] = comport
        self.com.serial_arg['baudrate'] = 57600

    @pyqtSignature("")
    def on_pushButton_com_rescan_released(self):
        """
        Slot documentation goes here.
        """
        self.ports = comthread.scanports()
        self.comboBox_com_ports.clear()
        self.comboBox_com_ports.addItems(self.ports)

    
    @pyqtSignature("")
    def on_pushButton_open_released(self):
        """
        Slot documentation goes here.
        """
        self.opencomport(str(self.comboBox_com_ports.currentText()))


    def opencomport(self, port):

        if not  self.com.isOpen():
            self.com.serial_arg['port'] = port
            self.com.serial_arg['baudrate'] = 57600
            self.com.open()
            if self.com.isOpen():
                self.pushButton_open.setText('Close')
                self.comboBox_com_ports.setEnabled(False)
                self.portstatus.emit("open")
                self.label_com_status.setText("OPEN")
        else:
            if self.com.isOpen():
                self.com.close()
                self.pushButton_open.setText('Open')
                self.comboBox_com_ports.setEnabled(True)
                self.portstatus.emit("closed")
                self.label_com_status.setText("CLOSED")
