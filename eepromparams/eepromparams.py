# -*- coding: utf-8 -*-

"""
Module implementing DriveParams.
"""

from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from ui_eepromparams import Ui_driveparams

import time

class eepromParams(QWidget, Ui_driveparams):
    """
    Class documentation goes here.
    """
    RcvParamsMsg = QtCore.pyqtSignal(tuple) # rcv params mesg from micro
    ReqParamsMsg = QtCore.pyqtSignal(str) # rcv params mesg from micro
    SndParamsMsg = QtCore.pyqtSignal(str) # snd params msg to micro

    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.RcvParamsMsg.connect(self._RcvParamsMsg)
        self.paramlist = [10, 11, 12, 13, 14, 15, 16, 110, 111, 112, 113,
                          114, 115, 116,  210, 211, 212, 213, 214, 215, 216]
        self.recieved = 0
        self._load()


    def _load(self):
        self.ReqParamsMsg.emit('XR 10')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 11')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 12')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 13')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 14')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 15')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 16')
        time.sleep(0.1)
        #Y
        self.ReqParamsMsg.emit('XR 110')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 111')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 112')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 113')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 114')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 115')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 116')
        time.sleep(0.1)
        #Z
        self.ReqParamsMsg.emit('XR 210')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 211')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 212')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 213')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 214')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 215')
        time.sleep(0.1)
        self.ReqParamsMsg.emit('XR 216')
        time.sleep(0.1)


    def _RcvParamsMsg(self, data):
        self.recieved = 1
        sw, dt = data
        #X axis params
        if sw == '10':
            self.doubleSpinBox_drv_para_X_accel.setValue(float(dt))
        if sw == '11':
            self.spinBox_drv_para_X_maxspeed.setValue(float(dt))
        if sw == '12':
            self.spinBox_drv_para_X_softend_pos.setValue(float(dt))
        if sw == '13':
            self.spinBox_drv_para_X_softend_neg.setValue(float(dt))
        if sw == '14':
            self.spinBox_drv_para_X_refpos.setValue(float(dt))
        if sw == '15':
            self.spinBox_drv_para_X_refspeed.setValue(float(dt))
        if sw == '16':
            self.spinBox_drv_para_X_poscor.setValue(float(dt))
            #Y axis params
        if sw == '110':
            self.doubleSpinBox_drv_para_Y_accel.setValue(float(dt))
        if sw == '111':
            self.spinBox_drv_para_Y_maxspeed.setValue(float(dt))
        if sw == '112':
            self.spinBox_drv_para_Y_softend_pos.setValue(float(dt))
        if sw == '113':
            self.spinBox_drv_para_Y_softend_neg.setValue(float(dt))
        if sw == '114':
            self.spinBox_drv_para_Y_refpos.setValue(float(dt))
        if sw == '115':
            self.spinBox_drv_para_Y_refspeed.setValue(float(dt))
        if sw == '116':
            self.spinBox_drv_para_Y_poscor.setValue(float(dt))
        #X axis params
        if sw == '210':
            self.doubleSpinBox_drv_para_Z_accel.setValue(float(dt))
        if sw == '211':
            self.spinBox_drv_para_Z_maxspeed.setValue(float(dt))
        if sw == '212':
            self.spinBox_drv_para_Z_softend_pos.setValue(float(dt))
        if sw == '213':
            self.spinBox_drv_para_Z_softend_neg.setValue(float(dt))
        if sw == '214':
            self.spinBox_drv_para_Z_refpos.setValue(float(dt))
        if sw == '215':
            self.spinBox_drv_para_Z_refspeed.setValue(float(dt))
        if sw == '216':
            self.spinBox_drv_para_Z_poscor.setValue(float(dt))


    def _save(self):
        #X
        self.SndParamsMsg.emit('XS 10 ' + str(self.doubleSpinBox_drv_para_X_accel.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 11 ' + str(self.spinBox_drv_para_X_maxspeed.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 12 ' + str(self.spinBox_drv_para_X_softend_pos.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 13 ' + str(self.spinBox_drv_para_X_softend_neg.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 14 ' + str(self.spinBox_drv_para_X_refpos.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 15 ' + str(self.spinBox_drv_para_X_refspeed.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 16 ' + str(self.spinBox_drv_para_X_poscor.value()) )
        time.sleep(0.1)
        #Y
        self.SndParamsMsg.emit('XS 110 ' + str(self.doubleSpinBox_drv_para_Y_accel.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 111 ' + str(self.spinBox_drv_para_Y_maxspeed.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 112 ' + str(self.spinBox_drv_para_Y_softend_pos.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 113 ' + str(self.spinBox_drv_para_Y_softend_neg.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 114 ' + str(self.spinBox_drv_para_Y_refpos.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 115 ' + str(self.spinBox_drv_para_Y_refspeed.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 116 ' + str(self.spinBox_drv_para_Y_poscor.value()) )
        time.sleep(0.1)
        #Z
        self.SndParamsMsg.emit('XS 210 ' + str(self.doubleSpinBox_drv_para_Z_accel.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 211 ' + str(self.spinBox_drv_para_Z_maxspeed.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 212 ' + str(self.spinBox_drv_para_Z_softend_pos.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 213 ' + str(self.spinBox_drv_para_Z_softend_neg.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 214 ' + str(self.spinBox_drv_para_Z_refpos.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 215 ' + str(self.spinBox_drv_para_Z_refspeed.value()) )
        time.sleep(0.1)
        self.SndParamsMsg.emit('XS 216 ' + str(self.spinBox_drv_para_Z_poscor.value()) )
        time.sleep(0.1)


    @pyqtSignature("")
    def on_pushButton_saveparam_released(self):
        """
        send parameters to micro eeprom
        with sanity check
        """
        quit_msg = "are you sane?"
        reply = QtGui.QMessageBox.question(self, 'write?',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.pushButton_saveparam.setText('Saving!')
            self._save()
            self.pushButton_saveparam.setText('&Save to Controller')
        else:
            pass


    @pyqtSignature("")
    def on_pushButton_loadparam_released(self):
        """
        load params to gui
        """
        self._load()
