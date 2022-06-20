import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import  PyQt5.QtCore as qtc

class new_order_home_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.setStyleSheet(self.main_widget.my_style.home_page_btn_style())
        self.Buy_btn = qtw.QPushButton("Buy")
        self.Buy_btn.clicked.connect(self.Buy_btn_fun)

        self.Sell_btn = qtw.QPushButton("Sell")
        self.Sell_btn.clicked.connect(self.Sell_btn_fun)

        self.new_package_btn = qtw.QPushButton("New Package")
        self.new_package_btn.clicked.connect(self.new_package_btn_fun)

        self.new_emp_btn = qtw.QPushButton("New Employee")
        self.new_emp_btn.clicked.connect(self.new_emp_btn_fun)

        self.set_layout()

    def Buy_btn_fun(self):
        self.main_widget.new_order_ly.setCurrentIndex(1)
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][1])
        self.main_widget.new_order_count = 1
        self.main_widget.update_cmb()

    def Sell_btn_fun(self):
        self.main_widget.new_order_ly.setCurrentIndex(2)
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][2])
        self.main_widget.new_order_count = 2

        self.main_widget.update_cmb()

    def new_package_btn_fun(self):
        self.main_widget.new_order_ly.setCurrentIndex(3)
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][3])

        self.main_widget.update_cmb()
        self.main_widget.new_order_count = 3

    def new_emp_btn_fun(self):
        self.main_widget.new_order_ly.setCurrentIndex(4)
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][4])
        self.main_widget.new_order_count = 4

    def set_layout(self):
        self.new_order_v_ly = qtw.QVBoxLayout()
        self.new_order_h1_ly = qtw.QHBoxLayout()
        self.new_order_h1_ly.addStretch()
        self.new_order_h1_ly.addWidget(self.Buy_btn)
        self.new_order_h1_ly.addStretch()
        self.new_order_h1_ly.addWidget(self.Sell_btn)
        self.new_order_h1_ly.addStretch()

        self.new_order_h2_ly = qtw.QHBoxLayout()
        self.new_order_h2_ly.addStretch()
        self.new_order_h2_ly.addWidget(self.new_package_btn)
        self.new_order_h2_ly.addStretch()
        self.new_order_h2_ly.addWidget(self.new_emp_btn)
        self.new_order_h2_ly.addStretch()

        self.new_order_v_ly.addLayout(self.new_order_h1_ly)
        self.new_order_v_ly.addLayout(self.new_order_h2_ly)
        self.setLayout(self.new_order_v_ly)




