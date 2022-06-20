import PyQt5.QtWidgets as qtw
from languages import langs
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class settings_home_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        self.setStyleSheet(self.main_widget.my_style.home_page_btn_style())
        self.change_password = qtw.QPushButton("change password")
        self.change_password.clicked.connect(self.change_password_btn_fun)
        self.create_new_username = qtw.QPushButton("Create new account")
        self.create_new_username.clicked.connect(self.create_new_username_btn_fun)
        self.laguage_settings = qtw.QPushButton("Set to Arabic")
        self.laguage_settings.clicked.connect(self.translate_lang)
        self.night_mode_btn = qtw.QPushButton("Light/dark Mode")
        self.night_mode_btn.clicked.connect(self.set_light_night_mode)
        self.set_layout()

    def translate_lang(self):
        my_lang=langs(self.main_widget)
        if self.main_widget.lang == 0:
            my_lang.set_arabic()
        else:
            my_lang.set_english()


    def set_light_night_mode(self):
        if (not self.main_widget.dark_state):
            self.main_widget.my_style.apply_dark_mode()
            self.main_widget.dark_state = 1
        else:
            self.main_widget.my_style.apply_light_mode()
            self.main_widget.dark_state = 0

    def create_new_username_btn_fun(self):
        self.main_widget.main_settings_widget.main_settings_ly.setCurrentIndex(1)
        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setText(self.main_widget.main_settings_widget.settings_bar_frame.settings_pages[self.main_widget.lang][1])
        self.main_widget.main_settings_widget.settings_bar_frame.count = 1

    def change_password_btn_fun(self):
        self.main_widget.main_settings_widget.main_settings_ly.setCurrentIndex(2)
        self.main_widget.main_settings_widget.settings_bar_frame.settings_bar_label.setText(self.main_widget.main_settings_widget.settings_bar_frame.settings_pages[self.main_widget.lang][2])
        self.main_widget.main_settings_widget.settings_bar_frame.count = 2

    def set_layout(self):
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

        self.setLayout(self.Settings_ly)