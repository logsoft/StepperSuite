# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import pyqtSignal
from PyQt4 import QtCore, QtGui
from ui_maincontrol import Ui_MainWindow
from lancCam import lancCam
from comport.comframe import ComFrame
from controller.controlbuttons import ControlButtons
from eepromparams.eepromparams import eepromParams
from drives.drives import Drives
from points.points import PointsEdit
import logging
import ConfigParser
from appdirs import AppDirs

#path, file = os.path.split(os.path.realpath(__file__))

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.log = logging.getLogger('log.gui')

        dirs = AppDirs("StepperSuite", "logsoft")
        path = dirs.user_data_dir + '/'
        print path
        
        self.pakt = 0
        
        #config parser
        config = ConfigParser.ConfigParser()
        #print path
        config.read(path + 'app.cfg')
        autoload =config.get("app", "autoload")
        autofile = path + config.get("app", "file")
        autoopen = config.get('com',  'autoopen')
        comport = config.get('com',  'port')

        
        #serial comunication to arduino
        self.myport = ComFrame(self.frame_com_placeholder)
        self.myport.com.rxmsg.connect(self.decodeData)
#        self.myport.portstatus.connect(self._com_state)


        #controller button class
        self.control = ControlButtons(self.frame_control_placeholder)
        self.control.control_msg.connect(self._sndToCom)

        #drives Button class
        self.drive = Drives(self.frame_drives_placeholder)
        self.drive.control_msg.connect(self._sndToCom)

        #teach code
#        self.teacher = teach.TeachIn(self)

        #drive EEPROM parameter
        self.eepromparams = eepromParams()
        self.eepromparams.SndParamsMsg.connect(self._sndToCom)
        self.eepromparams.ReqParamsMsg.connect(self._sndToCom)

        #point management
        self.pointedit = PointsEdit(self.frame_points_placeholder)
        self.pointedit.control_msg.connect(self._sndToCom)


        #lanc Camera 
        self.cam = lancCam()
        #self.cam.lancIn.connect(self._lancOut)
        self.cam.lancOut.connect(self._sndToCom)
        
        #set UI elements unacceptable

        #auto load/open things
        if autoload == '1':self.pointedit.loadfile(autofile)

        if autoopen == '1':self.myport.opencomport(comport)


    def _sndToCom(self, msg):
        """Send parameters to micro"""
        self.myport.com.txmsg.emit(msg)
    
#    def _com_state(self,state):
#        if state == "open" : self._UI_access(1)
#        if state == "closed" : self._UI_access(0)

    def moveAxis(self, data): # data: p,  tptp, destx,  desty,  destz,  spx, spy
        self.myport.com.txmsg.emit( 'P X '+ str(data[2]) +  ' ' + str(data[5]))
        self.myport.com.txmsg.emit( 'P Y '+ str(data[3]) +  ' ' + str(data[6]))
        if (data[4] != '-1'):
            self.myport.com.txmsg.emit( 'LS '+ str(data[4]))
        self.log.debug('$moveAxis: point%s, t%s, X%s, Y%s,Z%s, SX%s,SY%s' %(str(data[0]) ,  str(data[1]) , str(data[2]),  str(data[3]),
                                                                                                                                str(data[4]) , str(data[5]) , str(data[6]) ))
        #QtGui.qApp.processEvents()
    
    
    def decodeData(self, data):
        self.control.drive_msg.emit(data)
        self.pointedit.drive_msg.emit(data)

        if data[0] == 'XG':
            self.eepromparams.RcvParamsMsg.emit((data[1], data[2]))

        if data[0] == 'ls':
            self.cam.lancIn.emit(data[1])
            

    @pyqtSignature("")
    def on_action_Load_triggered(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.csv',  "Teachdata (*.csv)")
        self.pointedit.loadfile(filename)


    @pyqtSignature("")
    def on_action_Save_triggered(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.csv',  "Teachdata (*.csv)")
        self.pointedit.savefile(filename)


    @pyqtSignature("")
    def on_action_Drive_Parameter_triggered(self):
        """
        Show the drive parameter window
        """
        self.eepromparams.show()
    
    @pyqtSignature("")
    def on_pushButton_lancControl_released(self):
        """Show the lancControl window"""
        self.cam.show()

