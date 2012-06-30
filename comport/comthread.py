# -*- coding: utf-8 -*-

#comport
#providing serial interface to arduino via queue

#changelog:
#22.09.2011 - check recieved messages 4 CR (completenes) throw away if incomplete
#26.06.2012 - changed to own package

import serial
import glob
import os
import logging
import crcmod.predefined
import struct
import collections
import datetime
from PyQt4 import QtCore

def _scan():
    """scan for available ports. return a list of device names."""
    ports = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            ports.append(s.portstr)
            s.close()   # explicit close
        except serial.SerialException:
            pass
    return ports
    
def _scanposix():
    """scan for available ports. return a list of device names."""
    ports = []
    ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') # + glob.glob('/dev/ttyS*')
    return ports

def scanports():
    if os.name == 'posix':
        ports = _scanposix()
        return ports
    else:
        ports = _scan()
        return ports

class ComThread(QtCore.QThread):
    rxmsg = QtCore.pyqtSignal(list)
    txmsg = QtCore.pyqtSignal(QtCore.QString)
    safeTx = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(ComThread, self).__init__(parent)
        self.log = logging.getLogger('log.com')
        self.txmsg.connect(self.sendsafe)
        self.safeTx.connect(self.sendsafe)
        self.sendlist = collections.deque()
        self.crc16_func = crcmod.predefined.mkCrcFun('modbus')
        self.waitack = 0
        self.sendtime = 0
        
        self.exiting = False
        
        self.port = serial.Serial()
        self.serial_arg = dict( port= None,
                                baudrate=57600,
                                stopbits=serial.STOPBITS_ONE,
                                parity=serial.PARITY_NONE,
                                timeout=0.01)
        
    def __del__(self):   
        self.port.close()
        self.exiting = True
        self.exit()
        
    def send(self, txdata):
        if self.port.isOpen(): 
            self.port.write(str(txdata))
            self.log.debug('serial send: %s '%(txdata[:-1]))
        else:
            self.log.warning('no serial port to send this: %s'%(txdata[:-1]))

    def sendsafew(self, txdata):
        tx = txdata[:-1]
        self.sendsafe(tx)
        
    def sendsafe(self, txdata):
        if self.port.isOpen(): 
            #crc16_func = crcmod.predefined.mkCrcFun('modbus')
            
            s = ''
            s+=struct.pack('b',len(txdata)) 
            s+=str(txdata)
            s += '' + struct.pack('>H',self.crc16_func(s))
            s+='\r'
            
            #self.port.write(s)
            self.sendlist.append(s)
            self.log.debug('ser snd tolist: %r '%(s))
        else:
            self.log.warning('no serial port to send this: %r'%(txdata[:-1]))

    def open(self):
        try:
            if self.port: 
                self.port.close()
            self.port = serial.Serial(**self.serial_arg)
            self.log.info('serial opened:%s, %sBaud'%(self.serial_arg['port'] , self.serial_arg['baudrate']))
            self.start()
            self.exiting = False
        except serial.SerialException, e:
            self.log.warning('serial open error:%s'%(self.serial_arg['port'] ), e.message)

    def close(self):
        self.exiting = True
        self.exit(0)
        self.port.close()
        self.log.info('serial closed:%s'%(self.serial_arg['port'] ))

        
    def isOpen(self):
        return self.port.isOpen()
        
    def run(self):
        
        while not self.exiting:                
            if self.port.isOpen():
                #rx
                rxdata = self.port.readline()
                if '\n' in rxdata:   #check 4 complete message by chk 4 newline char
                    rxspl = rxdata.split()
                    
                    if len(rxspl) == 1:
                        if rxspl[0].isdigit() : v = int(rxspl[0][0])
                        else: v = 0
                             
                        if v == 0x06 :
                            self.log.debug('ser rcv ACK')
                            if len(self.sendlist) > 0 :self.sendlist.popleft() #remove message from sendlist
                            self.waitack = 0            #next
                            
                        if v == 0x15 :
                            self.log.debug('ser rcv NAK')
                            self.waitack = 0    #resend
                            
                    if len(rxspl) > 1:
                        #self.log.debug('serrcv raw: %s '%(rxdata))
                        
                            self.log.debug('serial rcv: %s '%(''.join(rxdata[:-2])))
                            #send to decode  if 1st char is uppercase and has CR
                                                   
                            if rxspl[0].isupper:
                                self.rxmsg.emit( rxspl)
                #tx
                if (self.waitack == 0):
                    if ( len(self.sendlist) > 0) :
                        s = self.sendlist[0]
                        x = len(s)
                        #if random.random() > 0.5 : s = s[:-4] +'V' + s[-3:]    #test micro crc check 
                        self.port.write(s)
                        self.log.debug('ser snd toPort: %r '%(s))
                        self.waitack = 1
                        self.sendtime = datetime.datetime.now()
                if self.waitack:
                    self.now = datetime.datetime.now()
                    if (self.now - self.sendtime).seconds> 2:
                        self.waitack = 0
                        self.log.debug('ser snd reset timeout')
                        if len(self.sendlist) > 0 :self.sendlist.popleft() #remove message from sendlist
                    
                        
            else:
                self.log.warning('serial error:%s, %sBaud'%(self.serial_arg['port'] , self.serial_arg['baudrate']))
