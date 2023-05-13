# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Benches(object):
    def setupUi(self, Benches):
        Benches.setObjectName("Benches")
        Benches.resize(400, 300)
        
        self.intropage = QtWidgets.QWizardPage()
        self.intropage.setObjectName("intropage")
        self.projname = QtWidgets.QLabel(parent=self.intropage)
        self.projname.setGeometry(QtCore.QRect(20, 160, 131, 21))
        self.projname.setStyleSheet("font: 300 9pt \"Ubuntu Light\";")
        self.projname.setObjectName("projname")
        self.intro = QtWidgets.QLabel(parent=self.intropage)
        self.intro.setGeometry(QtCore.QRect(10, 10, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.intro.setFont(font)
        self.intro.setAcceptDrops(False)
        self.intro.setStyleSheet("")
        self.intro.setWordWrap(True)
        self.intro.setObjectName("intro")
        self.enterproj = QtWidgets.QLineEdit(parent=self.intropage)
        self.enterproj.setGeometry(QtCore.QRect(180, 160, 191, 22))
        self.enterproj.setStyleSheet("color: #06a0ff;")
        self.enterproj.setObjectName("enterproj")
        Benches.addPage(self.intropage)
        self.projectspecs = QtWidgets.QWizardPage()
        self.projectspecs.setObjectName("projectspecs")
        self.label = QtWidgets.QLabel(parent=self.projectspecs)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(parent=self.projectspecs)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 151, 81))
        self.listWidget.setStyleSheet("color: #06a0ff;\n"
"border: 1px solid #62c0ff;\n"
"background-color: rgb(230, 244, 255);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_2 = QtWidgets.QLabel(parent=self.projectspecs)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.projectspecs)
        self.label_3.setGeometry(QtCore.QRect(210, 100, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.projectspecs)
        self.listWidget_2.setGeometry(QtCore.QRect(220, 130, 151, 81))
        self.listWidget_2.setStyleSheet("color: #06a0ff;\n"
"border: 1px solid #62c0ff;\n"
"background-color: rgb(230, 244, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.label_4 = QtWidgets.QLabel(parent=self.projectspecs)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 198, 243);\n"
"background-color: rgb(226, 245, 255);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.projectspecs)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: italic 8pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        Benches.addPage(self.projectspecs)
        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setObjectName("wizardPage")
        self.label_6 = QtWidgets.QLabel(parent=self.wizardPage)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(parent=self.wizardPage)
        self.checkBox.setGeometry(QtCore.QRect(110, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        Benches.addPage(self.wizardPage)

        self.retranslateUi(Benches)
        QtCore.QMetaObject.connectSlotsByName(Benches)

    def retranslateUi(self, Benches):
        _translate = QtCore.QCoreApplication.translate
        Benches.setWindowTitle(_translate("Benches", "Benches"))
        self.projname.setText(_translate("Benches", "<html><head/><body><p>Enter project name: </p></body></html>"))
        self.intro.setText(_translate("Benches", "<html><head/><body><p align=\"center\">Thanks for using Benches (v1.0)! </p><p align=\"center\">To begin experiments - enter a project name for your WandB project! </p></body></html>"))
        self.enterproj.setPlaceholderText(_translate("Benches", "benches"))
        self.label.setText(_translate("Benches", "Let\'s do some RL!"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Benches", "PPO"))
        item = self.listWidget.item(1)
        item.setText(_translate("Benches", "RPPO"))
        item = self.listWidget.item(2)
        item.setText(_translate("Benches", "SAC"))
        item = self.listWidget.item(3)
        item.setText(_translate("Benches", "TD3"))
        item = self.listWidget.item(4)
        item.setText(_translate("Benches", "DreamerV3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Benches", "Select Algorithm(s)"))
        self.label_3.setText(_translate("Benches", "Select Environment(s)"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Benches", "Pusher"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Benches", "Reacher"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Benches", "HalfCheetah"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Benches", "Reacher Hard (DM)"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Benches", "Cartpole (DM)"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("Benches", "Manipulator (DM) "))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Benches", "<html><head/><body><p align=\"justify\">Select all relevant algorithms and environments you would like to run experiments on.</p></body></html>"))
        self.label_5.setText(_translate("Benches", "<html><head/><body><p align=\"justify\"><span style=\" font-style:italic;\">Select all relevant algorithms and environments you would like to run experiments on.</span></p></body></html>"))
        self.label_6.setText(_translate("Benches", "Project Specifications:"))
        self.checkBox.setText(_translate("Benches", " save video to device"))