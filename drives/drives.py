# -*- coding: utf-8 -*-

"""
Module implementing Drives.
"""
from PyQt4 import QtCore
from PyQt4.QtGui import QFrame
from PyQt4.QtCore import pyqtSignature
from ui_drives import Ui_Frame
import logging
import time

class Drives(QFrame, Ui_Frame):
    """
    Class documentation goes here.
    """
    control_msg = QtCore.pyqtSignal(str)
    drive_msg  = QtCore.pyqtSignal(list)

    def __init__(self, parent = None):
        """
        Constructor
        """
        QFrame.__init__(self, parent)
        self.setupUi(self)
        self.log = logging.getLogger('drives')
        self.drive_msg.connect(self._driveupdate)

    def _driveupdate(self,msg):

        if msg[0] == 'Q':              #State X sets all!
            d = 1
            if msg[2] == '1':d = 0      #TODO switch logic
            if msg[1]  == 'X':
                self.checkBox_drv.setCheckState(d)
                self.pushButton_refauto.setEnabled(d) #0 off 1=on
                self.pushButton_refX.setEnabled(d) #0 off 1=on
                self.pushButton_refY.setEnabled(d) #0 off 1=on
                self.pushButton_refZ.setEnabled(d) #0 off 1=on


    @pyqtSignature("int")
    def on_checkBox_drv_stateChanged(self, p0):
        """
        Slot documentation goes here.
        """
        d=0
        if p0==0:d = 1
        self.control_msg.emit( 'S X '+ str(d) )
        self.control_msg.emit( 'S Y '+ str(d) )
        self.control_msg.emit( 'S Z '+ str(d) )
        self.log.info('Driver state set to: %s' %str(d) )

    @pyqtSignature("")
    def on_pushButton_refauto_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit( 'M X 200 500') #reference automatik
        self.control_msg.emit( 'M Y -200 500') #reference automatik
        time.sleep(1.0)
        self.control_msg.emit( 'R A') #reference automatik
        self.control_msg.emit( 'LS Z O 8 5000')
    
    @pyqtSignature("")
    def on_pushButton_refY_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit( 'R Y 0' )
    
    @pyqtSignature("")
    def on_pushButton_refX_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit( 'R X 0' )
    
    @pyqtSignature("")
    def on_pushButton_refZ_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit( 'R Z 0' )
