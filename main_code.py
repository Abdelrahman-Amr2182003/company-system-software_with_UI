import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import mysql.connector
import json

from languages import langs
from styles import  styles
from home_page import home_page
from stock_page import stock_page
from new_order_home_page import new_order_home_page
from buy_page import buy_page
from sell_page import sell_page
from new_package_page import  new_package_page
from new_employee_page import new_employee
from bars import top_bar,side_bar,new_order_bar,settings_bar,data_base_bar
from tables import database_page
from login_form import login_form
from info_page import main_info_page
from settings_page import settings_page
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ESSC")
        self.setWindowIcon(qtg.QIcon('icons//logo.png'))


        self.my_style=styles(self)
        self.load_create_database()
        self.load_color_lang_state()
        self.load_color_themes()
        self.default_stylesheet = self.styleSheet()

        self.main_pages = [
            ["Home Page", "Stock Page", "New Process Page", "DataBase Page", "Info Page", "Settings Page"],
            ["الفحة الرئيسية", "صفحة المخزون", "صفحة العمليات الجديدة", "صفحة قاعدة البينات", "صفحة المعلومات",
             "الإعدادات"]]
        ########################load users accounts#######################
        self.current_type = None
        self.resize(1500, 900)
        ####################Top frame#####################
        self.genral_w = qtw.QWidget()
        self.top_frame=top_bar(self)
        #####################Home Page Buttons##############################
        self.home_page_widget=home_page(self)

        ######################################Side frame####################
        self.side_frame=side_bar(self)
        #####################stock page#####################################
        self.stock_widget=stock_page(self)

        ########################New Order###################################

        self.new_order_widget = qtw.QWidget()
        self.new_order_ly = qtw.QStackedLayout()

        ############new order_home_page###################
        self.new_order_h_widget = new_order_home_page(self)
        ##################New Order bar#################################
        self.new_order_bar = new_order_bar(self)
        ############Create new package################
        self.new_package_widget = new_package_page(self)
        ##############Buy Product###################
        self.buy_product_widget = buy_page(self)
        ################Sell product#################
        self.sell_Product = sell_page(self)
        #############################Login Form######################
        self.login_widget = login_form(self)
        ############Databse###################
        self.database_widget = database_page(self)
        ####################add_employee page##################
        self.add_emp_page_widget=new_employee(self)

        self.update_tables()


        ##############Info Page##################
        self.main_info_widget=main_info_page(self)

        ##########settings#############
        self.main_settings_widget=settings_page(self)
        #####################Set Layout function#####################################
        self.set_layout()

        if self.dark_state == 1:
            self.my_style.apply_dark_mode()
        else:
            self.my_style.apply_light_mode()

        self.set_lang()
    def update_tables(self):
        ###############################Data base functions#####################################
        self.stock_widget.get_stock()
        self.add_emp_page_widget.get_employees()
        self.buy_product_widget.get_imports()
        self.sell_Product.get_exports()
        self.new_package_widget.load_products_into_package()
        self.update_cmb()

    def load_create_database(self):
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='2182003s2gbs')
        self.my_cursor = self.mydb.cursor()
        self.create_db("company_db")
        self.create_table('employees',
                          'code INTEGER(10) AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(100),position VARCHAR(100),salary INTEGER(10),hire_date Date')
        self.create_table('users', 'username VARCHAR(100) PRIMARY KEY,password VARCHAR(100),acc_type VARCHAR(10)')
        self.create_table(
            "imports",
            "code INTEGER(10) AUTO_INCREMENT PRIMARY KEY,supplier_Name VARCHAR(100),Email VARCHAR(100),Address VARCHAR(100),Link VARCHAR(400),Products VARCHAR(8000),type VARCHAR(50),cost INTEGER(100),total INTEGER(100),Losses INTEGER(100),date VARCHAR(20)")
        self.create_table("exports",
                          "code INTEGER(10) AUTO_INCREMENT PRIMARY KEY,client_Name VARCHAR(100),Email VARCHAR(100),Address VARCHAR(100),Link VARCHAR(400),Products VARCHAR(8000),cost INTEGER(100),total INTEGER(100),Profit INTEGER(100),Losses INTEGER(100),date VARCHAR(20)")

        self.create_table("stock",
                          "Product VARCHAR(40) PRIMARY KEY,availble INTEGER(10) Default 0,buying_price INTEGER(10),selling_price INTEGER(10),sold INTEGER(100) DEFAULT 0")

    def load_color_themes(self):
        try:
            with open('themes.txt', 'r') as f:
                l = f.read().split('|')
                self.light_colors = l[0]
                self.dark_colors = l[1]
        except:
            self.light_colors = '0,32,242'
            self.dark_colors = '0,0,0'
        self.light_theme = f'rgb({self.light_colors})'
        self.dark_theme = f"rgb({self.dark_colors})"
        self.aligments = ["left", "right"]

    def load_color_lang_state(self):
        try:
            with open('states.txt', 'r') as f:
                self.lang, self.dark_state = f.read().split(',')
                self.lang = int(self.lang)
                self.dark_state = int(self.dark_state)

        except:
            self.lang = 0
            self.dark_state = 1
    def update_cmb(self):
        packages_list=list(self.new_package_widget.packages_dict.keys())
        products_list=list(self.stock_widget.stock_data.keys())
        emps_list=list(self.add_emp_page_widget.employee_data.keys())

        self.new_package_widget.package_name.clear()
        self.new_package_widget.add_product_to_package.clear()

        self.buy_product_widget.product_name.clear()
        self.sell_Product.add_product.clear()
        self.sell_Product.add_Packages.clear()
        self.buy_product_widget.buy_package_name.clear()
        self.add_emp_page_widget.emp_code_input.clear()
        self.set_lang()


        self.new_package_widget.package_name.addItems(packages_list)
        self.new_package_widget.add_product_to_package.addItems(products_list)

        self.buy_product_widget.product_name.addItems(products_list)
        self.sell_Product.add_product.addItems(products_list)
        self.sell_Product.add_Packages.addItems(packages_list)
        self.buy_product_widget.buy_package_name.addItems(packages_list)
        self.add_emp_page_widget.emp_code_input.addItems(emps_list)


    def create_db(self, name):
        try:
            self.my_cursor.execute(f"CREATE DATABASE {name}")
            self.mydb = mysql.connector.connect(host='localhost', user='root', password='2182003s2gbs',
                                                database=name)
            self.my_cursor = self.mydb.cursor()

        except:
            self.mydb = mysql.connector.connect(host='localhost', user='root', password='2182003s2gbs',
                                                database=name)
            self.my_cursor = self.mydb.cursor()


    def create_table(self, name, config):
        try:
            self.my_cursor.execute(f"CREATE TABLE {name} ({config})")
        except:
            pass
    def del_table(self,name):
        self.my_cursor.execute(f"Drop TABLE {name}")
    def closeEvent(self, event):
        text = f"{self.lang},{self.dark_state}"
        with open('states.txt', 'w') as f:
            f.write(text)
        themes=f'{self.light_colors}|{self.dark_colors}'
        with open('themes.txt', 'w') as f:
            f.write(themes)
        with open('packages.json','w') as f:
            json.dump(self.new_package_widget.packages_dict,f)

    def set_lang(self):

        my_lang=langs(self)

        try:
            if self.lang == 0:
                my_lang.set_english()
            else:
                my_lang.set_arabic()
        except:
            pass
    def set_layout(self):
        #######################Stacked_genral_layouts########
        self.stacked_g = qtw.QStackedLayout()
        ############new_order_ly#################
        self.new_order_v_ly = qtw.QVBoxLayout()
        self.new_order_v_ly.addWidget(self.new_order_bar)
        self.new_order_ly.addWidget(self.new_order_h_widget)
        self.new_order_ly.addWidget(self.buy_product_widget)
        self.new_order_ly.addWidget(self.sell_Product)
        self.new_order_ly.addWidget(self.new_package_widget)
        self.new_order_ly.addWidget(self.add_emp_page_widget)
        self.new_order_v_ly.addLayout(self.new_order_ly)
        self.new_order_ly.setCurrentIndex(0)
        self.new_order_widget.setLayout(self.new_order_v_ly)
        ##########stacked layout##########
        self.main_ly = qtw.QStackedLayout()
        self.main_widget = qtw.QWidget(self.genral_w)
        self.main_ly.addWidget(self.home_page_widget)
        self.main_ly.addWidget(self.stock_widget)
        self.main_ly.addWidget(self.new_order_widget)
        self.main_ly.addWidget(self.database_widget)
        self.main_ly.addWidget(self.main_info_widget)
        self.main_ly.addWidget(self.main_settings_widget)
        self.main_widget.setLayout(self.main_ly)
        self.main_ly.setCurrentIndex(0)
        #######################Genral widget########################
        self.genral_ly = qtw.QVBoxLayout()
        self.genral_ly.setSpacing(0)
        self.genral_ly.addWidget(self.top_frame)
        self.horizontal_ly = qtw.QHBoxLayout()
        self.horizontal_ly.setSpacing(0)
        self.horizontal_ly.addWidget(self.side_frame)
        self.horizontal_ly.addWidget(self.main_widget)
        self.genral_ly.addLayout(self.horizontal_ly)
        self.genral_w.setLayout(self.genral_ly)

        #############################Stacked genral############################################
        self.stacked_g.addWidget(self.login_widget)
        self.stacked_g.addWidget(self.genral_w)
        self.stacked_g.setCurrentIndex(0)
        self.setLayout(self.stacked_g)
        self.show()
if __name__ == "__main__":
    app = qtw.QApplication([])
    screen = app.primaryScreen()
    mw = MainWindow()
    app.exec_()