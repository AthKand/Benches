import sys
from PyQt6 import QtWidgets
from utils.gui import Ui_Benches

class WizardApp(QtWidgets.QWizard, Ui_Benches):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    with open("./resources/style.qss", "r") as file:
        stylesheet = file.read()
        
    app.setStyleSheet(stylesheet)

    wizard = WizardApp()
    wizard.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
