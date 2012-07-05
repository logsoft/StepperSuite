__author__ = 'hpl'

from PyQt4.QtCore import QTimer
import time

class QPauseTimer (QTimer):
    def __init__ (self, parent = None):
        QTimer.__init__ (self, parent)
        self.startTime = 0
        self.interval    = 0
        QTimer.setSingleShot(self,True)
        self.timeout.connect(self._timeend)


    def _timeend(self):
        self.startTime = 0

    def tstart (self, interval):
        if not self.startTime:
            self.interval    = interval
        self.startTime = time.time ()
        self.start (self.interval)
        print 'start', self.interval

    def tpause (self):
        if self.isActive ():
            self.stop ()
            elapsedTime    = time.time () - self.startTime
            print 'elapsed ', elapsedTime
            # time() returns float secs, interval is int msec
            self.interval -= int (elapsedTime*1000)
            print 'pause ' , self.interval

    def tstop(self):
            self.stop()
            self.startTime = 0
            print 'stop'


