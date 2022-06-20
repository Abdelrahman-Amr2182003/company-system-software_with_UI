import PyQt5.QtWidgets as qtw

class database_home_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.employees_btn = qtw.QPushButton("Employees")
        self.employees_btn.clicked.connect(self.employees_btn_fun)
        self.employees_btn.setStyleSheet(self.main_widget.my_style.home_page_btn_style())

        self.imports_btn = qtw.QPushButton("imports")
        self.imports_btn.clicked.connect(self.imports_btn_fun)
        self.imports_btn.setStyleSheet(self.main_widget.my_style.home_page_btn_style())

        self.exports_btn = qtw.QPushButton("exports")
        self.exports_btn.clicked.connect(self.exports_btn_fun)
        self.exports_btn.setStyleSheet(self.main_widget.my_style.home_page_btn_style())

        self.calculations_btn = qtw.QPushButton("calculations")
        self.calculations_btn.clicked.connect(self.calculations_btn_fun)
        self.calculations_btn.setStyleSheet(self.main_widget.my_style.home_page_btn_style())
        self.set_layout()

    def employees_btn_fun(self):
        self.main_widget.database_widget.database_ly.setCurrentIndex(1)
        self.main_widget.database_widget.database_bar.database_bar_label.setText(self.main_widget.database_widget.database_bar.database_pages[self.main_widget.lang][1])
        self.main_widget.database_widget.database_bar.count = 1
        self.main_widget.update_cmb()

    def calculations_btn_fun(self):
        self.main_widget.database_widget.database_ly.setCurrentIndex(2)
        self.main_widget.database_widget.database_bar.database_bar_label.setText(self.main_widget.database_widget.database_bar.database_pages[self.main_widget.lang][2])
        self.main_widget.database_widget.database_bar.count = 2
        self.main_widget.database_widget.calc_widget.populate_calculations_tabel()
        self.main_widget.database_widget.calc_widget.populate_total_calc_table()
        self.main_widget.update_cmb()
    def imports_btn_fun(self):
        self.main_widget.database_widget.database_ly.setCurrentIndex(3)
        self.main_widget.database_widget.database_bar.database_bar_label.setText(self.main_widget.database_widget.database_bar.database_pages[self.main_widget.lang][3])
        self.main_widget.database_widget.database_bar.count = 3
        self.main_widget.update_cmb()

    def exports_btn_fun(self):
        self.main_widget.database_widget.database_ly.setCurrentIndex(4)
        self.main_widget.database_widget.database_bar.database_bar_label.setText(self.main_widget.database_widget.database_bar.database_pages[self.main_widget.lang][4])
        self.main_widget.database_widget.database_bar.count = 4
        self.main_widget.update_cmb()
    def set_layout(self):
        self.data_base_home_ly = qtw.QVBoxLayout()
        self.top_database_ly = qtw.QHBoxLayout()
        self.bottom_database_ly = qtw.QHBoxLayout()

        self.top_database_ly.addStretch()
        self.top_database_ly.addWidget(self.employees_btn)
        self.top_database_ly.addStretch()
        self.top_database_ly.addWidget(self.calculations_btn)
        self.top_database_ly.addStretch()

        self.bottom_database_ly.addStretch()
        self.bottom_database_ly.addWidget(self.imports_btn)
        self.bottom_database_ly.addStretch()
        self.bottom_database_ly.addWidget(self.exports_btn)
        self.bottom_database_ly.addStretch()

        self.data_base_home_ly.addLayout(self.top_database_ly)
        # self.home_ly.addStretch()
        self.data_base_home_ly.addLayout(self.bottom_database_ly)

        self.setLayout(self.data_base_home_ly)

