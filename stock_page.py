

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc


class stock_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget

        self.search_btn = qtw.QPushButton()
        self.search_btn.setIcon(qtg.QIcon("icons/search.png"))
        self.search_btn.setIconSize(qtc.QSize(50, 50))
        self.search_btn.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")
        self.search_box = qtw.QLineEdit()
        self.search_box.setStyleSheet(
            '''color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px''')
        self.stock_tabel = qtw.QTableWidget(20, 5)
        self.stock_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
        self.stock_tabel.setColumnWidth(0, 460)
        self.stock_tabel.setColumnWidth(1, 130)
        self.stock_tabel.setColumnWidth(2, 130)
        self.stock_tabel.setColumnWidth(3, 130)
        self.stock_tabel.horizontalHeader().setStretchLastSection(True)
        self.stock_tabel.verticalHeader().setStretchLastSection(True)
        self.stock_tabel.setHorizontalHeaderLabels(
            ["Product", "Availble", "price per unit", "Sell price per unit", "sold"])
        self.set_layout()
    def get_stock(self):
        self.main_widget.my_cursor.execute("SELECT * FROM stock")
        data=self.main_widget.my_cursor.fetchall()
        self.stock_data=dict()
        if self.stock_tabel.rowCount()<len(data):
            self.stock_tabel.setRowCount(len(data))
        for i,info in enumerate(data):
            prod,av,buy,sell,sold=info
            if sold is None:
                sold=0
            self.stock_data[str(prod)]=[av,buy,sell,sold]

            self.stock_tabel.setItem(i,0,qtw.QTableWidgetItem(str(prod)))
            self.stock_tabel.setItem(i,1,qtw.QTableWidgetItem(str(av)))
            self.stock_tabel.setItem(i,2,qtw.QTableWidgetItem(str(buy)))
            self.stock_tabel.setItem(i,3,qtw.QTableWidgetItem(str(sell)))
            self.stock_tabel.setItem(i,4,qtw.QTableWidgetItem(str(sold)))
    def set_layout(self):
        self.stock_ly = qtw.QVBoxLayout()

        self.top_ly = qtw.QHBoxLayout()
        self.top_ly.addStretch()
        self.top_ly.addWidget(self.search_box)
        self.top_ly.addWidget(self.search_btn)
        self.stock_ly.addLayout(self.top_ly)
        self.stock_ly.addWidget(self.stock_tabel)

        self.setLayout(self.stock_ly)