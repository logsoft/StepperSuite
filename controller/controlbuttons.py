# -*- coding: utf-8 -*-

"""
Module implementing ControlButtons.
"""
from PyQt4 import QtCore

from PyQt4.QtGui import QFrame
from PyQt4.QtCore import pyqtSignature

from Ui_controlbuttons import Ui_Frame_controlbuttons

class ControlButtons(QFrame, Ui_Frame_controlbuttons):
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
        self.drive_msg.connect(self._driveupdate)
        self.pushButton_Xp.setEnabled(0) #0 off 1=on
        self.pushButton_Xn.setEnabled(0) #0 off 1=on
        self.pushButton_Yp.setEnabled(0) #0 off 1=on
        self.pushButton_Yn.setEnabled(0) #0 off 1=on
        self.pushButton_Zp.setEnabled(0) #0 off 1=on
        self.pushButton_Zn.setEnabled(0) #0 off 1=on


    def _driveupdate(self,msg):

        if msg[0] == 'W' or msg[0] == 'L':
        #            self.timing.axismsg.emit(data)
            if msg[1]  == 'X': self.label_X_p.setText (msg[2])
            if msg[1]  == 'Y': self.label_Y_p.setText (msg[2])
            if msg[1]  == 'Z': self.label_Z_p.setText (msg[2])

        if msg[0] == 'G':              #Speed
            if msg[1]  == 'X': self.label_X_s.setText (msg[2])
            if msg[1]  == 'Y': self.label_Y_s.setText (msg[2])

        if msg[0] == 'Q':              #State X sets all!
            d = 1
            if msg[2] == '1':d = 0      #TODO switch logic
            if msg[1]  == 'X':
                self.pushButton_Xp.setEnabled(d) #0 off 1=on
                self.pushButton_Xn.setEnabled(d) #0 off 1=on
                self.pushButton_Yp.setEnabled(d) #0 off 1=on
                self.pushButton_Yn.setEnabled(d) #0 off 1=on
                self.pushButton_Zp.setEnabled(d) #0 off 1=on
                self.pushButton_Zn.setEnabled(d) #0 off 1=on



    @pyqtSignature("")
    def on_pushButton_Yp_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit( 'M Y '+ str(self.spinBox_steps.value()) +  ' ' + str(self.spinBox_jog.value()))
    
    @pyqtSignature("")
    def on_pushButton_Xn_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit('M X '+ str(self.spinBox_steps.value()*-1) +  ' ' + str(self.spinBox_jog.value()))
    
    @pyqtSignature("")
    def on_pushButton_Yn_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit('M Y '+ str(self.spinBox_steps.value()*-1) +  ' ' + str(self.spinBox_jog.value()))

    @pyqtSignature("")
    def on_pushButton_Xp_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit('M X '+ str(self.spinBox_steps.value()) +  ' ' + str(self.spinBox_jog.value()))

    @pyqtSignature("")
    def on_pushButton_Zp_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit('M Z '+ str(self.spinBox_steps.value()) +  ' ' + str(self.spinBox_jog.value()))

    @pyqtSignature("")
    def on_pushButton_Zn_released(self):
        """
        Slot documentation goes here.
        """
        self.control_msg.emit('M Z '+ str(self.spinBox_steps.value()*-1) +  ' ' + str(self.spinBox_jog.value()))
