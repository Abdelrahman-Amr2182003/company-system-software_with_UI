import PyQt5.QtWidgets as qtw

class change_password(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget = main_widget
        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())
        self.username_change_label = qtw.QLabel("Enter Username")
        self.username_change = qtw.QLineEdit()
        self.old_password_label = qtw.QLabel("Enter Old Password")
        self.old_password = qtw.QLineEdit()
        self.changed_password_label = qtw.QLabel("Enter New Password")
        self.changed_password = qtw.QLineEdit()
        self.confirmed_password_label = qtw.QLabel("Confirm New Password")
        self.confirmed_password = qtw.QLineEdit()
        self.submit_changed_password = qtw.QPushButton("Submit changes")
        self.submit_changed_password.clicked.connect(self.update_password)
        self.set_layout()
    def update_password(self):
        self.main_widget.main_settings_widget.create_acc_widget.load_users()
        users_data=self.main_widget.main_settings_widget.create_acc_widget.users_data
        username=self.username_change.text()
        old_password=self.old_password.text()
        new_password=self.changed_password.text()
        confirmed_password=self.confirmed_password.text()
        if username in list(users_data.keys()):
            if old_password ==users_data[username][0]:
                if new_password==confirmed_password:
                    try:

                        sql_stuff = """UPDATE users SET password=%s WHERE username=%s"""
                        self.main_widget.my_cursor.execute(sql_stuff, (new_password,username))
                    except:
                        pass

                else:
                    res = qtw.QMessageBox.information(self, "", "passwords dont match")
            else:
                res = qtw.QMessageBox.information(self, "", "wrong old password")
        else:
            res = qtw.QMessageBox.information(self, "", "user doesnt exist")
        self.main_widget.mydb.commit()
        self.main_widget.main_settings_widget.create_acc_widget.load_users()

        self.old_password.setText("")
        self.username_change.setText("")
        self.changed_password.setText("")
        self.confirmed_password.setText("")


    def set_layout(self):
        self.change_password_ly = qtw.QVBoxLayout()
        self.change_password_ly.addWidget(self.username_change_label)
        self.change_password_ly.addWidget(self.username_change)
        self.change_password_ly.addWidget(self.old_password_label)
        self.change_password_ly.addWidget(self.old_password)
        self.change_password_ly.addWidget(self.changed_password_label)
        self.change_password_ly.addWidget(self.changed_password)
        self.change_password_ly.addWidget(self.confirmed_password_label)
        self.change_password_ly.addWidget(self.confirmed_password)
        self.submit_changed_password_ly = qtw.QHBoxLayout()
        self.submit_changed_password_ly.addStretch()
        self.submit_changed_password_ly.addWidget(self.submit_changed_password)
        self.submit_changed_password_ly.addStretch()
        self.change_password_ly.addStretch()
        self.change_password_ly.addLayout(self.submit_changed_password_ly)
        self.setLayout(self.change_password_ly)
