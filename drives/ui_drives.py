# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drives.ui'
#
# Created: Fri Jun 29 21:46:17 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(160, 230)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_drv = QtGui.QCheckBox(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_drv.sizePolicy().hasHeightForWidth())
        self.checkBox_drv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.checkBox_drv.setFont(font)
        self.checkBox_drv.setObjectName("checkBox_drv")
        self.verticalLayout.addWidget(self.checkBox_drv)
        self.line = QtGui.QFrame(Frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButton_refauto = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_refauto.setFont(font)
        self.pushButton_refauto.setObjectName("pushButton_refauto")
        self.verticalLayout.addWidget(self.pushButton_refauto)
        self.line_2 = QtGui.QFrame(Frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.pushButton_refY = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_refY.setFont(font)
        self.pushButton_refY.setObjectName("pushButton_refY")
        self.verticalLayout.addWidget(self.pushButton_refY)
        self.pushButton_refX = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_refX.setFont(font)
        self.pushButton_refX.setObjectName("pushButton_refX")
        self.verticalLayout.addWidget(self.pushButton_refX)
        self.pushButton_refZ = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_refZ.setFont(font)
        self.pushButton_refZ.setObjectName("pushButton_refZ")
        self.verticalLayout.addWidget(self.pushButton_refZ)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_drv.setText(QtGui.QApplication.translate("Frame", "Driver On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refauto.setText(QtGui.QApplication.translate("Frame", "auto reference", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refY.setText(QtGui.QApplication.translate("Frame", "ref Y to 0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refX.setText(QtGui.QApplication.translate("Frame", "ref X to 0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refZ.setText(QtGui.QApplication.translate("Frame", "ref Z to 0", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

