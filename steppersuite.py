# -*- coding: utf-8 -*-

import os,sys
# Import Qt modules
from PyQt4 import QtCore,QtGui
# Import the compiled UI module
from ui.maincontrol import MainWindow

import logging.config

from appdirs import AppDirs
dirs = AppDirs("RaceGui", "somedude")

#print "script: sys.argv[0] is", repr(sys.argv[0])
#print "script: __file__ is", repr(__file__)
#print "script: cwd is", repr(os.getcwd())

from appdirs import AppDirs
dirs = AppDirs("racegui", "Acme")
path = dirs.user_data_dir

logging.config.fileConfig(path + '/log.cfg')
#print (path)

def main():
    # Again, this is boilerplate, it's going to be the same on
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    ui=MainWindow()
    ui.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":
    pass
    main()



#TODO?: Meldung x steps vor ziel = nächstes ziel in queue schieben?
#TODO?: achsen fahren nicht synchron unter ? bedingung - wirklich? beobachten!
#TODO?: USB autoreconnect? refresh usb list
#TODO?: referenzwertverschiebungen - notwendig??

#TODOok: micro verschluckt commando!! - handshake!
#TODOok: bei  refenenzfahrt vorher freifahren 
#TODOok: Software endschalter
#TODOok: cmd message rennphase auf gui ausgeben
#punkt verifizierung in timing entfernt
#TODOok: zoom mehr zurück als aus - testen ob ok
#TODOok: standalone start
#TODOok: udp port ini
#TODOok: log per ini ein/aus
#TODOok: Gehäuse
#TODOok: setupwerte in eeprom speichern
#TODOok: start/stop signale von udp implementieren
#TODOok: start/stop: bei stop ref und startpos, bei start automode
