# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'points.ui'
#
# Created: Wed Jul  4 20:36:40 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(580, 460)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_filename = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.label_filename.setFont(font)
        self.label_filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_filename.setObjectName("label_filename")
        self.gridLayout.addWidget(self.label_filename, 0, 0, 1, 4)
        self.tableWidget_points = QtGui.QTableWidget(Frame)
        self.tableWidget_points.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget_points.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_points.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_points.setAutoScrollMargin(16)
        self.tableWidget_points.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_points.setCornerButtonEnabled(True)
        self.tableWidget_points.setRowCount(1)
        self.tableWidget_points.setColumnCount(6)
        self.tableWidget_points.setObjectName("tableWidget_points")
        self.tableWidget_points.setColumnCount(6)
        self.tableWidget_points.setRowCount(1)
        self.tableWidget_points.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_points.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_points.horizontalHeader().setMinimumSectionSize(18)
        self.tableWidget_points.verticalHeader().setDefaultSectionSize(18)
        self.gridLayout.addWidget(self.tableWidget_points, 1, 0, 1, 4)
        self.pushButton_teachNew = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_teachNew.setFont(font)
        self.pushButton_teachNew.setObjectName("pushButton_teachNew")
        self.gridLayout.addWidget(self.pushButton_teachNew, 2, 0, 1, 1)
        self.pushButton_teachInsert = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_teachInsert.setFont(font)
        self.pushButton_teachInsert.setObjectName("pushButton_teachInsert")
        self.gridLayout.addWidget(self.pushButton_teachInsert, 2, 1, 1, 2)
        self.pushButton_deleteRow = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_deleteRow.setFont(font)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.gridLayout.addWidget(self.pushButton_deleteRow, 2, 3, 1, 1)
        self.pushButton_moveTo = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.pushButton_moveTo.setFont(font)
        self.pushButton_moveTo.setObjectName("pushButton_moveTo")
        self.gridLayout.addWidget(self.pushButton_moveTo, 3, 0, 1, 2)
        self.pushButton_testcycle = QtGui.QPushButton(Frame)
        self.pushButton_testcycle.setObjectName("pushButton_testcycle")
        self.gridLayout.addWidget(self.pushButton_testcycle, 3, 2, 1, 2)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_filename.setText(QtGui.QApplication.translate("Frame", "no file loaded yet !", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_teachNew.setText(QtGui.QApplication.translate("Frame", "Teach new", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_teachInsert.setText(QtGui.QApplication.translate("Frame", "Teach insert", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_deleteRow.setText(QtGui.QApplication.translate("Frame", "delete row", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_moveTo.setText(QtGui.QApplication.translate("Frame", "Move to Point", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_testcycle.setText(QtGui.QApplication.translate("Frame", "testcycle", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_testcycle.setShortcut(QtGui.QApplication.translate("Frame", "Space", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

