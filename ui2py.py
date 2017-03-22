# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python34\Lib\site-packages\PyQt4\ui2py.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import subprocess
import helpdialog
   

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(489, 343)
        MainWindow.setGeometry(853, 537, 489, 343)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(175, 0, 151, 51))
        self.label.setStyleSheet(_fromUtf8("color: rgb(128,128,128);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        

        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 331, 41))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(145, 145, 218);\n"
"border-radius:10px;\n"
"padding-left:20px;\n"
"font: 12pt \"MS Shell Dlg 2\";"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 130, 331, 41))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(145, 145, 218);\n"
"border-radius:10px;\n"
"padding-left:20px;\n"
"font: 12pt \"MS Shell Dlg 2\";"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 331, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(204,204,204);\n"
"border-radius:0px;\n"
"padding-left:15px;\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        
        self.pushButton.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.writeIntoFile)
        self.pushButton.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.invokeBatchFileSubprocess)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 160, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(204,204,204);\n"
"border-radius:0px;\n"
"padding-left:15px;\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        self.pushButton_2.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.openPyFolder)
                                  

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 240, 150, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(204,204,204);\n"
"border-radius:0px;\n"
"padding-left:15px;\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        self.pushButton.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.show_help_dialog)
        
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", ".ui file name", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", ".py file name", None))
        self.pushButton.setText(_translate("MainWindow", "Convert .ui to .py", None))
        self.pushButton_2.setText(_translate("MainWindow", "Open .py code folder", None))
        self.pushButton_3.setText(_translate("MainWindow", "Click for Help", None))
        self.label.setText(_translate("MainWindow", "Easy converter", None))


    def dragEnterEvent( self, event ):
            data = event.mimeData()
            urls = data.urls()
            if ( urls and urls[0].scheme() == '.ui' ):
                event.acceptProposedAction()

    def dragMoveEvent( self, event ):
            data = event.mimeData()
            urls = data.urls()
            if ( urls and urls[0].scheme() == '.ui' ):
                event.acceptProposedAction()

    def dropEvent( self, event ):
            data = event.mimeData()
            urls = data.urls()
            if ( urls and urls[0].scheme() == '.ui' ):
                # for some reason, this doubles up the intro slash
                filepath = str(urls[0].path())[1:]
                self.lineEdit.setText(filepath)
                self.lineEdit.setPlaceholderText(filepath)

    def writeIntoFile(self):    
        file = open(r"C:\python34\New\GTui2py2.bat","w")
        file.write(r"C:\Python34\Lib\site-packages\PyQt4\pyuic4.bat -x -o" + " " + self.lineEdit_2.text() +" "+ self.lineEdit.text())
        file.close()

    def invokeBatchFileSubprocess(self):
        os.system("C:/python34/New/GTui2py2.bat")

    def openPyFolder(self):
        subprocess.call("explorer c:\\python34\\new",shell=True)

    def show_help_dialog(self):
        newDialog = HelpClass.helpUi()
        newDialog.show()

    
    
    
        
        
        
        
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

