import PyQt5.QtWidgets as qtw
from bars import data_base_bar
import PyQt5.QtCore as qtc
from import_export_csv import import_export_csv
from database_home_page import database_home_page
import pandas as pd
import datetime

class employees_table_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.edited_items=[]
        self.redo_items=[]
        self.main_widget=main_widget
        self.emp_tabel = qtw.QTableWidget(20, 5)
        self.emp_tabel.setHorizontalHeaderLabels(
            ["Code", "Name", "Position", "Salary", "hiring date"])
        self.emp_tabel.horizontalHeader().setStretchLastSection(True)
        self.emp_tabel.verticalHeader().setStretchLastSection(True)
        self.emp_tabel.itemDoubleClicked.connect(self.get_item_editited)

        self.add_emp = qtw.QPushButton("Add")
        self.add_emp.clicked.connect(self.add_employee_btn_fun)
        self.add_emp.setStyleSheet(self.main_widget.my_style.button_style())
        self.remove_emp = qtw.QPushButton("remove")
        self.remove_emp.setStyleSheet(self.main_widget.my_style.button_style())
        self.remove_emp.clicked.connect(self.remove_emp_btn_fun)


        self.save_emp = qtw.QPushButton("Save")
        self.save_emp.setStyleSheet(self.main_widget.my_style.button_style())
        self.save_emp.clicked.connect(self.save_table)
        self.set_layout()

    def remove_emp_btn_fun(self):
        indices = self.emp_tabel.selectionModel().selectedRows()
        for index in sorted(indices):
            self.edited_items.append(['rem', index.row(), [self.emp_tabel.item(index.row(), i).text() for i in
                                                           range(self.emp_tabel.columnCount())]])
            self.emp_tabel.removeRow(index.row())
    def get_item_editited(self,item):
            self.edited_items.append(['edit',[self.emp_tabel.currentRow(),self.emp_tabel.currentColumn(),self.emp_tabel.item(self.emp_tabel.currentRow(),self.emp_tabel.currentColumn()).text()]])
    def undo(self):
        if len(self.edited_items)>0:
            if self.edited_items[-1][0]=='edit':
                typee,data=self.edited_items[-1]
                row, col, text=data
                self.redo_items.append(['edit',[row,col,self.emp_tabel.item(row,col).text()]])
                self.edited_items.pop(-1)
                self.emp_tabel.setItem(row,col,qtw.QTableWidgetItem(text))
            elif self.edited_items[-1][0]=='rem':
                typee,ind,data=self.edited_items[-1]
                self.emp_tabel.insertRow(ind)
                for i in range(len(data)):
                    self.emp_tabel.setItem(ind,i,qtw.QTableWidgetItem(data[i]))
                self.redo_items.append(['rem',ind,data])
                self.edited_items.pop(-1)
            elif self.edited_items[-1][0]=='add_csv':
                typee,st,end,directory=self.edited_items[-1]
                self.edited_items.pop(-1)
                for i in range(st , end):
                    self.emp_tabel.removeRow(st)
                self.redo_items.append(['add_csv',st,end,directory])
    def redo(self):
        if len(self.redo_items)>0:
            if self.redo_items[-1][0]=='edit':
                typee,[row,col,text] = self.redo_items[-1]
                self.emp_tabel.setItem(row,col,qtw.QTableWidgetItem(text))
                self.redo_items.pop(-1)
                self.edited_items.append(['edit',[row,col,text]])
            elif self.redo_items[-1][0] == 'rem':
                typee,ind,data=self.redo_items[-1]
                self.emp_tabel.removeRow(ind)
                self.redo_items.pop(-1)
                self.edited_items.append([typee,ind,data])
            elif self.redo_items[-1][0]=='add_csv':
                typee,st,end,directory=self.redo_items[-1]
                self.import_csv(directory)
                self.edited_items.append(['add_csv',st,end,directory])
                self.redo_items.pop(-1)



    def get_start_ind(self):
        ind=0
        while(self.emp_tabel.item(ind,0) is not None):
            ind+=1
        return ind

    def import_csv(self,directory):
        if 'csv' in directory:
            df=pd.read_csv(directory)
        elif 'xlsx' in directory:
            df=pd.read_excel(directory)
        df=df.iloc[:,:].values
        if len(df[0]) == self.emp_tabel.columnCount():
            start=self.get_start_ind()
            end=(start+len(df))
            for i in range(len(df)):
                self.emp_tabel.insertRow(start+i)
                for j in range(len(df[0])):
                    if df[i][j]=='nan':
                        self.emp_tabel.setItem(start + i, j, qtw.QTableWidgetItem(str("")))
                    else:
                        self.emp_tabel.setItem(start+i, j, qtw.QTableWidgetItem(str(df[i][j])))
            self.edited_items.append(['add_csv',start,end,directory])
        else:
            res = qtw.QMessageBox.information(self, "columns", f"table doesnt contain correct number of columns")


    def save_table(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to update employees info", qm.Yes | qm.No)
        if ret == qm.Yes:
            table=[]
            for i in range(self.emp_tabel.rowCount()):
                if self.emp_tabel.item(i,0) is not None:
                    code,name,position,salary,date = self.emp_tabel.item(i,0).text(),self.emp_tabel.item(i,1).text(),self.emp_tabel.item(i,2).text(),self.emp_tabel.item(i,3).text(),self.emp_tabel.item(i,4).text()
                    table.append([code,name,position,salary,date])
                    self.main_widget.my_cursor.execute("DELETE FROM employees;")
            for row in table:
                code, name, position, salary, date=row
                sql_stuff="INSERT INTO employees (code,name,position,salary,hire_date) VALUES(%s,%s,%s,%s,%s);"
                self.main_widget.my_cursor.execute(sql_stuff,(code,name,position,salary,date))
            self.main_widget.mydb.commit()
            self.main_widget.add_emp_page_widget.get_employees()

        else:
            pass
        self.main_widget.update_tables()


    def add_employee_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(2)
        self.main_widget.new_order_ly.setCurrentIndex(4)
        self.main_widget.add_emp_page_widget.count = 4
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][self.main_widget.main_ly.currentIndex()])
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][self.main_widget.new_order_ly.currentIndex()])
        self.main_widget.update_cmb()
    def set_layout(self):
        self.emp_ly = qtw.QVBoxLayout()
        self.emp_ly.addWidget(self.emp_tabel)
        self.emp_h = qtw.QHBoxLayout()
        self.emp_h.addWidget(self.add_emp)
        self.emp_h.addStretch()
        self.emp_h.addWidget(self.save_emp)
        self.emp_h.addStretch()
        self.emp_h.addWidget(self.remove_emp)
        self.emp_ly.addLayout(self.emp_h)
        self.setLayout(self.emp_ly)


class imports_table_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.edited_items = []
        self.redo_items = []
        self.main_widget=main_widget
        self.imp_tabel = qtw.QTableWidget(20, 10)
        self.imp_tabel.setHorizontalHeaderLabels(
            ["supplier Name", "Email", "Address", "Link", "Products", "process type", "Cost", "total","Losses", "Date"])
        self.imp_tabel.horizontalHeader().setStretchLastSection(True)
        self.imp_tabel.verticalHeader().setStretchLastSection(True)
        self.imp_tabel.itemDoubleClicked.connect(self.get_item_editited)

        self.add_imp = qtw.QPushButton("Add")
        self.add_imp.clicked.connect(self.add_imp_btn_fun)
        self.add_imp.setStyleSheet(self.main_widget.my_style.button_style())
        self.remove_imp = qtw.QPushButton("remove")
        self.remove_imp.setStyleSheet(self.main_widget.my_style.button_style())
        self.remove_imp.clicked.connect(self.remove_imp_btn_fun)

        self.save_imp = qtw.QPushButton("Save")
        self.save_imp.setStyleSheet(self.main_widget.my_style.button_style())
        self.save_imp.clicked.connect(self.save_table)
        self.set_layout()

    def remove_imp_btn_fun(self):
        indices = self.imp_tabel.selectionModel().selectedRows()
        for index in sorted(indices):
            self.edited_items.append(['rem', index.row(), [self.imp_tabel.item(index.row(), i).text() for i in
                                                           range(self.imp_tabel.columnCount())]])
            self.imp_tabel.removeRow(index.row())
    def get_item_editited(self,item):
            self.edited_items.append(['edit',[self.imp_tabel.currentRow(),self.imp_tabel.currentColumn(),self.imp_tabel.item(self.imp_tabel.currentRow(),self.imp_tabel.currentColumn()).text()]])
    def undo(self):
        if len(self.edited_items)>0:
            if self.edited_items[-1][0]=='edit':
                typee,data=self.edited_items[-1]
                row, col, text=data
                self.redo_items.append(['edit',[row,col,self.imp_tabel.item(row,col).text()]])
                self.edited_items.pop(-1)
                self.imp_tabel.setItem(row,col,qtw.QTableWidgetItem(text))
            elif self.edited_items[-1][0]=='rem':
                typee,ind,data=self.edited_items[-1]
                self.imp_tabel.insertRow(ind)
                for i in range(len(data)):
                    self.imp_tabel.setItem(ind,i,qtw.QTableWidgetItem(data[i]))
                self.redo_items.append(['rem',ind,data])
                self.edited_items.pop(-1)
            elif self.edited_items[-1][0]=='add_csv':
                typee,st,end,directory=self.edited_items[-1]
                self.edited_items.pop(-1)
                for i in range(st , end):
                    self.imp_tabel.removeRow(st)
                self.redo_items.append(['add_csv',st,end,directory])
    def redo(self):
        if len(self.redo_items)>0:
            if self.redo_items[-1][0]=='edit':
                typee,[row,col,text] = self.redo_items[-1]
                self.imp_tabel.setItem(row,col,qtw.QTableWidgetItem(text))
                self.redo_items.pop(-1)
                self.edited_items.append(['edit',[row,col,text]])
            elif self.redo_items[-1][0] == 'rem':
                typee,ind,data=self.redo_items[-1]
                self.imp_tabel.removeRow(ind)
                self.redo_items.pop(-1)
                self.edited_items.append([typee,ind,data])
            elif self.redo_items[-1][0]=='add_csv':
                typee,st,end,directory=self.redo_items[-1]
                self.import_csv(directory)
                self.edited_items.append(['add_csv',st,end,directory])
                self.redo_items.pop(-1)

    def get_start_ind(self):
        ind=0
        while(self.imp_tabel.item(ind,0) is not None):
            ind+=1
        return ind

    def import_csv(self,directory):
        if 'csv' in directory:
            df=pd.read_csv(directory)
        elif 'xlsx' in directory:
            df=pd.read_excel(directory)
        df=df.iloc[:,:].values
        if len(df[0])==self.imp_tabel.columnCount():
            #self.imp_tabel.setRowCount(self.imp_tabel.rowCount()+len(df))
            start=self.get_start_ind()
            end=(start+len(df))
            for i in range(len(df)):
                self.imp_tabel.insertRow(start+i)
                for j in range(len(df[0])):
                    if df[i][j]=='nan':
                        self.imp_tabel.setItem(start + i, j, qtw.QTableWidgetItem(str("")))
                    else:
                        self.imp_tabel.setItem(start+i, j, qtw.QTableWidgetItem(str(df[i][j])))
            self.edited_items.append(['add_csv',start,end,directory])
        else:
            res = qtw.QMessageBox.information(self, "columns", f"table doesnt contain correct number of columns")
    def insert_into_stock(self,name,qt,buy_price,sell_price):
        try:
            sql_stuff = "INSERT INTO stock  (product,availble,buying_price,selling_price) VALUES(%s,%s,%s,%s);"
            self.main_widget.my_cursor.execute(sql_stuff, (name, int(qt), int(buy_price), int(sell_price)))
        except:
            try:
                sql_stuff = "UPDATE stock SET availble=availble+%s WHERE product=%s"
                self.main_widget.my_cursor.execute(sql_stuff, (qt, name))
                sql_stuff = "UPDATE stock SET buying_price=%s WHERE product=%s"
                self.main_widget.my_cursor.execute(sql_stuff, (buy_price, name))

                sql_stuff = "UPDATE stock SET sell_price=%s WHERE product=%s"
                self.main_widget.my_cursor.execute(sql_stuff, (sell_price, name))
            except:
                pass
    def insert_into_imports(self,info):
        supplier_name, supplier_email, supplier_address, supplier_link, products, typee, tot_cost, total, losses, date = info
        try:
            sql_stuff = "INSERT INTO imports (supplier_Name,Email,Address,Link,Products,type,cost,total,Losses,Date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            self.main_widget.my_cursor.execute(sql_stuff, (
                supplier_name, supplier_email, supplier_address, supplier_link, products, typee, int(tot_cost),
                int(total), losses, date))
        except:
            pass
    def get_table_data(self):
        table = []
        for i in range(self.imp_tabel.rowCount()):
            row = []
            if self.imp_tabel.item(i, 0) is not None:
                for j in range(10):
                    row.append(self.imp_tabel.item(i, j).text())
                table.append(row)
        return table
    def save_table(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to update imports info", qm.Yes | qm.No)
        if ret == qm.Yes:
            table=self.get_table_data()
            self.main_widget.my_cursor.execute("DELETE FROM imports;")
            self.main_widget.my_cursor.execute("DELETE FROM stock;")
            f=False
            for ind,row in enumerate(table):
                supplier_name, supplier_email, supplier_address, supplier_link, products, typee, tot_cost,total, losses, date = row
                try:
                    productss = products.split('|')
                    name, info = productss[0].split(':')
                    qt, buy_price, sell_price = info.split(',')
                except:
                    res = qtw.QMessageBox.information(self, "incorrect format",
                                                      f"row doesnt have the correct format")
                    self.imp_tabel.selectRow(ind)
                    f = True
                    continue
                self.insert_into_imports(row)
                if typee == 'Stock Product' or typee == "منتج مخازن":
                    products=products.split('|')
                    for product in products:
                        try:
                            name,info=product.split(':')
                            qt, buy_price, sell_price=info.split(',')
                            self.insert_into_stock(name,qt,buy_price,sell_price)
                        except:
                            res = qtw.QMessageBox.information(self, "incorrect format",
                                                              f"row doesnt have the correct format")
                            self.imp_tabel.selectRow(ind)
                            f=True
                            break
                    if f:
                        break
            if f==False:
                self.main_widget.mydb.commit()
                self.main_widget.buy_product_widget.get_imports()
                self.main_widget.update_tables()

        else:
            pass


    def add_imp_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(2)
        self.main_widget.new_order_ly.setCurrentIndex(1)
        self.main_widget.new_order_bar.count = 1
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][self.main_widget.main_ly.currentIndex()])
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][self.main_widget.new_order_ly.currentIndex()])
        self.main_widget.update_cmb()
    def set_layout(self):
        self.imp_widget = qtw.QWidget()
        self.imp_ly = qtw.QVBoxLayout()
        self.imp_ly.addWidget(self.imp_tabel)
        self.imp_h = qtw.QHBoxLayout()
        self.imp_h.addWidget(self.add_imp)
        self.imp_h.addStretch()
        self.imp_h.addWidget(self.save_imp)
        self.imp_h.addStretch()
        self.imp_h.addWidget(self.remove_imp)
        self.imp_ly.addLayout(self.imp_h)
        self.setLayout(self.imp_ly)




class exports_table_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.edited_items = []
        self.redo_items = []
        self.main_widget=main_widget
        self.exports_tabel = qtw.QTableWidget(20, 9)
        self.exports_tabel.setHorizontalHeaderLabels(
            ["Client Name", "Email", "Address", "Link", "Products", "Cost", "Profit", "Losses", "Date"])
        self.exports_tabel.horizontalHeader().setStretchLastSection(True)
        self.exports_tabel.verticalHeader().setStretchLastSection(True)
        self.exports_tabel.itemDoubleClicked.connect(self.get_item_editited)

        self.add_exp = qtw.QPushButton("Add")
        self.add_exp.setStyleSheet(self.main_widget.my_style.button_style())
        self.add_exp.clicked.connect(self.add_exp_btn_fun)
        self.remove_exp = qtw.QPushButton("remove")
        self.remove_exp.setStyleSheet(self.main_widget.my_style.button_style())
        self.remove_exp.clicked.connect(self.remove_exp_btn_fun)

        self.save_exp = qtw.QPushButton("Save")
        self.save_exp.setStyleSheet(self.main_widget.my_style.button_style())
        self.save_exp.clicked.connect(self.save_table)

        self.set_layout()

    def remove_exp_btn_fun(self):
        indices = self.exports_tabel.selectionModel().selectedRows()
        for index in sorted(indices):
            self.edited_items.append(['rem', index.row(), [self.exports_tabel.item(index.row(), i).text() for i in
                                                           range(self.exports_tabel.columnCount())]])
            self.exports_tabel.removeRow(index.row())
    def get_item_editited(self,item):
            self.edited_items.append(['edit',[self.exports_tabel.currentRow(),self.exports_tabel.currentColumn(),self.exports_tabel.item(self.exports_tabel.currentRow(),self.exports_tabel.currentColumn()).text()]])
    def undo(self):
        if len(self.edited_items)>0:
            if self.edited_items[-1][0]=='edit':
                typee,data=self.edited_items[-1]
                row, col, text=data
                self.redo_items.append(['edit',[row,col,self.exports_tabel.item(row,col).text()]])
                self.edited_items.pop(-1)
                self.exports_tabel.setItem(row,col,qtw.QTableWidgetItem(text))
            elif self.edited_items[-1][0]=='rem':
                typee,ind,data=self.edited_items[-1]
                self.exports_tabel.insertRow(ind)
                for i in range(len(data)):
                    self.exports_tabel.setItem(ind,i,qtw.QTableWidgetItem(data[i]))
                self.redo_items.append(['rem',ind,data])
                self.edited_items.pop(-1)
            elif self.edited_items[-1][0]=='add_csv':
                typee,st,end,directory=self.edited_items[-1]
                self.edited_items.pop(-1)
                for i in range(st , end):
                    self.exports_tabel.removeRow(st)
                self.redo_items.append(['add_csv',st,end,directory])
    def redo(self):
        if len(self.redo_items)>0:
            if self.redo_items[-1][0]=='edit':
                typee,[row,col,text] = self.redo_items[-1]
                self.exports_tabel.setItem(row,col,qtw.QTableWidgetItem(text))
                self.redo_items.pop(-1)
                self.edited_items.append(['edit',[row,col,text]])
            elif self.redo_items[-1][0] == 'rem':
                typee,ind,data=self.redo_items[-1]
                self.exports_tabel.removeRow(ind)
                self.redo_items.pop(-1)
                self.edited_items.append([typee,ind,data])
            elif self.redo_items[-1][0]=='add_csv':
                typee,st,end,directory=self.redo_items[-1]
                self.import_csv(directory)
                self.edited_items.append(['add_csv',st,end,directory])
                self.redo_items.pop(-1)



    def get_start_ind(self):
        ind=0
        while(self.exports_tabel.item(ind,0) is not None):
            ind+=1
        return ind

    def import_csv(self,directory):
        if 'csv' in directory:
            df=pd.read_csv(directory)
        elif 'xlsx' in directory:
            df=pd.read_excel(directory)
        df=df.iloc[:,:].values
        if len(df[0])==self.exports_tabel.columnCount():
            start=self.get_start_ind()
            end=(start+len(df))
            for i in range(len(df)):
                self.exports_tabel.insertRow(start+i)
                for j in range(len(df[0])):
                    if df[i][j]=='nan':
                        self.exports_tabel.setItem(start + i, j, qtw.QTableWidgetItem(str("")))
                    else:
                        self.exports_tabel.setItem(start+i, j, qtw.QTableWidgetItem(str(df[i][j])))
            self.edited_items.append(['add_csv',start,end,directory])
        else:
            res = qtw.QMessageBox.information(self, "columns", f"table doesnt contain correct number of columns")
    def insert_into_stock(self,name,prod_qt):
        try:

            sql_stuff = """UPDATE stock SET sold=sold+%s WHERE Product=%s"""
            self.main_widget.my_cursor.execute(sql_stuff, (int(prod_qt), name))
        except:
            pass
        try:
            sql_stuff = """UPDATE stock SET availble=availble-%s WHERE Product=%s"""
            self.main_widget.my_cursor.execute(sql_stuff, (int(prod_qt), name))
        except:
            pass
    def insert_into_exports(self,info):
        name, email, address, link, products, tot_cost, profit, losses, date = info
        total = int(tot_cost) + int(profit)
        try:
            sql_stuff = """INSERT INTO exports(client_Name,Email,Address,Link,Products,cost,total,profit,Losses,date)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
            self.main_widget.my_cursor.execute(sql_stuff, (
                name, email, address, link, products, tot_cost, total, profit, int(losses), date))
        except:
            pass
    def clear_data(self):
        availbility=dict()
        self.main_widget.my_cursor.execute("DELETE FROM exports;")
        try:
            self.main_widget.my_cursor.execute("SELECT Product,sold,availble FROM stock;")
            data = self.main_widget.my_cursor.fetchall()
            for name, av, sold in data:
                sql_stuff = """UPDATE stock SET availble=%s WHERE Product=%s;"""
                self.main_widget.my_cursor.execute(sql_stuff, (int(av) + int(sold), name))
                availbility[name] = int(av) + int(sold)
            sql_stuff = """UPDATE stock SET sold=0;"""
            self.main_widget.my_cursor.execute(sql_stuff)
        except:
            pass
        return availbility
    def get_table_data(self):
        table = []
        for i in range(self.exports_tabel.rowCount()):
            row = []
            if self.exports_tabel.item(i, 0) is not None:
                for j in range(9):
                    row.append(self.exports_tabel.item(i, j).text())
                table.append(row)
        return table
    def do_updates(self):
        self.main_widget.mydb.commit()
        self.main_widget.sell_Product.get_exports()
        self.main_widget.update_tables()
    def save_table(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to update exports info", qm.Yes | qm.No)
        if ret == qm.Yes:
            f = False
            table=self.get_table_data()
            availbility = self.clear_data()
            for ind,row in enumerate(table):
                name, email, address, link, products, tot_cost, profit, losses, date = row
                try:
                    productss = products.split('|')
                    name, info = productss[0].split(':')
                    qt, buy_price, sell_price = info.split(',')
                except:
                    res = qtw.QMessageBox.information(self, "incorrect format",
                                                      f"row doesnt have the correct format")
                    self.exports_tabel.selectRow(ind)
                    f = True
                    continue
                self.insert_into_exports(row)
                products = products.split('|')
                for product in products:
                    try:
                        name, info = product.split(':')
                        qt, buy_price, sell_price = info.split(',')
                        if name in list(self.main_widget.stock_widget.stock_data.keys()):
                            av= availbility[name]
                            if int(qt)<=int(av):
                                self.insert_into_stock(name, qt)
                            else:
                                res = qtw.QMessageBox.information(self, "incorrect format",
                                                                  f"products quantity greater than availble")
                                self.exports_tabel.selectRow(ind)
                                f = True
                                break
                    except:
                        res = qtw.QMessageBox.information(self, "incorrect format",
                                                          f"row doesnt have the correct format")
                        self.exports_tabel.selectRow(ind)
                        f = True
                        break
                if f:
                    break
            if f == False:
                self.do_updates()

        else:
            pass
    def add_exp_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(2)
        self.main_widget.new_order_ly.setCurrentIndex(2)
        self.main_widget.new_order_bar.count = 2
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][self.main_widget.main_ly.currentIndex()])
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][self.main_widget.new_order_ly.currentIndex()])
        self.main_widget.update_cmb()

    def set_layout(self):
        self.exp_ly = qtw.QVBoxLayout()
        self.exp_ly.addWidget(self.exports_tabel)
        self.exp_h = qtw.QHBoxLayout()
        self.exp_h.addWidget(self.add_exp)
        self.exp_h.addStretch()
        self.exp_h.addWidget(self.save_exp)
        self.exp_h.addStretch()
        self.exp_h.addWidget(self.remove_exp)
        self.exp_ly.addLayout(self.exp_h)
        self.setLayout(self.exp_ly)



class calculations_table_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.calc_tabel = qtw.QTableWidget(20, 6)
        self.calc_tabel.setHorizontalHeaderLabels(
            ["Name", "type", "Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"])
        self.calc_tabel.horizontalHeader().setStretchLastSection(True)
        self.calc_tabel.verticalHeader().setStretchLastSection(True)

        self.tot_tabel = qtw.QTableWidget(5, 4)
        self.tot_tabel.setHorizontalHeaderLabels(["Period", "Spent", "Earned", "Profit"])
        self.tot_tabel.setItem(0, 0, qtw.QTableWidgetItem("Quarter 1"))
        self.tot_tabel.setItem(1, 0, qtw.QTableWidgetItem("Quarter 2"))
        self.tot_tabel.setItem(2, 0, qtw.QTableWidgetItem("Quarter 3"))
        self.tot_tabel.setItem(3, 0, qtw.QTableWidgetItem("Quarter 4"))
        self.tot_tabel.setItem(4, 0, qtw.QTableWidgetItem("Annual"))
        self.tot_tabel.horizontalHeader().setStretchLastSection(True)
        self.tot_tabel.verticalHeader().setStretchLastSection(True)

        self.annual_rent = qtw.QLabel()
        self.annual_salaries = qtw.QLabel()
        self.annual_rent.setStyleSheet("QLabel{color:white;font: bold 22px;}")
        self.annual_salaries.setStyleSheet("QLabel{color:white;font: bold 22px;}")
        self.years=qtw.QComboBox()
        now = datetime.datetime.now().year
        self.years.addItems([str(now-i) for i in range(10)])
        self.years.currentIndexChanged.connect(self.year_changed)

        self.set_layout()

    def year_changed(self):
        self.populate_calculations_tabel()
        self.populate_total_calc_table()

    def get_quarter_from_date(self,date):
        my_list=['','Quarter 1','Quarter 1','Quarter 1','Quarter 2','Quarter 2','Quarter 2','Quarter 3','Quarter 3','Quarter 3','Quarter 4','Quarter 4','Quarter 4']
        month=int(date.split('-')[-2])
        return my_list[month]
    def get_calc_by_client(self):
        suppliers=dict()
        clients=dict()

        for code in list(self.main_widget.buy_product_widget.imports_data.keys()):
            name, email, address, link, products, process_type, cost, total, losses, date=self.main_widget.buy_product_widget.imports_data[code]
            year=date.split('-')[0]
            if int(year)==int(self.years.currentText()):
                quarter=self.get_quarter_from_date(date)
                try:
                    suppliers[name][quarter]+=cost
                except:
                    suppliers[name]={'Quarter 1':0,'Quarter 2':0,'Quarter 3':0,'Quarter 4':0}
                    suppliers[name][quarter]=cost
        for code in list(self.main_widget.sell_Product.exports_data.keys()):
            code, name, email, address, link, products, cost, total, profit, losses, date=self.main_widget.sell_Product.exports_data[code]
            quarter=self.get_quarter_from_date(date)
            year = date.split('-')[0]
            if int(year) == int(self.years.currentText()):
                try:
                    clients[name][quarter]+=total
                except:
                    clients[name]={'Quarter 1':0,'Quarter 2':0,'Quarter 3':0,'Quarter 4':0}
                    clients[name][quarter]=total
        return suppliers,clients

    def populate_calculations_tabel(self):
        self.calc_tabel.clear()
        self.main_widget.set_lang()
        suppliers, clients = self.get_calc_by_client()
        if len(list(suppliers.keys())) + len(list(clients.keys())) > 0:
            if len(list(suppliers.keys())) + len(list(clients.keys()))>self.calc_tabel.rowCount():
                self.calc_tabel.setRowCount(len(list(suppliers.keys())) + len(list(clients.keys())))
            ind = 0
            for name in list(suppliers.keys()):
                self.calc_tabel.setItem(ind, 0, qtw.QTableWidgetItem(name))

                q1, q2, q3, q4 = list(suppliers[name].values())
                self.calc_tabel.setItem(ind, 1, qtw.QTableWidgetItem('import'))
                self.calc_tabel.setItem(ind, 2, qtw.QTableWidgetItem(str(q1)))
                self.calc_tabel.setItem(ind, 3, qtw.QTableWidgetItem(str(q2)))
                self.calc_tabel.setItem(ind, 4, qtw.QTableWidgetItem(str(q3)))
                self.calc_tabel.setItem(ind, 5, qtw.QTableWidgetItem(str(q4)))
                ind += 1
            for name in list(clients.keys()):
                self.calc_tabel.setItem(ind, 0, qtw.QTableWidgetItem(name))
                self.calc_tabel.setItem(ind, 1, qtw.QTableWidgetItem('export'))
                q1, q2, q3, q4 = list(clients[name].values())
                self.calc_tabel.setItem(ind, 2, qtw.QTableWidgetItem(str(q1)))
                self.calc_tabel.setItem(ind, 3, qtw.QTableWidgetItem(str(q2)))
                self.calc_tabel.setItem(ind, 4, qtw.QTableWidgetItem(str(q3)))
                self.calc_tabel.setItem(ind, 5, qtw.QTableWidgetItem(str(q4)))
                ind += 1

    def get_calc_col_vals(self,index):
        cost=[]
        earned=[]
        for i in range(self.calc_tabel.rowCount()):
            try:
                if self.calc_tabel.item(i,1).text()=='import':
                    cost.append(int(self.calc_tabel.item(i,index).text()))
                else:
                    earned.append(int(self.calc_tabel.item(i,index).text()))
            except:
                break
        cost=sum(cost)
        earned=sum(earned)
        profit=earned-cost
        return cost,earned,profit


    def populate_total_calc_table(self):
        self.main_widget.update_tables()
        self.tot_tabel.clear()
        self.main_widget.set_lang()
        tot_cost=0
        total=0
        tot_profit=0
        for i in range(4):
            cost,earned,profit=self.get_calc_col_vals(2+i)
            tot_cost+=cost
            total+=earned
            tot_profit+=profit
            self.tot_tabel.setItem(i,1,qtw.QTableWidgetItem(str(cost)))
            self.tot_tabel.setItem(i,2,qtw.QTableWidgetItem(str(earned)))
            self.tot_tabel.setItem(i,3,qtw.QTableWidgetItem(str(profit)))
        self.tot_tabel.setItem(4, 1, qtw.QTableWidgetItem(str(tot_cost)))
        self.tot_tabel.setItem(4 , 2, qtw.QTableWidgetItem(str(total)))
        self.tot_tabel.setItem(4 , 3, qtw.QTableWidgetItem(str(tot_profit)))
        tot_salary=0
        for i in list(self.main_widget.add_emp_page_widget.employee_data.keys()):
            salary=int(self.main_widget.add_emp_page_widget.employee_data[i][2])
            tot_salary+=salary
        self.annual_salaries.setText(f'Total salaries paid per year is  :   {tot_salary}')
        self.annual_rent.setText(f'Total rent paid per year is  :   {int(self.main_widget.main_info_widget.scrollable_info.rent)*12}')



    def set_layout(self):
        self.calc_ly = qtw.QVBoxLayout()
        self.years_ly=qtw.QHBoxLayout()
        self.years_ly.addStretch()
        self.years_ly.addWidget(self.years)
        self.calc_ly.addLayout(self.years_ly)
        self.calc_ly.addWidget(self.calc_tabel)
        self.calc_ly.addWidget(self.tot_tabel)
        self.calc_ly.addStretch()
        self.calc_ly.addWidget(self.annual_rent)
        self.calc_ly.addWidget(self.annual_salaries)
        self.calc_ly.addStretch()
        self.setLayout(self.calc_ly)

class database_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        ####################Data base page####################################

        self.database_main_widget = database_home_page(self.main_widget)
        self.database_main_widget.setStyleSheet(
            """QPushButton{border-radius:50px;min-width:200px;min-height:250px;border-style: outset;border-width: 1px;border-color: blue;color:white;font:bold 18px;}""")
        ################DataBase bar########################
        self.database_bar = data_base_bar(self.main_widget)
        ################################import-export csv ly#######################
        self.import_export_widget = import_export_csv(self.main_widget)
        ####################Employees tabel ly##################
        self.emp_widget = employees_table_page(self.main_widget)
        ################exports#######################
        self.exp_widget = exports_table_page(self.main_widget)
        ################imports########################
        self.imp_widget = imports_table_page(self.main_widget)
        ####################Calculations#################
        self.calc_widget = calculations_table_page(self.main_widget)
        self.set_layout()
    def set_layout(self):
        #############database_ly###################
        self.database_vertical_ly = qtw.QVBoxLayout()
        self.database_ly = qtw.QStackedLayout()
        self.database_vertical_ly.addWidget(self.database_bar)
        self.database_vertical_ly.addWidget(self.import_export_widget)
        self.database_vertical_ly.addLayout(self.database_ly)
        ######stacked database layout################
        self.database_ly.addWidget(self.database_main_widget)
        self.database_ly.addWidget(self.emp_widget)
        self.database_ly.addWidget(self.calc_widget)
        self.database_ly.addWidget(self.imp_widget)
        self.database_ly.addWidget(self.exp_widget)
        self.database_ly.setCurrentIndex(0)
        self.setLayout(self.database_vertical_ly)