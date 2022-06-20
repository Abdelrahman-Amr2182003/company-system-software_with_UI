

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class new_employee(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())


        self.select_employee_type_label =qtw.QLabel("Enter employment type")
        self.select_employee_type =qtw.QComboBox()
        self.select_employee_type.addItems(['New Employee' ,'update employee info'])
        self.emp_code_input_label =qtw.QLabel("Enter employee code")
        self.emp_code_input =qtw.QComboBox()
        self.emp_code_input.setToolTip("Only enter the code in case of an old employee")
        self.add_emp_name_label = qtw.QLabel()
        self.add_emp_name_label.setText("Enter Employee Name")
        self.add_emp_name = qtw.QLineEdit()

        self.add_emp_position_label = qtw.QLabel()
        self.add_emp_position_label.setText("Enter Employee Position")
        self.add_emp_position = qtw.QLineEdit()

        self.add_emp_salary_label = qtw.QLabel()
        self.add_emp_salary_label.setText("Enter Employee salary")
        self.add_emp_salary = qtw.QLineEdit()


        self.hire_date =qtw.QDateEdit(qtc.QDate(qtc.QDate().currentDate()))
        self.hire_date.setCalendarPopup(True)
        self.add_emp_submit = qtw.QPushButton("Submit")
        self.add_emp_clear_btn =qtw.QPushButton("clear")
        self.add_emp_submit.clicked.connect(self.add_emp_submit_btn_fn)
        self.add_emp_clear_btn.clicked.connect(self.clear_emp_btn_fun)
        self.set_layout()


    def add_emp_submit_btn_fn(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to update employees info", qm.Yes | qm.No)
        if ret == qm.Yes:
            type=self.select_employee_type.currentText()
            name = self.add_emp_name.text()
            position = self.add_emp_position.text()

            salary = self.add_emp_salary.text()
            date = self.hire_date.date().toString(qtc.Qt.ISODate)
            code=self.emp_code_input.currentText()
            if type=="New Employee":
                try:
                    sql_stuff="INSERT INTO employees (name,position,salary,hire_date) VALUES(%s,%s,%s,%s)"
                    self.main_widget.my_cursor.execute(sql_stuff, (name, position, salary, date))
                except:
                    pass
            elif type=='update employee info':

                try:
                    sql_stuff="UPDATE employees SET name=%s,position=%s,salary=%s,hire_date=%s WHERE code=%s"
                    self.main_widget.my_cursor.execute(sql_stuff, (name, position, salary, date,code))
                except:
                    res = qtw.QMessageBox.information(self, "Employee code not found", f"Couldn't find employee code you entered")

            self.main_widget.mydb.commit()
            self.get_employees()
            self.main_widget.update_cmb()
            self.main_widget.buy_product_widget.get_imports()
            self.main_widget.sell_Product.get_exports()
            self.clear_emp_btn_fun()
        else:
            pass
    def clear_emp_btn_fun(self):
        self.add_emp_name.setText("")
        self.add_emp_position.setText("")
        self.add_emp_salary.setText("")
        self.hire_date.setDate(qtc.QDate(qtc.QDate().currentDate()))


    def get_employees(self):
        try:
            self.employee_data=dict()
            self.main_widget.my_cursor.execute("SELECT * FROM employees")
            data=self.main_widget.my_cursor.fetchall()
            if self.main_widget.database_widget.emp_widget.emp_tabel.rowCount()<len(data):
                self.main_widget.database_widget.emp_widget.emp_tabel.setRowCount(len(data))
            if self.main_widget.database_widget.emp_widget.emp_tabel.rowCount()<len(data):
                self.main_widget.database_widget.emp_widget.emp_tabel.setRowCount(len(data))
            for i,emp in enumerate(data):
                code,name,position,salary,hiring_date=emp
                self.employee_data[str(code)]=[name,position,salary,hiring_date]
                self.main_widget.database_widget.emp_widget.emp_tabel.setItem(i,0,qtw.QTableWidgetItem(str(code)))
                self.main_widget.database_widget.emp_widget.emp_tabel.setItem(i,1,qtw.QTableWidgetItem(str(name)))
                self.main_widget.database_widget.emp_widget.emp_tabel.setItem(i,2,qtw.QTableWidgetItem(str(position)))
                self.main_widget.database_widget.emp_widget.emp_tabel.setItem(i,3,qtw.QTableWidgetItem(str(salary)))
                self.main_widget.database_widget.emp_widget.emp_tabel.setItem(i,4,qtw.QTableWidgetItem(str(hiring_date)))
        except:
            pass


    def set_layout(self):
        self.add_emp_ly = qtw.QVBoxLayout()

        self.add_emp_ly.addWidget(self.select_employee_type_label)
        self.add_emp_ly.addWidget(self.select_employee_type)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.emp_code_input_label)
        self.add_emp_ly.addWidget(self.emp_code_input)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.add_emp_name_label)
        self.add_emp_ly.addWidget(self.add_emp_name)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.add_emp_salary_label)
        self.add_emp_ly.addWidget(self.add_emp_salary)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.add_emp_position_label)
        self.add_emp_ly.addWidget(self.add_emp_position)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.hire_date)
        self.add_emp_ly.addStretch()

        self.add_emp_submit_clear_ly = qtw.QHBoxLayout()

        self.add_emp_submit_clear_ly.addWidget(self.add_emp_submit)
        self.add_emp_submit_clear_ly.addStretch()
        self.add_emp_submit_clear_ly.addWidget(self.add_emp_clear_btn)
        self.add_emp_ly.addLayout(self.add_emp_submit_clear_ly)

        self.setLayout(self.add_emp_ly)
