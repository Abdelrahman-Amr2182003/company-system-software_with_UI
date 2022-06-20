
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import  PyQt5.QtCore as qtc
import json
class info_page(qtw.QScrollArea):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget = main_widget
        self.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)

        self.logo = qtw.QLabel()
        self.logo.setPixmap(qtg.QPixmap('icons//logo.png'))
        self.rent = 0
        self.info_name_label = qtw.QLabel("Name: ")
        self.info_name_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_add_label = qtw.QLabel("Company Address: ")
        self.info_add_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_emp_label = qtw.QLabel("Number of employees: ")
        self.info_emp_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_Mobile_label = qtw.QLabel("Mobile numbers: ")
        self.info_Mobile_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_Website_label = qtw.QLabel("Website: ")
        self.info_Website_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_Rent_label = qtw.QLabel("Rent: ")
        self.info_Rent_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_description_label = qtw.QLabel("Description: ")
        self.info_description_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_name_label_2 = qtw.QLabel()
        self.info_name_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_name_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_add_label_2 = qtw.QLabel()
        self.info_add_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_add_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_emp_label_2 = qtw.QLabel(str(len(self.main_widget.add_emp_page_widget.employee_data.keys())))
        self.info_emp_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_emp_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_Mobile_label_2 = qtw.QLabel()
        self.info_Mobile_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_Mobile_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_Website_label_2 = qtw.QLabel()
        self.info_Website_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_Website_label_2.setStyleSheet("QLabel{color:blue;}")
        self.info_Rent_label_2 = qtw.QLabel()
        self.info_Rent_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_Rent_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_description_label_2 = qtw.QLabel()
        self.info_description_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_description_label_2.setStyleSheet("QLabel{color:blue;}")
        self.load_text()
        self.set_layout()
    def load_text(self):
            if self.main_widget.lang==0:
                with open('info_english.json','r') as f:
                    info_dict=json.load(f)
            else:
                with open('info_arabic.json','r') as f:
                    info_dict=json.load(f)
            self.info_name_label_2.setText(info_dict['name'])
            self.info_add_label_2.setText(info_dict['address'])
            self.info_Website_label_2.setText(info_dict['website'])
            self.info_Mobile_label_2.setText(info_dict['mobiles'])
            self.info_Rent_label_2.setText(str(info_dict['rent']))
            self.info_description_label_2.setText(info_dict['description'])
            self.rent=str(info_dict['rent'])


    def set_layout(self):
        self.info_ly = qtw.QVBoxLayout()
        self.logo_ly = qtw.QHBoxLayout()
        self.logo_ly.addStretch()
        self.logo_ly.addWidget(self.logo)
        self.logo_ly.addStretch()

        self.info_name_label_ly = qtw.QHBoxLayout()
        # self.info_name_label_ly.addStretch()
        self.info_name_label_ly.addWidget(self.info_name_label)
        self.info_name_label_ly.addWidget(self.info_name_label_2)
        self.info_name_label_ly.addStretch()

        self.info_add_label_ly = qtw.QHBoxLayout()
        # self.info_add_label_ly.addStretch()
        self.info_add_label_ly.addWidget(self.info_add_label)
        self.info_add_label_ly.addWidget(self.info_add_label_2)
        self.info_add_label_ly.addStretch()

        self.info_emp_label_ly = qtw.QHBoxLayout()
        # self.info_emp_label_ly.addStretch()
        self.info_emp_label_ly.addWidget(self.info_emp_label)
        self.info_emp_label_ly.addWidget(self.info_emp_label_2)
        self.info_emp_label_ly.addStretch()

        self.info_mobile_label_ly = qtw.QHBoxLayout()
        # self.info_mobile_label_ly.addStretch()
        self.info_mobile_label_ly.addWidget(self.info_Mobile_label)
        self.info_mobile_label_ly.addWidget(self.info_Mobile_label_2)
        self.info_mobile_label_ly.addStretch()

        self.info_website_label_ly = qtw.QHBoxLayout()
        # self.info_website_label_ly.addStretch()
        self.info_website_label_ly.addWidget(self.info_Website_label)
        self.info_website_label_ly.addWidget(self.info_Website_label_2)
        self.info_website_label_ly.addStretch()

        self.info_Rent_label_ly = qtw.QHBoxLayout()
        # self.info_Rent_label_ly.addStretch()
        self.info_Rent_label_ly.addWidget(self.info_Rent_label)
        self.info_Rent_label_ly.addWidget(self.info_Rent_label_2)
        self.info_Rent_label_ly.addStretch()

        self.info_description_label_ly = qtw.QHBoxLayout()
        # self.info_description_label_ly.addStretch()
        self.info_description_label_ly.addWidget(self.info_description_label)
        self.info_description_label_ly.addWidget(self.info_description_label_2)
        self.info_description_label_ly.addStretch()

        self.info_ly.addLayout(self.logo_ly)
        self.info_ly.addLayout(self.info_name_label_ly)
        self.info_ly.addLayout(self.info_add_label_ly)
        self.info_ly.addLayout(self.info_emp_label_ly)
        self.info_ly.addLayout(self.info_mobile_label_ly)
        self.info_ly.addLayout(self.info_website_label_ly)
        self.info_ly.addLayout(self.info_Rent_label_ly)
        self.info_ly.addLayout(self.info_description_label_ly)

        self.setLayout(self.info_ly)

class edit_info(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())

        self.edit_company_name = qtw.QLineEdit()
        self.edit_company_address = qtw.QLineEdit()
        self.edit_company_website = qtw.QLineEdit()
        self.edit_company_mobiles = qtw.QLineEdit()
        self.edit_company_rent = qtw.QLineEdit()
        self.edit_company_description = qtw.QTextEdit()

        self.edit_company_name_label = qtw.QLabel("Enter new company Name")
        self.edit_company_address_label = qtw.QLabel("Enter new company Address")
        self.edit_company_website_label = qtw.QLabel("Enter new company Website")
        self.edit_company_mobiles_label = qtw.QLabel("Enter new Mobile numbers")
        self.edit_company_rent_label = qtw.QLabel("Enter company new Rent")
        self.edit_company_description_label = qtw.QLabel("Enter new Description")
        self.submit_new_info=qtw.QPushButton("Submit")
        self.submit_new_info.setStyleSheet(self.main_widget.my_style.button_style())
        self.submit_new_info.clicked.connect(self.save_new_info)
        self.load_text()
        self.set_layout()
    def save_new_info(self):
        info_dict=dict()
        info_dict['name']=self.edit_company_name.text()
        info_dict['address']=self.edit_company_address.text()
        info_dict['website']=self.edit_company_website.text()
        info_dict['mobiles']=self.edit_company_mobiles.text()
        info_dict['rent']=self.edit_company_rent.text()
        info_dict['description']=self.edit_company_description.toPlainText()
        if self.main_widget.lang==0:
            with open('info_english.json','w') as f:
                json.dump(info_dict,f)
        else:
            with open('info_arabic.json','w') as f:
                json.dump(info_dict,f)
        self.load_text()
        self.main_widget.main_info_widget.scrollable_info.load_text()

    def load_text(self):
            if self.main_widget.lang==0:
                with open('info_english.json','r') as f:
                    info_dict=json.load(f)
            else:
                with open('info_arabic.json','r') as f:
                    info_dict=json.load(f)
            self.edit_company_name.setText(info_dict['name'])
            self.edit_company_address.setText(info_dict['address'])
            self.edit_company_website.setText(info_dict['website'])
            self.edit_company_mobiles.setText(info_dict['mobiles'])
            self.edit_company_rent.setText(info_dict['rent'])
            self.edit_company_description.setText(info_dict['description'])



    def set_layout(self):
        self.edit_info_ly = qtw.QVBoxLayout()
        self.edit_info_ly.addWidget(self.edit_company_name_label)
        self.edit_info_ly.addWidget(self.edit_company_name)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_address_label)
        self.edit_info_ly.addWidget(self.edit_company_address)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_mobiles_label)
        self.edit_info_ly.addWidget(self.edit_company_mobiles)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_website_label)
        self.edit_info_ly.addWidget(self.edit_company_website)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_rent_label)
        self.edit_info_ly.addWidget(self.edit_company_rent)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_description_label)
        self.edit_info_ly.addWidget(self.edit_company_description)
        self.edit_info_ly.addStretch()
        self.button_ly = qtw.QHBoxLayout()
        self.button_ly.addStretch()
        self.button_ly.addWidget(self.submit_new_info)
        self.button_ly.addStretch()
        self.edit_info_ly.addLayout(self.button_ly)
        self.edit_info_ly.addStretch()
        self.setLayout(self.edit_info_ly)

class main_info_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.msgSc = qtw.QShortcut(qtg.QKeySequence('Ctrl+E'), self)
        self.msgSc.activated.connect(self.navigate_info_pages)
        ###################info page######################
        self.scrollable_info = info_page(self.main_widget)
        ##################Edit info############################
        self.edit_info_page_widget = edit_info(self.main_widget)
        self.set_layout()
    def navigate_info_pages(self):
        if self.main_widget.current_type == 'admin':
            if (self.main_info_ly.currentIndex() == 1):
                self.main_info_ly.setCurrentIndex(0)
            else:
                self.main_info_ly.setCurrentIndex(1)
    def set_layout(self):
        #########info_ly#####################
        self.main_info_ly = qtw.QStackedLayout()
        self.main_info_ly.addWidget(self.scrollable_info)
        self.main_info_ly.addWidget(self.edit_info_page_widget)
        self.setLayout(self.main_info_ly)

