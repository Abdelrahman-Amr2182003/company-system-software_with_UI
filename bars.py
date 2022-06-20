import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import  PyQt5.QtCore as qtc
from sort_dialog import sort_dialog
from filter_dialog import filter_dialog

class top_bar(qtw.QFrame):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.menue_btn = qtw.QPushButton()
        self.menue_btn.setIcon(qtg.QIcon('icons//i.png'))
        self.menue_btn.setIconSize(qtc.QSize(50, 50))
        self.menue_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.menue_btn.clicked.connect(self.menue_btn_fun)
        self.top_frame_label = qtw.QLabel()
        self.top_frame_label.setStyleSheet("QLabel{color:white;font: bold 14px;}")
        self.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][0])
        self.set_layout()
    def menue_btn_fun(self):
        if self.main_widget.side_frame.x() == -self.main_widget.side_frame.width():
            self.menue_btn.setIcon(qtg.QIcon('icons//left.png'))
            self.anim = qtc.QPropertyAnimation(self.main_widget.side_frame, b"pos")
            self.anim.setEndValue(qtc.QPoint(self.x(), self.main_widget.side_frame.y()))
            self.anim.setDuration(300)

            self.anim_2 = qtc.QPropertyAnimation(self.main_widget.main_widget, b'pos')
            self.anim_2.setStartValue(qtc.QPoint(11, 81))
            self.anim_2.setEndValue(qtc.QPoint(81, 81))
            self.anim_2.setDuration(300)

            self.group_animation = qtc.QParallelAnimationGroup()
            self.group_animation.addAnimation(self.anim)
            self.group_animation.addAnimation(self.anim_2)
            self.group_animation.start()


        else:
            self.menue_btn.setIcon(qtg.QIcon('icons//i.png'))

            self.anim_h = qtc.QPropertyAnimation(self.main_widget.side_frame, b"pos")
            self.anim_h.setEndValue(qtc.QPoint(-(self.main_widget.side_frame.width()), self.main_widget.side_frame.y()))
            self.anim_h.setDuration(400)

            self.anim_2_h = qtc.QPropertyAnimation(self.main_widget.main_widget, b'pos')
            self.anim_2_h.setStartValue(qtc.QPoint(81, 81))
            self.anim_2_h.setEndValue(qtc.QPoint(11, 81))
            self.anim_2_h.setDuration(400)

            self.group_animation_h = qtc.QParallelAnimationGroup()
            self.group_animation_h.addAnimation(self.anim_h)
            self.group_animation_h.addAnimation(self.anim_2_h)
            self.group_animation_h.start()
    def set_layout(self):
        self.top_frame_ly = qtw.QHBoxLayout()
        self.top_frame_ly.addWidget(self.menue_btn)
        self.top_frame_ly.addStretch()
        self.top_frame_ly.addWidget(self.top_frame_label)
        self.top_frame_ly.addStretch()
        self.setLayout(self.top_frame_ly)
class side_bar(qtw.QFrame):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.home_btn = qtw.QPushButton()
        self.home_btn.setIcon(qtg.QIcon('icons//home.png'))
        self.home_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.home_btn.setIconSize(qtc.QSize(50, 50))
        self.home_btn.clicked.connect(self.home_btn_fun)

        self.stock_btn = qtw.QPushButton()
        self.stock_btn.setIcon(qtg.QIcon('icons//stock.png'))
        self.stock_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.stock_btn.setIconSize(qtc.QSize(50, 50))
        self.stock_btn.clicked.connect(self.main_widget.home_page_widget.stock_btn_fun)

        self.new_btn = qtw.QPushButton()
        self.new_btn.setIcon(qtg.QIcon('icons//new.png'))
        self.new_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.new_btn.setIconSize(qtc.QSize(50, 50))
        self.new_btn.clicked.connect(self.main_widget.home_page_widget.new_order_btn_fun)

        self.data_btn = qtw.QPushButton()
        self.data_btn.setIcon(qtg.QIcon('icons//database.png'))
        self.data_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.data_btn.setIconSize(qtc.QSize(50, 50))
        self.data_btn.clicked.connect(self.main_widget.home_page_widget.database_btn_fun)

        self.info_btn = qtw.QPushButton()
        self.info_btn.setIcon(qtg.QIcon('icons//info.png'))
        self.info_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.info_btn.setIconSize(qtc.QSize(50, 50))
        self.info_btn.clicked.connect(self.main_widget.home_page_widget.info_btn_fun)

        self.settings_btn = qtw.QPushButton()
        self.settings_btn.setIcon(qtg.QIcon('icons//settings.png'))
        self.settings_btn.setStyleSheet(self.main_widget.my_style.menue_btn_style())
        self.settings_btn.setIconSize(qtc.QSize(50, 50))
        self.settings_btn.clicked.connect(self.settings_btn_fun)
        self.set_layout()

    def home_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(0)
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][0])

    def settings_btn_fun(self):
        self.main_widget.main_ly.setCurrentIndex(5)
        self.main_widget.top_frame.top_frame_label.setText(self.main_widget.main_pages[self.main_widget.lang][5])
    def set_layout(self):
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

        self.setLayout(self.side_frame_ly)

class new_order_bar(qtw.QFrame):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.count=0
        self.new_order_pages = [
            ["New Order Home Page", "Buying page", "Selling page", "New Package page", "Add Employee"],
            ["الفحة الرئيسية", "صفحة شراء المنتجات", "صفحة بيع المنتجات", "صفحة اصافة مجموعة جديدة", "اضف موظف جديد"]]

        self.new_order_back_btn = qtw.QPushButton()
        self.new_order_back_btn.setIcon(qtg.QIcon("icons//back.png"))
        self.new_order_back_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.new_order_back_btn.clicked.connect(self.new_order_back_btn_fun)

        self.new_order_forward_btn = qtw.QPushButton()
        self.new_order_forward_btn.setIcon(qtg.QIcon("icons//forward.png"))
        self.new_order_forward_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.new_order_forward_btn.clicked.connect(self.new_order_forward_btn_fun)

        self.new_order_home_btn = qtw.QPushButton()
        self.new_order_home_btn.setIcon(qtg.QIcon("icons//home.png"))
        self.new_order_home_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.new_order_home_btn.clicked.connect(self.new_order_home_btn_fun)

        self.new_order_bar_label = qtw.QLabel()
        self.new_order_bar_label.setStyleSheet("QLabel{color:white;font: bold 14px;}")
        self.new_order_bar_label.setText(self.new_order_pages[self.main_widget.lang][0])
        self.set_layout()
    def new_order_home_btn_fun(self):

        self.main_widget.update_cmb()
        self.main_widget.new_order_ly.setCurrentIndex(0)
        self.new_order_bar_label.setText(self.new_order_pages[self.main_widget.lang][0])
        self.count = 0

    def new_order_back_btn_fun(self):
        if (self.count >= 1):
            self.count -= 1
        else:
            self.count = 4
        self.main_widget.new_order_ly.setCurrentIndex(self.count)
        self.new_order_bar_label.setText(self.new_order_pages[self.main_widget.lang][self.count])
        self.main_widget.update_cmb()
    def new_order_forward_btn_fun(self):
        if (self.count < 4):
            self.count += 1
        else:
            self.count = 0
        self.main_widget.new_order_ly.setCurrentIndex(self.count)
        self.new_order_bar_label.setText(self.new_order_pages[self.main_widget.lang][self.count])
        self.main_widget.update_cmb()
    def set_layout(self):
        self.new_order_top_bar_ly = qtw.QHBoxLayout()
        self.new_order_top_bar_ly.addWidget(self.new_order_back_btn)
        self.new_order_top_bar_ly.addWidget(self.new_order_forward_btn)
        self.new_order_top_bar_ly.addWidget(self.new_order_home_btn)
        self.new_order_top_bar_ly.addStretch()
        self.new_order_top_bar_ly.addWidget(self.new_order_bar_label)
        self.new_order_top_bar_ly.addStretch()

        self.setLayout(self.new_order_top_bar_ly)
class settings_bar(qtw.QFrame):
    def __init__(self,main_widget):
        super().__init__()
        self.settings_pages = [["Home Page", "Create new account", "change password"],
                               ["الفحة الرئيسية", "حساب جدييد", "تغيير كلمة المرور"]]
        self.main_widget=main_widget
        self.count=0
        self.setStyleSheet(
            """QFrame{border-radius:5px;border-width:0px;border-style:outset;background-color:rgb(0,0,0);min-height:50px;}""")
        self.settings_back_btn = qtw.QPushButton()
        self.settings_back_btn.setIcon(qtg.QIcon("icons//back.png"))
        self.settings_back_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.settings_back_btn.clicked.connect(self.settings_back_btn_fun)

        self.settings_forward_btn = qtw.QPushButton()
        self.settings_forward_btn.setIcon(qtg.QIcon("icons//forward.png"))
        self.settings_forward_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.settings_forward_btn.clicked.connect(self.settings_forward_btn_fun)

        self.settings_home_btn = qtw.QPushButton()
        self.settings_home_btn.setIcon(qtg.QIcon("icons//home.png"))
        self.settings_home_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.settings_home_btn.clicked.connect(self.settings_home_btn_fun)

        self.settings_bar_label = qtw.QLabel()
        self.settings_bar_label.setStyleSheet("QLabel{color:white;font bold 14px;}")
        self.settings_bar_label.setText(self.settings_pages[self.main_widget.lang][0])
        self.edit_theme_color = qtw.QPushButton()

        self.settings_color_btn = qtw.QPushButton()
        self.settings_color_btn.setIcon(qtg.QIcon("icons//colors.png"))
        self.settings_color_btn.setIconSize(qtc.QSize(30, 30))
        self.settings_color_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.settings_color_btn.clicked.connect(self.change_color_btn_fun)
        self.set_layout()

    def settings_home_btn_fun(self):
        self.count = 0
        self.main_widget.main_settings_widget.main_settings_ly.setCurrentIndex(self.count)
        self.settings_bar_label.setText(self.settings_pages[self.main_widget.lang][self.main_widget.main_settings_widget.main_settings_ly.currentIndex()])

    def settings_back_btn_fun(self):
        if self.count > 0:
            self.count -= 1

        else:
            self.count = 2
        self.main_widget.main_settings_widget.main_settings_ly.setCurrentIndex(self.count)
        self.settings_bar_label.setText(self.settings_pages[self.main_widget.lang][self.main_widget.main_settings_widget.main_settings_ly.currentIndex()])

    def settings_forward_btn_fun(self):
        if self.count < 2:
            self.count += 1

        else:
            self.count = 0
        self.main_widget.main_settings_widget.main_settings_ly.setCurrentIndex(self.count)
        self.settings_bar_label.setText(self.settings_pages[self.main_widget.lang][self.main_widget.main_settings_widget.main_settings_ly.currentIndex()])


    def change_color_btn_fun(self):
        if self.main_widget.dark_state==1:
            color = qtw.QColorDialog.getColor(qtg.QColor(0, 0, 0), self, "choose color")
            self.main_widget.dark_theme=f'rgb({color.red()},{color.green()},{color.blue()})'
            self.main_widget.dark_colors=f'{color.red()},{color.green()},{color.blue()}'
            self.main_widget.my_style.apply_dark_mode()
        elif self.main_widget.dark_state==0:
            color = qtw.QColorDialog.getColor(qtg.QColor(0, 32, 242), self, "choose color")
            self.main_widget.light_theme=f'rgb({color.red()},{color.green()},{color.blue()})'
            self.main_widget.light_colors=f'{color.red()},{color.green()},{color.blue()}'
            self.main_widget.my_style.apply_light_mode()

    def set_layout(self):
        self.settings_top_bar_ly = qtw.QHBoxLayout()
        self.settings_top_bar_ly.addWidget(self.settings_back_btn)
        self.settings_top_bar_ly.addWidget(self.settings_forward_btn)
        self.settings_top_bar_ly.addWidget(self.settings_home_btn)
        self.settings_top_bar_ly.addWidget(self.settings_color_btn)
        self.settings_top_bar_ly.addStretch()
        self.settings_top_bar_ly.addWidget(self.settings_bar_label)
        self.settings_top_bar_ly.addStretch()
        self.setLayout(self.settings_top_bar_ly)
class data_base_bar(qtw.QFrame):
    def __init__(self,main_widget):
        super().__init__()

        self.count = 0
        self.database_pages = [["Database Home Page", "Employees Table", "Calculations Tabel", "Imports Tabel",
                                "Exports Tabel"], ["الفحة الرئيسية", "جدول الموظفبن", "جدول الحسابات", "جدول الواردات",
                                                   "جدول التصديرات"]]
        self.main_widget=main_widget
        self.back_btn = qtw.QPushButton()
        self.back_btn.setIcon(qtg.QIcon("icons//back.png"))
        self.back_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.back_btn.clicked.connect(self.back_btn_fun)

        self.forward_btn = qtw.QPushButton()
        self.forward_btn.setIcon(qtg.QIcon("icons//forward.png"))
        self.forward_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.forward_btn.clicked.connect(self.forward_btn_fun)

        self.database_home_btn = qtw.QPushButton()
        self.database_home_btn.setIcon(qtg.QIcon("icons//home.png"))
        self.database_home_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.database_home_btn.clicked.connect(self.database_home_btn_fun)

        self.database_bar_label = qtw.QLabel()
        self.database_bar_label.setStyleSheet("QLabel{color:white;font: bold 15px;}")
        self.database_bar_label.setText(self.database_pages[self.main_widget.lang][0])

        self.sort_db_btn = qtw.QPushButton()
        self.sort_db_btn.setIcon(qtg.QIcon("icons//sort.png"))
        self.sort_db_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.sort_db_btn.clicked.connect(self.sort_db_btn_fun)

        self.filter_db_btn = qtw.QPushButton()
        self.filter_db_btn.setIcon(qtg.QIcon("icons//filter.png"))
        self.filter_db_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.filter_db_btn.clicked.connect(self.filter_btn_fun)

        self.undo_db_btn = qtw.QPushButton()
        self.undo_db_btn.setIcon(qtg.QIcon("icons//undo.png"))
        self.undo_db_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.undo_db_btn.clicked.connect(self.undo_db_btn_fun)

        self.redo_db_btn = qtw.QPushButton()
        self.redo_db_btn.setIcon(qtg.QIcon(qtg.QPixmap("icons//undo.png").transformed(qtg.QTransform().rotate(180))))
        self.redo_db_btn.setStyleSheet(self.main_widget.my_style.bar_btn_style())
        self.redo_db_btn.clicked.connect(self.redo_db_btn_fun)

        self.search_box_db = qtw.QLineEdit()
        self.search_box_db.setStyleSheet(
            '''color:white;min-height:30px;border-radius:10px;font:bold 14px;min-width:100px''')
        self.search_btn_db = qtw.QPushButton()
        self.search_btn_db.setIcon(qtg.QIcon("icons/search.png"))
        self.search_btn_db.setIconSize(qtc.QSize(50, 50))
        self.search_btn_db.setStyleSheet(
            "QPushButton{ border-radius:20px;min-width:50px;min-height:50px;background-color:rgb(30,50,255);}QPushButton::hover{border-radius:20px;min-width:50px;min-height:50px;background-color:cyan};")
        self.search_btn_db.clicked.connect(self.search_tables)
        self.set_layout()
    def search_table(self,table):
        target=self.search_box_db.text().lower()
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                if table.item(i,j) is not None:
                    text=table.item(i,j).text()
                    if target in text.lower():
                        table.selectRow(i)
    def search_tables(self):
        if self.main_widget.database_widget.database_ly.currentIndex()==1:
            self.search_table(self.main_widget.database_widget.emp_widget.emp_tabel)
        if self.main_widget.database_widget.database_ly.currentIndex()==2:
            self.search_table(self.main_widget.database_widget.calc_widget.calc_tabel)
        if self.main_widget.database_widget.database_ly.currentIndex()==3:
            self.search_table(self.main_widget.database_widget.imp_widget.imp_tabel)
        if self.main_widget.database_widget.database_ly.currentIndex()==4:
            self.search_table(self.main_widget.database_widget.exp_widget.exports_tabel)

    def undo_db_btn_fun(self):
        if self.main_widget.database_widget.database_ly.currentIndex()==1:
            self.main_widget.database_widget.emp_widget.undo()
        if self.main_widget.database_widget.database_ly.currentIndex()==3:
            self.main_widget.database_widget.imp_widget.undo()
        if self.main_widget.database_widget.database_ly.currentIndex()==4:
            self.main_widget.database_widget.exp_widget.undo()

    def redo_db_btn_fun(self):
        if self.main_widget.database_widget.database_ly.currentIndex()==1:
            self.main_widget.database_widget.emp_widget.redo()
        if self.main_widget.database_widget.database_ly.currentIndex()==3:
            self.main_widget.database_widget.imp_widget.redo()
        if self.main_widget.database_widget.database_ly.currentIndex()==4:
            self.main_widget.database_widget.exp_widget.redo()
    def filter_btn_fun(self):

        if self.main_widget.database_widget.database_ly.currentIndex()==4:
            self.filter_dialog_bar = filter_dialog(self.main_widget, self.main_widget.database_widget.exp_widget.exports_tabel, 6)
        if self.main_widget.database_widget.database_ly.currentIndex()==3:
            self.filter_dialog_bar=filter_dialog(self.main_widget,self.main_widget.database_widget.imp_widget.imp_tabel,6)

    def sort_db_btn_fun(self):
        if self.main_widget.database_widget.database_ly.currentIndex()==4:
            self.sort_dilog=sort_dialog(self.main_widget.database_widget.exp_widget.exports_tabel,6,8,"profit","date")
        if self.main_widget.database_widget.database_ly.currentIndex()==3:
            self.sort_dilog=sort_dialog(self.main_widget.database_widget.imp_widget.imp_tabel,6,8,"cost","date")



    def database_home_btn_fun(self):
        self.main_widget.database_widget.database_ly.setCurrentIndex(0)
        self.database_bar_label.setText(self.database_pages[self.main_widget.lang][0])
        self.count = 0
        self.main_widget.update_cmb()
    def back_btn_fun(self):
        if (self.count >= 1):
            self.count -= 1
        else:
            self.count = 4
        self.main_widget.database_widget.database_ly.setCurrentIndex(self.count)
        self.database_bar_label.setText(self.database_pages[self.main_widget.lang][self.count])
        self.main_widget.update_cmb()
        if self.main_widget.database_widget.database_ly.currentIndex()==2:
            self.main_widget.database_widget.calc_widget.populate_calculations_tabel()
            self.main_widget.database_widget.calc_widget.populate_total_calc_table()
    def forward_btn_fun(self):
        if (self.count < 4):
            self.count += 1
        else:
            self.count = 0
        self.main_widget.database_widget.database_ly.setCurrentIndex(self.count)
        self.database_bar_label.setText(self.database_pages[self.main_widget.lang][self.count])
        if self.main_widget.database_widget.database_ly.currentIndex()==2:
            self.main_widget.database_widget.calc_widget.populate_calculations_tabel()
            self.main_widget.database_widget.calc_widget.populate_total_calc_table()
        self.main_widget.update_cmb()

    def set_layout(self):
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
        self.setLayout(self.database_top_bar_ly)
