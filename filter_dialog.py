import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from range_slider import RangeSlider
from styles import styles
class filter_dialog(qtw.QDialog):
    def __init__(self,main_widget,table,col_ind):
        super().__init__()
        self.main_widget=main_widget
        self.col_ind=col_ind
        self.table=table
        max_val = max(list([int(self.table.item(i, self.col_ind).text()) for i in range(self.table.rowCount()) if (self.table.item(i,self.col_ind) is not None)]))
        print(max_val)
        self.dialog_style = styles(self)
        self.filter_btn=qtw.QPushButton("Filter")
        self.filter_btn.setStyleSheet(self.dialog_style.button_style())


        self.low_spinbox=qtw.QSpinBox()
        self.low_spinbox.setRange(0,max_val)
        self.low_spinbox.setStyleSheet(self.dialog_style.spin_box_style())
        self.low_spinbox.valueChanged.connect(self.spin_box_change)
        self.high_spinbox=qtw.QSpinBox()
        self.high_spinbox.setRange(0,max_val)
        self.high_spinbox.setStyleSheet(self.dialog_style.spin_box_style())
        self.high_spinbox.valueChanged.connect(self.spin_box_change)

        self.filter_btn.clicked.connect(self.filter_btn_fun)


        self.filter_range=RangeSlider(qtc.Qt.Horizontal)
        self.filter_range.setMinimum(0)
        self.filter_range.setMaximum(max_val)
        self.filter_range.setMinimumHeight(30)
        self.filter_range.setLow(0)
        self.filter_range.setHigh(max_val)
        self.filter_range.sliderMoved.connect(self.filter_range_print)


        self.reset_btn=qtw.QPushButton("Reset")
        self.reset_btn.setStyleSheet(self.dialog_style.button_style())
        self.reset_btn.clicked.connect(self.reset_btn_fun)

        self.set_layout()
    def filter_range_print(self):
        first,second=self.filter_range.low(),self.filter_range.high()
        self.low_spinbox.setValue(first)
        self.high_spinbox.setValue(second)
    def spin_box_change(self):
        self.filter_range.setLow(self.low_spinbox.value())
        self.filter_range.setHigh(self.high_spinbox.value())


    def filter_btn_fun(self):
        first, second = self.filter_range.low(), self.filter_range.high()
        for i in range(self.table.rowCount()):
            if self.table.item(i,self.col_ind) is not None:
                if int(self.table.item(i,self.col_ind).text()) in range(first,second+1):
                    pass
                else:
                    self.table.removeRow(i)
    def reset_btn_fun(self):
        self.main_widget.stock_widget.get_stock()
        self.main_widget.add_emp_page_widget.get_employees()
        self.main_widget.buy_product_widget.get_imports()
        self.main_widget.sell_Product.get_exports()
        self.main_widget.new_package_widget.load_products_into_package()
        self.main_widget.update_cmb()


    def set_layout(self):
        self.h_ly=qtw.QHBoxLayout()
        self.v_ly=qtw.QVBoxLayout()
        self.h_ly.addWidget(self.filter_btn)
        self.h_ly.addStretch()
        self.h_ly.addWidget(self.reset_btn)
        self.v_ly.addLayout(self.h_ly)
        self.v_ly.addStretch()
        self.v_ly.addWidget(self.filter_range)
        self.h2_ly=qtw.QHBoxLayout()
        self.h2_ly.addWidget(self.low_spinbox)
        self.h2_ly.addStretch()
        self.h2_ly.addWidget(self.high_spinbox)
        self.v_ly.addLayout(self.h2_ly)

        self.setLayout(self.v_ly)
        self.show()
        self.exec()