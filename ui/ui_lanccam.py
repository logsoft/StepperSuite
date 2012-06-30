# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lanccam.ui'
#
# Created: Thu Jun 28 20:51:37 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(339, 221)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "lanc remote", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_zoomIn = QtGui.QPushButton(Form)
        self.pushButton_zoomIn.setGeometry(QtCore.QRect(0, 20, 91, 41))
        self.pushButton_zoomIn.setText(QtGui.QApplication.translate("Form", "ZOOM &IN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_zoomIn.setObjectName(_fromUtf8("pushButton_zoomIn"))
        self.pushButton_zoomOut = QtGui.QPushButton(Form)
        self.pushButton_zoomOut.setGeometry(QtCore.QRect(0, 70, 90, 41))
        self.pushButton_zoomOut.setText(QtGui.QApplication.translate("Form", "ZOOM &OUT", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_zoomOut.setObjectName(_fromUtf8("pushButton_zoomOut"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 180, 121, 36))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_statusName = QtGui.QLabel(self.layoutWidget)
        self.label_statusName.setEnabled(False)
        self.label_statusName.setText(QtGui.QApplication.translate("Form", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_statusName.setObjectName(_fromUtf8("label_statusName"))
        self.verticalLayout.addWidget(self.label_statusName)
        self.label_statusData = QtGui.QLabel(self.layoutWidget)
        self.label_statusData.setEnabled(False)
        self.label_statusData.setText(QtGui.QApplication.translate("Form", "data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_statusData.setObjectName(_fromUtf8("label_statusData"))
        self.verticalLayout.addWidget(self.label_statusData)
        self.pushButton_focFar = QtGui.QPushButton(Form)
        self.pushButton_focFar.setGeometry(QtCore.QRect(240, 10, 91, 41))
        self.pushButton_focFar.setText(QtGui.QApplication.translate("Form", "FOCUS &FAR", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_focFar.setObjectName(_fromUtf8("pushButton_focFar"))
        self.pushButton_focNear = QtGui.QPushButton(Form)
        self.pushButton_focNear.setGeometry(QtCore.QRect(240, 60, 90, 41))
        self.pushButton_focNear.setText(QtGui.QApplication.translate("Form", "FOCUS &NEAR", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_focNear.setObjectName(_fromUtf8("pushButton_focNear"))
        self.pushButton_focAuto = QtGui.QPushButton(Form)
        self.pushButton_focAuto.setGeometry(QtCore.QRect(240, 110, 90, 41))
        self.pushButton_focAuto.setText(QtGui.QApplication.translate("Form", "FOCUS &AUTO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_focAuto.setObjectName(_fromUtf8("pushButton_focAuto"))
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 20, 131, 75))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_zoomSpeed = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_zoomSpeed.setFont(font)
        self.label_zoomSpeed.setText(QtGui.QApplication.translate("Form", "ZOOM Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_zoomSpeed.setTextFormat(QtCore.Qt.PlainText)
        self.label_zoomSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_zoomSpeed.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_zoomSpeed.setObjectName(_fromUtf8("label_zoomSpeed"))
        self.verticalLayout_2.addWidget(self.label_zoomSpeed)
        self.hSlider_zoomSpeed = QtGui.QSlider(self.layoutWidget1)
        self.hSlider_zoomSpeed.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.hSlider_zoomSpeed.setMinimum(1)
        self.hSlider_zoomSpeed.setMaximum(8)
        self.hSlider_zoomSpeed.setPageStep(1)
        self.hSlider_zoomSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider_zoomSpeed.setTickPosition(QtGui.QSlider.TicksAbove)
        self.hSlider_zoomSpeed.setTickInterval(1)
        self.hSlider_zoomSpeed.setObjectName(_fromUtf8("hSlider_zoomSpeed"))
        self.verticalLayout_2.addWidget(self.hSlider_zoomSpeed)
        self.label_zoomSpeed_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_zoomSpeed_2.setFont(font)
        self.label_zoomSpeed_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_zoomSpeed_2.setMouseTracking(True)
        self.label_zoomSpeed_2.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_zoomSpeed_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_zoomSpeed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_zoomSpeed_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_zoomSpeed_2.setObjectName(_fromUtf8("label_zoomSpeed_2"))
        self.verticalLayout_2.addWidget(self.label_zoomSpeed_2)
        self.pushButton_reset = QtGui.QPushButton(Form)
        self.pushButton_reset.setGeometry(QtCore.QRect(290, 160, 41, 41))
        self.pushButton_reset.setText(QtGui.QApplication.translate("Form", "&RESET", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.pushButton_on = QtGui.QPushButton(Form)
        self.pushButton_on.setGeometry(QtCore.QRect(190, 160, 41, 41))
        self.pushButton_on.setText(QtGui.QApplication.translate("Form", "O&N", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_on.setObjectName(_fromUtf8("pushButton_on"))
        self.pushButton_off = QtGui.QPushButton(Form)
        self.pushButton_off.setGeometry(QtCore.QRect(240, 160, 41, 41))
        self.pushButton_off.setText(QtGui.QApplication.translate("Form", "&OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_off.setObjectName(_fromUtf8("pushButton_off"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.hSlider_zoomSpeed, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_zoomSpeed_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

