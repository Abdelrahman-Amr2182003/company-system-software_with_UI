import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import json
class new_package_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.load_packages_file()
        self.package_tabel_current=0
        self.main_widget=main_widget
        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())
        self.package_name_label = qtw.QLabel("Package Name")
        self.package_name = qtw.QComboBox()
        self.package_name.currentIndexChanged.connect(self.load_products_into_package)
        self.package_name.setEditable(True)

        self.add_product_to_package_label = qtw.QLabel("Product")
        self.add_product_to_package = qtw.QComboBox()
        self.product_qt_package = qtw.QSpinBox()
        self.product_qt_package.setRange(0, 1000000000)

        self.add_btn = qtw.QPushButton("Add")
        self.add_btn.clicked.connect(self.add_btn_fun)
        self.package_tabel = qtw.QTableWidget(5, 2)
        self.package_tabel.setHorizontalHeaderLabels(["product Name", "Quantity"])
        self.package_tabel.horizontalHeader().setStretchLastSection(True)
        self.package_tabel.verticalHeader().setStretchLastSection(True)

        self.save_btn = qtw.QPushButton("Save package")
        self.save_btn.clicked.connect(self.save_package_btn_fun)

        self.remove_btn = qtw.QPushButton("remove Package")
        self.remove_btn.clicked.connect(self.remove_package_btn_fun)

        self.clear_packages_btn = qtw.QPushButton("Clear")
        self.clear_packages_btn.clicked.connect(self.clear_package_btn_fun)
        self.set_layout()
    def load_packages_file(self):
        self.packages_dict = dict()
        try:
            with open('packages.json', 'r') as f:
                self.packages_dict = json.load(f)
        except:
            pass
    def add_btn_fun(self):
        data = []
        for i in range(self.package_tabel_current):

            data.append(self.package_tabel.item(i, 0).text())

        if self.package_tabel.rowCount()<=self.package_tabel_current:
            self.package_tabel.setRowCount(self.package_tabel_current+2)
        if self.add_product_to_package.currentText() in data:
            for i in range(self.package_tabel_current):
                if self.add_product_to_package.currentText() ==self.package_tabel.item(i,0).text():
                    self.package_tabel.setItem(i, 1,qtw.QTableWidgetItem(str(self.product_qt_package.value())))
        else:
            self.package_tabel.setItem(self.package_tabel_current,0,qtw.QTableWidgetItem(str(self.add_product_to_package.currentText())))

            self.package_tabel.setItem(self.package_tabel_current,1,qtw.QTableWidgetItem(str(self.product_qt_package.value())))

        self.add_product_to_package.setCurrentText("")

        self.product_qt_package.setValue(0)

        self.package_tabel_current+=1

    def load_products_into_package(self):
        self.package_tabel.clear()
        self.main_widget.set_lang()
        self.package_tabel_current=0
        name=self.package_name.currentText()
        if name in list(self.packages_dict.keys()):
            prods=self.packages_dict[name]
            for prod in prods:
                if self.package_tabel.rowCount() <= self.package_tabel_current:
                    self.package_tabel.setRowCount(self.package_tabel_current + 2)
                self.package_tabel.setItem(self.package_tabel_current, 0,
                                           qtw.QTableWidgetItem(str(prod[0])))

                self.package_tabel.setItem(self.package_tabel_current, 1,qtw.QTableWidgetItem(str(prod[1])))
                self.package_tabel_current+=1
        self.main_widget.set_lang()

    def save_package_btn_fun(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '',"Are you sure you want to save this package", qm.Yes | qm.No)
        if ret==qm.Yes:
            name=self.package_name.currentText()
            products=[]
            for i in range(self.package_tabel_current):
                prod=self.package_tabel.item(i,0).text()
                qt=self.package_tabel.item(i,1).text()
                products.append([prod,qt])
            self.packages_dict[name]=products

        self.clear_package_btn_fun()
        self.main_widget.update_cmb()



    def remove_package_btn_fun(self):
        self.packages_dict.pop(self.package_name.currentText())
        self.main_widget.update_cmb()



    def clear_package_btn_fun(self):

        self.package_tabel_current = 0
        self.package_tabel.clear()
        self.add_product_to_package.setCurrentText("")
        self.product_qt_package.setValue(0)
        self.package_tabel.setRowCount(5)
        self.main_widget.set_lang()

    def set_layout(self):
        self.package_ly = qtw.QVBoxLayout()
        self.package_ly.addWidget(self.package_name_label)
        self.package_ly.addWidget(self.package_name)
        
        self.package_ly.addWidget(self.add_product_to_package_label)

        self.part_h_ly = qtw.QHBoxLayout()
        self.part_h_ly.addWidget(self.add_product_to_package)
        self.part_h_ly.addStretch()
        self.part_h_ly.addWidget(self.product_qt_package)
        self.part_h_ly.addStretch()
        self.part_h_ly.addWidget(self.add_btn)
        self.part_h_ly.addStretch()
        self.package_ly.addLayout(self.part_h_ly)

        self.tabel_h_ly = qtw.QHBoxLayout()
        self.tabel_h_ly.addWidget(self.package_tabel)
        self.tabel_h_ly.addStretch()
        self.package_ly.addLayout(self.tabel_h_ly)
        self.package_ly.addStretch()
        self.save_rem_ly = qtw.QHBoxLayout()
        self.save_rem_ly.addStretch()
        self.save_rem_ly.addWidget(self.save_btn)
        self.save_rem_ly.addStretch()
        self.save_rem_ly.addWidget(self.clear_packages_btn)
        self.save_rem_ly.addStretch()
        self.save_rem_ly.addWidget(self.remove_btn)
        self.save_rem_ly.addStretch()
        self.package_ly.addLayout(self.save_rem_ly)
        self.setLayout(self.package_ly)
