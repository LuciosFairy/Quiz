import sys

from PyQt6.QtWidgets import QDialog, QApplication

from ApiHandler import ApiHandler
from Questions import Questions
from configLayout import Ui_Config


class ConfigWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Config()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("")
        self.ui.comboBox.addItems(ApiHandler.getCategories())
        self.ui.confirmButton.clicked.connect(self.nextWindow)
        self.show()
        
    def nextWindow(self):
        category = self.ui.comboBox.currentText()
        numberOfQuestions = self.ui.spinBox.value()
        questions = Questions(category, numberOfQuestions)
        questions.exec()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ConfigWindow()
    sys.exit(app.exec())

