import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class sell_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.sell_table_current=0
        self.main_widget=main_widget
        self.setStyleSheet(self.main_widget.my_style.main_widgets_style())
        self.client_name = qtw.QLineEdit()
        self.client_email = qtw.QLineEdit()
        self.client_address = qtw.QLineEdit()
        self.client_link = qtw.QLineEdit()
        self.client_name_label = qtw.QLabel("client Name")
        self.client_email_label = qtw.QLabel("client Email")
        self.client_address_label = qtw.QLabel("client Address")
        self.client_link_label = qtw.QLabel("client website Link")

        self.add_product = qtw.QComboBox()

        self.add_Packages = qtw.QComboBox()
        self.packages_qt = qtw.QSpinBox()
        self.packages_qt.setRange(0, 1000000000)
        self.product_qt = qtw.QSpinBox()
        self.product_qt.setRange(0, 1000000000)

        self.add_service_type = qtw.QLineEdit()
        self.add_service_fees = qtw.QSpinBox()
        self.add_service_fees.setRange(0, 1000000000)
        self.service_cost = qtw.QSpinBox()
        self.service_cost.setRange(0, 1000000000)
        self.service_cost_label = qtw.QLabel("Service Cost")
        self.service_qt = qtw.QSpinBox()
        self.service_qt.setRange(0, 1000000000)
        self.service_qt_label = qtw.QLabel("quantity")
        self.add_service_btn = qtw.QPushButton("Add service")
        self.add_service_btn.clicked.connect(self.add_service_btn_fun)

        self.add_product_label = qtw.QLabel("Product Name")
        self.add_Packegas_label = qtw.QLabel("package Name")
        self.product_qt_label = qtw.QLabel("Quantity")
        self.packages_qt_label = qtw.QLabel("Quantity")
        self.add_service_fees_label = qtw.QLabel("Service Fees")
        self.add_service_type_label = qtw.QLabel("Service name")

        self.prod_tabel = qtw.QTableWidget(5, 4)
        self.prod_tabel.setHorizontalHeaderLabels(["Product", "Quantity", "Buy Price", "selling Price"])
        self.prod_tabel.horizontalHeader().setStretchLastSection(True)
        self.prod_tabel.verticalHeader().setStretchLastSection(True)

        self.total_tabel = qtw.QTableWidget(1, 3)
        self.total_tabel.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.total_tabel.horizontalHeader().setStretchLastSection(True)
        self.total_tabel.verticalHeader().setStretchLastSection(True)

        # self.total_tabel.setFixedHeight(75)
        # self.total_tabel.setStyleSheet("min-width:50px;")

        self.sell_submit = qtw.QPushButton("Submit")
        self.sell_submit.setStyleSheet(self.main_widget.my_style.button_style())
        self.sell_submit.clicked.connect(self.sell_submit_btn_fun)
        self.clear_sell_page_btn = qtw.QPushButton("Clear")
        self.clear_sell_page_btn.setStyleSheet(self.main_widget.my_style.button_style())
        self.clear_sell_page_btn.clicked.connect(self.clear_sell_page_btn_fun)

        self.add_product_btn = qtw.QPushButton("Add product")
        self.add_product_btn.clicked.connect(self.add_product_btn_fun)
        self.add_Packages_btn = qtw.QPushButton("Add package")
        self.add_Packages_btn.clicked.connect(self.add_package_btn_fun)
        self.sell_date = qtw.QDateEdit(qtc.QDate(qtc.QDate().currentDate()), self)
        self.sell_date.setCalendarPopup(True)  # have a calender to select date from
        self.sell_date_label = qtw.QLabel("Date")
        self.set_layout()

    def add_product_btn_fun(self):
        name=self.add_product.currentText()
        ind=None
        for i in range(self.sell_table_current):
            if name==self.prod_tabel.item(i, 0).text():
                ind=i

        if self.prod_tabel.rowCount()<=self.sell_table_current:
            self.prod_tabel.setRowCount(self.sell_table_current+2)

        if name in list(self.main_widget.stock_widget.stock_data.keys()):
            if  self.main_widget.stock_widget.stock_data[name][0]>=int(self.product_qt.value()):
                if ind is not None:
                    self.prod_tabel.setItem(ind, 1,qtw.QTableWidgetItem(str(int(self.prod_tabel.item(ind,1).text())+int(self.product_qt.value() ) ) ) )
                else:
                    self.prod_tabel.setItem(self.sell_table_current,0,qtw.QTableWidgetItem(name))
                    self.prod_tabel.setItem(self.sell_table_current,1,qtw.QTableWidgetItem(str(self.product_qt.value())))
                    self.prod_tabel.setItem(self.sell_table_current,2,qtw.QTableWidgetItem(str(self.main_widget.stock_widget.stock_data[name][1])))
                    self.prod_tabel.setItem(self.sell_table_current,3,qtw.QTableWidgetItem(str(self.main_widget.stock_widget.stock_data[name][2])))
                    self.sell_table_current += 1

            else:
                res=qtw.QMessageBox.information(self,"Quantity",f"not enough {name} in stock")

        else:
                res = qtw.QMessageBox.information(self,"invalid product",f"{name} not in stock")
        self.update_sell_total_table()
    def add_package_btn_fun(self):

        p_name=self.add_Packages.currentText()
        p_qt=int(self.packages_qt.value())
        prods=self.main_widget.new_package_widget.packages_dict[p_name]

        valid=True
        for name,qt in prods:
            qt=int(qt)
            if name in list(self.main_widget.stock_widget.stock_data.keys()):
                if self.main_widget.stock_widget.stock_data[name][0]>=qt*p_qt:
                    pass
                else:
                    valid=False
            else:
                valid = False
        if valid:
            for name,qt in prods:
                qt=int(qt)
                ind = None
                for i in range(self.sell_table_current):
                    if name==self.prod_tabel.item(i, 0).text():
                        ind=i

                if self.prod_tabel.rowCount()<=self.sell_table_current:
                    self.prod_tabel.setRowCount(self.sell_table_current+2)
                if ind is not None:
                    self.prod_tabel.setItem(ind, 1, qtw.QTableWidgetItem(
                        str(int(self.prod_tabel.item(ind, 1).text()) + (qt * p_qt))))
                else:
                    self.prod_tabel.setItem(self.sell_table_current,0,qtw.QTableWidgetItem(name))
                    self.prod_tabel.setItem(self.sell_table_current,1,qtw.QTableWidgetItem(str(qt*p_qt)))
                    self.prod_tabel.setItem(self.sell_table_current,2,qtw.QTableWidgetItem(str(self.main_widget.stock_widget.stock_data[name][1])))
                    self.prod_tabel.setItem(self.sell_table_current,3,qtw.QTableWidgetItem(str(self.main_widget.stock_widget.stock_data[name][2])))
                    self.sell_table_current += 1

            self.update_sell_total_table()


        else:
            res = qtw.QMessageBox.information(self, "invalid package","Package is invalid right now")
            self.update_sell_total_table()
    def add_service_btn_fun(self):
        if self.prod_tabel.rowCount()<=self.sell_table_current:
            self.prod_tabel.setRowCount(self.sell_table_current+2)
        self.prod_tabel.setItem(self.sell_table_current,0,qtw.QTableWidgetItem(self.add_service_type.text()))
        self.prod_tabel.setItem(self.sell_table_current,1,qtw.QTableWidgetItem(str(self.service_qt.value())))
        self.prod_tabel.setItem(self.sell_table_current, 2, qtw.QTableWidgetItem(str(self.service_cost.value())))
        self.prod_tabel.setItem(self.sell_table_current, 3, qtw.QTableWidgetItem(str(self.add_service_fees.value())))
        self.sell_table_current+=1
        self.update_sell_total_table()
    def update_sell_total_table(self):#cost accuired profit
        tot_cost=0
        tot_acc=0
        for i in range(self.sell_table_current):
            tot_cost+=(int(self.prod_tabel.item(i,2).text())*int(self.prod_tabel.item(i,1).text()))
            tot_acc+=(int(self.prod_tabel.item(i,3).text())*int(self.prod_tabel.item(i,1).text()))
        tot_profit=tot_acc-tot_cost
        self.total_tabel.setItem(0,0,qtw.QTableWidgetItem(str(tot_cost)))
        self.total_tabel.setItem(0,1,qtw.QTableWidgetItem(str(tot_acc)))
        self.total_tabel.setItem(0,2,qtw.QTableWidgetItem(str(tot_profit)))

    def clear_sell_page_btn_fun(self):
        self.prod_tabel.clear()
        self.total_tabel.clear()
        self.client_link.setText("")
        self.client_address.setText("")
        self.client_name.setText("")
        self.client_email.setText("")
        self.add_service_type.setText("")
        self.add_service_fees.setValue(0)
        self.service_cost.setValue(0)
        self.product_qt.setValue(0)
        self.packages_qt.setValue(0)
        self.sell_table_current=0
        self.main_widget.set_lang()
    def sell_submit_btn_fun(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to save this export process", qm.Yes | qm.No)
        if ret == qm.Yes:
            name=self.client_name.text()
            email=self.client_email.text()
            address=self.client_address.text()
            link=self.client_link.text()
            date=self.sell_date.date().toString(qtc.Qt.ISODate)
            products = []
            tot_cost=int(self.total_tabel.item(0,0).text())
            total=int(self.total_tabel.item(0,1).text())
            profit=int(self.total_tabel.item(0,2).text())
            for i in range(self.sell_table_current):
                products.append(self.prod_tabel.item(i,0).text() + ":" + f"""{self.prod_tabel.item(i,1).text()},{self.prod_tabel.item(i,2).text()},{self.prod_tabel.item(i,3).text()}""")

            products = '|'.join(products)
            try:
                sql_stuff="""INSERT INTO exports(client_Name,Email,Address,Link,Products,cost,total,profit,Losses,date)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
                self.main_widget.my_cursor.execute(sql_stuff,(name,email,address,link,products,tot_cost,total,profit,0,date))
            except:
                pass
            for i in range(self.sell_table_current):
                name=self.prod_tabel.item(i,0).text()
                prod_qt=self.prod_tabel.item(i,1).text()
                if name in list(self.main_widget.stock_widget.stock_data.keys()):
                    try:

                        sql_stuff="""UPDATE stock SET sold=sold+%s WHERE Product=%s"""
                        self.main_widget.my_cursor.execute(sql_stuff,(int(prod_qt),name))
                    except:
                        pass
                    try:
                        sql_stuff="""UPDATE stock SET availble=availble-%s WHERE Product=%s"""
                        self.main_widget.my_cursor.execute(sql_stuff,(prod_qt,name))
                    except:
                        pass

            self.main_widget.mydb.commit()
            self.clear_sell_page_btn_fun()
            self.main_widget.stock_widget.get_stock()
            self.main_widget.update_cmb()
            self.get_exports()
    def get_exports(self):

        self.main_widget.my_cursor.execute("SELECT * FROM exports")
        data = self.main_widget.my_cursor.fetchall()
        if self.main_widget.database_widget.exp_widget.exports_tabel.rowCount()<len(data):
            self.main_widget.database_widget.exp_widget.exports_tabel.setRowCount(len(data))
        self.exports_data = dict()
        if self.main_widget.database_widget.exp_widget.exports_tabel.rowCount()<len(data):
            self.main_widget.database_widget.exp_widget.exports_tabel.setRowCount(len(data))
        for i, info in enumerate(data):
            code, name, email, address, link, products, cost, total,profit, losses, date = info
            self.exports_data[str(code)] = [code, name, email, address, link, products, cost, total,profit, losses, date]

            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 0, qtw.QTableWidgetItem(str(name)))
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 1, qtw.QTableWidgetItem(str(email)))
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 2, qtw.QTableWidgetItem(str(address)))
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 3, qtw.QTableWidgetItem(str(link)))
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 4, qtw.QTableWidgetItem(str(products)))
            item = qtw.QTableWidgetItem()
            item.setData(qtc.Qt.DisplayRole,cost)
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 5, item)
            item = qtw.QTableWidgetItem()
            item.setData(qtc.Qt.DisplayRole, profit)
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 6, item)
            item = qtw.QTableWidgetItem()
            item.setData(qtc.Qt.DisplayRole, losses)
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 7, item)
            self.main_widget.database_widget.exp_widget.exports_tabel.setItem(i, 8, qtw.QTableWidgetItem(str(date)))

    def set_layout(self):

        self.sell_Product_ly = qtw.QVBoxLayout()
        self.sell_Product_ly.addWidget(self.client_name_label)
        self.sell_Product_ly.addWidget(self.client_name)

        self.sell_Product_ly.addWidget(self.client_email_label)
        self.sell_Product_ly.addWidget(self.client_email)

        self.sell_Product_ly.addWidget(self.client_address_label)
        self.sell_Product_ly.addWidget(self.client_address)

        self.sell_Product_ly.addWidget(self.client_link_label)
        self.sell_Product_ly.addWidget(self.client_link)

        self.s_product_ly = qtw.QHBoxLayout()
        self.s_t1 = qtw.QVBoxLayout()
        self.s_t1.addWidget(self.add_product_label)
        self.s_t1.addWidget(self.add_product)
        self.s_t2 = qtw.QVBoxLayout()
        self.s_t2.addWidget(self.product_qt_label)
        self.s_t2.addWidget(self.product_qt)
        self.s_product_ly.addLayout(self.s_t1)
        self.s_product_ly.addLayout(self.s_t2)
        self.s_product_ly.addStretch()
        self.s_product_ly.addWidget(self.add_product_btn)
        self.sell_Product_ly.addLayout(self.s_product_ly)

        self.s_package_ly = qtw.QHBoxLayout()
        self.s_t3 = qtw.QVBoxLayout()
        self.s_t3.addWidget(self.add_Packegas_label)
        self.s_t3.addWidget(self.add_Packages)
        self.s_t4 = qtw.QVBoxLayout()
        self.s_t4.addWidget(self.packages_qt_label)
        self.s_t4.addWidget(self.packages_qt)
        self.s_package_ly.addLayout(self.s_t3)
        self.s_package_ly.addLayout(self.s_t4)
        self.s_package_ly.addStretch()
        self.s_package_ly.addWidget(self.add_Packages_btn)
        self.sell_Product_ly.addLayout(self.s_package_ly)

        self.s_service_ly = qtw.QHBoxLayout()
        self.s_t5 = qtw.QVBoxLayout()
        self.s_t5.addWidget(self.add_service_type_label)
        self.s_t5.addWidget(self.add_service_type)
        self.s_t6 = qtw.QVBoxLayout()
        self.s_t6.addWidget(self.add_service_fees_label)
        self.s_t6.addWidget(self.add_service_fees)
        self.s_t7 = qtw.QVBoxLayout()
        self.s_t7.addWidget(self.service_cost_label)
        self.s_t7.addWidget(self.service_cost)
        self.s_t8 = qtw.QVBoxLayout()
        self.s_t8.addWidget(self.service_qt_label)
        self.s_t8.addWidget(self.service_qt)

        self.s_service_ly.addLayout(self.s_t5)
        self.s_service_ly.addLayout(self.s_t8)
        self.s_service_ly.addLayout(self.s_t6)
        self.s_service_ly.addLayout(self.s_t7)
        self.s_service_ly.addLayout(self.s_t8)
        self.s_service_ly.addStretch()
        self.s_service_ly.addWidget(self.add_service_btn)

        self.sell_Product_ly.addLayout(self.s_service_ly)
        self.sell_Product_ly.addWidget(self.sell_date_label)
        self.sell_Product_ly.addWidget(self.sell_date)

        self.h1 = qtw.QHBoxLayout()
        self.h2 = qtw.QHBoxLayout()
        self.h1.addWidget(self.prod_tabel)
        self.h1.addStretch()
        self.h2.addWidget(self.total_tabel)
        self.h2.addStretch()
        self.sell_Product_ly.addLayout(self.h1)
        self.sell_Product_ly.addLayout(self.h2)
        self.sell_Product_ly.addStretch()

        self.submit_clear_ly = qtw.QHBoxLayout()
        self.submit_clear_ly.addWidget(self.sell_submit)
        self.submit_clear_ly.addStretch()
        self.submit_clear_ly.addWidget(self.clear_sell_page_btn)
        self.sell_Product_ly.addLayout(self.submit_clear_ly)
        self.sell_Product_ly.addStretch()
        self.setLayout(self.sell_Product_ly)
