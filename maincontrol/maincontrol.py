# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import pyqtSignal
from Ui_maincontrol import Ui_MainWindow
from comport.comframe import ComFrame
from controller.controlbuttons import ControlButtons
from eepromparams.eepromparams import eepromParams
from drives.drives import Drives
from points.points import PointsEdit
from lanccam.lanccam import LancCam
from sequencer.sequencer import Sequecer
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
        
        self.points = []        #this is the globally points list - no use!?
        
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

        #controller button class
        self.control = ControlButtons(self.frame_control_placeholder)
        self.control.control_msg.connect(self._sndToCom)

        #drives Button class
        self.drive = Drives(self.frame_drives_placeholder)
        self.drive.control_msg.connect(self._sndToCom)

        #drive EEPROM parameter
        self.eepromparams = eepromParams()
        self.eepromparams.SndParamsMsg.connect(self._sndToCom)
        self.eepromparams.ReqParamsMsg.connect(self._sndToCom)

        #point management
        self.pointedit = PointsEdit(self.frame_points_placeholder)
        self.pointedit.control_msg.connect(self._sndToCom)
        self.pointedit.points_msg.connect(self._pointsmsg)

        #sequencer
        self.Sequencer = Sequecer(self.frame_sequencer_placeholder)


        #lanc Camera
        self.cam = LancCam()
        self.cam.lancOut.connect(self._sndToCom)

        #auto load/open things
        if autoload == '1':self.pointedit.loadfile(autofile)
        if autoopen == '1':self.myport.opencomport(comport)


    def _pointsmsg(self,points):
        self.points = points
        self.Sequencer.points_msg.emit(points)


    def _sndToCom(self, msg):
        """Send parameters to micro"""
        self.myport.com.txmsg.emit(msg)

    
    def decodeData(self, data):
        #this modules get all data
        self.control.drive_msg.emit(data)
        self.pointedit.drive_msg.emit(data)
        self.drive.drive_msg.emit(data)
        #selected data
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

