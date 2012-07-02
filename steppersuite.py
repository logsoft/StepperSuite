# -*- coding: utf-8 -*-

import sys
# Import Qt modules
from PyQt4 import QtCore,QtGui
# Import the compiled UI module
from ui.maincontrol import MainWindow

import logging.config

from appdirs import AppDirs
dirs = AppDirs("StepperSuite", "logsoft")
path = dirs.user_data_dir


#print "script: sys.argv[0] is", repr(sys.argv[0])
#print "script: __file__ is", repr(__file__)
#print "script: cwd is", repr(os.getcwd())

logging.config.fileConfig(path + '/log.cfg')


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
