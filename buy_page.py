import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import qdarkstyle
from qtwidgets import Toggle, AnimatedToggle
import mysql.connector
import json
class buy_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.prod_table_current = 0
        self.main_widget=main_widget

        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())
        self.supplier_name_s = qtw.QLineEdit()
        self.supplier_email_s = qtw.QLineEdit()
        self.supplier_address_s = qtw.QLineEdit()
        self.supplier_link_s = qtw.QLineEdit()
        self.supplier_name_s_label = qtw.QLabel("supplier Name")
        self.supplier_email_s_label = qtw.QLabel("supplier Email")
        self.supplier_address_s_label = qtw.QLabel("supplier Address")
        self.supplier_link_s_label = qtw.QLabel("supplier website Link")

        self.product_name = qtw.QComboBox()
        self.product_name.setEditable(True)
        self.product_quantity = qtw.QSpinBox()
        self.product_quantity.setRange(0, 1000000000)
        self.product_price = qtw.QSpinBox()
        self.product_price.setRange(0, 1000000000)
        self.product_selling_price = qtw.QSpinBox()
        self.product_selling_price.setRange(0, 1000000000)

        self.buy_package_name_label = qtw.QLabel("package name")
        self.buy_package_quantity_label = qtw.QLabel("quantity")
        self.buy_package_name = qtw.QComboBox()
        self.buy_package_quantity = qtw.QSpinBox()
        self.buy_package_quantity.setRange(0, 1000000000)
        self.add_buy_package_btn = qtw.QPushButton("Add package")
        self.add_buy_package_btn.setStyleSheet(self.main_widget.my_style.button_style())
        self.add_buy_package_btn.clicked.connect(self.add_buy_package_btn_fun)

        self.product_name_label = qtw.QLabel("Product name")
        self.product_quantity_label = qtw.QLabel("quantity")
        self.product_price_label = qtw.QLabel("price")
        self.product_selling_price_label = qtw.QLabel("selling price")
        self.add_b_prod = qtw.QPushButton("Add Product")
        self.add_b_prod.setStyleSheet(self.main_widget.my_style.button_style())
        self.add_b_prod.clicked.connect(self.add_b_prod_btn_fun)

        self.products_tabel = qtw.QTableWidget(2, 4)
        self.products_tabel.setHorizontalHeaderLabels(["Product", "Quantity", "Buy Price", "selling Price"])
        self.products_tabel.horizontalHeader().setStretchLastSection(True)
        self.products_tabel.verticalHeader().setStretchLastSection(True)

        self.total_tabel_b = qtw.QTableWidget(1, 3)
        self.total_tabel_b.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.total_tabel_b.horizontalHeader().setStretchLastSection(True)
        self.total_tabel_b.verticalHeader().setStretchLastSection(True)


        self.btn_group = qtw.QButtonGroup()
        self.stock_product = qtw.QRadioButton("Stock Product")
        self.used_product = qtw.QRadioButton("used Product")
        self.service_product = qtw.QRadioButton("service")
        self.btn_group.addButton(self.stock_product, )
        self.btn_group.addButton(self.used_product)
        self.btn_group.addButton(self.service_product)

        self.type_label = qtw.QLabel("Select Product type")

        self.dte = qtw.QDateEdit(qtc.QDate(qtc.QDate().currentDate()), self)
        self.dte.setCalendarPopup(True)  # have a calender to select date from
        self.dte_label = qtw.QLabel("Date")
        self.buy_submit = qtw.QPushButton("Submit")
        self.buy_submit.clicked.connect(self.buy_submit_btn_fun)
        self.buy_submit.setStyleSheet(self.main_widget.my_style.button_style())

        self.clear_buy_page = qtw.QPushButton("clear")
        self.clear_buy_page.clicked.connect(self.clear_buy_page_btn_fun)
        self.set_layout()



    def clear_buy_page_btn_fun(self):
        self.prod_table_current = 0
        self.products_tabel.clear()
        self.total_tabel_b.clear()
        self.products_tabel.setRowCount(2)
        self.product_name.setCurrentText("")
        self.product_quantity.setValue(0)
        self.product_price.setValue(0)
        self.product_selling_price.setValue(0)
        self.supplier_link_s.setText("")
        self.supplier_name_s.setText("")
        self.supplier_address_s.setText("")
        self.supplier_email_s.setText("")
        self.buy_package_name.setCurrentText("")
        self.buy_package_quantity.setValue(0)
        self.main_widget.set_lang()

    def add_b_prod_btn_fun(self):
        if self.products_tabel.rowCount()<=(self.prod_table_current):
            self.products_tabel.setRowCount(self.prod_table_current+2)
        ind=None
        for i in range(self.prod_table_current):
            if self.product_name.currentText()==self.products_tabel.item(i,0).text():
                ind=i
                break
        if ind  is not None:
            self.products_tabel.setItem(ind, 1,
                                        qtw.QTableWidgetItem(str(int(self.products_tabel.item(ind,1).text())+self.product_quantity.value())))
            self.products_tabel.setItem(ind, 2,
                                        qtw.QTableWidgetItem(str(self.product_price.value())))
            self.products_tabel.setItem(ind, 3,
                                        qtw.QTableWidgetItem(str(self.product_selling_price.value())))
        else:
            self.products_tabel.setItem(self.prod_table_current,0,qtw.QTableWidgetItem(str(self.product_name.currentText())))
            self.products_tabel.setItem(self.prod_table_current,1,qtw.QTableWidgetItem(str(self.product_quantity.value())))
            self.products_tabel.setItem(self.prod_table_current,2,qtw.QTableWidgetItem(str(self.product_price.value())))
            self.products_tabel.setItem(self.prod_table_current,3,qtw.QTableWidgetItem(str(self.product_selling_price.value())))
            self.prod_table_current += 1


        tot_cost=0
        total=0
        for i in range(self.prod_table_current):
            sell_price = int(self.products_tabel.item(i, 3).text())
            buy_price = int(self.products_tabel.item(i, 2).text())
            tot_cost += int(self.products_tabel.item(i, 1).text()) * buy_price
            total += int(self.products_tabel.item(i, 1).text()) * max(buy_price, sell_price)
        total_profit = total - tot_cost

        self.total_tabel_b.setItem(0,0,qtw.QTableWidgetItem(str(tot_cost)))
        self.total_tabel_b.setItem(0,1,qtw.QTableWidgetItem(str(total)))
        self.total_tabel_b.setItem(0,2,qtw.QTableWidgetItem(str(total_profit)))

        self.product_name.setCurrentText("")
        self.product_quantity.setValue(0)
        self.product_price.setValue(0)
        self.product_selling_price.setValue(0)
        self.repaint()





    def add_buy_package_btn_fun(self):
        p_name = self.buy_package_name.currentText()
        p_qt = int(self.buy_package_quantity.value())
        prods = self.main_widget.new_package_widget.packages_dict[p_name]

        for name, qt in prods:
            ind = None
            qt = int(qt)
            for i in range(self.prod_table_current):
                if name == self.products_tabel.item(i, 0).text():
                    ind = i

            if self.products_tabel.rowCount() <= self.prod_table_current:
                self.products_tabel.setRowCount(self.prod_table_current + 2)
            if ind is not None:
                self.products_tabel.setItem(ind, 1, qtw.QTableWidgetItem(
                    str(int(self.products_tabel.item(ind, 1).text()) + (qt * p_qt))))
            else:
                self.products_tabel.setItem(self.prod_table_current, 0, qtw.QTableWidgetItem(name))
                self.products_tabel.setItem(self.prod_table_current, 1, qtw.QTableWidgetItem(str(qt * p_qt)))
                self.products_tabel.setItem(self.prod_table_current, 2,
                                        qtw.QTableWidgetItem(str(self.main_widget.stock_widget.stock_data[name][1])))
                self.products_tabel.setItem(self.prod_table_current, 3,
                                        qtw.QTableWidgetItem(str(self.main_widget.stock_widget.stock_data[name][2])))
                self.prod_table_current += 1
        tot_cost = 0
        total = 0

        for i in range(self.prod_table_current):
            sell_price=int(self.products_tabel.item(i, 3).text())
            buy_price=int(self.products_tabel.item(i, 2).text())
            tot_cost += int(self.products_tabel.item(i, 1).text()) * buy_price
            total += int(self.products_tabel.item(i, 1).text()) *max(buy_price,sell_price)
        total_profit = total - tot_cost

        self.total_tabel_b.setItem(0, 0, qtw.QTableWidgetItem(str(tot_cost)))
        self.total_tabel_b.setItem(0, 1, qtw.QTableWidgetItem(str(total)))
        self.total_tabel_b.setItem(0, 2, qtw.QTableWidgetItem(str(total_profit)))


        self.buy_package_name.setCurrentText("")
        self.buy_package_quantity.setValue(0)
        self.repaint()








    def buy_submit_btn_fun(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '',"Are you sure you want to save this import process", qm.Yes | qm.No)
        if ret==qm.Yes:
            supplier_name=self.supplier_name_s.text()
            supplier_email=self.supplier_email_s.text()
            supplier_address=self.supplier_address_s.text()
            supplier_link=self.supplier_link_s.text()
            date=self.dte.date().toString(qtc.Qt.ISODate)
            tot_cost=self.total_tabel_b.item(0,0).text()
            total=self.total_tabel_b.item(0,1).text()
            type=self.btn_group.checkedButton().text()
            products=[]
            for i in range(self.prod_table_current):
                products.append(self.products_tabel.item(i,0).text()+":"+f"""{self.products_tabel.item(i,1).text()},{self.products_tabel.item(i,2).text()},{self.products_tabel.item(i,3).text()}""")
            products='|'.join(products)
            try:
                sql_stuff="INSERT INTO imports (supplier_Name,Email,Address,Link,Products,type,cost,total,Losses,Date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                self.main_widget.my_cursor.execute(sql_stuff,(supplier_name,supplier_email,supplier_address,supplier_link,products,type,int(tot_cost),int(total),0,date))
                print(supplier_name,supplier_email,supplier_address,supplier_link,products,type,int(tot_cost),int(total),0,date)
            except:
                print('mamamamamamamama')
            if type=='Stock Product' or type == "منتج مخازن" :
                for i in range(self.prod_table_current):
                    name=self.products_tabel.item(i,0).text()
                    qt=self.products_tabel.item(i, 1).text()
                    buy_price=self.products_tabel.item(i, 2).text()
                    sell_price=self.products_tabel.item(i,3).text()
                    try:
                        sql_stuff = "INSERT INTO stock  (product,availble,buying_price,selling_price) VALUES(%s,%s,%s,%s);"
                        self.main_widget.my_cursor.execute(sql_stuff, (name,int(qt),int(buy_price),int(sell_price)))
                    except:
                        try:
                            sql_stuff = "UPDATE stock SET availble=availble+%s WHERE product=%s"
                            self.main_widget.my_cursor.execute(sql_stuff, (qt,name))

                            sql_stuff = "UPDATE stock SET buying_price=%s WHERE product=%s"
                            self.main_widget.my_cursor.execute(sql_stuff, (buy_price,name))

                            sql_stuff = "UPDATE stock SET sell_price=%s WHERE product=%s"
                            self.main_widget.my_cursor.execute(sql_stuff, (sell_price,name))
                        except:
                            pass
            self.main_widget.mydb.commit()
            self.main_widget.stock_widget.get_stock()
            self.main_widget.update_cmb()
            self.clear_buy_page_btn_fun()
            self.get_imports()
    def get_imports(self):
        self.main_widget.my_cursor.execute("SELECT * FROM imports")
        data=self.main_widget.my_cursor.fetchall()
        if self.main_widget.database_widget.imp_widget.imp_tabel.rowCount()<len(data):
            self.main_widget.database_widget.imp_widget.imp_tabel.setRowCount(len(data))
        self.imports_data=dict()
        if self.main_widget.database_widget.imp_widget.imp_tabel.rowCount() < len(data):
            self.main_widget.database_widget.imp_widget.imp_tabel.setRowCount(len(data))
        for i,info in enumerate(data):
            code,name,email,address,link,products,process_type,cost,total,losses,date=info
            self.imports_data[str(code)]=[name,email,address,link,products,process_type,cost,total,losses,date]

            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,0,qtw.QTableWidgetItem(str(name)))
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,1,qtw.QTableWidgetItem(str(email)))
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,2,qtw.QTableWidgetItem(str(address)))
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,3,qtw.QTableWidgetItem(str(link)))
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,4,qtw.QTableWidgetItem(str(products)))
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,5,qtw.QTableWidgetItem(str(process_type)))

            item = qtw.QTableWidgetItem()
            item.setData(qtc.Qt.DisplayRole, cost)
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,6,item)

            item = qtw.QTableWidgetItem()
            item.setData(qtc.Qt.DisplayRole, total)
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i, 7, item)

            item = qtw.QTableWidgetItem()
            item.setData(qtc.Qt.DisplayRole, losses)
            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,8,item)


            self.main_widget.database_widget.imp_widget.imp_tabel.setItem(i,9,qtw.QTableWidgetItem(str(date)))

    def set_layout(self):
        self.buy_ly = qtw.QVBoxLayout()
        self.buy_ly.addWidget(self.supplier_name_s_label)
        self.buy_ly.addWidget(self.supplier_name_s)

        self.buy_ly.addWidget(self.supplier_email_s_label)
        self.buy_ly.addWidget(self.supplier_email_s)

        self.buy_ly.addWidget(self.supplier_address_s_label)
        self.buy_ly.addWidget(self.supplier_address_s)

        self.buy_ly.addWidget(self.supplier_link_s_label)
        self.buy_ly.addWidget(self.supplier_link_s)

        self.product_ly = qtw.QHBoxLayout()
        self.t1 = qtw.QVBoxLayout()
        self.t1.addWidget(self.product_name_label)
        self.t1.addWidget(self.product_name)

        self.t2 = qtw.QVBoxLayout()
        self.t2.addWidget(self.product_quantity_label)
        self.t2.addWidget(self.product_quantity)

        self.t3 = qtw.QVBoxLayout()
        self.t3.addWidget(self.product_price_label)
        self.t3.addWidget(self.product_price)

        self.t4 = qtw.QVBoxLayout()
        self.t4.addWidget(self.product_selling_price_label)
        self.t4.addWidget(self.product_selling_price)

        self.t5 = qtw.QVBoxLayout()
        self.t5.addWidget(self.dte_label)
        self.t5.addWidget(self.dte)
        self.product_ly.addLayout(self.t1)
        self.product_ly.addLayout(self.t2)
        self.product_ly.addLayout(self.t3)
        self.product_ly.addLayout(self.t4)
        self.product_ly.addLayout(self.t5)
        self.product_ly.addStretch()
        self.product_ly.addWidget(self.add_b_prod)
        self.buy_ly.addLayout(self.product_ly)

        self.package_ly_buy = qtw.QHBoxLayout()
        self.package_name_ly = qtw.QVBoxLayout()
        self.package_name_ly.addWidget(self.buy_package_name_label)
        self.package_name_ly.addWidget(self.buy_package_name)
        self.package_qt_ly = qtw.QVBoxLayout()
        self.package_qt_ly.addWidget(self.buy_package_quantity_label)
        self.package_qt_ly.addWidget(self.buy_package_quantity)
        self.package_ly_buy.addLayout(self.package_name_ly)
        self.package_ly_buy.addLayout(self.package_qt_ly)
        self.package_ly_buy.addStretch()
        self.package_ly_buy.addWidget(self.add_buy_package_btn)
        self.buy_ly.addLayout(self.package_ly_buy)

        self.h3 = qtw.QHBoxLayout()
        self.h4 = qtw.QHBoxLayout()
        self.h3.addWidget(self.products_tabel)
        self.h3.addStretch()
        self.h4.addWidget(self.total_tabel_b)
        self.h4.addStretch()

        self.buy_ly.addLayout(self.h3)
        # self.buy_ly.addStretch()

        self.buy_ly.addLayout(self.h4)
        self.buy_ly.addStretch()

        self.buy_ly.addWidget(self.type_label)
        self.type_ly = qtw.QHBoxLayout()
        self.type_ly.addWidget(self.stock_product)
        self.type_ly.addWidget(self.used_product)
        self.type_ly.addWidget(self.service_product)
        self.buy_ly.addLayout(self.type_ly)
        self.submit_clear_buy_ly = qtw.QHBoxLayout()
        self.submit_clear_buy_ly.addWidget(self.buy_submit)
        self.submit_clear_buy_ly.addStretch()
        self.submit_clear_buy_ly.addWidget(self.clear_buy_page)
        self.buy_ly.addLayout(self.submit_clear_buy_ly)
        self.buy_ly.addStretch()
        self.setLayout(self.buy_ly)
