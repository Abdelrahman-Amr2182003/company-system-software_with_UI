
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from styles import styles

class home_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.home_page_style=styles(self.main_widget)
        self.stock_btn_home = qtw.QPushButton()
        self.stock_btn_home.setIcon(qtg.QIcon("icons//stock.png"))
        self.stock_btn_home.setStyleSheet(self.home_page_style.home_page_btn_style())
        self.stock_btn_home.setIconSize(qtc.QSize(80, 80))
        self.stock_btn_home.clicked.connect(self.stock_btn_fun)
        self.data_btn_home = qtw.QPushButton()
        self.data_btn_home.setIcon(qtg.QIcon("icons//database.png"))
        self.data_btn_home.setStyleSheet(self.home_page_style.home_page_btn_style())
        self.data_btn_home.setIconSize(qtc.QSize(80, 80))
        self.data_btn_home.clicked.connect(self.database_btn_fun)
        self.new_btn_home = qtw.QPushButton()
        self.new_btn_home.setIcon(qtg.QIcon("icons//new.png"))
        self.new_btn_home.setStyleSheet(self.home_page_style.home_page_btn_style())
        self.new_btn_home.setIconSize(qtc.QSize(80, 80))
        self.new_btn_home.clicked.connect(self.new_order_btn_fun)
        self.info_btn_home = qtw.QPushButton()
        self.info_btn_home.setIcon(qtg.QIcon("icons//info.png"))
        self.info_btn_home.setStyleSheet(self.home_page_style.home_page_btn_style())
        self.info_btn_home.setIconSize(qtc.QSize(80, 80))
        self.info_btn_home.clicked.connect(self.info_btn_fun)
        self.set_layout()
    def stock_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(1)
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][1])
        self.main_widget.update_cmb()
        self.main_widget.update_tables()


    def new_order_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(2)
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][2])
        self.main_widget.update_cmb()
        self.main_widget.update_tables()

    def database_btn_fun(self):
        if self.main_widget.current_type == "manger" or self.main_widget.current_type == "admin":
            self.main_widget.main_ly.setCurrentIndex(3)
            self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][3])
            self.main_widget.database_widget.calc_widget.populate_calculations_tabel()
            self.main_widget.database_widget.calc_widget.populate_total_calc_table()
        self.main_widget.update_tables()

    def info_btn_fun(self):

        self.main_widget.main_ly.setCurrentIndex(4)
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][4])
        self.main_widget.main_info_widget.scrollable_info.load_text()
        self.main_widget.main_info_widget.edit_info_page_widget.load_text()
        self.main_widget.update_tables()


    def set_layout(self):
        self.home_ly = qtw.QVBoxLayout()
        self.top_home_ly = qtw.QHBoxLayout()
        self.bottom_home_ly = qtw.QHBoxLayout()
        self.top_home_ly.addStretch()
        self.top_home_ly.addWidget(self.stock_btn_home)
        self.top_home_ly.addStretch()
        self.top_home_ly.addWidget(self.new_btn_home)
        self.top_home_ly.addStretch()
        self.bottom_home_ly.addStretch()
        self.bottom_home_ly.addWidget(self.data_btn_home)
        self.bottom_home_ly.addStretch()
        self.bottom_home_ly.addWidget(self.info_btn_home)
        self.bottom_home_ly.addStretch()
        self.home_ly.addLayout(self.top_home_ly)
        # self.home_ly.addStretch()
        self.home_ly.addLayout(self.bottom_home_ly)
        self.setLayout(self.home_ly)



