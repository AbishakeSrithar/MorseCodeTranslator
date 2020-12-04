# Simple Morse Code Translator.
# Change interpreter to Python 3.8.2 64-bit if not working.

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Morse Code Translator')

        # Window with Box Layout
        self.setLayout(qtw.QVBoxLayout())
        self.interface()
        self.input = []
        self.output = []
        self.prev = []
        self.morse_dictionary = {".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m-", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z"}

        self.show()

    def interface(self):
        # Container with Grid Layout
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Buttons
        self.answer_field = qtw.QLineEdit()

        btn_translate = qtw.QPushButton('Translate', clicked=self.translate)
        btn_backspace = qtw.QPushButton('Backspace', clicked=self.backspace)
        btn_clear = qtw.QPushButton('Clear', clicked=self.clear)

        btn_dot = qtw.QPushButton('Dot', clicked=lambda: self.key_press('.'))
        btn_dash = qtw.QPushButton('Dash', clicked=lambda: self.key_press('-'))
        btn_letter = qtw.QPushButton('End of Letter', clicked=lambda: self.key_press(' '))
        btn_word = qtw.QPushButton('End of Letter and Word', clicked=lambda: self.key_press('|'))

        # Adding Buttons to Grid
        container.layout().addWidget(self.answer_field,0,0,1,6)
        container.layout().addWidget(btn_translate,1,0,1,3)
        container.layout().addWidget(btn_backspace,1,3,1,3)
        container.layout().addWidget(btn_clear,2,0,1,2)
        container.layout().addWidget(btn_dot,2,2,1,2)
        container.layout().addWidget(btn_dash,2,4,1,2)
        container.layout().addWidget(btn_letter,3,0,1,3)
        container.layout().addWidget(btn_word,3,3,1,3)
        self.layout().addWidget(container)

    def key_press(self, key):
        if key == "." or key == "-":
            self.input.append(key)
        elif key == " " and self.input:
            self.prev.append("".join(self.input) + " ")
            self.input = []
        elif key == "|" and self.input:
            self.prev.append("".join(self.input) + "   ")
            self.input = []
        self.display()
        
    def translate(self):
        temp_string2 = ""
        self.prev.append("".join(self.input) + " ")
        self.input = []
        for key in self.prev:
            if len(key) >= 4 and key[-3] == " ":
                if key[:-3] in self.morse_dictionary:
                    temp_string2 += self.morse_dictionary[key[:-3]] + " "
                else:
                    qtw.QMessageBox.about(self, "Error", "Not valid Morse Code")
                    self.clear()

            elif len(key) >= 2 and key[-1] == " ":
                if key[:-1] in self.morse_dictionary:
                    temp_string2 += self.morse_dictionary[key[:-1]]
                else:
                    qtw.QMessageBox.about(self, "Error", "Not valid Morse Code")
                    self.clear()

        self.answer_field.setText(temp_string2)

    def backspace(self):
        if self.input:
            self.input.pop()
            self.display()
        else:
            self.clear()

    def clear(self):
            self.input = []
            self.prev = []
            self.display()

    def display(self):
        self.answer_field.setText("".join(self.prev) + "".join(self.input))
            

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
app.exec_()

        



        




    