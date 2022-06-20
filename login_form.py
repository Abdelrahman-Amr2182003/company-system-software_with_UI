
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc


class login_form(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.login_label = qtw.QLabel()
        self.login_label.setPixmap(qtg.QPixmap("icons//login.png"))
        self.login_label.setStyleSheet("QLabel{border-radius:175px;min-width:350px;min-height:350px;}")

        self.username_in = qtw.QLineEdit()
        self.password_in = qtw.QLineEdit()
        self.password_in.setEchoMode(qtw.QLineEdit.Password)
        self.password_label = qtw.QLabel("Enter your password")
        self.username_label = qtw.QLabel("Enter your username")
        self.login_btn = qtw.QPushButton("Login")
        self.username_in.setStyleSheet(self.main_widget.my_style.line_edit_style())
        self.password_in.setStyleSheet(self.main_widget.my_style.line_edit_style())
        self.login_btn.setStyleSheet(self.main_widget.my_style.button_style())
        self.wrong_pass = qtw.QLabel()
        self.wrong_pass.setStyleSheet("QLabel{color:red;}")
        self.login_btn.clicked.connect(self.login_btn_fun)
        self.wrong_pass.hide()
        self.username_in.setText("abdelrahman")
        self.password_in.setText("0138792")
        self.set_layout()
    def login_btn_fun(self):
        users=[i for i in list(self.main_widget.main_settings_widget.create_acc_widget.users_data.keys())]
        passwords=[i[0] for i in list(self.main_widget.main_settings_widget.create_acc_widget.users_data.values())]
        types = [i[1] for i in list(self.main_widget.main_settings_widget.create_acc_widget.users_data.values())]
        if self.username_in.text() in users:
            if (self.password_in.text() == passwords[users.index(self.username_in.text())]):
                self.main_widget.current_type = types[users.index(self.username_in.text())]
                self.main_widget.stacked_g.setCurrentIndex(1)
            else:
                self.wrong_pass.setText(["Wrong password", "كلمة مرور غير صحيحة"][self.main_widget.lang])
                self.wrong_pass.show()
        else:
            self.wrong_pass.setText(["Wrong username", "اسم مستخدم غير صحيح"][self.main_widget.lang])
            self.wrong_pass.show()
        if self.main_widget.current_type != "admin":
            self.main_widget.database_widget.emp_widget.emp_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
            self.main_widget.database_widget.imp_widget.imp_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
            self.main_widget.database_widget.exp_widget.exports_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
        self.main_widget.database_widget.calc_widget.calc_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)

    def set_layout(self):
        self.login_h_ly = qtw.QHBoxLayout()
        self.login_form_ly = qtw.QVBoxLayout()
        self.login_label_ly = qtw.QHBoxLayout()
        self.login_label_ly.addStretch()
        self.login_label_ly.addWidget(self.login_label)
        self.login_label_ly.addStretch()
        self.login_form_ly.addLayout(self.login_label_ly)
        self.login_form_ly.addWidget(self.username_label)
        self.login_form_ly.addWidget(self.username_in)
        self.login_form_ly.addWidget(self.password_label)
        self.login_form_ly.addWidget(self.password_in)
        self.login_form_ly.addWidget(self.login_btn)
        self.login_form_ly.addWidget(self.wrong_pass)
        self.login_form_ly.addStretch()
        self.login_h_ly.addStretch()
        self.login_h_ly.addLayout(self.login_form_ly)
        self.login_h_ly.addStretch()
        self.setLayout(self.login_h_ly)

