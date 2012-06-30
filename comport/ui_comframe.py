# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comframe.ui'
#
# Created: Thu Jun 28 22:39:20 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(160, 150)
        Frame.setMinimumSize(QtCore.QSize(160, 150))
        Frame.setMaximumSize(QtCore.QSize(250, 270))
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        Frame.setFrameShape(QtGui.QFrame.NoFrame)
        Frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(4, 4, 149, 20))
        self.label.setMinimumSize(QtCore.QSize(140, 20))
        self.label.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Frame", "COM Port Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_com_rescan = QtGui.QPushButton(Frame)
        self.pushButton_com_rescan.setGeometry(QtCore.QRect(4, 87, 149, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(72)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_com_rescan.sizePolicy().hasHeightForWidth())
        self.pushButton_com_rescan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(10)
        self.pushButton_com_rescan.setFont(font)
        self.pushButton_com_rescan.setText(QtGui.QApplication.translate("Frame", "rescan list", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_com_rescan.setShortcut(QtGui.QApplication.translate("Frame", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_com_rescan.setObjectName(_fromUtf8("pushButton_com_rescan"))
        self.comboBox_com_ports = QtGui.QComboBox(Frame)
        self.comboBox_com_ports.setGeometry(QtCore.QRect(4, 27, 149, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_com_ports.sizePolicy().hasHeightForWidth())
        self.comboBox_com_ports.setSizePolicy(sizePolicy)
        self.comboBox_com_ports.setMinimumSize(QtCore.QSize(107, 0))
        self.comboBox_com_ports.setBaseSize(QtCore.QSize(9, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(10)
        self.comboBox_com_ports.setFont(font)
        self.comboBox_com_ports.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.comboBox_com_ports.setObjectName(_fromUtf8("comboBox_com_ports"))
        self.pushButton_open = QtGui.QPushButton(Frame)
        self.pushButton_open.setGeometry(QtCore.QRect(4, 117, 149, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(72)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(10)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setText(QtGui.QApplication.translate("Frame", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open.setShortcut(QtGui.QApplication.translate("Frame", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open.setObjectName(_fromUtf8("pushButton_open"))
        self.label_com_status = QtGui.QLabel(Frame)
        self.label_com_status.setGeometry(QtCore.QRect(4, 57, 149, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(10)
        self.label_com_status.setFont(font)
        self.label_com_status.setText(QtGui.QApplication.translate("Frame", "COM Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_com_status.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_com_status.setObjectName(_fromUtf8("label_com_status"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

