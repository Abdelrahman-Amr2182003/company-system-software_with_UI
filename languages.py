
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import qdarkstyle

class langs:
    def __init__(self,main_widget):
        self.main_widget=main_widget
    def set_english(self):
        self.main_widget.lang = 0

        self.main_widget.new_package_widget.clear_packages_btn.setText("clear")
        self.main_widget.main_settings_widget.change_password_widget.username_change_label.setText("Enter Username")
        self.main_widget.main_settings_widget.change_password_widget.old_password_label.setText("Enter Old Password")
        self.main_widget.main_settings_widget.change_password_widget.changed_password_label.setText("Enter New Password")
        self.main_widget.main_settings_widget.change_password_widget.confirmed_password_label.setText("Confirm New Password")
        self.main_widget.main_settings_widget.change_password_widget.submit_changed_password.setText("Submit changes")

        self.main_widget.main_settings_widget.create_acc_widget.add_username_label.setText("Enter username")
        self.main_widget.main_settings_widget.create_acc_widget.new_password_label.setText("Enter password")
        self.main_widget.main_settings_widget.create_acc_widget.add_confirmed_password_label.setText("Confirm password")
        self.main_widget.main_settings_widget.create_acc_widget.account_password_type_label.setText("Enter acocunt type password")
        self.main_widget.main_settings_widget.create_acc_widget.create_btn.setText("Create")

        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setText(self.main_widget.main_settings_widget.settings_bar_frame.settings_pages[self.main_widget.lang][self.main_widget.main_settings_widget.main_settings_ly.currentIndex()])

        self.main_widget.add_emp_page_widget.add_emp_position_label.setText("Enter Employee Position")
        self.main_widget.add_emp_page_widget.add_emp_name_label.setText("Enter Emplyee Name")
        self.main_widget.add_emp_page_widget.add_emp_salary_label.setText("Enter Employee salary")
        self.main_widget.add_emp_page_widget.select_employee_type_label.setText("Enter employment type")
        self.main_widget.add_emp_page_widget.emp_code_input_label.setText("Enter employee code")
        self.main_widget.add_emp_page_widget.add_emp_submit.setText("Submit")
        self.main_widget.add_emp_page_widget.add_emp_clear_btn.setText("clear")

        self.main_widget.new_package_widget.package_name_label.setText("Package Name")
        self.main_widget.new_package_widget.add_product_to_package_label.setText("Product")
        self.main_widget.new_package_widget.package_tabel.setHorizontalHeaderLabels(["product Name", "Quantity"])

        self.main_widget.new_package_widget.add_btn.setText("Add")
        self.main_widget.new_package_widget.save_btn.setText("Save package")
        self.main_widget.new_package_widget.remove_btn.setText("remove Package")

        self.main_widget.stock_widget.stock_tabel.setHorizontalHeaderLabels(
            ["Product", "Availble", "price per unit", "Sell price per unit", "sold"])
        self.main_widget.new_order_h_widget.Buy_btn.setText("Buy")
        self.main_widget.new_order_h_widget.Sell_btn.setText("Sell")
        self.main_widget.new_order_h_widget.new_package_btn.setText("New Package")

        self.main_widget.buy_product_widget.supplier_name_s_label.setText("supplier Name")
        self.main_widget.buy_product_widget.supplier_email_s_label.setText("supplier Email")
        self.main_widget.buy_product_widget.supplier_address_s_label.setText("supplier Address")
        self.main_widget.buy_product_widget.supplier_link_s_label.setText("supplier website Link")
        self.main_widget.buy_product_widget.product_name_label.setText("Product name")
        self.main_widget.buy_product_widget.product_quantity_label.setText("quantity")
        self.main_widget.buy_product_widget.product_price_label.setText("price")
        self.main_widget.buy_product_widget.product_selling_price_label.setText("selling price")
        self.main_widget.buy_product_widget.add_b_prod.setText("Add Product")
        self.main_widget.buy_product_widget.products_tabel.setHorizontalHeaderLabels(["Product", "Quantity", "Buy Price", "selling Price"])
        self.main_widget.buy_product_widget.total_tabel_b.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.main_widget.buy_product_widget.stock_product.setText("Stock Product")
        self.main_widget.buy_product_widget.used_product.setText("used Product")
        self.main_widget.buy_product_widget.service_product.setText("service")
        self.main_widget.buy_product_widget.type_label.setText("Select Product type")
        self.main_widget.buy_product_widget.dte_label.setText("Date")
        self.main_widget.buy_product_widget.buy_submit.setText("Submit")
        self.main_widget.buy_product_widget.clear_buy_page.setText("clear")
        self.main_widget.buy_product_widget.add_buy_package_btn.setText("Add package")
        self.main_widget.buy_product_widget.buy_package_name_label.setText("package name")
        self.main_widget.buy_product_widget.buy_package_quantity_label.setText("quantity")



        self.main_widget.sell_Product.client_name_label.setText("client Name")
        self.main_widget.sell_Product.client_email_label.setText("client Email")
        self.main_widget.sell_Product.client_address_label.setText("client Address")
        self.main_widget.sell_Product.client_link_label.setText("client website Link")
        self.main_widget.sell_Product.add_product_label.setText("Product Name")
        self.main_widget.sell_Product.add_Packegas_label.setText("package Name")
        self.main_widget.sell_Product.product_qt_label.setText("Quantity")
        self.main_widget.sell_Product.packages_qt_label.setText("Quantity")
        self.main_widget.sell_Product.add_service_fees_label.setText("Service Fees")
        self.main_widget.sell_Product.add_service_type_label.setText("Service name")
        self.main_widget.sell_Product.prod_tabel.setHorizontalHeaderLabels(
            ["Product", "Quantity", "Buy Price", "selling Price"])
        self.main_widget.sell_Product.total_tabel.setHorizontalHeaderLabels(["Cost", "Accuired", "Profit"])
        self.main_widget.sell_Product.sell_submit.setText("Submit")

        self.main_widget.sell_Product.service_qt_label.setText("quantity")
        self.main_widget.sell_Product.add_service_btn.setText("Add service")

        self.main_widget.sell_Product.service_cost_label.setText("Service Cost")

        self.main_widget.sell_Product.add_product_btn.setText("Add product")

        self.main_widget.sell_Product.add_Packages_btn.setText("Add package")

        self.main_widget.sell_Product.sell_date_label.setText("Date")
        self.main_widget.sell_Product.clear_sell_page_btn.setText("clear")



        self.main_widget.login_widget.password_label.setText("Enter your password")
        self.main_widget.login_widget.username_label.setText("Enter your username")
        self.main_widget.login_widget.login_btn.setText("Login")


        self.main_widget.database_widget.database_main_widget.employees_btn.setText("Employees")
        self.main_widget.database_widget.database_main_widget.imports_btn.setText("imports")
        self.main_widget.database_widget.database_main_widget.exports_btn.setText("exports")
        self.main_widget.database_widget.database_main_widget.calculations_btn.setText("calculations")


        self.main_widget.database_widget.import_export_widget.import_csv_btn.setText("Import CSV")
        self.main_widget.database_widget.import_export_widget.export_csv_btn.setText("Export CSV")

        l = ["Employees", "imports", "Exports", "Calculations"]
        self.main_widget.database_widget.import_export_widget.import_csv_cmb.clear()
        self.main_widget.database_widget.import_export_widget.export_csv_cmb.clear()
        self.main_widget.database_widget.import_export_widget.import_csv_cmb.addItems(l[:-1])
        self.main_widget.database_widget.import_export_widget.export_csv_cmb.addItems(l)

        self.main_widget.database_widget.emp_widget.emp_tabel.setHorizontalHeaderLabels(
            ["Code", "Name", "Position", "Salary","hiring date"])
        self.main_widget.database_widget.emp_widget.add_emp.setText("Add")
        self.main_widget.database_widget.emp_widget.remove_emp.setText("remove")
        self.main_widget.database_widget.emp_widget.save_emp.setText("Save")


        self.main_widget.database_widget.exp_widget.exports_tabel.setHorizontalHeaderLabels(
            ["Client Name", "Email", "Address", "Link", "Products", "Cost", "Profit", "Losses", "Date"])
        self.main_widget.database_widget.exp_widget.add_exp.setText("Add")
        self.main_widget.database_widget.exp_widget.remove_exp.setText("remove")
        self.main_widget.database_widget.exp_widget.save_exp.setText("Save")


        self.main_widget.database_widget.imp_widget.imp_tabel.setHorizontalHeaderLabels(
            ["supplier Name", "Email", "Address", "Link", "Products","process type", "Cost","total", "Losses", "Date"])
        self.main_widget.database_widget.imp_widget.add_imp.setText("Add")
        self.main_widget.database_widget.imp_widget.remove_imp.setText("remove")

        self.main_widget.database_widget.imp_widget.save_imp.setText("Save")



        self.main_widget.database_widget.calc_widget.calc_tabel.setHorizontalHeaderLabels(["Name", "type", "Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"])

        self.main_widget.database_widget.calc_widget.tot_tabel.setHorizontalHeaderLabels(["Period", "Spent", "Earned", "Profit"])
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(0, 0, qtw.QTableWidgetItem("Quarter 1"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(1, 0, qtw.QTableWidgetItem("Quarter 2"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(2, 0, qtw.QTableWidgetItem("Quarter 3"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(3, 0, qtw.QTableWidgetItem("Quarter 4"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(4, 0, qtw.QTableWidgetItem("Annual"))





        self.main_widget.main_info_widget.scrollable_info.info_name_label.setText("Name: ")

        self.main_widget.main_info_widget.scrollable_info.info_add_label.setText("Company Address: ")

        self.main_widget.main_info_widget.scrollable_info.info_emp_label.setText("Number of employees: ")

        self.main_widget.main_info_widget.scrollable_info.info_Mobile_label.setText("Mobile numbers: ")

        self.main_widget.main_info_widget.scrollable_info.info_Website_label.setText("Website: ")

        self.main_widget.main_info_widget.scrollable_info.info_Rent_label.setText("Rent: ")

        self.main_widget.main_info_widget.scrollable_info.info_description_label.setText("Description: ")




        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_name_label.setText("Enter new company Name")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_address_label.setText("Enter new company Address")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_website_label.setText("Enter new company Website")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_mobiles_label.setText("Enter new Mobile numbers")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_rent_label = qtw.QLabel("Enter company new Rent")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_description_label.setText("Enter new Description")
        self.main_widget.main_info_widget.edit_info_page_widget.submit_new_info.setText("Submit")



        self.main_widget.main_settings_widget.Settings_widget.change_password.setText("change username password")
        self.main_widget.main_settings_widget.Settings_widget.create_new_username.setText("Create new account")
        self.main_widget.main_settings_widget.Settings_widget.laguage_settings.setText("Set to Arabic")
        self.main_widget.main_settings_widget.Settings_widget.night_mode_btn.setText("Light/dark Mode")



        self.main_widget.main_info_widget.scrollable_info.info_name_label_ly.setDirection(0)  # left tor right alligment
        self.main_widget.main_info_widget.scrollable_info.info_add_label_ly.setDirection(0)
        self.main_widget.main_info_widget.scrollable_info.info_emp_label_ly.setDirection(0)
        self.main_widget.main_info_widget.scrollable_info.info_mobile_label_ly.setDirection(0)
        self.main_widget.main_info_widget.scrollable_info.info_website_label_ly.setDirection(0)
        self.main_widget.main_info_widget.scrollable_info.info_Rent_label_ly.setDirection(0)
        self.main_widget.main_info_widget.scrollable_info.info_description_label_ly.setDirection(0)



        self.main_widget.main_settings_widget.change_password_widget.username_change_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_settings_widget.change_password_widget.old_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_settings_widget.change_password_widget.confirmed_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_settings_widget.change_password_widget.changed_password_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.main_settings_widget.create_acc_widget.add_username_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_settings_widget.create_acc_widget.new_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_settings_widget.create_acc_widget.add_confirmed_password_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_settings_widget.create_acc_widget.account_password_type_label.setAlignment(qtc.Qt.AlignLeft)



        self.main_widget.add_emp_page_widget.add_emp_position_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.add_emp_page_widget.add_emp_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.add_emp_page_widget.add_emp_salary_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.add_emp_page_widget.select_employee_type_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.add_emp_page_widget.emp_code_input_label.setAlignment(qtc.Qt.AlignLeft)


        self.main_widget.new_package_widget.package_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.new_package_widget.add_product_to_package_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.buy_product_widget.supplier_name_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.supplier_email_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.supplier_address_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.supplier_link_s_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.product_quantity_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.product_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.product_selling_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.type_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.dte_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.sell_Product.client_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.client_email_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.client_address_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.client_link_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.add_product_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.add_Packegas_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.product_qt_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.packages_qt_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.add_service_fees_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.add_service_type_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.product_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.product_selling_price_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.buy_package_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.buy_product_widget.buy_package_quantity_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.sell_Product.service_cost_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.sell_Product.sell_date_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.sell_Product.service_qt_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.login_widget.password_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.login_widget.username_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.top_frame.top_frame_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setAlignment(qtc.Qt.AlignLeft)

        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_name_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_address_label.setAlignment(
            qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_website_label.setAlignment(
            qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_mobiles_label.setAlignment(
            qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_description_label.setAlignment(
            qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_rent_label.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_name.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_address.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_website.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_mobiles.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_description.setAlignment(qtc.Qt.AlignLeft)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_rent.setAlignment(qtc.Qt.AlignLeft)


        self.main_widget.database_widget.database_bar.database_bar_label.setText(self.main_widget.database_widget.database_bar.database_pages[self.main_widget.lang][self.main_widget.database_widget.database_ly.currentIndex()])
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][self.main_widget.new_order_ly.currentIndex()])
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][self.main_widget.main_ly.currentIndex()])

    def set_arabic(self):
        self.main_widget.lang = 1
        self.main_widget.new_package_widget.clear_packages_btn.setText("??????")
        self.main_widget.main_settings_widget.change_password_widget.username_change_label.setText("???????? ?????? ????????????????")
        self.main_widget.main_settings_widget.change_password_widget.old_password_label.setText("???????? ???????????????????? ??????????????")

        self.main_widget.main_settings_widget.change_password_widget.changed_password_label.setText("???????? ???????????????????? ??????????????")
        self.main_widget.main_settings_widget.change_password_widget.confirmed_password_label.setText("?????????? ????????????????????")
        self.main_widget.main_settings_widget.change_password_widget.submit_changed_password.setText("?????????? ????????????????")

        self.main_widget.main_settings_widget.create_acc_widget.add_username_label.setText("???????? ?????? ????????????????")
        self.main_widget.main_settings_widget.create_acc_widget.new_password_label.setText("???????? ???????? ????????????")
        self.main_widget.main_settings_widget.create_acc_widget.add_confirmed_password_label.setText("?????????? ????????????????????")
        self.main_widget.main_settings_widget.create_acc_widget.account_password_type_label.setText("???????? ???????? ???????? ?????? ????????????")

        self.main_widget.main_settings_widget.create_acc_widget.create_btn.setText("?????????? ???????? ????????")

        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setText(self.main_widget.main_settings_widget.settings_bar_frame.settings_pages[self.main_widget.lang][self.main_widget.main_settings_widget.main_settings_ly.currentIndex()])

        self.main_widget.add_emp_page_widget.add_emp_position_label.setText("???????? ???????? ????????????")
        self.main_widget.add_emp_page_widget.add_emp_name_label.setText("???????? ?????? ????????????")
        self.main_widget.add_emp_page_widget.add_emp_salary_label.setText("???????? ???????? ????????????")
        self.main_widget.add_emp_page_widget.select_employee_type_label.setText("???????? ?????? ?????????? ??????????????")
        self.main_widget.add_emp_page_widget.emp_code_input_label.setText("???????? ?????? ????????????")
        self.main_widget.add_emp_page_widget.add_emp_submit.setText("??????????")
        self.main_widget.add_emp_page_widget.add_emp_clear_btn.setText("??????")



        self.main_widget.new_package_widget.package_name_label.setText("?????? ????????????????")
        self.main_widget.new_package_widget.add_product_to_package_label.setText("????????????")
        self.main_widget.new_package_widget.package_tabel.setHorizontalHeaderLabels(["?????? ????????????", "????????????"])
        self.main_widget.new_package_widget.add_btn.setText("??????")
        self.main_widget.new_package_widget.save_btn.setText("?????? ????????????????")
        self.main_widget.new_package_widget.remove_btn.setText("?????????? ????????????????")


        self.main_widget.stock_widget.stock_tabel.setHorizontalHeaderLabels(
            ["????????????", "????????????", "?????? ????????????", "?????? ?????? ????????????", "???????????? ??????????????"])

        self.main_widget.new_order_h_widget.Buy_btn.setText("????????")
        self.main_widget.new_order_h_widget.Sell_btn.setText("??????")

        self.main_widget.new_order_h_widget.new_package_btn.setText("???????????? ??????????")

        self.main_widget.buy_product_widget.supplier_name_s_label.setText("?????? ????????????")
        self.main_widget.buy_product_widget.supplier_email_s_label.setText("???????? ????????????")
        self.main_widget.buy_product_widget.supplier_address_s_label.setText("?????????? ????????????")
        self.main_widget.buy_product_widget.supplier_link_s_label.setText("???????? ???????? ????????????")
        self.main_widget.buy_product_widget.product_name_label.setText("?????? ????????????")
        self.main_widget.buy_product_widget.product_quantity_label.setText("????????????")
        self.main_widget.buy_product_widget.product_price_label.setText("??????????")
        self.main_widget.buy_product_widget.product_selling_price_label.setText("?????? ??????????")

        self.main_widget.buy_product_widget.add_b_prod.setText("?????? ????????????")
        self.main_widget.buy_product_widget.products_tabel.setHorizontalHeaderLabels(["????????????", "????????????", "?????? ????????????", "?????? ??????????"])
        self.main_widget.buy_product_widget.total_tabel_b.setHorizontalHeaderLabels(["??????????????", "????????????", "????????????"])
        self.main_widget.buy_product_widget.stock_product.setText("???????? ??????????")
        self.main_widget.buy_product_widget.used_product.setText("???????? ??????????????")
        self.main_widget.buy_product_widget.service_product.setText("????????")
        self.main_widget.buy_product_widget.type_label.setText("???????????? ?????? ????????????")
        self.main_widget.buy_product_widget.dte_label.setText("??????????????")
        self.main_widget.buy_product_widget.buy_submit.setText("?????????? ??????????????")
        self.main_widget.buy_product_widget.clear_buy_page.setText("clear")
        self.main_widget.buy_product_widget.add_buy_package_btn.setText("?????? ????????????")
        self.main_widget.buy_product_widget.buy_package_name_label.setText("?????? ????????????????")
        self.main_widget.buy_product_widget.buy_package_quantity_label.setText("????????????")



        self.main_widget.sell_Product.client_name_label.setText("?????? ????????????")
        self.main_widget.sell_Product.client_email_label.setText("???????? ????????????")
        self.main_widget.sell_Product.client_address_label.setText("?????????? ????????????")
        self.main_widget.sell_Product.client_link_label.setText("???????? ???????? ????????????")
        self.main_widget.sell_Product.add_product_label.setText("?????? ????????????")
        self.main_widget.sell_Product.add_Packegas_label.setText("?????? ????????????????")
        self.main_widget.sell_Product.product_qt_label.setText("????????????")
        self.main_widget.sell_Product.packages_qt_label.setText("????????????")
        self.main_widget.sell_Product.add_service_fees_label.setText("?????? ??????????")
        self.main_widget.sell_Product.add_service_type_label.setText("?????? ????????????")
        self.main_widget.sell_Product.prod_tabel.setHorizontalHeaderLabels(["????????????", "????????????", "?????? ????????????", "?????? ??????????"])
        self.main_widget.sell_Product.total_tabel.setHorizontalHeaderLabels(["??????????????", "????????????", "??????????"])
        self.main_widget.sell_Product.sell_submit.setText("?????????? ??????????????")
        self.main_widget.sell_Product.service_cost_label.setText("?????????? ????????????")
        self.main_widget.sell_Product.add_product_btn.setText("?????? ????????")
        self.main_widget.sell_Product.add_Packages_btn.setText("?????? ????????????")
        self.main_widget.sell_Product.sell_date_label.setText("??????????????")
        self.main_widget.sell_Product.service_qt_label.setText("????????????")
        self.main_widget.sell_Product.add_service_btn.setText("?????? ????????")
        self.main_widget.sell_Product.clear_sell_page_btn.setText("??????")

        self.main_widget.login_widget.password_label.setText("???????? ???????? ????????")
        self.main_widget.login_widget.username_label.setText("???????? ?????? ????????????????")
        self.main_widget.login_widget.login_btn.setText("?????????? ????????????")

        self.main_widget.database_widget.database_bar.database_bar_label.setText(self.main_widget.database_widget.database_bar.database_pages[self.main_widget.lang][self.main_widget.database_widget.database_ly.currentIndex()])
        self.main_widget.new_order_bar.new_order_bar_label.setText(self.main_widget.new_order_bar.new_order_pages[self.main_widget.lang][self.main_widget.new_order_ly.currentIndex()])
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][self.main_widget.main_ly.currentIndex()])



        self.main_widget.database_widget.database_main_widget.employees_btn.setText("????????????????")
        self.main_widget.database_widget.database_main_widget.imports_btn.setText("????????????????")
        self.main_widget.database_widget.database_main_widget.exports_btn.setText("????????????????")
        self.main_widget.database_widget.database_main_widget.calculations_btn.setText("????????????????")




        self.main_widget.database_widget.import_export_widget.import_csv_btn.setText("???????? ?????? ????????")
        self.main_widget.database_widget.import_export_widget.export_csv_btn.setText("?????? ???????? ????????")

        l = ["????????????????", "????????????????", "????????????????", "????????????????"]
        self.main_widget.database_widget.import_export_widget.import_csv_cmb.clear()
        self.main_widget.database_widget.import_export_widget.export_csv_cmb.clear()
        self.main_widget.database_widget.import_export_widget.import_csv_cmb.addItems(l[:-1])
        self.main_widget.database_widget.import_export_widget.export_csv_cmb.addItems(l)

        self.main_widget.database_widget.emp_widget.emp_tabel.setHorizontalHeaderLabels(
            ["?????? ????????????", "?????? ????????????", "??????????", "????????????", "?????????? ??????????????"])
        self.main_widget.database_widget.emp_widget.add_emp.setText("??????")
        self.main_widget.database_widget.emp_widget.remove_emp.setText("??????????")
        self.main_widget.database_widget.emp_widget.save_emp.setText("??????")


        self.main_widget.database_widget.exp_widget.exports_tabel.setHorizontalHeaderLabels(
            ["?????? ????????????", "????????????", "??????????????", "????????????", "????????????????", "??????????????", "??????????", "??????????????", "??????????????"])
        self.main_widget.database_widget.exp_widget.add_exp.setText("??????")
        self.main_widget.database_widget.exp_widget.remove_exp.setText("??????????")
        self.main_widget.database_widget.exp_widget.save_exp.setText("??????")


        self.main_widget.database_widget.imp_widget.imp_tabel.setHorizontalHeaderLabels(
            ["?????? ????????????", "????????????", "??????????????", "????????????", "????????????????","?????? ??????????????", "??????????????","????????????????", "??????????????", "??????????????"])
        self.main_widget.database_widget.imp_widget.add_imp.setText("??????")
        self.main_widget.database_widget.imp_widget.remove_imp.setText("??????????")

        self.main_widget.database_widget.imp_widget.save_imp.setText("??????")



        self.main_widget.database_widget.calc_widget.calc_tabel.setHorizontalHeaderLabels(
            ["??????????", "?????? ??????????????", "?????????? ??????????", "?????????? ????????????", "?????????? ????????????", "???????????? ????????????"])

        self.main_widget.database_widget.calc_widget.tot_tabel.setHorizontalHeaderLabels(["???????????? ??????????????", "??????????????????", "????????????", "??????????"])
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(0, 0, qtw.QTableWidgetItem("?????????? ??????????"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(1, 0, qtw.QTableWidgetItem("?????????? ????????????"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(2, 0, qtw.QTableWidgetItem("?????????? ????????????"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(3, 0, qtw.QTableWidgetItem("???????????? ????????????"))
        self.main_widget.database_widget.calc_widget.tot_tabel.setItem(4, 0, qtw.QTableWidgetItem("????????????"))




        self.main_widget.main_info_widget.scrollable_info.info_name_label.setText("??????????: ")

        self.main_widget.main_info_widget.scrollable_info.info_add_label.setText("?????????? ????????????: ")

        self.main_widget.main_info_widget.scrollable_info.info_emp_label.setText("?????? ????????????????: ")

        self.main_widget.main_info_widget.scrollable_info.info_Mobile_label.setText("????????????: ")

        self.main_widget.main_info_widget.scrollable_info.info_Website_label.setText("???????? ????????????: ")

        self.main_widget.main_info_widget.scrollable_info.info_Rent_label.setText("??????????????: ")

        self.main_widget.main_info_widget.scrollable_info.info_description_label.setText("??????????: ")



        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_name_label.setText("???????? ?????? ????????????")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_address_label.setText("???????? ?????????? ????????????")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_website_label.setText("???????? ???????? ???????? ????????????")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_mobiles_label.setText("???????? ?????????? ???????????? ??????????")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_description_label.setText("???????? ?????????? ????????????")
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_rent_label.setText("???????? ?????????? ????????????")
        self.main_widget.main_info_widget.edit_info_page_widget.submit_new_info.setText("??????????")


        self.main_widget.main_settings_widget.Settings_widget.change_password.setText("?????????? ???????? ???????? ?????? ????????????????")
        self.main_widget.main_settings_widget.Settings_widget.create_new_username.setText("?????????? ???????? ????????")
        self.main_widget.main_settings_widget.Settings_widget.laguage_settings.setText("??English")
        self.main_widget.main_settings_widget.Settings_widget.night_mode_btn.setText("?????????? ????????????-??????????")

        self.main_widget.main_info_widget.scrollable_info.info_name_label_ly.setDirection(1)  # right to left alligment
        self.main_widget.main_info_widget.scrollable_info.info_add_label_ly.setDirection(1)
        self.main_widget.main_info_widget.scrollable_info.info_emp_label_ly.setDirection(1)
        self.main_widget.main_info_widget.scrollable_info.info_mobile_label_ly.setDirection(1)
        self.main_widget.main_info_widget.scrollable_info.info_website_label_ly.setDirection(1)
        self.main_widget.main_info_widget.scrollable_info.info_Rent_label_ly.setDirection(1)
        self.main_widget.main_info_widget.scrollable_info.info_description_label_ly.setDirection(1)


        self.main_widget.top_frame.top_frame_label.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.main_settings_widget.change_password_widget.username_change_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.change_password_widget.old_password_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.change_password_widget.confirmed_password_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.change_password_widget.changed_password_label.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.main_settings_widget.create_acc_widget.add_username_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.create_acc_widget.new_password_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.create_acc_widget.add_confirmed_password_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.create_acc_widget.account_password_type_label.setAlignment(qtc.Qt.AlignRight)


        self.main_widget.add_emp_page_widget.add_emp_position_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.add_emp_page_widget.add_emp_name_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.add_emp_page_widget.add_emp_salary_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.add_emp_page_widget.select_employee_type_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.add_emp_page_widget.emp_code_input_label.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.new_package_widget.package_name_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.new_package_widget.add_product_to_package_label.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.buy_product_widget.supplier_name_s_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.supplier_email_s_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.supplier_address_s_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.supplier_link_s_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.product_quantity_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.product_price_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.product_selling_price_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.type_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.dte_label.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.sell_Product.client_name_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.client_email_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.client_address_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.client_link_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.add_product_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.add_Packegas_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.product_qt_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.packages_qt_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.add_service_fees_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.add_service_type_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.service_qt_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.service_cost_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.sell_Product.sell_date_label.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.buy_product_widget.product_price_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.product_selling_price_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.buy_package_name_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.buy_product_widget.buy_package_quantity_label.setAlignment(qtc.Qt.AlignRight)


        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_name_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_address_label.setAlignment(
            qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_website_label.setAlignment(
            qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_mobiles_label.setAlignment(
            qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_description_label.setAlignment(
            qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_rent_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_name.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_address.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_website.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_mobiles.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_description.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_info_widget.edit_info_page_widget.edit_company_rent.setAlignment(qtc.Qt.AlignRight)

        self.main_widget.login_widget.password_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.login_widget.username_label.setAlignment(qtc.Qt.AlignRight)
        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setAlignment(qtc.Qt.AlignRight)

