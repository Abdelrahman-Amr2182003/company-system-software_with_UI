import PyQt5.QtWidgets as qtw

from create_new_account import create_new_account
from settings_home_page import settings_home_page
from bars import settings_bar
from change_password import change_password
class settings_page(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget = main_widget
        #############Settings home#########################
        self.Settings_widget = settings_home_page(self.main_widget)
        #######################Create new account####################################
        self.create_acc_widget = create_new_account(self.main_widget)
        #############################Change password ###############################
        self.change_password_widget = change_password(self.main_widget)
        ##################Settings Order bar#################################
        self.settings_bar_frame = settings_bar(self.main_widget)
        self.set_layout()



    def set_layout(self):
        self.main_settings_v_ly = qtw.QVBoxLayout()
        self.main_settings_ly = qtw.QStackedLayout()
        self.main_settings_ly.addWidget(self.Settings_widget)
        self.main_settings_ly.addWidget(self.create_acc_widget)
        self.main_settings_ly.addWidget(self.change_password_widget)
        self.main_settings_ly.setCurrentIndex(0)
        self.main_settings_v_ly.addWidget(self.settings_bar_frame)
        self.main_settings_v_ly.addLayout(self.main_settings_ly)
        self.setLayout(self.main_settings_v_ly)
