# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comframe.ui'
#
# Created: Mon Jul  2 17:31:48 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frame(object):
    def setupUi(self, frame):
        frame.setObjectName("frame")
        frame.resize(160, 150)
        frame.setMinimumSize(QtCore.QSize(160, 150))
        frame.setMaximumSize(QtCore.QSize(250, 270))
        frame.setFrameShape(QtGui.QFrame.StyledPanel)
        frame.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(frame)
        self.label.setGeometry(QtCore.QRect(4, 4, 149, 20))
        self.label.setMinimumSize(QtCore.QSize(140, 20))
        self.label.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.pushButton_com_rescan = QtGui.QPushButton(frame)
        self.pushButton_com_rescan.setGeometry(QtCore.QRect(4, 87, 149, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(72)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_com_rescan.sizePolicy().hasHeightForWidth())
        self.pushButton_com_rescan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_com_rescan.setFont(font)
        self.pushButton_com_rescan.setObjectName("pushButton_com_rescan")
        self.comboBox_com_ports = QtGui.QComboBox(frame)
        self.comboBox_com_ports.setGeometry(QtCore.QRect(4, 27, 149, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_com_ports.sizePolicy().hasHeightForWidth())
        self.comboBox_com_ports.setSizePolicy(sizePolicy)
        self.comboBox_com_ports.setMinimumSize(QtCore.QSize(107, 0))
        self.comboBox_com_ports.setBaseSize(QtCore.QSize(9, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.comboBox_com_ports.setFont(font)
        self.comboBox_com_ports.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.comboBox_com_ports.setObjectName("comboBox_com_ports")
        self.pushButton_open = QtGui.QPushButton(frame)
        self.pushButton_open.setGeometry(QtCore.QRect(4, 117, 149, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(72)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")
        self.label_com_status = QtGui.QLabel(frame)
        self.label_com_status.setGeometry(QtCore.QRect(4, 57, 149, 19))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.label_com_status.setFont(font)
        self.label_com_status.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_com_status.setObjectName("label_com_status")

        self.retranslateUi(frame)
        QtCore.QMetaObject.connectSlotsByName(frame)

    def retranslateUi(self, frame):
        frame.setWindowTitle(QtGui.QApplication.translate("frame", "Comportframe", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frame", "COM Port Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_com_rescan.setText(QtGui.QApplication.translate("frame", "rescan list", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_com_rescan.setShortcut(QtGui.QApplication.translate("frame", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open.setText(QtGui.QApplication.translate("frame", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open.setShortcut(QtGui.QApplication.translate("frame", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.label_com_status.setText(QtGui.QApplication.translate("frame", "COM Status", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frame = QtGui.QFrame()
    ui = Ui_frame()
    ui.setupUi(frame)
    frame.show()
    sys.exit(app.exec_())

