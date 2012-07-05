# -*- coding: utf-8 -*-

"""
Module implementing Sequecer.
"""
from PyQt4 import QtCore
from PyQt4.QtGui import QFrame
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QObject
from QPauseTimer import QPauseTimer
import time

from Ui_sequencer import Ui_Frame

class Sequecer(QFrame, Ui_Frame):
    """
    Class documentation goes here.
    """

    points_msg =  QtCore.pyqtSignal(list)
    drive_msg  =  QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        """
        Constructor
        """
        QFrame.__init__(self, parent)
        self.setupUi(self)

        self.points =[]
        self.point_prev = 0
        self.point_next = 0
        self.point_drv = 0

        self.points_msg.connect(self._pointsmsg)

        self.interval = 0
        self.timer = QPauseTimer(self)
        self.timer.timeout.connect(self._timeout)

        self.displayrefresh = QTimer(self)
        self.displayrefresh.start(100)      #100ms refresh rate of display
        self.displayrefresh.timeout.connect(self._refresh)

        self.spinBox_goto.setValue(1)
        self.spinBox_goto.setMinimum(1)
        self.spinBox_loop_from.setMinimum(1)
        self.spinBox_loop_times.setMinimum(1)
        self.spinBox_loop_to.setMinimum(1)
        self.spinBox_point_first.setMinimum(1)
        self.spinBox_point_last.setMinimum(1)

    def _pointsmsg(self,points):
        self.points = points
        self.spinBox_goto.setMaximum(len(self.points))
        self.spinBox_loop_from.setMaximum(len(self.points))
        self.spinBox_loop_to.setMaximum(len(self.points))
        self.spinBox_point_first.setMaximum(len(self.points))
        self.spinBox_point_last.setMaximum(len(self.points))

    def _refresh(self):
        if self.timer.isActive():
            togo = int((time.time() - self.timer.startTime)*1000)
            self.label_time_akt.setText(str(togo))
            self.label_time_next.setText(str(self.timer.interval))
        if not self.timer.isActive() and not self.timer.ispaused:
            self.label_time_akt.setText('0')
            self.label_time_next.setText('0')


    def _timeout(self):
        #self.pushButton_start.setChecked(0)
        print 'timeout'
        print 'end@ ', self._endat()
        print 'loopfrom  ', self._loopfrom()
        print 'loopto  ', self._loopto()
        self.label_pos_akt.setText(str(self.point_next))

        if (self.point_next == self._endat()
            and not self.checkBox_loop_do.isChecked()):
            self._stop()
        elif (self.point_next >= self._loopfrom()
              and self.checkBox_loop_do.isChecked()):
            self.point_next = self._loopto()
        else: self.point_next = self._countup()


        if self.point_next != self.point_prev:
            self.point_prev = self.point_next
            self.interval = int(self.points[self.point_next - 1][1])
            self.timer.tstart(self.interval)
            self.label_pos_next.setText(str(self.point_next))
            self._sendDriveToPoint(self.point_next)


    def _getPointData(self,point):
        time = self.points[point - 1][1]
        posx = self.points[point - 1][2]
        posy = self.points[point - 1][3]
        posz = self.points[point - 1][4]
        lanc = self.points[point - 1][5]
        return time,posx,posy,posz,lanc


    def _sendDriveToPoint(self, point):
        time,posx,posy,posz,lanc = self._getPointData(point)
        self.drive_msg.emit( 'P X '+ posx +  ' ' + str(2000))
        self.drive_msg.emit( 'P Y '+ posy +  ' ' + str(2000))
        self.drive_msg.emit( 'P Z '+ posz +  ' ' + str(2000))
        # TODO: lanc , speed
        self.label_pos_next.setText(str(self.point_next))


    def _startfrom(self):
        if self.checkBox_point_first.isChecked(): return 1
        else: return self.spinBox_point_first.value()


    def _endat(self):
        if self.checkBox_point_last.isChecked(): return len(self.points)
        else: return self.spinBox_point_last.value()


    def _loopfrom(self):
        if self.checkBox_loop_fromlast.isChecked(): return len(self.points)
        else: return self.spinBox_loop_from.value()


    def _loopto(self):
        if self.checkBox_loop_tofirst.isChecked(): return 1
        else: return self.spinBox_loop_to.value()

    def _countup(self):
        if self.point_next + 1 <= len(self.points):
            return  self.point_next + 1
        else: self._stop()

    def _gettime(self,point):
        return int(self.points[self.point_next - 1][1])


    def _stop(self):
        self.timer.tstop()
        self.pushButton_start.setChecked(0)
        self.pushButton_pause.setChecked(0)
        self.label_pos_next.setText('0')

    @pyqtSignature("bool")
    def on_pushButton_start_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        if checked:
            if not self.timer.ispaused:
                self.point_next = self._startfrom()
                self.interval = self._gettime(self.point_next)
            self.timer.tstart(self.interval)

        if not checked:
            if self.timer.isActive():
                self.timer.tpause()



    @pyqtSignature("")
    def on_pushButton_pause_toggled(self,checked):
        """
        Slot documentation goes here.
        """
        if checked:
            self.timer.tpause()
            self.pushButton_start.setChecked(0)
        else:
            if self.timer.ispaused:
                self.pushButton_start.setChecked(1)

    @pyqtSignature("")
    def on_pushButton_stop_released(self):
        """
        Slot documentation goes here.
        """
        self._stop()

    @pyqtSignature("")
    def on_pushButton_goto_released(self):
        """
        Slot documentation goes here.
        """
        self.point_next = self.spinBox_goto.value()
        self._sendDriveToPoint(self.point_next)
        self.label_pos_akt.setText(str(self.point_next))
        self.label_pos_next.setText(str(self.point_next))


    @pyqtSignature("bool")
    def on_radioButton_t1_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("bool")
    def on_radioButton_t2_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("bool")
    def on_radioButton_s1_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("bool")
    def on_radioButton_S2_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("bool")
    def on_radioButton_S3_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("int")
    def on_checkBox_loop_do_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    


        #        self.pushButton_start.setStyleSheet(" background-color: lime;"
        #                                            " border-width: 1px;"
        #                                            "border-style: solid;"
        #                                            " border-radius: 4px; " )