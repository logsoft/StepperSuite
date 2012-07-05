# -*- coding: utf-8 -*-

"""
Module implementing lancCam.
"""

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
from Ui_lanccam import Ui_Form
import time

class LancCam(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    lancIn = QtCore.pyqtSignal(str) # rcv params mesg from micro
    lancOut = QtCore.pyqtSignal(str) # snd mesg to micro
        
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.lancIn.connect(self._lancIn)
        self.ZoomSpeed = 1 #0 is nix
        
    def _lancIn(self, data):
        print data
    
    @pyqtSignature("")
    def on_pushButton_zoomIn_pressed(self):
        """
        ZOOM IN  on with speed
        """
        msg = 'LS Z I ' + str(self.ZoomSpeed) + ' 32000'
        self.lancOut.emit(msg)
    
    @pyqtSignature("")
    def on_pushButton_zoomIn_released(self):
        """
        ZOOM IN  off
        """
        self.lancOut.emit('LS Z I 0')
    
    @pyqtSignature("")
    def on_pushButton_zoomOut_pressed(self):
        """
        ZOOM OUT  on with speed and always 32767ms time 
        (will shut off by release button) 
        """
        msg = 'LS Z O ' + str(self.ZoomSpeed) + ' 32000'
        self.lancOut.emit(msg)
        
    @pyqtSignature("")
    def on_pushButton_zoomOut_released(self):
        """
        ZOOM OUT  off
        """
        self.lancOut.emit('LS Z O 0')

    @pyqtSignature("")
    def on_pushButton_focFar_pressed(self):
        """Focus far on"""
        self.lancOut.emit('LS F F 1') 
    
    @pyqtSignature("")
    def on_pushButton_focFar_released(self):
        """Focus far off"""
        self.lancOut.emit('LS F F 0')
    
    @pyqtSignature("")
    def on_pushButton_focNear_pressed(self):
        """Focus near on"""
        self.lancOut.emit('LS F N 1') 
    
    @pyqtSignature("")
    def on_pushButton_focNear_released(self):
        """Focus near off"""
        self.lancOut.emit('LS F N 0')
    
    @pyqtSignature("")
    def on_pushButton_focAuto_released(self):
        """Focus Auto"""
        self.lancOut.emit('LS F A')
    
   
    @pyqtSignature("int")
    def on_hSlider_zoomSpeed_valueChanged(self, value):
        """
        Zoom speed setting
        """
        self.ZoomSpeed = value
    
    @pyqtSignature("")
    def on_pushButton_reset_released(self):
        """
        Send reset signal
        """
        self.lancOut.emit('LS O')
        time.sleep(3)                          #assume after 20 sec we got pos
        self.lancOut.emit('LS N')               
        time.sleep(3)                          #assume after 20 sec we got pos
        self.lancOut.emit('LS F A')
        
    @pyqtSignature("")
    def on_pushButton_on_released(self):
        """
        Send ON signal
        """
        self.lancOut.emit('LS N')
    
    @pyqtSignature("")
    def on_pushButton_off_released(self):
        """
        Send OFF signal
        """
        self.lancOut.emit('LS O')
