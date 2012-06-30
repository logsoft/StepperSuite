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
import csv
import ConfigParser
import  time

#import com,  timing,  udprcv,  teach
#from app import com, timing,  udprcv,  teach

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
        
        dirs = AppDirs("racegui", "Acme")
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
        #comport = config.get('com',  'port')

        
        #serial comunication to arduino
        self.myport = ComFrame(self.frame_com_placeholder)
        self.myport.com.rxmsg.connect(self.decodeData)
        self.myport.portstatus.connect(self._com_state)


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


        #lanc Camera 
        self.cam = lancCam()
        #self.cam.lancIn.connect(self._lancOut)
        self.cam.lancOut.connect(self._sndToCom)
        
        #set UI elements unacceptable

        #auto load/open things
#        if autoload == '1':self._loaddat(autofile)
#        if autoopen == '1':self._opencom()


    def _sndToCom(self, msg):
        """Send parameters to micro"""
        self.myport.com.txmsg.emit(msg)
    
    def _loaddat(self, filename):
        try:
            with open(filename, 'rb') as file:
                csvread = csv.reader(file, delimiter='\t',
                                quotechar='"',  quoting = csv.QUOTE_ALL)
                self.teacher.teachpoints = []
                for row in csvread:
                    self.teacher.teachpoints.append(row)
                self.update_Teachline()
                self.label_filename.setText(filename)
        except:
            pass

    def _com_state(self,state):
        if state == "open" : self._UI_access(1)
        if state == "closed" : self._UI_access(0)

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

        if data[0] == 'XG':
            self.eepromparams.RcvParamsMsg.emit((data[1], data[2]))

        if data[0] == 'ls':
            self.cam.lancIn.emit(data[1])
            

    def update_Teachline(self):
        if self.spinBox_teachPoint.value() <=  len(self.teacher.teachpoints)-1:
            pd = self.teacher.GetPoint(self.spinBox_teachPoint.value()) #(p , t , tf, x , y , z )
            self.spinBox_teach_time.setValue(int(pd[1]))
            self.lineEdit_teach_tfact.setText(pd[2])
            self.lineEdit_teach_x.setText(str(pd[3]))
            self.lineEdit_teach_y.setText(str(pd[4]))
            self.lineEdit_teach_z.setText(str(pd[5]))
        else:
            self.spinBox_teach_time.setValue(-1)
            self.lineEdit_teach_tfact.setText('-1')
            self.lineEdit_teach_x.setText('none')
            self.lineEdit_teach_y.setText('none')
            self.lineEdit_teach_z.setText('none')
        

    @pyqtSignature("int")
    def on_checkBox_drv_stateChanged(self, p0):
        d=0
        if p0==0:d = 1
        self.myport.com.txmsg.emit( 'S X '+ str(d))
        self.myport.com.txmsg.emit( 'S Y '+ str(d))
        self.log.info('Driver state set to: %s' %str(d) )

    @pyqtSignature("")
    def on_pushButton_teachMove_released(self):
        pd = self.teacher.GetPoint(int(self.spinBox_teachPoint.text()))
        self.myport.com.txmsg.emit( 'P X '+ pd[3] +  ' ' + str(2000))
        self.myport.com.txmsg.emit( 'P Y '+ pd[4] +  ' ' + str(2000))
        self.myport.com.txmsg.emit( 'LS '+ pd[5] )
        
    @pyqtSignature("")
    def on_pushButton_teachIn_released(self):
        #p = str(self.spinBox_teachPoint.text())
        p = len(self.teacher.teachpoints) 
        t = str(self.spinBox_teach_time.text())
        tf = str(self.lineEdit_teach_tfact.text())
        self.lineEdit_teach_x.setText(self.label_X_p.text())
        self.lineEdit_teach_y.setText(str(self.label_Y_p.text()))
#        self.lineEdit_teach_z.setText(str(self.label_Z_pos.text()))
        x = str(self.label_X_p.text())
        y= str(self.label_Y_p.text())
        #z= str(self.label_Z_pos.text())
        z = self.lineEdit_teach_z.text()   
        
        data = [p , t , tf , x , y , z ]
        #print data
        self.teacher.Teach(data)
        i = int(self.spinBox_teachPoint.text()) +1
        self.spinBox_teachPoint.setValue(p)
    
    @pyqtSignature("")
    def on_pushButton_tc_released(self):
        self.pakt
        pd = self.teacher.GetPoint(self.pakt)
        self.pakt += 1
        if self.pakt > len(self.teacher.teachpoints)-1: self.pakt = 0
        pi = int(self.spinBox_teachPoint.text())
        self.myport.com.txmsg.emit( 'P X '+ pd[3] +  ' ' + str(2000))
        self.myport.com.txmsg.emit( 'P Y '+ pd[4] +  ' ' + str(2000))
        self.myport.com.txmsg.emit( 'LS '+ pd[5] )
    
    @pyqtSignature("")
    def on_action_Load_triggered(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.csv',  "Teachdata (*.csv)")
        print filename
        #self._loaddat(filename)
        self.pointedit.loaddata(filename)


    @pyqtSignature("")
    def on_action_Save_triggered(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.csv',  "Teachdata (*.csv)")
        try:
            with open(filename, 'wb') as file:
                csvwrite = csv.writer(file, delimiter='\t',
                                quotechar='"',  quoting = csv.QUOTE_ALL)
                for row in self.teacher.teachpoints:
                    print row
                    csvwrite.writerow(row)
        except:
            pass
            
    @pyqtSignature("")
    def on_spinBox_teachPoint_editingFinished(self):
        self.update_Teachline()
    
    @pyqtSignature("int")
    def on_spinBox_teachPoint_valueChanged(self, p0):
        self.update_Teachline()
    
    @pyqtSignature("")
    def on_pushButton_teachInsert_released(self):
        p = str(self.spinBox_teachPoint.text())
        t = str(self.spinBox_teach_time.text())
        tf = str(self.lineEdit_teach_tfact.text())
        self.lineEdit_teach_x.setText(self.label_X_p.text())
        self.lineEdit_teach_y.setText(str(self.label_Y_p.text()))
        x = str(self.label_X_p.text())
        y= str(self.label_Y_p.text())
        #z= str(self.label_Z_pos.text())
        z = self.lineEdit_teach_z.text()
        print z
        data = [p , t , tf,   x , y , z ]
        self.teacher.insTeach(data)
        self.update_Teachline()

    @pyqtSignature("")
    def on_pushButton_teachDelete_released(self):
        self.teacher.delTeach(self.spinBox_teachPoint.text())
        self.update_Teachline()
    
    @pyqtSignature("")
    def on_pushButton_teachEdit_released(self):
        p = str(self.spinBox_teachPoint.text())
        t = str(self.spinBox_teach_time.text())
        tf = str(self.lineEdit_teach_tfact.text())
        x = self.lineEdit_teach_x.text()
        y = self.lineEdit_teach_y.text()
        z =self.lineEdit_teach_z.text()
        data = [p , t , tf,   x , y , z ]
        self.teacher.editTeach(data)
        self.update_Teachline()
    

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

