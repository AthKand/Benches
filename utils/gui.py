from PyQt6 import QtCore, QtGui, QtWidgets

# Custom delegate for checkable combo box items
class CheckableComboBoxDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        if not index.data(QtCore.Qt.ItemDataRole.UserRole):
            option.state &= ~QtWidgets.QStyle.StateFlag.State_Enabled

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

        self.delegate = CheckableComboBoxDelegate()

        # Replace the QListWidget instances with QComboBox instances
        self.checkCombo = QtWidgets.QComboBox(parent=self.projectspecs)
        self.checkCombo.setGeometry(QtCore.QRect(20, 130, 151, 25))
        self.checkCombo.setObjectName("checkCombo")
        self.checkCombo_2 = QtWidgets.QComboBox(parent=self.projectspecs)
        self.checkCombo_2.setGeometry(QtCore.QRect(220, 130, 151, 25))
        self.checkCombo_2.setObjectName("checkCombo_2")

        # Add checkable items to the combo boxes and set the custom delegate
        algorithms = ["PPO", "RPPO", "SAC", "TD3", "DreamerV3"]
        for algorithm in algorithms:
            self.checkCombo.addItem(algorithm)
            item = self.checkCombo.model().item(self.checkCombo.count() - 1, 0)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.checkCombo.setItemDelegate(self.delegate)

        environments = ["Pusher", "Reacher", "HalfCheetah", "Reacher Hard (DM)", "Cartpole (DM)", "Manipulator (DM)"]
        for environment in environments:
            self.checkCombo_2.addItem(environment)
            item = self.checkCombo_2.model().item(self.checkCombo_2.count() - 1, 0)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.checkCombo_2.setItemDelegate(self.delegate)

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

        for i in range(self.checkCombo.count()):
            self.checkCombo.setItemText(i, _translate("Benches", self.checkCombo.itemText(i)))

        self.label_2.setText(_translate("Benches", "Select Algorithm(s)"))
        self.label_3.setText(_translate("Benches", "Select Environment(s)"))

        for i in range(self.checkCombo_2.count()):
            self.checkCombo_2.setItemText(i, _translate("Benches", self.checkCombo_2.itemText(i)))
        
        self.label_4.setText(_translate("Benches", "<html><head/><body><p align=\"justify\">Select all relevant algorithms and environments you would like to run experiments on.</p></body></html>"))
        self.label_5.setText(_translate("Benches", "<html><head/><body><p align=\"justify\"><span style=\" font-style:italic;\">Select all relevant algorithms and environments you would like to run experiments on.</span></p></body></html>"))
        self.label_6.setText(_translate("Benches", "Project Specifications:"))
        self.checkBox.setText(_translate("Benches", " save video to device"))
