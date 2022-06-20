import PyQt5.QtWidgets as qtw
from styles import styles
import PyQt5.QtCore as qtc
class sort_dialog(qtw.QDialog):
    def __init__(self,table,first_col,second_col,first_compartor,second_compartor):
        super().__init__()
        self.first_col=first_col
        self.second_col=second_col
        self.table=table
        self.dialog_style=styles(self)

        self.sort_by_price=qtw.QPushButton(f"Sort By {first_compartor}")
        self.sort_by_price.setStyleSheet(self.dialog_style.button_style())
        self.sort_by_price.clicked.connect(self.sort_by_price_btn_fun)
        self.sort_by_date = qtw.QPushButton(f"Sort By {second_compartor}")
        self.sort_by_date.setStyleSheet(self.dialog_style.button_style())
        self.sort_by_date.clicked.connect(self.sort_by_date_btn_fun)
        self.set_layout()

    def sort_by_price_btn_fun(self):
        self.table.sortByColumn(self.first_col,qtc.Qt.DescendingOrder)


    def sort_by_date_btn_fun(self):
        self.table.sortByColumn(self.second_col,qtc.Qt.DescendingOrder)


    def set_layout(self):
        self.dialog_ly=qtw.QHBoxLayout()
        self.dialog_ly.addWidget(self.sort_by_price)
        self.dialog_ly.addStretch()
        self.dialog_ly.addWidget(self.sort_by_date)
        self.setLayout(self.dialog_ly)
        self.show()
        self.exec()