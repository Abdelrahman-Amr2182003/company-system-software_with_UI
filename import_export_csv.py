import PyQt5.QtWidgets as qtw
import pandas as pd
import os
import datetime
class import_export_csv(qtw.QWidget):
    def __init__(self,main_widget):
        super().__init__()
        self.main_widget=main_widget
        l = ["Employees", "imports", "Exports", "Calculations"]
        self.import_csv_btn = qtw.QPushButton("Import CSV")
        self.import_csv_btn.setStyleSheet(self.main_widget.my_style.button_style())
        self.import_csv_btn.clicked.connect(self.import_tables)
        self.export_csv_btn = qtw.QPushButton("Export CSV")
        self.export_csv_btn.setStyleSheet(self.main_widget.my_style.button_style())
        self.export_csv_btn.clicked.connect(self.export_csv)
        self.import_csv_cmb = qtw.QComboBox()
        self.import_csv_cmb.setStyleSheet(self.main_widget.my_style.cmb_style())
        self.export_csv_cmb = qtw.QComboBox()
        self.export_csv_cmb.setStyleSheet(self.main_widget.my_style.cmb_style())
        self.import_csv_cmb.addItems(l[:-1])
        self.export_csv_cmb.addItems(l)
        self.set_layout()
    def export_csv(self):
        self.dir_path = qtw.QFileDialog.getExistingDirectory(self, "Choose Directory", "C:\\")
        if self.export_csv_cmb.currentText()=='Employees':
            table=self.main_widget.database_widget.emp_widget.emp_tabel
            self.save_table('employees_table',table)
        if self.export_csv_cmb.currentText()=='imports':
            table=self.main_widget.database_widget.imp_widget.imp_tabel
            self.save_table('imports_table',table)
        if self.export_csv_cmb.currentText()=='Exports':
            table=self.main_widget.database_widget.exp_widget.exports_tabel
            self.save_table('exports_table',table)
        if self.export_csv_cmb.currentText()=='Calculations':
            table=self.main_widget.database_widget.calc_widget.calc_tabel
            table_2=self.main_widget.database_widget.calc_widget.tot_tabel
            self.save_table('calculations_table',table)
            self.save_table('total_calculations',table_2)
    def import_tables(self):
        directory = qtw.QFileDialog.getOpenFileName(self, 'Open File', 'C:\\', "Image files (*.xlsx *.csv)")
        if self.import_csv_cmb.currentText()=="imports":
            self.main_widget.database_widget.imp_widget.import_csv(directory[0])
        if self.import_csv_cmb.currentText()=="Exports":
            self.main_widget.database_widget.exp_widget.import_csv(directory[0])
        if self.import_csv_cmb.currentText()=="Employees":
            self.main_widget.database_widget.emp_widget.import_csv(directory[0])



    def save_table(self,name,table):
        n_rows=table.rowCount()
        n_cols=table.columnCount()
        headers=[table.horizontalHeaderItem(i).text() for i in range(n_cols)]
        table_df=pd.DataFrame(columns = headers)
        flag=True
        for i in range(n_rows):
            row=[]
            if table.item(i, 0) is not None:
                for j in range(n_cols):
                    text=table.item(i,j).text()
                    row.append(text)
                a_series = pd.Series(row, index=table_df.columns)
                table_df = table_df.append(a_series, ignore_index=True)
        try:
            table_df.to_excel(os.path.join(self.dir_path, f"{name}_{str(datetime.date.today())}.xlsx"))
        except:
            count=0
            while(flag):
                print(count)
                try:
                    table_df.to_excel(os.path.join(self.dir_path,f"{name}_{str(datetime.date.today())}({count}).xlsx"))
                    flag=False
                except:
                    count+=1

    def set_layout(self):
        self.import_csv_ly = qtw.QVBoxLayout()
        self.export_csv_ly = qtw.QVBoxLayout()
        self.import_csv_ly.addWidget(self.import_csv_cmb)
        self.import_csv_ly.addWidget(self.import_csv_btn)
        self.export_csv_ly.addWidget(self.export_csv_cmb)
        self.export_csv_ly.addWidget(self.export_csv_btn)
        self.import_export_ly = qtw.QHBoxLayout()
        self.import_export_ly.addLayout(self.import_csv_ly)
        self.import_export_ly.addLayout(self.export_csv_ly)
        self.setLayout(self.import_export_ly)

