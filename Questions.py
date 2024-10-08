# Modifying the Questions.py to add score tracking functionality


from PyQt6.QtWidgets import QDialog, QRadioButton, QSizePolicy, QMessageBox
from ApiHandler import ApiHandler
from Question import Question
from questionLayout import Ui_Question


class Questions(QDialog):
    def __init__(self, category: str, limit: int):
        super().__init__()
        self.ui = Ui_Question()
        self.questions = ApiHandler.getQuestions(category, limit)
        self.ui.setupUi(self)
        self.number_of_question = 0
        self.score = 0
        self.buttons: [QRadioButton] = []
        self.get_question(self.questions[self.number_of_question])
        self.ui.nextButton.clicked.connect(self.next_question)
        self.show()

    def get_question(self, question: Question):
        self.ui.questionLabel.setText(question.question_text)
        for button in self.buttons:
            self.ui.verticalLayout.removeWidget(button)
        self.buttons = []

        for answer in question.answers:
            button = QRadioButton(text=answer)
            button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            self.buttons.append(button)

        for button in self.buttons:
            self.ui.verticalLayout.addWidget(button)

    def next_question(self):
        selected_answer = self.get_selected_answer()
        if selected_answer is not None:
            if selected_answer == self.questions[self.number_of_question].correct_answer:
                self.score += 1

        self.number_of_question += 1

        if self.number_of_question < len(self.questions):
            self.get_question(self.questions[self.number_of_question])
        else:
            self.show_score()

    def get_selected_answer(self):
        for button in self.buttons:
            if button.isChecked():
                return button.text()
        return None

    def show_score(self):
        msg_box = QMessageBox()
        msg_box.setText(f"Quiz Skonczony! Twoj wynik: {self.score}/{len(self.questions)}")
        msg_box.exec()
        self.close()
