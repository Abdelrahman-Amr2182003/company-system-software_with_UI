import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import qdarkstyle
from qtwidgets import Toggle, AnimatedToggle
import mysql.connector
import json
import datetime

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ESSC")
        self.setWindowIcon(qtg.QIcon('icons//logo.png'))



        self.mydb = mysql.connector.connect(host='localhost', user='root', password='2182003s2gbs')
        self.my_cursor = self.mydb.cursor()
        self.create_db("company_db")
        self.create_table('employees','code INTEGER(10) AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(100),position VARCHAR(100),salary INTEGER(10),hire_date Date')
        self.create_table('users','username VARCHAR(100) PRIMARY KEY,password VARCHAR(100),acc_type VARCHAR(10)')
        self.create_table(
                    "imports","code INTEGER(10) AUTO_INCREMENT PRIMARY KEY,supplier_Name VARCHAR(100),Email VARCHAR(100),Address VARCHAR(100),Link VARCHAR(400),Products VARCHAR(8000),type VARCHAR(50),cost INTEGER(100),total INTEGER(100),Losses INTEGER(100),date VARCHAR(20)")
        self.create_table("exports","code INTEGER(10) AUTO_INCREMENT PRIMARY KEY,client_Name VARCHAR(100),Email VARCHAR(100),Address VARCHAR(100),Link VARCHAR(400),Products VARCHAR(8000),cost INTEGER(100),total INTEGER(100),Profit INTEGER(100),Losses INTEGER(100),date VARCHAR(20)")

        self.create_table("stock","Product VARCHAR(40) PRIMARY KEY,availble INTEGER(10) Default 0,buying_price INTEGER(10),selling_price INTEGER(10),sold INTEGER(100) DEFAULT 0")



        try:
            with open('states.txt', 'r') as f:
                self.lang, self.dark_state = f.read().split(',')
                self.lang = int(self.lang)
                self.dark_state = int(self.dark_state)

        except:
            self.lang = 0
            self.dark_state = 1
        try:
            with open('themes.txt','r') as f:
                l=f.read().split('|')
                self.light_colors=l[0]
                self.dark_colors=l[1]
        except:
            self.light_colors='0,32,242'
            self.dark_colors='0,0,0'

        self.default_stylesheet = self.styleSheet()


        ##########counters##############
        self.count = 0#for data base pages
        self.new_order_count = 0
        self.settings_count = 0

        self.prod_table_current=0

        self.package_tabel_current=0
        self.sell_table_current=0
        #################load packages################################
        self.packages_dict=dict()
        try:
            with open('packages.json','r') as f:
                self.packages_dict=json.load(f)
        except:
            pass

        #############3load color theme#################
        self.light_theme=f'rgb({self.light_colors})'
        self.dark_theme=f"rgb({self.dark_colors})"
        self.aligments = ["left", "right"]

        ############pages_names################
        self.new_order_pages = [
            ["New Order Home Page", "Buying page", "Selling page", "New Package page", "Add Employee"],
            ["الفحة الرئيسية", "صفحة شراء المنتجات", "صفحة بيع المنتجات", "صفحة اصافة مجموعة جديدة", "اضف موظف جديد"]]
        self.database_pages = [["Database Home Page", "Employees Table", "Calculations Tabel", "Imports Tabel",
                                "Exports Tabel"], ["الفحة الرئيسية", "جدول الموظفبن", "جدول الحسابات", "جدول الواردات",
                                                   "جدول التصديرات"]]
        self.settings_pages = [["Home Page", "Create new account", "change password"],
                               ["الفحة الرئيسية", "حساب جدييد", "تغيير كلمة المرور"]]
        self.main_pages = [
            ["Home Page", "Stock Page", "New Process Page", "DataBase Page", "Info Page", "Settings Page"],
            ["الفحة الرئيسية", "صفحة المخزون", "صفحة العمليات الجديدة", "صفحة قاعدة البينات", "صفحة المعلومات",
             "الإعدادات"]]
        ########################load users accounts#######################
        self.usernames = ["Abdelrahman_Amr", "ahmad amr", "mohamed ahmed"]
        self.passwords = ["2182003s2GBS", "2182003s2gbs", "2182003s1z"]
        self.types = ['admin', 'manger', 'employee']
        self.accout_types = ["admin", "manger", "employee"]


        self.current_type = None


        self.width, self.height = 1500, 950
        self.resize(self.width, self.height)


        self.msgSc = qtw.QShortcut(qtg.QKeySequence('Ctrl+E'), self)

        self.msgSc.activated.connect(self.navigate_info_pages)
        ####################Top frame#####################

        self.genral_w = qtw.QWidget()
        self.top_frame = qtw.QFrame(self.genral_w)
        # self.top_frame.setStyleSheet(
        #    "QFrame{border-width:0px;background-color:black;min-height:70px;min-width:" + str(self.width) + "px;}")
        self.menue_btn = qtw.QPushButton()
        self.menue_btn.setIcon(qtg.QIcon('icons//i.png'))
        self.menue_btn.setIconSize(qtc.QSize(50, 50))
        self.menue_btn.setStyleSheet(self.menue_btn_style())
        self.menue_btn.clicked.connect(self.menue_btn_fun)
        self.top_frame_label = qtw.QLabel()
        self.top_frame_label.setStyleSheet("QLabel{color:white;font bold 14px;}")
        self.top_frame_label.setText(self.main_pages[self.lang][0])

        #####################Home Page Buttons##############################
        self.stock_btn_home = qtw.QPushButton()
        self.stock_btn_home.setIcon(qtg.QIcon("icons//stock.png"))
        self.stock_btn_home.setStyleSheet(self.home_page_btn_style())
        self.stock_btn_home.setIconSize(qtc.QSize(80, 80))
        self.stock_btn_home.clicked.connect(self.stock_btn_fun)
        self.data_btn_home = qtw.QPushButton()
        self.data_btn_home.setIcon(qtg.QIcon("icons//database.png"))
        self.data_btn_home.setStyleSheet(self.home_page_btn_style())
        self.data_btn_home.setIconSize(qtc.QSize(80, 80))
        self.data_btn_home.clicked.connect(self.database_btn_fun)
        self.new_btn_home = qtw.QPushButton()
        self.new_btn_home.setIcon(qtg.QIcon("icons//new.png"))
        self.new_btn_home.setStyleSheet(self.home_page_btn_style())
        self.new_btn_home.setIconSize(qtc.QSize(80, 80))
        self.new_btn_home.clicked.connect(self.new_order_btn_fun)
        self.info_btn_home = qtw.QPushButton()
        self.info_btn_home.setIcon(qtg.QIcon("icons//info.png"))
        self.info_btn_home.setStyleSheet(self.home_page_btn_style())
        self.info_btn_home.setIconSize(qtc.QSize(80, 80))
        self.info_btn_home.clicked.connect(self.info_btn_fun)
        ######################################Side frame####################################################################
        self.side_frame = qtw.QFrame(self.genral_w)
        # self.side_frame.setStyleSheet("QFrame{border-width:0px;background-color:black;min-width:70px;min-height:" + str(
        #    self.height - 70) + "px;}")
        self.home_btn = qtw.QPushButton()
        self.home_btn.setIcon(qtg.QIcon('icons//home.png'))
        self.home_btn.setStyleSheet(self.menue_btn_style())
        self.home_btn.setIconSize(qtc.QSize(50, 50))
        self.home_btn.clicked.connect(self.home_btn_fun)

        self.stock_btn = qtw.QPushButton()
        self.stock_btn.setIcon(qtg.QIcon('icons//stock.png'))
        self.stock_btn.setStyleSheet(self.menue_btn_style())
        self.stock_btn.setIconSize(qtc.QSize(50, 50))
        self.stock_btn.clicked.connect(self.stock_btn_fun)

        self.new_btn = qtw.QPushButton()
        self.new_btn.setIcon(qtg.QIcon('icons//new.png'))
        self.new_btn.setStyleSheet(self.menue_btn_style())
        self.new_btn.setIconSize(qtc.QSize(50, 50))
        self.new_btn.clicked.connect(self.new_order_btn_fun)

        self.data_btn = qtw.QPushButton()
        self.data_btn.setIcon(qtg.QIcon('icons//database.png'))
        self.data_btn.setStyleSheet(self.menue_btn_style())
        self.data_btn.setIconSize(qtc.QSize(50, 50))
        self.data_btn.clicked.connect(self.database_btn_fun)

        self.info_btn = qtw.QPushButton()
        self.info_btn.setIcon(qtg.QIcon('icons//info.png'))
        self.info_btn.setStyleSheet(self.menue_btn_style())
        self.info_btn.setIconSize(qtc.QSize(50, 50))
        self.info_btn.clicked.connect(self.info_btn_fun)

        self.settings_btn = qtw.QPushButton()
        self.settings_btn.setIcon(qtg.QIcon('icons//settings.png'))
        self.settings_btn.setStyleSheet(self.menue_btn_style())
        self.settings_btn.setIconSize(qtc.QSize(50, 50))
        self.settings_btn.clicked.connect(self.settings_btn_fun)

        #####################stock page##############################
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
        # self.stock_tabel.setColumnWidth(4, 400)
        self.stock_tabel.horizontalHeader().setStretchLastSection(True)
        self.stock_tabel.verticalHeader().setStretchLastSection(True)

        self.stock_tabel.setHorizontalHeaderLabels(
            ["Product", "Availble", "price per unit", "Sell price per unit", "sold"])

        ########################New Order##############################################

        self.new_order_widget = qtw.QWidget()
        self.new_order_ly = qtw.QStackedLayout()

        ############new order_home_page###################

        self.new_order_h_widget = qtw.QWidget()
        self.new_order_h_widget.setStyleSheet(self.home_page_btn_style())
        self.Buy_btn = qtw.QPushButton("Buy")
        self.Buy_btn.clicked.connect(self.Buy_btn_fun)

        self.Sell_btn = qtw.QPushButton("Sell")
        self.Sell_btn.clicked.connect(self.Sell_btn_fun)

        self.new_package_btn = qtw.QPushButton("New Package")
        self.new_package_btn.clicked.connect(self.new_package_btn_fun)

        self.new_emp_btn = qtw.QPushButton("New Employee")
        self.new_emp_btn.clicked.connect(self.new_emp_btn_fun)

        ##################New Order bar#################################
        self.new_order_bar = qtw.QFrame()
        # self.new_order_bar.setStyleSheet(
        #    "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:rgb(0,0,0);min-height:50px;}")
        self.new_order_back_btn = qtw.QPushButton()
        self.new_order_back_btn.setIcon(qtg.QIcon("icons//back.png"))
        self.new_order_back_btn.setStyleSheet(self.bar_btn_style())
        self.new_order_back_btn.clicked.connect(self.new_order_back_btn_fun)

        self.new_order_forward_btn = qtw.QPushButton()
        self.new_order_forward_btn.setIcon(qtg.QIcon("icons//forward.png"))
        self.new_order_forward_btn.setStyleSheet(self.bar_btn_style())
        self.new_order_forward_btn.clicked.connect(self.new_order_forward_btn_fun)

        self.new_order_home_btn = qtw.QPushButton()
        self.new_order_home_btn.setIcon(qtg.QIcon("icons//home.png"))
        self.new_order_home_btn.setStyleSheet(self.bar_btn_style())
        self.new_order_home_btn.clicked.connect(self.new_order_home_btn_fun)

        self.new_order_bar_label = qtw.QLabel()
        self.new_order_bar_label.setStyleSheet("QLabel{color:white;font bold 14px;}")
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][0])


        ############Create new package################
        self.new_package_widget = qtw.QWidget()
        self.new_package_widget.setStyleSheet(self.main_widgets_style())
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

        self.clear_packages_btn=qtw.QPushButton("Clear")
        self.clear_packages_btn.clicked.connect(self.clear_package_btn_fun)


        ##############Buy Product###################

        self.buy_product_widget = qtw.QWidget()

        self.buy_product_widget.setStyleSheet(self.main_widgets_style())
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
        self.add_buy_package_btn=qtw.QPushButton("Add package")
        self.add_buy_package_btn.setStyleSheet(self.button_style())
        self.add_buy_package_btn.clicked.connect(self.add_buy_package_btn_fun)

        self.product_name_label = qtw.QLabel("Product name")
        self.product_quantity_label = qtw.QLabel("quantity")
        self.product_price_label = qtw.QLabel("price")
        self.product_selling_price_label = qtw.QLabel("selling price")
        self.add_b_prod = qtw.QPushButton("Add Product")
        self.add_b_prod.setStyleSheet(self.button_style())
        self.add_b_prod.clicked.connect(self.add_b_prod_btn_fun)

        self.products_tabel = qtw.QTableWidget(2, 4)
        self.products_tabel.setHorizontalHeaderLabels(["Product", "Quantity", "Buy Price", "selling Price"])
        self.products_tabel.horizontalHeader().setStretchLastSection(True)
        self.products_tabel.verticalHeader().setStretchLastSection(True)

        self.total_tabel_b = qtw.QTableWidget(1, 3)
        self.total_tabel_b.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.total_tabel_b.horizontalHeader().setStretchLastSection(True)
        self.total_tabel_b.verticalHeader().setStretchLastSection(True)

        # self.total_tabel_b.setFixedHeight(75)
        # self.total_tabel_b.setStyleSheet("min-height:100px;max-height:100px;")
        self.btn_group=qtw.QButtonGroup()
        self.stock_product = qtw.QRadioButton("Stock Product")
        self.used_product = qtw.QRadioButton("used Product")
        self.service_product = qtw.QRadioButton("service")
        self.btn_group.addButton(self.stock_product,)
        self.btn_group.addButton(self.used_product)
        self.btn_group.addButton(self.service_product)

        self.type_label = qtw.QLabel("Select Product type")

        self.dte = qtw.QDateEdit(qtc.QDate(qtc.QDate().currentDate()), self)
        self.dte.setCalendarPopup(True)  # have a calender to select date from
        self.dte_label = qtw.QLabel("Date")
        self.buy_submit = qtw.QPushButton("Submit")
        self.buy_submit.clicked.connect(self.buy_submit_btn_fun)
        self.buy_submit.setStyleSheet(self.button_style())

        self.clear_buy_page=qtw.QPushButton("clear")
        self.clear_buy_page.clicked.connect(self.clear_buy_page_btn_fun)

        ################Sell product#################
        self.sell_Product = qtw.QWidget()
        self.sell_Product.setStyleSheet(self.main_widgets_style())
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
        self.service_qt=qtw.QSpinBox()
        self.service_qt.setRange(0, 1000000000)
        self.service_qt_label=qtw.QLabel("quantity")
        self.add_service_btn=qtw.QPushButton("Add service")
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
        self.sell_submit.setStyleSheet(self.button_style())
        self.sell_submit.clicked.connect(self.sell_submit_btn_fun)
        self.clear_sell_page_btn=qtw.QPushButton("Clear")
        self.clear_sell_page_btn.setStyleSheet(self.button_style())
        self.clear_sell_page_btn.clicked.connect(self.clear_sell_page_btn_fun)


        self.add_product_btn = qtw.QPushButton("Add product")
        self.add_product_btn.clicked.connect(self.add_product_btn_fun)
        self.add_Packages_btn = qtw.QPushButton("Add package")
        self.add_Packages_btn.clicked.connect(self.add_package_btn_fun)
        self.sell_date = qtw.QDateEdit(qtc.QDate(qtc.QDate().currentDate()), self)
        self.sell_date.setCalendarPopup(True)  # have a calender to select date from
        self.sell_date_label = qtw.QLabel("Date")

        #############################Login Form######################
        self.login_label = qtw.QLabel()
        self.login_label.setPixmap(qtg.QPixmap("icons//login.png"))
        self.login_label.setStyleSheet("QLabel{border-radius:175px;min-width:350px;min-height:350px;}")

        self.username_in = qtw.QLineEdit()
        self.username_in.setText(self.usernames[0])
        self.password_in = qtw.QLineEdit()
        self.password_in.setEchoMode(qtw.QLineEdit.Password)
        self.password_in.setText(self.passwords[0])
        self.password_label = qtw.QLabel("Enter your password")
        self.username_label = qtw.QLabel("Enter your username")
        self.login_btn = qtw.QPushButton("Login")
        self.username_in.setStyleSheet(self.line_edit_style())
        self.password_in.setStyleSheet(self.line_edit_style())
        self.login_btn.setStyleSheet(self.button_style())
        self.wrong_pass = qtw.QLabel()
        self.wrong_pass.setStyleSheet("QLabel{color:red;}")
        self.login_btn.clicked.connect(self.login_btn_fun)
        self.wrong_pass.hide()
        ####################Data base page####################################
        self.employees_btn = qtw.QPushButton("Employees")
        self.employees_btn.clicked.connect(self.employees_btn_fun)
        self.employees_btn.setStyleSheet(self.home_page_btn_style())

        self.imports_btn = qtw.QPushButton("imports")
        self.imports_btn.clicked.connect(self.imports_btn_fun)
        self.imports_btn.setStyleSheet(self.home_page_btn_style())

        self.exports_btn = qtw.QPushButton("exports")
        self.exports_btn.clicked.connect(self.exports_btn_fun)
        self.exports_btn.setStyleSheet(self.home_page_btn_style())

        self.calculations_btn = qtw.QPushButton("calculations")
        self.calculations_btn.clicked.connect(self.calculations_btn_fun)
        self.calculations_btn.setStyleSheet(self.home_page_btn_style())

        ################DataBase bar########################

        self.database_bar = qtw.QFrame()
        # self.database_bar.setStyleSheet(
        #    "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:rgb(0,0,0);min-height:50px;}")
        self.back_btn = qtw.QPushButton()
        self.back_btn.setIcon(qtg.QIcon("icons//back.png"))
        self.back_btn.setStyleSheet(self.bar_btn_style())
        self.back_btn.clicked.connect(self.back_btn_fun)

        self.forward_btn = qtw.QPushButton()
        self.forward_btn.setIcon(qtg.QIcon("icons//forward.png"))
        self.forward_btn.setStyleSheet(self.bar_btn_style())
        self.forward_btn.clicked.connect(self.forward_btn_fun)

        self.database_home_btn = qtw.QPushButton()
        self.database_home_btn.setIcon(qtg.QIcon("icons//home.png"))
        self.database_home_btn.setStyleSheet(self.bar_btn_style())
        self.database_home_btn.clicked.connect(self.database_home_btn_fun)

        self.database_bar_label = qtw.QLabel()
        self.database_bar_label.setStyleSheet("QLabel{color:white;font bold 15px;}")
        self.database_bar_label.setText(self.database_pages[self.lang][0])

        self.sort_db_btn = qtw.QPushButton()
        self.sort_db_btn.setIcon(qtg.QIcon("icons//sort.png"))
        self.sort_db_btn.setStyleSheet(self.bar_btn_style())

        self.filter_db_btn = qtw.QPushButton()
        self.filter_db_btn.setIcon(qtg.QIcon("icons//filter.png"))
        self.filter_db_btn.setStyleSheet(self.bar_btn_style())

        self.undo_db_btn = qtw.QPushButton()
        self.undo_db_btn.setIcon(qtg.QIcon("icons//undo.png"))
        self.undo_db_btn.setStyleSheet(self.bar_btn_style())

        self.redo_db_btn = qtw.QPushButton()
        self.redo_db_btn.setIcon(qtg.QIcon(qtg.QPixmap("icons//undo.png").transformed(qtg.QTransform().rotate(180))))
        self.redo_db_btn.setStyleSheet(self.bar_btn_style())

        self.search_box_db = qtw.QLineEdit()
        self.search_box_db.setStyleSheet(
            '''color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px''')
        self.search_btn_db = qtw.QPushButton()
        self.search_btn_db.setIcon(qtg.QIcon("icons/search.png"))
        self.search_btn_db.setIconSize(qtc.QSize(50, 50))
        self.search_btn_db.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")

        ################################import-export csv ly#######################
        l = ["Employees", "imports", "Exports", "Calculations"]
        self.import_csv_btn = qtw.QPushButton("Import CSV")
        self.import_csv_btn.setStyleSheet(self.button_style())
        self.export_csv_btn = qtw.QPushButton("Export CSV")
        self.export_csv_btn.setStyleSheet(self.button_style())

        self.import_csv_cmb = qtw.QComboBox()
        self.import_csv_cmb.setStyleSheet(self.cmb_style())
        self.export_csv_cmb = qtw.QComboBox()
        self.export_csv_cmb.setStyleSheet(self.cmb_style())

        self.import_csv_cmb.addItems(l)
        self.export_csv_cmb.addItems(l)
        ####################Employees tabel ly##################
        self.emp_tabel = qtw.QTableWidget(20, 6)
        self.emp_tabel.setHorizontalHeaderLabels(
            ["Code", "Name", "Position", "Salary", "Total experience", "inside experience"])
        self.emp_tabel.horizontalHeader().setStretchLastSection(True)
        self.emp_tabel.verticalHeader().setStretchLastSection(True)

        self.add_emp = qtw.QPushButton("Add")
        self.add_emp.clicked.connect(self.add_employee_btn_fun)
        self.add_emp.setStyleSheet(self.button_style())
        self.remove_emp = qtw.QPushButton("remove")
        self.remove_emp.setStyleSheet(self.button_style())

        self.save_emp = qtw.QPushButton("Save")
        self.save_emp.setStyleSheet(self.button_style())
        ################exports#######################

        self.exports_tabel = qtw.QTableWidget(20, 9)
        self.exports_tabel.setHorizontalHeaderLabels(
            ["Client Name", "Email", "Address", "Link", "Products", "Cost", "Profit", "Losses", "Date"])
        self.exports_tabel.horizontalHeader().setStretchLastSection(True)
        self.exports_tabel.verticalHeader().setStretchLastSection(True)

        self.add_exp = qtw.QPushButton("Add")
        self.add_exp.setStyleSheet(self.button_style())
        self.add_exp.clicked.connect(self.add_exp_btn_fun)
        self.remove_exp = qtw.QPushButton("remove")
        self.remove_exp.setStyleSheet(self.button_style())

        self.save_exp = qtw.QPushButton("Save")
        self.save_exp.setStyleSheet(self.button_style())
        ##############imports###################

        self.imp_tabel = qtw.QTableWidget(20, 8)
        self.imp_tabel.setHorizontalHeaderLabels(
            ["supplier Name", "Email", "Address", "Link", "Products", "Cost", "Losses", "Date"])
        self.imp_tabel.horizontalHeader().setStretchLastSection(True)
        self.imp_tabel.verticalHeader().setStretchLastSection(True)

        self.add_imp = qtw.QPushButton("Add")
        self.add_imp.clicked.connect(self.add_imp_btn_fun)
        self.add_imp.setStyleSheet(self.button_style())
        self.remove_imp = qtw.QPushButton("remove")
        self.remove_imp.setStyleSheet(self.button_style())

        self.save_imp = qtw.QPushButton("Save")
        self.save_imp.setStyleSheet(self.button_style())
        ##############Calculations#############
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
        ####################add_employee page##################
        self.select_employee_type_label=qtw.QLabel("Enter process type")
        self.select_employee_type=qtw.QComboBox()
        self.select_employee_type.addItems(['New Employee','update employee info'])
        self.emp_code_input_label=qtw.QLabel("Enter employee code")
        self.emp_code_input=qtw.QComboBox()
        self.emp_code_input.setToolTip("Only enter the code in case of an old employee")
        self.add_emp_page_widget = qtw.QWidget()
        self.add_emp_page_widget.setStyleSheet(self.main_widgets_style())
        self.add_emp_name_label = qtw.QLabel()
        self.add_emp_name_label.setText("Enter Employee Name")
        self.add_emp_name = qtw.QLineEdit()

        self.add_emp_position_label = qtw.QLabel()
        self.add_emp_position_label.setText("Enter Employee Position")
        self.add_emp_position = qtw.QLineEdit()

        self.add_emp_salary_label = qtw.QLabel()
        self.add_emp_salary_label.setText("Enter Employee salary")
        self.add_emp_salary = qtw.QLineEdit()


        self.hire_date=qtw.QDateEdit(qtc.QDate(qtc.QDate().currentDate()))
        self.hire_date.setCalendarPopup(True)
        self.add_emp_submit = qtw.QPushButton("Submit")
        self.add_emp_clear_btn=qtw.QPushButton("clear")
        self.add_emp_submit.clicked.connect(self.add_emp_submit_btn_fn)
        self.add_emp_clear_btn.clicked.connect(self.clear_emp_btn_fun)
        ###################info page######################
        self.scrollable_info = qtw.QScrollArea()
        self.scrollable_info.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        self.scrollable_info.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        self.scrollable_info.setWidgetResizable(True)

        self.logo = qtw.QLabel()
        self.logo.setPixmap(qtg.QPixmap('icons//logo.png'))
        self.company_name = "Enviromental Saftey Services Co.(ESSC)"
        self.address = "Smouha Sidi Gaber Alexandria, Egypt."
        self.website = "http://esscegypt.com/"
        self.mobile = "P: 2005037440 M: 201129070766 / 201008003018 / 201280773379"
        self.n_employees = str(self.emp_tabel.rowCount())
        self.rent = str(0)
        self.description = "ESSC provides environmental and safety consulting services, too general supplies and contracting;\nwe offer these services to our clients not only for pollution control and protection place,\n but also for resource preservation.\n through cleaner production and adequate mitigation measures in design, operation,and proper management manners.      "

        self.info_name_label = qtw.QLabel("Name: ")
        self.info_name_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_add_label = qtw.QLabel("Company Address: ")
        self.info_add_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_emp_label = qtw.QLabel("Number of employees: ")
        self.info_emp_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_Mobile_label = qtw.QLabel("Mobile numbers: ")
        self.info_Mobile_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_Website_label = qtw.QLabel("Website: ")
        self.info_Website_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_Rent_label = qtw.QLabel("Rent: ")
        self.info_Rent_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_description_label = qtw.QLabel("Description: ")
        self.info_description_label.setFont(qtg.QFont("Arial", 14, 75, False))

        self.info_name_label_2 = qtw.QLabel(self.company_name)
        self.info_name_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_name_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_add_label_2 = qtw.QLabel("Company Address: ")
        self.info_add_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_add_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_emp_label_2 = qtw.QLabel(self.n_employees)
        self.info_emp_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_emp_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_Mobile_label_2 = qtw.QLabel(self.mobile)
        self.info_Mobile_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_Mobile_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_Website_label_2 = qtw.QLabel(self.website)
        self.info_Website_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_Website_label_2.setStyleSheet("QLabel{color:blue;}")
        self.info_Rent_label_2 = qtw.QLabel(self.rent)
        self.info_Rent_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_Rent_label_2.setStyleSheet("QLabel{color:blue;}")

        self.info_description_label_2 = qtw.QLabel(self.description)
        self.info_description_label_2.setFont(qtg.QFont("Arial", 14, 75, False))
        self.info_description_label_2.setStyleSheet("QLabel{color:blue;}")

        ##################Edit info############################

        self.edit_info_page_widget = qtw.QWidget()
        self.edit_info_page_widget.setStyleSheet(self.main_widgets_style())

        self.edit_company_name = qtw.QLineEdit()
        self.edit_company_address = qtw.QLineEdit()
        self.edit_company_website = qtw.QLineEdit()
        self.edit_company_mobiles = qtw.QLineEdit()
        self.edit_company_rent = qtw.QLineEdit()
        self.edit_company_description = qtw.QTextEdit()

        self.edit_company_name_label = qtw.QLabel("Enter new company Name")
        self.edit_company_address_label = qtw.QLabel("Enter new company Address")
        self.edit_company_website_label = qtw.QLabel("Enter new company Website")
        self.edit_company_mobiles_label = qtw.QLabel("Enter new Mobile numbers")
        self.edit_company_rent_label = qtw.QLabel("Enter company new Rent")
        self.edit_company_description_label = qtw.QLabel("Enter new Description")

        #############Settings#########################
        self.main_settings_widget = qtw.QWidget()
        self.Settings_widget = qtw.QWidget()
        self.Settings_widget.setStyleSheet(self.home_page_btn_style())
        self.change_password = qtw.QPushButton("change password")
        self.change_password.clicked.connect(self.change_password_btn_fun)
        self.create_new_username = qtw.QPushButton("Create new account")
        self.create_new_username.clicked.connect(self.create_new_username_btn_fun)
        self.laguage_settings = qtw.QPushButton("Set to Arabic")
        self.laguage_settings.clicked.connect(self.translate_lang)
        self.night_mode_btn = qtw.QPushButton("Light/dark Mode")
        self.night_mode_btn.clicked.connect(self.set_light_night_mode)

        # self.toggle = AnimatedToggle(
        # checked_color="#00FFFF",
        # pulse_checked_color="#44FFB000"
        # )
        # self.toggle.setChecked(True)
        # self.toggle.toggled.connect(self.set_light_night_mode)

        #######################Create new account####################################

        self.create_acc_widget = qtw.QWidget()
        self.create_acc_widget.setStyleSheet(self.main_widgets_style())
        self.add_username_label = qtw.QLabel("Enter username")
        self.new_password_label = qtw.QLabel("Enter Password")
        self.add_confirmed_password_label = qtw.QLabel("Confirm password")

        self.add_username = qtw.QLineEdit()
        self.new_password = qtw.QLineEdit()
        self.add_confirmed_password = qtw.QLineEdit()

        self.account_type = qtw.QComboBox()
        self.account_type.addItems(["Employee", "Manger", "Admin"])
        self.account_type_label = qtw.QLabel("Enter account type")
        self.account_type_password = qtw.QLineEdit()
        self.account_password_type_label = qtw.QLabel("Enter account type password")
        self.create_btn = qtw.QPushButton("Create")
        #############################Change password ###############################
        self.change_password_widget = qtw.QWidget()
        self.change_password_widget.setStyleSheet(self.main_widgets_style())
        self.username_change_label = qtw.QLabel("Enter Username")
        self.username_change = qtw.QLineEdit()
        self.old_password_label = qtw.QLabel("Enter Old Password")
        self.old_password = qtw.QLineEdit()
        self.changed_password_label = qtw.QLabel("Enter New Password")
        self.changed_password = qtw.QLineEdit()
        self.confirmed_password_label = qtw.QLabel("Confirm New Password")
        self.confirmed_password = qtw.QLineEdit()
        self.submit_changed_password = qtw.QPushButton("Submit changes")

        ##################Settings Order bar#################################
        self.settings_bar_frame = qtw.QFrame()
        self.settings_bar_frame.setStyleSheet(
            """QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:rgb(0,0,0);min-height:50px;}""")
        self.settings_back_btn = qtw.QPushButton()
        self.settings_back_btn.setIcon(qtg.QIcon("icons//back.png"))
        self.settings_back_btn.setStyleSheet(self.bar_btn_style())
        self.settings_back_btn.clicked.connect(self.settings_back_btn_fun)

        self.settings_forward_btn = qtw.QPushButton()
        self.settings_forward_btn.setIcon(qtg.QIcon("icons//forward.png"))
        self.settings_forward_btn.setStyleSheet(self.bar_btn_style())
        self.settings_forward_btn.clicked.connect(self.settings_forward_btn_fun)

        self.settings_home_btn = qtw.QPushButton()
        self.settings_home_btn.setIcon(qtg.QIcon("icons//home.png"))
        self.settings_home_btn.setStyleSheet(self.bar_btn_style())
        self.settings_home_btn.clicked.connect(self.settings_home_btn_fun)

        self.settings_bar_label = qtw.QLabel()
        self.settings_bar_label.setStyleSheet("QLabel{color:white;font bold 14px;}")
        self.settings_bar_label.setText(self.settings_pages[self.lang][0])
        self.edit_theme_color=qtw.QPushButton()

        self.settings_color_btn=qtw.QPushButton()
        self.settings_color_btn.setIcon(qtg.QIcon("icons//colors.png"))
        self.settings_color_btn.setIconSize(qtc.QSize(30,30))
        self.settings_color_btn.setStyleSheet(self.bar_btn_style())
        self.settings_color_btn.clicked.connect(self.change_color_btn_fun)
        ###############################Data base functions#####################################
        self.get_stock()
        self.get_employees()
        self.update_cmb()

        #####################Set Layout function#####################################
        self.set_layout()

        if self.dark_state == 1:
            self.apply_dark_mode()
        else:
            self.apply_light_mode()
        self.set_lang()
        self.load_products_into_package()


    def add_b_prod_btn_fun(self):
        if self.products_tabel.rowCount()<=(self.prod_table_current):
            self.products_tabel.setRowCount(self.prod_table_current+2)
        ind=None
        for i in range(self.prod_table_current):
            if self.product_name.currentText()==self.products_tabel.item(i,0).text():
                ind=i
                print(ind)
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

        self.product_name.setCurrentText("")
        self.product_quantity.setValue(0)
        self.product_price.setValue(0)
        self.product_selling_price.setValue(0)
        tot_cost=0
        total=0

        for i in range(self.prod_table_current):
            tot_cost+=int(self.products_tabel.item(i,1).text())*int(self.products_tabel.item(i,2).text())
            total+=int(self.products_tabel.item(i,1).text())*int(self.products_tabel.item(i,3).text())
        total_profit=total-tot_cost

        self.total_tabel_b.setItem(0,0,qtw.QTableWidgetItem(str(tot_cost)))
        self.total_tabel_b.setItem(0,1,qtw.QTableWidgetItem(str(total)))
        self.total_tabel_b.setItem(0,2,qtw.QTableWidgetItem(str(total_profit)))

        self.repaint()





    def add_buy_package_btn_fun(self):
        p_name = self.buy_package_name.currentText()
        p_qt = int(self.buy_package_quantity.value())
        prods = self.packages_dict[p_name]

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
                                        qtw.QTableWidgetItem(str(self.stock_data[name][1])))
                self.products_tabel.setItem(self.prod_table_current, 3,
                                        qtw.QTableWidgetItem(str(self.stock_data[name][2])))
                self.prod_table_current += 1
        tot_cost = 0
        total = 0

        for i in range(self.prod_table_current):
            tot_cost += int(self.products_tabel.item(i, 1).text()) * int(self.products_tabel.item(i, 2).text())
            total += int(self.products_tabel.item(i, 1).text()) * int(self.products_tabel.item(i, 3).text())
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
                self.my_cursor.execute(sql_stuff,(supplier_name,supplier_email,supplier_address,supplier_link,products,type,int(tot_cost),int(total),0,date))
            except:
                pass
            if type=='Stock Product':
                for i in range(self.prod_table_current):
                    name=self.products_tabel.item(i,0).text()
                    qt=self.products_tabel.item(i, 1).text()
                    buy_price=self.products_tabel.item(i, 2).text()
                    sell_price=self.products_tabel.item(i,3).text()
                    try:
                        sql_stuff = "INSERT INTO stock  (product,availble,buying_price,selling_price) VALUES(%s,%s,%s,%s);"
                        self.my_cursor.execute(sql_stuff, (name,int(qt),int(buy_price),int(sell_price)))
                    except:
                        try:
                            sql_stuff = "UPDATE stock SET availble=availble+%s WHERE product=%s"
                            self.my_cursor.execute(sql_stuff, (qt,name))

                            sql_stuff = "UPDATE stock SET buying_price=%s WHERE product=%s"
                            self.my_cursor.execute(sql_stuff, (buy_price,name))

                            sql_stuff = "UPDATE stock SET sell_price=%s WHERE product=%s"
                            self.my_cursor.execute(sql_stuff, (sell_price,name))
                        except:
                            pass
            self.get_stock()
            self.update_cmb()
            self.clear_buy_page_btn_fun()



        self.mydb.commit()
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
        self.set_lang()


    def get_stock(self):
        self.my_cursor.execute("SELECT * FROM stock")
        data=self.my_cursor.fetchall()
        self.stock_data=dict()
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

    def update_cmb(self):
        packages_list=list(self.packages_dict.keys())
        products_list=list(self.stock_data.keys())
        emps_list=list(self.employee_data.keys())
        self.package_name.clear()
        self.add_product_to_package.clear()
        self.product_name.clear()
        self.add_product.clear()
        self.add_Packages.clear()
        self.buy_package_name.clear()
        self.emp_code_input.clear()
        self.package_name.addItems(packages_list)
        self.add_product_to_package.addItems(products_list)
        self.product_name.addItems(products_list)
        self.add_product.addItems(products_list)
        self.add_Packages.addItems(packages_list)
        self.buy_package_name.addItems(packages_list)
        self.emp_code_input.addItems(emps_list)


    def load_products_into_package(self):
        self.package_tabel.clear()
        self.set_lang()
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


    def remove_package_btn_fun(self):
        self.packages_dict.pop(self.package_name.currentText())
        self.update_cmb()



    def clear_package_btn_fun(self):
        self.package_tabel_current = 0
        self.package_tabel.clear()
        self.add_product_to_package.setCurrentText("")
        self.product_qt_package.setValue(0)
        self.package_tabel.setRowCount(5)
        self.update_cmb()
        self.set_lang()
    def add_product_btn_fun(self):
        name=self.add_product.currentText()
        ind=None
        for i in range(self.sell_table_current):
            if name==self.prod_tabel.item(i, 0).text():
                ind=i

        if self.prod_tabel.rowCount()<=self.sell_table_current:
            self.prod_tabel.setRowCount(self.sell_table_current+2)

        if name in list(self.stock_data.keys()):
            if  self.stock_data[name][0]>=int(self.product_qt.value()):
                if ind is not None:
                    self.prod_tabel.setItem(ind, 1,qtw.QTableWidgetItem(str(int(self.prod_tabel.item(ind,1).text())+int(self.product_qt.value() ) ) ) )
                else:
                    self.prod_tabel.setItem(self.sell_table_current,0,qtw.QTableWidgetItem(name))
                    self.prod_tabel.setItem(self.sell_table_current,1,qtw.QTableWidgetItem(str(self.product_qt.value())))
                    self.prod_tabel.setItem(self.sell_table_current,2,qtw.QTableWidgetItem(str(self.stock_data[name][1])))
                    self.prod_tabel.setItem(self.sell_table_current,3,qtw.QTableWidgetItem(str(self.stock_data[name][2])))
                    self.sell_table_current += 1

            else:
                res=qtw.QMessageBox.information(self,"Quantity",f"not enough {name} in stock")

        else:
                res = qtw.QMessageBox.information(self,"invalid product",f"{name} not in stock")
        self.update_sell_total_table()
    def add_package_btn_fun(self):

        p_name=self.add_Packages.currentText()
        p_qt=int(self.packages_qt.value())
        prods=self.packages_dict[p_name]

        valid=True
        for name,qt in prods:
            qt=int(qt)
            if name in list(self.stock_data.keys()):
                if self.stock_data[name][0]>=qt*p_qt:
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
                    self.prod_tabel.setItem(self.sell_table_current,2,qtw.QTableWidgetItem(str(self.stock_data[name][1])))
                    self.prod_tabel.setItem(self.sell_table_current,3,qtw.QTableWidgetItem(str(self.stock_data[name][2])))
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
        self.set_lang()
    def sell_submit_btn_fun(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to save this import process", qm.Yes | qm.No)
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
                self.my_cursor.execute(sql_stuff,(name,email,address,link,products,tot_cost,total,profit,0,date))
            except:
                pass
            for i in range(self.sell_table_current):
                name=self.prod_tabel.item(i,0).text()
                prod_qt=self.prod_tabel.item(i,1).text()
                if name in list(self.stock_data.keys()):
                    try:

                        sql_stuff="""UPDATE stock SET sold=sold+%s WHERE Product=%s"""
                        self.my_cursor.execute(sql_stuff,(int(prod_qt),name))
                    except:
                        pass
                    try:
                        sql_stuff="""UPDATE stock SET availble=availble-%s WHERE Product=%s"""
                        self.my_cursor.execute(sql_stuff,(prod_qt,name))
                    except:
                        pass
            self.mydb.commit()
            self.get_stock()
            self.update_cmb()
    def add_emp_submit_btn_fn(self):
        qm = qtw.QMessageBox(self)
        ret = qm.question(self, '', "Are you sure you want to update employees info", qm.Yes | qm.No)
        if ret == qm.Yes:
            type=self.select_employee_type.currentText()
            name = self.add_emp_name.text()
            position = self.add_emp_position.text()

            salary = self.add_emp_salary.text()
            date = self.hire_date.date().toString(qtc.Qt.ISODate)
            code=self.emp_code_input.currentText()
            if type=="New Employee":
                try:
                    sql_stuff="INSERT INTO employees (name,position,salary,hire_date) VALUES(%s,%s,%s,%s)"
                    self.my_cursor.execute(sql_stuff, (name, position, salary, date))
                except:
                    pass
            elif type=='update employee info':

                try:
                    sql_stuff="UPDATE employees SET name=%s,position=%s,salary=%s,hire_date=%s WHERE code=%s"
                    self.my_cursor.execute(sql_stuff, (name, position, salary, date,code))
                except:
                    res = qtw.QMessageBox.information(self, "Employee code not found", f"Couldn't find employee code you entered")

            self.mydb.commit()
            self.get_employees()
            self.update_cmb()
            self.clear_emp_btn_fun()
        else:
            pass
    def clear_emp_btn_fun(self):
        self.add_emp_name.setText("")
        self.add_emp_position.setText("")
        self.add_emp_salary.setText("")
        self.hire_date.setDate(qtc.QDate(qtc.QDate().currentDate()))


    def get_employees(self):
        try:
            self.employee_data=dict()
            self.my_cursor.execute("SELECT * FROM employees")
            data=self.my_cursor.fetchall()
            for emp in data:
                code,name,position,salary,hire_date=emp
                self.employee_data[str(code)]=[name,position,salary,hire_date]
        except:
            pass


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
            json.dump(self.packages_dict,f)

    def set_lang(self):
        try:
            if self.lang == 0:
                self.set_english()
            else:
                self.set_arabic()
        except:
            pass
    def translate_lang(self):
        if self.lang == 0:
            self.set_arabic()
        else:
            self.set_english()

    def login_btn_fun(self):
        if self.username_in.text() in self.usernames:
            if (self.password_in.text() == self.passwords[self.usernames.index(self.username_in.text())]):
                self.current_type = self.types[self.usernames.index(self.username_in.text())]
                self.stacked_g.setCurrentIndex(1)
            else:
                self.wrong_pass.setText(["Wrong password", "كلمة مرور غير صحيحة"][self.lang])
                self.wrong_pass.show()
        else:
            self.wrong_pass.setText(["Wrong username", "اسم مستخدم غير صحيح"][self.lang])
            self.wrong_pass.show()
        if self.current_type != "admin":
            self.emp_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
            self.calc_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
            self.imp_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
            self.exports_tabel.setEditTriggers(qtw.QTableWidget.NoEditTriggers)

    def set_light_night_mode(self):

        if (not self.dark_state):
            self.apply_dark_mode()
            self.dark_state = 1
        else:
            self.apply_light_mode()
            self.dark_state = 0
    def change_color_btn_fun(self):
        if self.dark_state==1:
            color = qtw.QColorDialog.getColor(qtg.QColor(0, 0, 0), self, "choose color")
            self.dark_theme=f'rgb({color.red()},{color.green()},{color.blue()})'
            self.dark_colors=f'{color.red()},{color.green()},{color.blue()}'
            self.apply_dark_mode()
        elif self.dark_state==0:
            color = qtw.QColorDialog.getColor(qtg.QColor(0, 32, 242), self, "choose color")
            self.light_theme=f'rgb({color.red()},{color.green()},{color.blue()})'
            self.light_colors=f'{color.red()},{color.green()},{color.blue()}'
            self.apply_light_mode()

    def menue_btn_fun(self):
        if self.side_frame.x() == -self.side_frame.width():
            self.menue_btn.setIcon(qtg.QIcon('icons//left.png'))
            self.anim = qtc.QPropertyAnimation(self.side_frame, b"pos")
            self.anim.setEndValue(qtc.QPoint(self.top_frame.x(), self.side_frame.y()))
            self.anim.setDuration(300)

            self.anim_2 = qtc.QPropertyAnimation(self.main_widget, b'pos')
            self.anim_2.setStartValue(qtc.QPoint(11, 81))
            self.anim_2.setEndValue(qtc.QPoint(81, 81))
            self.anim_2.setDuration(300)

            self.group_animation = qtc.QParallelAnimationGroup()
            self.group_animation.addAnimation(self.anim)
            self.group_animation.addAnimation(self.anim_2)
            self.group_animation.start()


        else:
            self.menue_btn.setIcon(qtg.QIcon('icons//i.png'))
            self.anim_h = qtc.QPropertyAnimation(self.side_frame, b"pos")
            self.anim_h.setEndValue(qtc.QPoint(-(self.side_frame.width()), self.side_frame.y()))
            self.anim_h.setDuration(400)

            self.anim_2_h = qtc.QPropertyAnimation(self.main_widget, b'pos')
            self.anim_2_h.setStartValue(qtc.QPoint(81, 81))
            self.anim_2_h.setEndValue(qtc.QPoint(11, 81))
            self.anim_2_h.setDuration(400)

            self.group_animation_h = qtc.QParallelAnimationGroup()
            self.group_animation_h.addAnimation(self.anim_h)
            self.group_animation_h.addAnimation(self.anim_2_h)
            self.group_animation_h.start()

    def add_employee_btn_fun(self):
        self.main_ly.setCurrentIndex(2)
        self.new_order_ly.setCurrentIndex(4)
        self.new_order_count = 4
        self.top_frame_label.setText(self.main_pages[self.lang][self.main_ly.currentIndex()])
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.new_order_ly.currentIndex()])
        self.update_cmb()

    def add_imp_btn_fun(self):
        self.main_ly.setCurrentIndex(2)
        self.new_order_ly.setCurrentIndex(1)
        self.new_order_count = 1
        self.top_frame_label.setText(self.main_pages[self.lang][self.main_ly.currentIndex()])
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.new_order_ly.currentIndex()])
        self.update_cmb()

    def add_exp_btn_fun(self):
        self.main_ly.setCurrentIndex(2)
        self.new_order_ly.setCurrentIndex(2)
        self.new_order_count = 2
        self.top_frame_label.setText(self.main_pages[self.lang][self.main_ly.currentIndex()])
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.new_order_ly.currentIndex()])
        self.update_cmb()

    def home_btn_fun(self):
        self.main_ly.setCurrentIndex(0)
        self.top_frame_label.setText(self.main_pages[self.lang][0])

    def stock_btn_fun(self):
        self.main_ly.setCurrentIndex(1)
        self.top_frame_label.setText(self.main_pages[self.lang][1])
        self.update_cmb()

    def new_order_btn_fun(self):
        self.main_ly.setCurrentIndex(2)
        self.top_frame_label.setText(self.main_pages[self.lang][2])
        self.update_cmb()
    def database_btn_fun(self):
        if self.current_type == "manger" or self.current_type == "admin":
            self.main_ly.setCurrentIndex(3)
            self.top_frame_label.setText(self.main_pages[self.lang][3])

    def info_btn_fun(self):
        self.main_ly.setCurrentIndex(4)
        self.top_frame_label.setText(self.main_pages[self.lang][4])

    def settings_btn_fun(self):
        self.main_ly.setCurrentIndex(5)
        self.top_frame_label.setText(self.main_pages[self.lang][5])

    def employees_btn_fun(self):
        self.database_ly.setCurrentIndex(1)
        self.database_bar_label.setText(self.database_pages[self.lang][1])
        self.count = 1
        self.update_cmb()

    def calculations_btn_fun(self):
        self.database_ly.setCurrentIndex(2)
        self.database_bar_label.setText(self.database_pages[self.lang][2])
        self.count = 2
        self.update_cmb()
    def imports_btn_fun(self):
        self.database_ly.setCurrentIndex(3)
        self.database_bar_label.setText(self.database_pages[self.lang][3])
        self.count = 3
        self.update_cmb()

    def exports_btn_fun(self):
        self.database_ly.setCurrentIndex(4)
        self.database_bar_label.setText(self.database_pages[self.lang][4])
        self.count = 4
        self.update_cmb()

    def database_home_btn_fun(self):
        self.database_ly.setCurrentIndex(0)
        self.database_bar_label.setText(self.database_pages[self.lang][0])
        self.count = 0
        self.update_cmb()
        self.update_cmb()
    def back_btn_fun(self):
        if (self.count >= 1):
            self.count -= 1
        else:
            self.count = 4
        self.database_ly.setCurrentIndex(self.count)
        self.database_bar_label.setText(self.database_pages[self.lang][self.count])
        self.update_cmb()
    def forward_btn_fun(self):
        if (self.count < 4):
            self.count += 1
        else:
            self.count = 0
        self.database_ly.setCurrentIndex(self.count)
        self.database_bar_label.setText(self.database_pages[self.lang][self.count])

        self.update_cmb()

    def Buy_btn_fun(self):
        self.new_order_ly.setCurrentIndex(1)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][1])
        self.new_order_count = 1
        self.update_cmb()

    def Sell_btn_fun(self):
        self.new_order_ly.setCurrentIndex(2)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][2])
        self.new_order_count = 2

        self.update_cmb()

    def new_package_btn_fun(self):
        self.new_order_ly.setCurrentIndex(3)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][3])

        self.update_cmb()
        self.new_order_count = 3

    def new_emp_btn_fun(self):
        self.new_order_ly.setCurrentIndex(4)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][4])
        self.new_order_count = 4

    def new_order_home_btn_fun(self):

        self.update_cmb()
        self.new_order_ly.setCurrentIndex(0)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][0])
        self.new_order_count = 0

    def new_order_back_btn_fun(self):
        if (self.new_order_count >= 1):
            self.new_order_count -= 1
        else:
            self.new_order_count = 4
        self.new_order_ly.setCurrentIndex(self.new_order_count)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.new_order_count])
        self.update_cmb()
    def new_order_forward_btn_fun(self):
        if (self.new_order_count < 4):
            self.new_order_count += 1
        else:
            self.new_order_count = 0
        self.new_order_ly.setCurrentIndex(self.new_order_count)
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.new_order_count])
        self.update_cmb()
    def navigate_info_pages(self):
        if self.current_type == 'admin':
            if (self.main_info_ly.currentIndex() == 1):
                self.main_info_ly.setCurrentIndex(0)
            else:
                self.main_info_ly.setCurrentIndex(1)

    def create_new_username_btn_fun(self):
        self.main_settings_ly.setCurrentIndex(1)
        self.settings_bar_label.setText(self.settings_pages[self.lang][1])
        self.settings_count = 1

    def change_password_btn_fun(self):
        self.main_settings_ly.setCurrentIndex(2)
        self.settings_bar_label.setText(self.settings_pages[self.lang][2])
        self.settings_count = 2

    def settings_home_btn_fun(self):
        self.settings_count = 0
        self.main_settings_ly.setCurrentIndex(self.settings_count)
        self.settings_bar_label.setText(self.settings_pages[self.lang][self.main_settings_ly.currentIndex()])

    def settings_back_btn_fun(self):
        if self.settings_count > 0:
            self.settings_count -= 1

        else:
            self.settings_count = 2
        self.main_settings_ly.setCurrentIndex(self.settings_count)
        self.settings_bar_label.setText(self.settings_pages[self.lang][self.main_settings_ly.currentIndex()])

    def settings_forward_btn_fun(self):
        if self.settings_count < 2:
            self.settings_count += 1

        else:
            self.settings_count = 0
        self.main_settings_ly.setCurrentIndex(self.settings_count)
        self.settings_bar_label.setText(self.settings_pages[self.lang][self.main_settings_ly.currentIndex()])

    def set_layout(self):
        ###################loging form######################
        self.login_w = qtw.QWidget()
        self.login_h_ly = qtw.QHBoxLayout()
        self.login_form_ly = qtw.QVBoxLayout()
        self.login_label_ly = qtw.QHBoxLayout()
        self.login_label_ly.addStretch()
        self.login_label_ly.addWidget(self.login_label)
        self.login_label_ly.addStretch()
        self.login_form_ly.addLayout(self.login_label_ly)
        self.login_form_ly.addWidget(self.username_label)
        self.login_form_ly.addWidget(self.username_in)
        self.login_form_ly.addWidget(self.password_label)
        self.login_form_ly.addWidget(self.password_in)
        self.login_form_ly.addWidget(self.login_btn)
        self.login_form_ly.addWidget(self.wrong_pass)
        self.login_form_ly.addStretch()
        self.login_h_ly.addStretch()
        self.login_h_ly.addLayout(self.login_form_ly)
        self.login_h_ly.addStretch()
        self.login_w.setLayout(self.login_h_ly)
        #######################Stacked_genral_layouts########
        self.stacked_g = qtw.QStackedLayout()

        ############Top Frame################

        self.top_frame_ly = qtw.QHBoxLayout()
        self.top_frame_ly.addWidget(self.menue_btn)
        self.top_frame_ly.addStretch()
        self.top_frame_ly.addWidget(self.top_frame_label)
        self.top_frame_ly.addStretch()
        self.top_frame.setLayout(self.top_frame_ly)
        # self.top_frame.setGeometry(0, 0, self.width, 70)
        #####################Side Frame###########################

        self.side_frame_ly = qtw.QVBoxLayout()

        self.side_frame_ly.addWidget(self.home_btn)
        self.side_frame_ly.addStretch()

        self.side_frame_ly.addWidget(self.stock_btn)
        self.side_frame_ly.addStretch()

        self.side_frame_ly.addWidget(self.new_btn)
        self.side_frame_ly.addStretch()

        self.side_frame_ly.addWidget(self.data_btn)
        self.side_frame_ly.addStretch()

        self.side_frame_ly.addWidget(self.info_btn)
        self.side_frame_ly.addStretch()

        self.side_frame_ly.addWidget(self.settings_btn)
        self.side_frame_ly.addStretch()

        self.side_frame.setLayout(self.side_frame_ly)
        # self.side_frame.setGeometry(-70, 70, 70, self.height - 70)
        ############stock_ly####################

        self.stock_widget = qtw.QWidget()
        self.stock_ly = qtw.QVBoxLayout()

        self.top_ly = qtw.QHBoxLayout()
        self.top_ly.addStretch()
        self.top_ly.addWidget(self.search_box)
        self.top_ly.addWidget(self.search_btn)
        self.stock_ly.addLayout(self.top_ly)
        self.stock_ly.addWidget(self.stock_tabel)

        self.stock_widget.setLayout(self.stock_ly)

        #############database_ly###################
        self.database_widget = qtw.QWidget()
        self.database_vertical_ly = qtw.QVBoxLayout()
        self.database_main_widget = qtw.QWidget()
        self.database_main_widget.setStyleSheet(
            """QPushButton{border-radius:50px;min-width:200px;min-height:250px;border-style: outset;border-width: 1px;border-color: blue;color:white;font:bold 18px;}""")

        self.database_ly = qtw.QStackedLayout()
        self.data_base_home_ly = qtw.QVBoxLayout()

        self.top_database_ly = qtw.QHBoxLayout()
        self.bottom_database_ly = qtw.QHBoxLayout()

        self.top_database_ly.addStretch()
        self.top_database_ly.addWidget(self.employees_btn)
        self.top_database_ly.addStretch()
        self.top_database_ly.addWidget(self.calculations_btn)
        self.top_database_ly.addStretch()

        self.bottom_database_ly.addStretch()
        self.bottom_database_ly.addWidget(self.imports_btn)
        self.bottom_database_ly.addStretch()
        self.bottom_database_ly.addWidget(self.exports_btn)
        self.bottom_database_ly.addStretch()

        self.data_base_home_ly.addLayout(self.top_database_ly)
        # self.home_ly.addStretch()
        self.data_base_home_ly.addLayout(self.bottom_database_ly)

        self.database_main_widget.setLayout(self.data_base_home_ly)
        ############database bar ly ########################
        self.database_top_bar_ly = qtw.QHBoxLayout()
        self.database_top_bar_ly.addWidget(self.back_btn)
        self.database_top_bar_ly.addWidget(self.forward_btn)
        self.database_top_bar_ly.addWidget(self.database_home_btn)
        self.database_top_bar_ly.addWidget(self.sort_db_btn)
        self.database_top_bar_ly.addWidget(self.filter_db_btn)
        self.database_top_bar_ly.addWidget(self.undo_db_btn)
        self.database_top_bar_ly.addWidget(self.redo_db_btn)

        self.database_top_bar_ly.addStretch()
        self.database_top_bar_ly.addWidget(self.database_bar_label)
        self.database_top_bar_ly.addStretch()
        self.database_top_bar_ly.addWidget(self.search_box_db)
        self.database_top_bar_ly.addWidget(self.search_btn_db)

        self.database_bar.setLayout(self.database_top_bar_ly)

        #############import export csv#################
        self.import_csv_ly = qtw.QVBoxLayout()
        self.export_csv_ly = qtw.QVBoxLayout()
        self.import_csv_ly.addWidget(self.import_csv_cmb)
        self.import_csv_ly.addWidget(self.import_csv_btn)
        self.export_csv_ly.addWidget(self.export_csv_cmb)
        self.export_csv_ly.addWidget(self.export_csv_btn)
        self.import_export_ly = qtw.QHBoxLayout()
        self.import_export_ly.addLayout(self.import_csv_ly)
        self.import_export_ly.addLayout(self.export_csv_ly)

        self.database_vertical_ly.addWidget(self.database_bar)
        self.database_vertical_ly.addLayout(self.import_export_ly)
        self.database_vertical_ly.addLayout(self.database_ly)
        ################employeees_ly################
        self.emp_widget = qtw.QWidget()
        self.emp_ly = qtw.QVBoxLayout()
        self.emp_ly.addWidget(self.emp_tabel)
        self.emp_h = qtw.QHBoxLayout()
        self.emp_h.addWidget(self.add_emp)
        self.emp_h.addStretch()
        self.emp_h.addWidget(self.save_emp)
        self.emp_h.addStretch()
        self.emp_h.addWidget(self.remove_emp)
        self.emp_ly.addLayout(self.emp_h)
        self.emp_widget.setLayout(self.emp_ly)
        ##################imports_ly###############
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
        self.imp_widget.setLayout(self.imp_ly)
        #################exports_ly###############
        self.exp_widget = qtw.QWidget()
        self.exp_ly = qtw.QVBoxLayout()
        self.exp_ly.addWidget(self.exports_tabel)
        self.exp_h = qtw.QHBoxLayout()
        self.exp_h.addWidget(self.add_exp)
        self.exp_h.addStretch()
        self.exp_h.addWidget(self.save_exp)
        self.exp_h.addStretch()
        self.exp_h.addWidget(self.remove_exp)
        self.exp_ly.addLayout(self.exp_h)
        self.exp_widget.setLayout(self.exp_ly)

        ###############Calculations_ly#############

        self.calc_widget = qtw.QWidget()
        self.calc_ly = qtw.QVBoxLayout()
        self.calc_ly.addWidget(self.calc_tabel)
        # self.calc_ly.addStretch()
        self.calc_ly.addWidget(self.tot_tabel)
        self.calc_ly.addStretch()
        self.calc_widget.setLayout(self.calc_ly)

        ######stacked database layout################

        self.database_ly.addWidget(self.database_main_widget)
        self.database_ly.addWidget(self.emp_widget)
        self.database_ly.addWidget(self.calc_widget)
        self.database_ly.addWidget(self.imp_widget)
        self.database_ly.addWidget(self.exp_widget)

        self.database_ly.setCurrentIndex(0)

        self.database_widget.setLayout(self.database_vertical_ly)

        ################New order home page #############################
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
        self.new_order_h_widget.setLayout(self.new_order_v_ly)
        #################New order bar########################
        self.new_order_top_bar_ly = qtw.QHBoxLayout()
        self.new_order_top_bar_ly.addWidget(self.new_order_back_btn)
        self.new_order_top_bar_ly.addWidget(self.new_order_forward_btn)
        self.new_order_top_bar_ly.addWidget(self.new_order_home_btn)
        self.new_order_top_bar_ly.addStretch()
        self.new_order_top_bar_ly.addWidget(self.new_order_bar_label)
        self.new_order_top_bar_ly.addStretch()

        self.new_order_bar.setLayout(self.new_order_top_bar_ly)

        ##################Buy Product#############################
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

        self.package_ly_buy=qtw.QHBoxLayout()
        self.package_name_ly=qtw.QVBoxLayout()
        self.package_name_ly.addWidget(self.buy_package_name_label)
        self.package_name_ly.addWidget(self.buy_package_name)
        self.package_qt_ly=qtw.QVBoxLayout()
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
        self.submit_clear_buy_ly=qtw.QHBoxLayout()
        self.submit_clear_buy_ly.addWidget(self.buy_submit)
        self.submit_clear_buy_ly.addStretch()
        self.submit_clear_buy_ly.addWidget(self.clear_buy_page)
        self.buy_ly.addLayout(self.submit_clear_buy_ly)
        self.buy_ly.addStretch()
        self.buy_product_widget.setLayout(self.buy_ly)
        ################### Sell product###################
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
        self.s_t8=qtw.QVBoxLayout()
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

        self.submit_clear_ly=qtw.QHBoxLayout()
        self.submit_clear_ly.addWidget(self.sell_submit)
        self.submit_clear_ly.addStretch()
        self.submit_clear_ly.addWidget(self.clear_sell_page_btn)
        self.sell_Product_ly.addLayout(self.submit_clear_ly)
        self.sell_Product_ly.addStretch()
        self.sell_Product.setLayout(self.sell_Product_ly)
        ####################Create new package#####################
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
        self.new_package_widget.setLayout(self.package_ly)
        ######################Add Employee############
        self.add_emp_ly = qtw.QVBoxLayout()


        self.add_emp_ly.addWidget(self.select_employee_type_label)
        self.add_emp_ly.addWidget(self.select_employee_type)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.emp_code_input_label)
        self.add_emp_ly.addWidget(self.emp_code_input)
        self.add_emp_ly.addStretch()


        self.add_emp_ly.addWidget(self.add_emp_name_label)
        self.add_emp_ly.addWidget(self.add_emp_name)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.add_emp_salary_label)
        self.add_emp_ly.addWidget(self.add_emp_salary)
        self.add_emp_ly.addStretch()

        self.add_emp_ly.addWidget(self.add_emp_position_label)
        self.add_emp_ly.addWidget(self.add_emp_position)
        self.add_emp_ly.addStretch()


        self.add_emp_ly.addWidget(self.hire_date)
        self.add_emp_ly.addStretch()

        self.add_emp_submit_clear_ly=qtw.QHBoxLayout()

        self.add_emp_submit_clear_ly.addWidget(self.add_emp_submit)
        self.add_emp_submit_clear_ly.addStretch()
        self.add_emp_submit_clear_ly.addWidget(self.add_emp_clear_btn)
        self.add_emp_ly.addLayout(self.add_emp_submit_clear_ly)

        self.add_emp_page_widget.setLayout(self.add_emp_ly)

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

        #########info_ly#####################

        self.info_widget = qtw.QWidget()
        self.main_info_ly = qtw.QStackedLayout()

        self.info_ly = qtw.QVBoxLayout()
        self.logo_ly = qtw.QHBoxLayout()
        self.logo_ly.addStretch()
        self.logo_ly.addWidget(self.logo)
        self.logo_ly.addStretch()

        self.info_name_label_ly = qtw.QHBoxLayout()
        # self.info_name_label_ly.addStretch()
        self.info_name_label_ly.addWidget(self.info_name_label)
        self.info_name_label_ly.addWidget(self.info_name_label_2)
        self.info_name_label_ly.addStretch()

        self.info_add_label_ly = qtw.QHBoxLayout()
        # self.info_add_label_ly.addStretch()
        self.info_add_label_ly.addWidget(self.info_add_label)
        self.info_add_label_ly.addWidget(self.info_add_label_2)
        self.info_add_label_ly.addStretch()

        self.info_emp_label_ly = qtw.QHBoxLayout()
        # self.info_emp_label_ly.addStretch()
        self.info_emp_label_ly.addWidget(self.info_emp_label)
        self.info_emp_label_ly.addWidget(self.info_emp_label_2)
        self.info_emp_label_ly.addStretch()

        self.info_mobile_label_ly = qtw.QHBoxLayout()
        # self.info_mobile_label_ly.addStretch()
        self.info_mobile_label_ly.addWidget(self.info_Mobile_label)
        self.info_mobile_label_ly.addWidget(self.info_Mobile_label_2)
        self.info_mobile_label_ly.addStretch()

        self.info_website_label_ly = qtw.QHBoxLayout()
        # self.info_website_label_ly.addStretch()
        self.info_website_label_ly.addWidget(self.info_Website_label)
        self.info_website_label_ly.addWidget(self.info_Website_label_2)
        self.info_website_label_ly.addStretch()

        self.info_Rent_label_ly = qtw.QHBoxLayout()
        # self.info_Rent_label_ly.addStretch()
        self.info_Rent_label_ly.addWidget(self.info_Rent_label)
        self.info_Rent_label_ly.addWidget(self.info_Rent_label_2)
        self.info_Rent_label_ly.addStretch()

        self.info_description_label_ly = qtw.QHBoxLayout()
        # self.info_description_label_ly.addStretch()
        self.info_description_label_ly.addWidget(self.info_description_label)
        self.info_description_label_ly.addWidget(self.info_description_label_2)
        self.info_description_label_ly.addStretch()

        self.info_ly.addLayout(self.logo_ly)
        self.info_ly.addLayout(self.info_name_label_ly)
        self.info_ly.addLayout(self.info_add_label_ly)
        self.info_ly.addLayout(self.info_emp_label_ly)
        self.info_ly.addLayout(self.info_mobile_label_ly)
        self.info_ly.addLayout(self.info_website_label_ly)
        self.info_ly.addLayout(self.info_Rent_label_ly)
        self.info_ly.addLayout(self.info_description_label_ly)

        self.info_widget.setLayout(self.info_ly)
        self.scrollable_info.setWidget(self.info_widget)

        self.main_info_ly.addWidget(self.scrollable_info)

        #####################################edit_info#######################
        self.edit_info_ly = qtw.QVBoxLayout()
        self.edit_info_ly.addWidget(self.edit_company_name_label)
        self.edit_info_ly.addWidget(self.edit_company_name)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_address_label)
        self.edit_info_ly.addWidget(self.edit_company_address)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_mobiles_label)
        self.edit_info_ly.addWidget(self.edit_company_mobiles)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_website_label)
        self.edit_info_ly.addWidget(self.edit_company_website)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_rent_label)
        self.edit_info_ly.addWidget(self.edit_company_rent)
        self.edit_info_ly.addStretch()

        self.edit_info_ly.addWidget(self.edit_company_description_label)
        self.edit_info_ly.addWidget(self.edit_company_description)
        self.edit_info_ly.addStretch()
        self.edit_info_page_widget.setLayout(self.edit_info_ly)
        self.main_info_ly.addWidget(self.edit_info_page_widget)
        self.main_info_widget = qtw.QWidget()
        self.main_info_widget.setLayout(self.main_info_ly)

        ############home_ly#################
        self.home_widget = qtw.QWidget()
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
        self.home_widget.setLayout(self.home_ly)

        #######################Create account layout#####################

        self.create_acc_ly = qtw.QVBoxLayout()

        self.create_acc_ly.addWidget(self.add_username_label)
        self.create_acc_ly.addWidget(self.add_username)
        self.create_acc_ly.addWidget(self.new_password_label)
        self.create_acc_ly.addWidget(self.new_password)
        self.create_acc_ly.addWidget(self.add_confirmed_password_label)
        self.create_acc_ly.addWidget(self.add_confirmed_password)
        self.create_acc_ly.addWidget(self.account_type_label)
        self.create_acc_ly.addWidget(self.account_type)
        self.create_acc_ly.addWidget(self.account_password_type_label)
        self.create_acc_ly.addWidget(self.account_type_password)
        self.create_acc_ly.addStretch()
        self.create_btn_ly = qtw.QHBoxLayout()
        self.create_btn_ly.addStretch()
        self.create_btn_ly.addWidget(self.create_btn)
        self.create_btn_ly.addStretch()
        self.create_acc_ly.addLayout(self.create_btn_ly)
        self.create_acc_widget.setLayout(self.create_acc_ly)
        #################Home Settings_ly########
        self.Settings_ly = qtw.QVBoxLayout()
        self.top_Settings_ly = qtw.QHBoxLayout()
        self.bottom_Settings_ly = qtw.QHBoxLayout()
        self.top_Settings_ly.addStretch()
        self.top_Settings_ly.addWidget(self.change_password)
        self.top_Settings_ly.addStretch()
        self.top_Settings_ly.addWidget(self.create_new_username)
        self.top_Settings_ly.addStretch()
        self.bottom_Settings_ly.addStretch()
        self.bottom_Settings_ly.addWidget(self.laguage_settings)
        self.bottom_Settings_ly.addStretch()
        self.bottom_Settings_ly.addWidget(self.night_mode_btn)
        self.bottom_Settings_ly.addStretch()
        self.Settings_ly.addLayout(self.top_Settings_ly)
        self.Settings_ly.addLayout(self.bottom_Settings_ly)

        self.Settings_widget.setLayout(self.Settings_ly)
        ################Change Password########################
        self.change_password_ly = qtw.QVBoxLayout()
        self.change_password_ly.addWidget(self.username_change_label)
        self.change_password_ly.addWidget(self.username_change)
        self.change_password_ly.addWidget(self.old_password_label)
        self.change_password_ly.addWidget(self.old_password)
        self.change_password_ly.addWidget(self.changed_password_label)
        self.change_password_ly.addWidget(self.changed_password)
        self.change_password_ly.addWidget(self.confirmed_password_label)
        self.change_password_ly.addWidget(self.confirmed_password)
        self.submit_changed_password_ly = qtw.QHBoxLayout()
        self.submit_changed_password_ly.addStretch()
        self.submit_changed_password_ly.addWidget(self.submit_changed_password)
        self.submit_changed_password_ly.addStretch()
        self.change_password_ly.addStretch()
        self.change_password_ly.addLayout(self.submit_changed_password_ly)
        self.change_password_widget.setLayout(self.change_password_ly)

        ########################settings bar ly########################
        self.settings_top_bar_ly = qtw.QHBoxLayout()
        self.settings_top_bar_ly.addWidget(self.settings_back_btn)
        self.settings_top_bar_ly.addWidget(self.settings_forward_btn)
        self.settings_top_bar_ly.addWidget(self.settings_home_btn)
        self.settings_top_bar_ly.addWidget(self.settings_color_btn)
        self.settings_top_bar_ly.addStretch()
        self.settings_top_bar_ly.addWidget(self.settings_bar_label)
        self.settings_top_bar_ly.addStretch()
        self.settings_bar_frame.setLayout(self.settings_top_bar_ly)

        ###############main_settings_stacked####################
        self.main_settings_v_ly = qtw.QVBoxLayout()
        self.main_settings_ly = qtw.QStackedLayout()
        self.main_settings_ly.addWidget(self.Settings_widget)
        self.main_settings_ly.addWidget(self.create_acc_widget)
        self.main_settings_ly.addWidget(self.change_password_widget)
        self.main_settings_ly.setCurrentIndex(0)

        self.main_settings_v_ly.addWidget(self.settings_bar_frame)
        self.main_settings_v_ly.addLayout(self.main_settings_ly)
        self.main_settings_widget.setLayout(self.main_settings_v_ly)

        ##########stacked layout##########
        self.main_ly = qtw.QStackedLayout()
        self.main_widget = qtw.QWidget(self.genral_w)
        self.main_ly.addWidget(self.home_widget)
        self.main_ly.addWidget(self.stock_widget)
        self.main_ly.addWidget(self.new_order_widget)
        self.main_ly.addWidget(self.database_widget)
        self.main_ly.addWidget(self.main_info_widget)
        self.main_ly.addWidget(self.main_settings_widget)
        self.main_widget.setLayout(self.main_ly)
        # self.main_widget.setGeometry(0, 72, self.width, self.height - 73)
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
        self.stacked_g.addWidget(self.login_w)
        self.stacked_g.addWidget(self.genral_w)
        self.stacked_g.setCurrentIndex(0)
        self.setLayout(self.stacked_g)
        self.show()

    def bar_btn_style(self):
        return """border-radius:15px;min-width:30px;min-height:30px"""

    def cmb_style(self):
        return """QComboBox{

        color:white;
        min-height:32px;
        border-radius:10px;
        font:bold 14px;
        min-width:300px;

        }"""

    def cmb_style_light(self):
        return """QComboBox{

                color:black;
                min-height:32px;
                border-radius:10px;
                font:bold 14px;
                min-width:300px;
                border-color:""" + self.light_theme + """;
                border-width:2px;
                border-style:outset;
                }"""

    def line_edit_style(self):
        return '''
        color:white;
        min-height:2em;
        border-radius:5px;
        font:bold 14px;
        min-width:25em
        '''

    def line_edit_style_light(self):
        return '''
        color:black;
        min-height:2em;
        border-radius:5px;
        font:bold 14px;
        min-width:25em
        border-color:'''+self.light_theme+''';
        border-width:2px;
        border-style:outset;
        '''

    def button_style(self):
        s = """
        QPushButton{
            background-color:blue;
            color:white;
            border-radius:10px;
            min-width:14em;
            min-height:2em;
            font:bold 14px;
        }

        QPushButton::hover{
            background-color:rgb(50,250,250);
            color:white;
            border-radius:10px;
            min-width:14em;
            min-height:3em;
            font:bold 14px;
        }


        """
        return s

    def home_page_btn_style(self):
        return """QPushButton{border-radius:50px;min-width:200px;min-height:250px;border-style: outset;border-width: 1px;border-color: blue;}"""

    def home_page_btn_style_light(self):
        return """QPushButton{border-radius:50px;min-width:200px;background-color:white;min-height:250px;border-style: outset;border-width: 1px;border-color: blue;color:black;} 

        QPushButton::hover{border-radius:50px;min-width:200px;
        background-color:rgb(50,250,250);
        min-height:250px;
        border-style: outset;
        border-width: 1px;
        border-color: """+self.light_theme+""";
        color:black;}
        """

    def menue_btn_style(self):
        return """QPushButton{ border-radius:25px;min-width:50px;min-height:50px;}"""

    def apply_dark_mode(self, ):
        self.settings_bar_label.setStyleSheet("QLabel{color:white;font bold 15px;}")
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.change_password_widget.setStyleSheet(self.main_widgets_style())

        self.create_acc_widget.setStyleSheet(self.main_widgets_style())
        self.settings_bar_frame.setStyleSheet(
            """QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:"""+self.dark_theme+""";min-height:50px;}""")
        self.database_bar_label.setStyleSheet("QLabel{color:white;font bold 15px;}")
        self.top_frame_label.setStyleSheet("QLabel{color:white;font bold 15px;}")
        self.import_csv_cmb.setStyleSheet(self.cmb_style())
        self.export_csv_cmb.setStyleSheet(self.cmb_style())
        self.add_emp_page_widget.setStyleSheet(self.main_widgets_style())
        self.edit_info_page_widget.setStyleSheet(self.main_widgets_style())
        self.new_package_widget.setStyleSheet(self.main_widgets_style())
        self.sell_Product.setStyleSheet(self.main_widgets_style())
        self.buy_product_widget.setStyleSheet(self.main_widgets_style())
        self.employees_btn.setStyleSheet(self.home_page_btn_style())
        self.calculations_btn.setStyleSheet(self.home_page_btn_style())
        self.imports_btn.setStyleSheet(self.home_page_btn_style())
        self.exports_btn.setStyleSheet(self.home_page_btn_style())
        self.database_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.dark_theme + ";min-height:50px;}")
        self.new_order_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.dark_theme + ";min-height:50px;}")
        self.new_order_bar_label.setStyleSheet("QLabel{color:white;font bold 14px;}")
        self.username_in.setStyleSheet(self.line_edit_style())
        self.password_in.setStyleSheet(self.line_edit_style())
        # self.setStyleSheet("background-color:white;")
        self.search_btn.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")
        self.search_box.setStyleSheet(
            "color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")

        self.search_btn_db.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")
        self.search_box_db.setStyleSheet(
            "color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")
        self.top_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.dark_theme + ";min-height:70px;max-height:70px;min-width:" + str(
                self.width) + "px;}")
        self.side_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.dark_theme + ";min-width:70px;max-width:70px;min-height:" + str(
                self.height - 70) + "px;}")
        self.Settings_widget.setStyleSheet(self.home_page_btn_style())
        self.Buy_btn.setStyleSheet(self.home_page_btn_style())
        self.Sell_btn.setStyleSheet(self.home_page_btn_style())
        self.new_package_btn.setStyleSheet(self.home_page_btn_style())
        self.repaint()

    def apply_light_mode(self):
        self.settings_bar_label.setStyleSheet("QLabel{color:black;font bold 15px;}")
        self.change_password_widget.setStyleSheet(self.main_widgets_light_style())
        self.create_acc_widget.setStyleSheet(self.main_widgets_light_style())
        self.settings_bar_frame.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.light_theme + ";min-height:50px;}")
        self.Settings_widget.setStyleSheet(self.home_page_btn_style_light())
        self.database_bar_label.setStyleSheet("QLabel{color:black;font bold 15px;}")
        self.top_frame_label.setStyleSheet("QLabel{color:black;font bold 15px;}")

        self.import_csv_cmb.setStyleSheet(self.cmb_style_light())
        self.export_csv_cmb.setStyleSheet(self.cmb_style_light())

        self.add_emp_page_widget.setStyleSheet(self.main_widgets_light_style())
        self.edit_info_page_widget.setStyleSheet(self.main_widgets_light_style())
        self.new_package_widget.setStyleSheet(self.main_widgets_light_style())
        self.sell_Product.setStyleSheet(self.main_widgets_light_style())
        self.buy_product_widget.setStyleSheet(self.main_widgets_light_style())
        self.Buy_btn.setStyleSheet(self.home_page_btn_style_light())
        self.Sell_btn.setStyleSheet(self.home_page_btn_style_light())
        self.new_package_btn.setStyleSheet(self.home_page_btn_style_light())
        self.employees_btn.setStyleSheet(self.home_page_btn_style_light())
        self.calculations_btn.setStyleSheet(self.home_page_btn_style_light())
        self.imports_btn.setStyleSheet(self.home_page_btn_style_light())
        self.exports_btn.setStyleSheet(self.home_page_btn_style_light())
        self.database_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.light_theme + ";min-height:50px;}")
        self.new_order_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.light_theme + ";min-height:50px;}")
        self.new_order_bar_label.setStyleSheet("QLabel{color:black;font bold 14px;}")
        self.username_in.setStyleSheet(self.line_edit_style_light())
        self.password_in.setStyleSheet(self.line_edit_style_light())
        self.setStyleSheet("background-color:white;")
        self.search_btn.setStyleSheet(
            "QPushButton{ border-radius:25px;min-width:50px;min-height:50px;background-color:cyan;}QPushButton::hover{border-radius:25px;min-width:50px;min-height:50px;background-color:blue;}")
        self.search_box.setStyleSheet(
            "color:black;border-color:cyan;border-width:2px;border-style:outset;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")

        self.search_btn_db.setStyleSheet(
            "QPushButton{ border-radius:25px;min-width:50px;min-height:50px;background-color:cyan;}QPushButton::hover{border-radius:25px;min-width:50px;min-height:50px;background-color:blue;}")
        self.search_box_db.setStyleSheet(
            "color:black;border-color:" + self.light_theme + ";border-width:2px;border-style:outset;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")

        self.top_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.light_theme + ";min-height:70px;max-height:70px;min-width:" + str(
                self.width) + "px;}")
        self.side_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.light_theme + ";min-width:70px;max-width:70px;min-height:" + str(
                self.height - 70) + "px;}")
        self.repaint()

    def set_english(self):
        self.lang = 0
        self.clear_packages_btn.setText("clear")
        self.username_change_label.setText("Enter Username")
        self.old_password_label.setText("Enter Old Password")
        self.changed_password_label.setText("Enter New Password")
        self.confirmed_password_label.setText("Confirm New Password")
        self.submit_changed_password.setText("Submit changes")

        self.add_username_label.setText("Enter username")
        self.new_password_label.setText("Enter password")
        self.add_confirmed_password_label.setText("Confirm password")
        self.account_type_label.setText("Enter account type")
        self.account_password_type_label.setText("Enter acocunt type password")
        self.account_type.clear()
        self.account_type.addItems(["Employee", "Manger", "Admin"])
        self.create_btn.setText("Create")

        self.settings_bar_label.setText(self.settings_pages[self.lang][self.main_settings_ly.currentIndex()])

        self.add_emp_position_label.setText("Enter Employee Position")
        self.add_emp_name_label.setText("Enter Emplyee Name")
        self.add_emp_salary_label.setText("Enter Employee salary")
        self.package_name_label.setText("Package Name")
        self.add_product_to_package_label.setText("Product")
        self.package_tabel.setHorizontalHeaderLabels(["product Name", "Quantity"])

        self.add_btn.setText("Add")
        self.save_btn.setText("Save package")
        self.remove_btn.setText("remove Package")

        self.stock_tabel.setHorizontalHeaderLabels(
            ["Product", "Availble", "price per unit", "Sell price per unit", "sold"])
        self.Buy_btn.setText("Buy")
        self.Sell_btn.setText("Sell")
        self.new_package_btn.setText("New Package")
        self.supplier_name_s_label.setText("supplier Name")
        self.supplier_email_s_label.setText("supplier Email")
        self.supplier_address_s_label.setText("supplier Address")
        self.supplier_link_s_label.setText("supplier website Link")
        self.product_name_label.setText("Product name")
        self.product_quantity_label.setText("quantity")
        self.product_price_label.setText("price")
        self.product_selling_price_label.setText("selling price")
        self.add_b_prod.setText("Add Product")
        self.products_tabel.setHorizontalHeaderLabels(["Product", "Quantity", "Buy Price", "selling Price"])
        self.total_tabel_b.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.stock_product.setText("Stock Product")
        self.used_product.setText("used Product")
        self.service_product.setText("service")

        self.type_label.setText("Select Product type")
        self.dte_label.setText("Date")

        self.buy_submit.setText("Submit")
        self.client_name_label.setText("client Name")
        self.client_email_label.setText("client Email")
        self.client_address_label.setText("client Address")
        self.client_link_label.setText("client website Link")
        self.add_product_label.setText("Product Name")
        self.add_Packegas_label.setText("package Name")
        self.product_qt_label.setText("Quantity")
        self.packages_qt_label.setText("Quantity")
        self.add_service_fees_label.setText("Service Fees")
        self.add_service_type_label.setText("Service name")
        self.prod_tabel.setHorizontalHeaderLabels(["Product", "Quantity", "Buy Price", "selling Price"])
        self.total_tabel.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.sell_submit.setText("Submit")

        self.service_cost_label.setText("Service Cost")

        self.add_product_btn.setText("Add product")

        self.add_Packages_btn.setText("Add package")

        self.sell_date_label.setText("Date")
        self.password_label.setText("Enter your password")
        self.username_label.setText("Enter your username")
        self.login_btn.setText("Login")

        self.employees_btn.setText("Employees")
        self.imports_btn.setText("imports")

        self.exports_btn.setText("exports")

        self.calculations_btn.setText("calculations")
        self.import_csv_btn.setText("Import CSV")
        self.export_csv_btn.setText("Export CSV")

        l = ["Employees", "imports", "Exports", "Calculations"]
        self.import_csv_cmb.clear()
        self.export_csv_cmb.clear()
        self.import_csv_cmb.addItems(l)
        self.export_csv_cmb.addItems(l)

        self.emp_tabel.setHorizontalHeaderLabels(
            ["Code", "Name", "Position", "Salary", "Total experience", "inside experience"])
        self.add_emp.setText("Add")
        self.remove_emp.setText("remove")
        self.save_emp.setText("Save")
        self.exports_tabel.setHorizontalHeaderLabels(
            ["Client Name", "Email", "Address", "Link", "Products", "Cost", "Profit", "Losses", "Date"])
        self.add_exp.setText("Add")
        self.remove_exp.setText("remove")
        self.save_exp.setText("Save")
        self.imp_tabel.setHorizontalHeaderLabels(
            ["supplier Name", "Email", "Address", "Link", "Products", "Cost", "Losses", "Date"])
        self.add_imp.setText("Add")
        self.remove_imp.setText("remove")

        self.save_imp.setText("Save")
        self.calc_tabel.setHorizontalHeaderLabels(["Name", "type", "Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"])

        self.tot_tabel.setHorizontalHeaderLabels(["Period", "Spent", "Earned", "Profit"])
        self.tot_tabel.setItem(0, 0, qtw.QTableWidgetItem("Quarter 1"))
        self.tot_tabel.setItem(1, 0, qtw.QTableWidgetItem("Quarter 2"))
        self.tot_tabel.setItem(2, 0, qtw.QTableWidgetItem("Quarter 3"))
        self.tot_tabel.setItem(3, 0, qtw.QTableWidgetItem("Quarter 4"))
        self.tot_tabel.setItem(4, 0, qtw.QTableWidgetItem("Annual"))
        self.address = "Smouha Sidi Gaber Alexandria, Egypt."
        self.description = "ESSC provides environmental and safety consulting services, too general supplies and contracting;\nwe offer these services to our clients not only for pollution control and protection place,\n but also for resource preservation.\n through cleaner production and adequate mitigation measures in design, operation,and proper management manners.      "

        self.info_add_label_2.setText(self.address)
        self.info_description_label_2.setText(self.description)
        self.info_name_label_2.setText(self.company_name)
        self.info_Mobile_label.setText(self.mobile)
        self.info_Website_label_2.setText(self.website)
        self.info_emp_label_2.setText(self.n_employees)
        self.info_Rent_label_2.setText(self.rent)

        self.info_name_label.setText("Name: ")

        self.info_add_label.setText("Company Address: ")

        self.info_emp_label.setText("Number of employees: ")

        self.info_Mobile_label.setText("Mobile numbers: ")

        self.info_Website_label.setText("Website: ")

        self.info_Rent_label.setText("Rent: ")

        self.info_description_label.setText("Description: ")

        self.info_add_label_2.setText("Company Address: ")
        self.edit_company_name_label.setText("Enter new company Name")
        self.edit_company_address_label.setText("Enter new company Address")
        self.edit_company_website_label.setText("Enter new company Website")
        self.edit_company_mobiles_label.setText("Enter new Mobile numbers")
        self.edit_company_rent_label = qtw.QLabel("Enter company new Rent")
        self.edit_company_description_label.setText("Enter new Description")
        self.change_password.setText("change username password")
        self.create_new_username.setText("Create new account")
        self.laguage_settings.setText("Set to Arabic")
        self.night_mode_btn.setText("Light/dark Mode")
        self.info_name_label_ly.setDirection(0)  # left tor right alligment
        self.info_add_label_ly.setDirection(0)
        self.info_emp_label_ly.setDirection(0)
        self.info_mobile_label_ly.setDirection(0)
        self.info_website_label_ly.setDirection(0)
        self.info_Rent_label_ly.setDirection(0)
        self.info_description_label_ly.setDirection(0)
        self.username_change_label.setAlignment(qtc.Qt.AlignLeft)
        self.old_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.confirmed_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.changed_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_username_label.setAlignment(qtc.Qt.AlignLeft)
        self.new_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.account_type_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_confirmed_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.account_password_type_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_emp_position_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_emp_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_emp_salary_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_emp_exp_label.setAlignment(qtc.Qt.AlignLeft)
        self.package_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_product_to_package_label.setAlignment(qtc.Qt.AlignLeft)
        self.supplier_name_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.supplier_email_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.supplier_address_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.supplier_link_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.product_quantity_label.setAlignment(qtc.Qt.AlignLeft)
        self.product_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.product_selling_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.type_label.setAlignment(qtc.Qt.AlignLeft)
        self.dte_label.setAlignment(qtc.Qt.AlignLeft)
        self.client_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.client_email_label.setAlignment(qtc.Qt.AlignLeft)
        self.client_address_label.setAlignment(qtc.Qt.AlignLeft)
        self.client_link_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_product_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_Packegas_label.setAlignment(qtc.Qt.AlignLeft)
        self.product_qt_label.setAlignment(qtc.Qt.AlignLeft)
        self.packages_qt_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_service_fees_label.setAlignment(qtc.Qt.AlignLeft)
        self.add_service_type_label.setAlignment(qtc.Qt.AlignLeft)
        self.product_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.product_selling_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.service_cost_label.setAlignment(qtc.Qt.AlignLeft)
        self.sell_date_label.setAlignment(qtc.Qt.AlignLeft)
        self.password_label.setAlignment(qtc.Qt.AlignLeft)
        self.username_label.setAlignment(qtc.Qt.AlignLeft)
        self.top_frame_label.setAlignment(qtc.Qt.AlignLeft)

        self.settings_bar_label.setAlignment(qtc.Qt.AlignLeft)

        self.database_bar_label.setText(self.database_pages[self.lang][self.new_order_ly.currentIndex()])
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.database_ly.currentIndex()])
        self.top_frame_label.setText(self.main_pages[self.lang][self.main_ly.currentIndex()])

    def set_arabic(self):
        self.lang = 1
        self.clear_packages_btn.setText("مسح")
        self.username_change_label.setText("ادخل اسم المستخدم")
        self.old_password_label.setText("ادخل كلمةالمرور القديمة")

        self.changed_password_label.setText("ادخل كلمةالمرور الجديدة")
        self.confirmed_password_label.setText("تاكيد كلمةالمرور")
        self.submit_changed_password.setText("توثيق التغيرات")

        self.add_username_label.setText("ادخل اسم المستخدم")
        self.new_password_label.setText("ادخل كلمة المرور")
        self.add_confirmed_password_label.setText("تاكيد كلمةالمرور")
        self.account_type_label.setText("ادخل نوع الحساب")
        self.account_password_type_label.setText("ادخل كلمة مرور نوع الحساب")
        self.account_type.clear()
        self.account_type.addItems(["موظف", "مدير", "مشرف"])
        self.create_btn.setText("انشاء حساب جديد")

        self.settings_bar_label.setText(self.settings_pages[self.lang][self.main_settings_ly.currentIndex()])

        self.add_emp_position_label.setText("ادخل منصب الموظف")
        self.add_emp_name_label.setText("ادخل اسم الموظف")
        self.add_emp_salary_label.setText("ادخل راتب الموظف")
        self.add_emp_exp_label.setText("ادخل عدد سنين خبرة الموظف")

        self.edit_company_rent_label.setText("ادخل ايجار الشركة")
        self.package_name_label.setText("اسم المجموعة")
        self.add_product_to_package_label.setText("المنتج")
        self.package_tabel.setHorizontalHeaderLabels(["اسم المنتج", "الكمية"])
        self.add_btn.setText("اضف")
        self.save_btn.setText("حفظ المجموعة")
        self.remove_btn.setText("ازالة المجموعة")
        self.stock_tabel.setHorizontalHeaderLabels(
            ["المنتج", "المتاح", "سعر الوحدة", "سعر بيع الوحدة", "الكمية المباعة"])

        self.Buy_btn.setText("شراء")
        self.Sell_btn.setText("بيع")

        self.new_package_btn.setText("مجموعة جديدة")
        self.supplier_name_s_label.setText("اسم المورد")
        self.supplier_email_s_label.setText("بريد المورد")
        self.supplier_address_s_label.setText("عنوان المورد")
        self.supplier_link_s_label.setText("رابط موقع المورد")
        self.product_name_label.setText("اسم المنتج")
        self.product_quantity_label.setText("الكمية")
        self.product_price_label.setText("السعر")
        self.product_selling_price_label.setText("سعر البيع")

        self.add_b_prod.setText("اضف المنتج")
        self.products_tabel.setHorizontalHeaderLabels(["المنتج", "الكمية", "سعر الشراء", "سعر البيع"])
        self.total_tabel_b.setHorizontalHeaderLabels(["التكلفة", "العائد", "المكسب"])
        self.stock_product.setText("منتج مخازن")
        self.used_product.setText("منتج استعمال")
        self.service_product.setText("خدمة")
        self.type_label.setText("اختيار نوع المنتج")
        self.dte_label.setText("التاريخ")
        self.buy_submit.setText("توثيق العملية")
        self.client_name_label.setText("اسم العميل")
        self.client_email_label.setText("بريد العميل")
        self.client_address_label.setText("عنوان العميل")
        self.client_link_label.setText("رابط موقع العميل")
        self.add_product_label.setText("اسم المنتج")
        self.add_Packegas_label.setText("اسم المجموعة")
        self.product_qt_label.setText("الكمية")
        self.packages_qt_label.setText("الكمية")
        self.add_service_fees_label.setText("ثمن الخمة")
        self.add_service_type_label.setText("اسم الخدمة")
        self.prod_tabel.setHorizontalHeaderLabels(["المنتج", "الكمية", "سعر الشراء", "سعر البيع"])
        self.total_tabel.setHorizontalHeaderLabels(["التكلفة", "العائد", "الربح"])
        self.sell_submit.setText("توثيق العملية")
        self.service_cost_label.setText("تكلفة الخدمة")
        self.add_product_btn.setText("اضف منتج")
        self.add_Packages_btn.setText("اضف مجموعة")
        self.sell_date_label.setText("التاريخ")
        self.password_label.setText("ادخل كلمة السر")
        self.username_label.setText("ادخل اسم المستخدم")
        self.login_btn.setText("تسجيل الدخول")

        self.database_bar_label.setText(self.database_pages[self.lang][self.new_order_ly.currentIndex()])
        self.new_order_bar_label.setText(self.new_order_pages[self.lang][self.database_ly.currentIndex()])
        self.top_frame_label.setText(self.main_pages[self.lang][self.main_ly.currentIndex()])

        self.employees_btn.setText("الموظفين")
        self.imports_btn.setText("الواردات")

        self.exports_btn.setText("الصادرات")

        self.calculations_btn.setText("الحسابات")
        self.import_csv_btn.setText("ادخل ملف اكسل")
        self.export_csv_btn.setText("حفظ كملف اكسل")

        l = ["الموظفين", "الواردات", "الصادرات", "الحسابات"]
        self.import_csv_cmb.clear()
        self.export_csv_cmb.clear()
        self.import_csv_cmb.addItems(l)
        self.export_csv_cmb.addItems(l)

        self.emp_tabel.setHorizontalHeaderLabels(
            ["كود الموظف", "اسم الموظف", "منصبه", "المرتب", "خبرة الموظف", "خبرة الموظف في الشركة"])
        self.add_emp.setText("اضف")
        self.remove_emp.setText("ازالة")
        self.save_emp.setText("حفظ")
        self.exports_tabel.setHorizontalHeaderLabels(
            ["اسم العميل", "البريد", "العنوان", "الرابط", "المنتجات", "التكلفة", "الربح", "الخسارة", "التاريخ"])
        self.add_exp.setText("اضف")
        self.remove_exp.setText("ازالة")
        self.save_exp.setText("حفظ")
        self.imp_tabel.setHorizontalHeaderLabels(
            ["اسم المورد", "البريد", "العنوان", "الرابط", "المنتجات", "التكلفة", "الخسارة", "التاريخ"])
        self.add_imp.setText("اضف")
        self.remove_imp.setText("ازالة")

        self.save_imp.setText("حفظ")
        self.calc_tabel.setHorizontalHeaderLabels(
            ["الاسم", "نوع العملية", "الربع الأول", "الربع الثاني", "الربع الثالث", "االربع الرابع"])

        self.tot_tabel.setHorizontalHeaderLabels(["الفترة الزمنية", "المصروفات", "العائد", "الربح"])
        self.tot_tabel.setItem(0, 0, qtw.QTableWidgetItem("الربع الأول"))
        self.tot_tabel.setItem(1, 0, qtw.QTableWidgetItem("الربع الثاني"))
        self.tot_tabel.setItem(2, 0, qtw.QTableWidgetItem("الربع الثالث"))
        self.tot_tabel.setItem(3, 0, qtw.QTableWidgetItem("االربع الرابع"))
        self.tot_tabel.setItem(4, 0, qtw.QTableWidgetItem("السنوي"))
        self.address = ".سموحة سيدى جابر الإسكندرية ، مصر"
        self.description = "تقدم الشركة خدمات استشارية تتعلق بالبيئة والسلامة ، بالإضافة إلى التوريدات والتعاقدات العامة ؛ نحن نقدم هذه الخدمات لعملائنا ليس فقط من أجل مكافحة التلوث وحمايته ، ولكن أيضًا للحفاظ على الموارد من خلال الإنتاج الأنظف وتدابير التخفيف المناسبة في التصميم والتشغيل السليم و آداب الإدارة."

        self.info_add_label_2.setText(self.address)
        self.info_description_label_2.setText(self.description)
        self.info_name_label_2.setText(self.company_name)
        self.info_Mobile_label.setText(self.mobile)
        self.info_Website_label_2.setText(self.website)
        self.info_emp_label_2.setText(self.n_employees)
        self.info_Rent_label_2.setText(self.rent)
        self.info_name_label.setText("الاسم: ")

        self.info_add_label.setText("عنوان الشركة: ")

        self.info_emp_label.setText("عدد الموظفين: ")

        self.info_Mobile_label.setText("الهاتف: ")

        self.info_Website_label.setText("رابط الموقع: ")

        self.info_Rent_label.setText("الايجار: ")

        self.info_description_label.setText("الوصف: ")

        self.info_add_label_2.setText("عنوان الشركة: ")
        self.edit_company_name_label.setText("ادخل اسم الشركة")
        self.edit_company_address_label.setText("ادخل عنوان الشركة")
        self.edit_company_website_label.setText("ادخل رابط موفع الشركة")
        self.edit_company_mobiles_label.setText("أدخل أرقام موبايل جديدة")
        self.edit_company_rent_label = qtw.QLabel("أدخل الاجار")
        self.edit_company_description_label.setText("ادخل الوصف الجديد")
        self.change_password.setText("تغيير كلمة مرور اسم المستخدم")
        self.create_new_username.setText("انشاء حساب جديد")
        self.laguage_settings.setText("ُEnglish")
        self.night_mode_btn.setText("الوضع الداكن-الضوء")

        self.info_name_label_ly.setDirection(1)  # right to left alligment
        self.info_add_label_ly.setDirection(1)
        self.info_emp_label_ly.setDirection(1)
        self.info_mobile_label_ly.setDirection(1)
        self.info_website_label_ly.setDirection(1)
        self.info_Rent_label_ly.setDirection(1)
        self.info_description_label_ly.setDirection(1)
        self.top_frame_label.setAlignment(qtc.Qt.AlignRight)
        self.username_change_label.setAlignment(qtc.Qt.AlignRight)
        self.old_password_label.setAlignment(qtc.Qt.AlignRight)
        self.confirmed_password_label.setAlignment(qtc.Qt.AlignRight)
        self.changed_password_label.setAlignment(qtc.Qt.AlignRight)
        self.add_username_label.setAlignment(qtc.Qt.AlignRight)
        self.new_password_label.setAlignment(qtc.Qt.AlignRight)
        self.account_type_label.setAlignment(qtc.Qt.AlignRight)
        self.add_confirmed_password_label.setAlignment(qtc.Qt.AlignRight)
        self.account_password_type_label.setAlignment(qtc.Qt.AlignRight)
        self.add_emp_position_label.setAlignment(qtc.Qt.AlignRight)
        self.add_emp_name_label.setAlignment(qtc.Qt.AlignRight)
        self.add_emp_salary_label.setAlignment(qtc.Qt.AlignRight)
        self.add_emp_exp_label.setAlignment(qtc.Qt.AlignRight)
        self.package_name_label.setAlignment(qtc.Qt.AlignRight)
        self.add_product_to_package_label.setAlignment(qtc.Qt.AlignRight)
        self.supplier_name_s_label.setAlignment(qtc.Qt.AlignRight)
        self.supplier_email_s_label.setAlignment(qtc.Qt.AlignRight)
        self.supplier_address_s_label.setAlignment(qtc.Qt.AlignRight)
        self.supplier_link_s_label.setAlignment(qtc.Qt.AlignRight)
        self.product_quantity_label.setAlignment(qtc.Qt.AlignRight)
        self.product_price_label.setAlignment(qtc.Qt.AlignRight)
        self.product_selling_price_label.setAlignment(qtc.Qt.AlignRight)
        self.type_label.setAlignment(qtc.Qt.AlignRight)
        self.dte_label.setAlignment(qtc.Qt.AlignRight)
        self.client_name_label.setAlignment(qtc.Qt.AlignRight)
        self.client_email_label.setAlignment(qtc.Qt.AlignRight)
        self.client_address_label.setAlignment(qtc.Qt.AlignRight)
        self.client_link_label.setAlignment(qtc.Qt.AlignRight)
        self.add_product_label.setAlignment(qtc.Qt.AlignRight)
        self.add_Packegas_label.setAlignment(qtc.Qt.AlignRight)
        self.product_qt_label.setAlignment(qtc.Qt.AlignRight)
        self.packages_qt_label.setAlignment(qtc.Qt.AlignRight)
        self.add_service_fees_label.setAlignment(qtc.Qt.AlignRight)
        self.add_service_type_label.setAlignment(qtc.Qt.AlignRight)
        self.product_price_label.setAlignment(qtc.Qt.AlignRight)
        self.product_selling_price_label.setAlignment(qtc.Qt.AlignRight)
        self.service_cost_label.setAlignment(qtc.Qt.AlignRight)
        self.sell_date_label.setAlignment(qtc.Qt.AlignRight)
        self.password_label.setAlignment(qtc.Qt.AlignRight)
        self.username_label.setAlignment(qtc.Qt.AlignRight)
        self.settings_bar_label.setAlignment(qtc.Qt.AlignRight)

    def main_widgets_light_style(self):

        return """
                            QDateEdit{
                            min-height:32px;
                            min-width:100px;
                            max-width:100px;
                            }
                            QRadioButton::indicator{
                            width: 30px;
                            height: 30px;
                            border-radius: 15px;
                            border-width:1px;
                            border-style:outset;
                            border-color:black;
                            margin-left: 2px;

                            }
                            QRadioButton::indicator:checked {
                            background-color:""" + self.light_theme + """;
                            }
                            QRadioButton{
                             font:bold 14px;
                             color:black;
                             }
                            QLineEdit{
                            color:black;
                            border-color:""" + self.light_theme + """;
                            border-width:2px;
                            border-style:outset;
                            min-height:32px;
                            min-width:700px;
                            max-height:32px;
                            max-width:700px;
                            border-radius:10px;
                            font:bold 14px;
                            }
                            QLabel{
                            color:black;
                            font:bold 14px;}
                            QSpinBox{
                            min-height:32px;
                            min-width:35px;
                            max-height:32px;
                            max-width:35px;

                            }
                            QComboBox{
                            border-color:""" + self.light_theme + """;
                            border-width:2px;
                            border-style:outset;
                            color:black;
                            border-radius:10px;
                            font:bold 14px;
                            min-height:32px;
                            min-width:700px;
                            max-height:32px;
                            max-width:700px;
                            }
                             QPushButton{
                                background-color:blue;
                                color:white;
                                border-radius:10px;
                                min-width:14em;
                                min-height:2em;
                                font:bold 14px;
                            }

                            QPushButton::hover{
                                background-color:rgb(50,250,250);
                                color:white;
                                border-radius:10px;
                                min-width:14em;
                                min-height:3em;
                                font:bold 14px;
                            }
                            """

    def main_widgets_style(self):
        return """
        QDateEdit{
        min-height:32px;
        min-width:100px;
        max-width:100px;
        }
        QRadioButton::indicator{
        width: 30px;
        height: 30px;
        border-radius: 15px;
        }
        QRadioButton{
         font:bold 14px;
         }
        QLineEdit{color:white;
        min-height:32px;
        min-width:700px;
        max-height:32px;
        max-width:700px;
        border-radius:10px;
        font:bold 14px;
        }
        QLabel{
        color:white;
        font:bold 14px;
        }
        QSpinBox{
        min-height:32px;
        min-width:35px;
        max-height:32px;
        max-width:35px;

        }
        QComboBox{
        color:white;
        border-radius:10px;
        font:bold 14px;
        min-height:32px;
        min-width:700px;
        max-height:32px;
        max-width:700px;
        }
         QPushButton{
            background-color:blue;
            color:white;
            border-radius:10px;
            min-width:14em;
            min-height:2em;
            font:bold 14px;
        }

        QPushButton::hover{
            background-color:rgb(50,250,250);
            color:white;
            border-radius:10px;
            min-width:14em;
            min-height:3em;
            font:bold 14px;
        }
        """


if __name__ == "__main__":
    app = qtw.QApplication([])
    screen = app.primaryScreen()
    mw = MainWindow()
    app.exec_()