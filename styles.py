import qdarkstyle


class styles:
    def __init__(self, main_widget):
        self.main_widget = main_widget

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
                border-color:""" + self.main_widget.light_theme + """;
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
        border-color:''' + self.main_widget.light_theme + ''';
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
        border-color: """ + self.main_widget.light_theme + """;
        color:black;}
        """

    def menue_btn_style(self):
        return """QPushButton{ border-radius:25px;min-width:50px;min-height:50px;}"""

    def main_widgets_light_style(self):
        return """          QWidget{
                            background-color:white;
                            }
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
                            background-color:""" + self.main_widget.light_theme + """;
                            }
                            QRadioButton{
                             font:bold 14px;
                             color:black;
                             }
                            QLineEdit{
                            color:black;
                            border-color:""" + self.main_widget.light_theme + """;
                            border-width:2px;
                            border-style:outset;
                            min-height:32px;
                            min-width:700px;
                            max-height:32px;
                            max-width:700px;
                            border-radius:10px;
                            font:bold 14px;
                            background-color:white;
                            }
                            QLabel{
                            color:black;
                            font:bold 14px;
                            background-color:white;
                            }
                            QSpinBox{
                            min-height:32px;
                            min-width:35px;
                            max-height:32px;
                            max-width:35px;

                            }
                            QComboBox{
                            border-color:""" + self.main_widget.light_theme + """;
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
    def spin_box_style(self):
        return """
        
        QSpinBox{
        min-height:32px;
        min-width:50px;
        max-height:32px;
        max-width:120px;

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
        min-width:50px;
        max-height:32px;
        max-width:50px;

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

    def apply_dark_mode(self, ):
        self.main_widget.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.main_widget.database_widget.calc_widget.years.setStyleSheet(self.cmb_style())

        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setStyleSheet("QLabel{color:white;font: bold 15px;}")
        self.main_widget.main_settings_widget.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.main_widget.main_settings_widget.change_password_widget.setStyleSheet(self.main_widgets_style())

        self.main_widget.main_settings_widget.create_acc_widget.setStyleSheet(self.main_widgets_style())
        self.main_widget.main_settings_widget.settings_bar_frame.setStyleSheet(
            """QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:""" + self.main_widget.dark_theme + """;min-height:50px;}""")
        self.main_widget.database_widget.database_bar.database_bar_label.setStyleSheet("QLabel{color:white;font: bold 15px;}")
        self.main_widget.top_frame.top_frame_label.setStyleSheet("QLabel{color:white;font: bold 15px;}")


        self.main_widget.database_widget.import_export_widget.import_csv_cmb.setStyleSheet(self.cmb_style())
        self.main_widget.database_widget.import_export_widget.export_csv_cmb.setStyleSheet(self.cmb_style())

        self.main_widget.add_emp_page_widget.setStyleSheet(self.main_widgets_style())
        self.main_widget.main_info_widget.edit_info_page_widget.setStyleSheet(self.main_widgets_style())
        self.main_widget.new_package_widget.setStyleSheet(self.main_widgets_style())
        self.main_widget.sell_Product.setStyleSheet(self.main_widgets_style())
        self.main_widget.buy_product_widget.setStyleSheet(self.main_widgets_style())



        self.main_widget.database_widget.database_main_widget.employees_btn.setStyleSheet(self.home_page_btn_style())
        self.main_widget.database_widget.database_main_widget.calculations_btn.setStyleSheet(self.home_page_btn_style())
        self.main_widget.database_widget.database_main_widget.imports_btn.setStyleSheet(self.home_page_btn_style())
        self.main_widget.database_widget.database_main_widget.exports_btn.setStyleSheet(self.home_page_btn_style())



        self.main_widget.database_widget.database_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.main_widget.dark_theme + ";min-height:50px;}")
        self.main_widget.new_order_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.main_widget.dark_theme + ";min-height:50px;}")
        self.main_widget.new_order_bar.new_order_bar_label.setStyleSheet("QLabel{color:white;font: bold 14px;}")
        self.main_widget.login_widget.username_in.setStyleSheet(self.line_edit_style())
        self.main_widget.login_widget.password_in.setStyleSheet(self.line_edit_style())
        self.main_widget.stock_widget.search_btn.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")
        self.main_widget.stock_widget.search_box.setStyleSheet(
            "color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")

        self.main_widget.database_widget.database_bar.search_btn_db.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")
        self.main_widget.database_widget.database_bar.search_box_db.setStyleSheet(
            "color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")
        self.main_widget.top_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.main_widget.dark_theme + ";min-height:70px;max-height:70px;min-width:" + str(
                self.main_widget.width()) + "px;}")
        self.main_widget.side_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.main_widget.dark_theme + ";min-width:70px;max-width:70px;min-height:" + str(
                self.main_widget.height() - 70) + "px;}")
        self.main_widget.main_settings_widget.Settings_widget.setStyleSheet(self.home_page_btn_style())

        self.main_widget.new_order_h_widget.Buy_btn.setStyleSheet(self.home_page_btn_style())
        self.main_widget.new_order_h_widget.Sell_btn.setStyleSheet(self.home_page_btn_style())
        self.main_widget.new_order_h_widget.new_package_btn.setStyleSheet(self.home_page_btn_style())
        self.main_widget.repaint()

    def apply_light_mode(self):
        self.main_widget.database_widget.calc_widget.years.setStyleSheet(self.cmb_style_light())
        self.main_widget.setStyleSheet("background-color:white;")
        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setStyleSheet("QLabel{color:black;font: bold 15px;}")
        self.main_widget.main_settings_widget.change_password_widget.setStyleSheet(self.main_widgets_light_style())
        self.main_widget.main_settings_widget.create_acc_widget.setStyleSheet(self.main_widgets_light_style())
        self.main_widget.main_settings_widget.settings_bar_frame.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.main_widget.light_theme + ";min-height:50px;}QPushButton{background-color:white;}")
        self.main_widget.main_settings_widget.Settings_widget.setStyleSheet(self.home_page_btn_style_light())


        self.main_widget.database_widget.database_bar.database_bar_label.setStyleSheet("QLabel{color:black;font: bold 15px;}")
        self.main_widget.top_frame.top_frame_label.setStyleSheet("QLabel{color:black;font: bold 15px;}")

        self.main_widget.database_widget.import_export_widget.import_csv_cmb.setStyleSheet(self.cmb_style_light())
        self.main_widget.database_widget.import_export_widget.export_csv_cmb.setStyleSheet(self.cmb_style_light())

        self.main_widget.add_emp_page_widget.setStyleSheet(self.main_widgets_light_style())
        self.main_widget.main_info_widget.edit_info_page_widget.setStyleSheet(self.main_widgets_light_style())
        self.main_widget.new_package_widget.setStyleSheet(self.main_widgets_light_style())
        self.main_widget.sell_Product.setStyleSheet(self.main_widgets_light_style())
        self.main_widget.buy_product_widget.setStyleSheet(self.main_widgets_light_style())

        self.main_widget.new_order_h_widget.Buy_btn.setStyleSheet(self.home_page_btn_style_light())
        self.main_widget.new_order_h_widget.Sell_btn.setStyleSheet(self.home_page_btn_style_light())
        self.main_widget.new_order_h_widget.new_package_btn.setStyleSheet(self.home_page_btn_style_light())



        self.main_widget.database_widget.database_main_widget.employees_btn.setStyleSheet(self.home_page_btn_style_light())
        self.main_widget.database_widget.database_main_widget.calculations_btn.setStyleSheet(self.home_page_btn_style_light())
        self.main_widget.database_widget.database_main_widget.imports_btn.setStyleSheet(self.home_page_btn_style_light())
        self.main_widget.database_widget.database_main_widget.exports_btn.setStyleSheet(self.home_page_btn_style_light())



        self.main_widget.database_widget.database_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.main_widget.light_theme + ";min-height:50px;}")
        self.main_widget.new_order_bar.setStyleSheet(
            "QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:" + self.main_widget.light_theme + ";min-height:50px;}")
        self.main_widget.new_order_bar.new_order_bar_label.setStyleSheet("QLabel{color:black;font: bold 14px;}")
        self.main_widget.login_widget.username_in.setStyleSheet(self.line_edit_style_light())
        self.main_widget.login_widget.password_in.setStyleSheet(self.line_edit_style_light())
        self.main_widget.stock_widget.search_btn.setStyleSheet(
            "QPushButton{ border-radius:25px;min-width:50px;min-height:50px;background-color:cyan;}QPushButton::hover{border-radius:25px;min-width:50px;min-height:50px;background-color:blue;}")
        self.main_widget.stock_widget.search_box.setStyleSheet(
            "color:black;border-color:cyan;border-width:2px;border-style:outset;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")

        self.main_widget.database_widget.database_bar.search_btn_db.setStyleSheet(
            "QPushButton{ border-radius:25px;min-width:50px;min-height:50px;background-color:cyan;}QPushButton::hover{border-radius:25px;min-width:50px;min-height:50px;background-color:blue;}")
        self.main_widget.database_widget.database_bar.search_box_db.setStyleSheet(
            "color:black;border-color:" + self.main_widget.light_theme + ";border-width:2px;border-style:outset;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px")

        self.main_widget.top_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.main_widget.light_theme + ";min-height:70px;max-height:70px;min-width:" + str(
                self.main_widget.width()) + "px;}")
        self.main_widget.side_frame.setStyleSheet(
            "QFrame{border-width:0px;background-color:" + self.main_widget.light_theme + ";min-width:70px;max-width:70px;min-height:" + str(
                self.main_widget.height() - 70) + "px;}")
        self.main_widget.repaint()

