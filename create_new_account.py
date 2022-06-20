import PyQt5.QtWidgets as qtw

class create_new_account(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.types_passwords=['employee','manger','admin']
        self.types=['employee','manger','admin']
        for i in range(len(self.types)):
            try:
                sql_stuff = """INSERT INTO users(username,password,acc_type)VALUES(%s,%s,%s);"""
                self.main_widget.my_cursor.execute(sql_stuff,(self.types[i], self.types_passwords[i], self.types[i]))
            except:
                pass
        self.main_widget.mydb.commit()
        self.load_users()
        self.types_passwords=[self.users_data['employee'][0],self.users_data['manger'][0],self.users_data['admin'][0]]
        self.main_widget = main_widget
        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())
        self.add_username_label = qtw.QLabel("Enter username")
        self.new_password_label = qtw.QLabel("Enter Password")
        self.add_confirmed_password_label = qtw.QLabel("Confirm password")

        self.add_username = qtw.QLineEdit()
        self.new_password = qtw.QLineEdit()
        self.add_confirmed_password = qtw.QLineEdit()
        self.account_type_password = qtw.QLineEdit()
        self.account_password_type_label = qtw.QLabel("Enter account type password")
        self.create_btn = qtw.QPushButton("Create")
        self.create_btn.clicked.connect(self.create_acc)
        self.set_layout()
    def load_users(self):
        self.users_data=dict()
        self.main_widget.my_cursor.execute("SELECT * FROM users")
        data = self.main_widget.my_cursor.fetchall()
        for i, info in enumerate(data):
            user_name,password,acc_type= info
            self.users_data[str(user_name)] = [str(password),str(acc_type)]
    def create_acc(self):
        if self.account_type_password.text() in self.types_passwords:
            acc_type=self.types[self.types_passwords.index(self.account_type_password.text())]
            username=self.add_username.text()
            password=self.new_password.text()
            if username != 'admin' or username != 'manger' or username != 'employee':
                if self.add_confirmed_password.text()==self.new_password.text():

                    try:
                        sql_stuff = """INSERT INTO users(username,password,acc_type)VALUES(%s,%s,%s);"""
                        self.main_widget.my_cursor.execute(sql_stuff,
                                                           (username,password,acc_type))
                    except:
                        res = qtw.QMessageBox.information(self, "","Username already exists")
                else:
                    res = qtw.QMessageBox.information(self, "", "Passwords doesnt match")
            else:
                res = qtw.QMessageBox.information(self, "", "Cant create username with this name")
        else:
            res = qtw.QMessageBox.information(self, "", "Wrong account type password")
        self.main_widget.mydb.commit()
        self.new_password.setText("")
        self.add_confirmed_password.setText("")
        self.add_username.setText("")
        self.account_type_password.setText("")
        self.load_users()

    def set_layout(self):
        self.create_acc_ly = qtw.QVBoxLayout()
        self.create_acc_ly.addWidget(self.add_username_label)
        self.create_acc_ly.addWidget(self.add_username)
        self.create_acc_ly.addWidget(self.new_password_label)
        self.create_acc_ly.addWidget(self.new_password)
        self.create_acc_ly.addWidget(self.add_confirmed_password_label)
        self.create_acc_ly.addWidget(self.add_confirmed_password)
        self.create_acc_ly.addWidget(self.account_password_type_label)
        self.create_acc_ly.addWidget(self.account_type_password)
        self.create_acc_ly.addStretch()
        self.create_btn_ly = qtw.QHBoxLayout()
        self.create_btn_ly.addStretch()
        self.create_btn_ly.addWidget(self.create_btn)
        self.create_btn_ly.addStretch()
        self.create_acc_ly.addLayout(self.create_btn_ly)
        self.setLayout(self.create_acc_ly)
