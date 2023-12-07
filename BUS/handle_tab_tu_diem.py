from DAO import database_layer,database_layer_sqlite
from PyQt6.QtWidgets import QListWidget,QListWidgetItem
from PyQt6.QtGui import QStandardItemModel,QStandardItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QCoreApplication,QUrl
# from PyQt6 import QtCore, QtGui, QtWidgets

class handle_tab_tu_diem:
    def __init__(self) -> None:
        self.data_mysql=database_layer.database()
        self.data=database_layer_sqlite.DatabaseLayer()  
    def load_data_to_dic(self,list_view_tu_dien,):
        # data_tuple=self.data.execute_query(query)
        data_tuple=self.data.get_sign_name()
        # list_view=QListWidget()
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        for data  in data_tuple:
            item = QListWidgetItem(data[0])
            item.setFont(font)
            list_view_tu_dien.addItem(item)
        list_view_tu_dien.setCurrentRow(0)
        return list_view_tu_dien
    def change_text_lable_giai_thich(self,selected_item,lable_giai_thich,media_player):
        print(selected_item)
        _translate = QCoreApplication.translate
        data=self.data.get_link_and_sign_description(selected_item)
        description=''.join([f'<p><span style=\" font-size:16pt; font-weight:600;\">{item}.</span></p>' for item in str(data[0]).split('.')])
        lable_giai_thich.setText(_translate("Form", f"<html><head/><body>{description}</body></html>"))
        media_player.setSource(QUrl.fromLocalFile(f'./assets/videos/{data[1]}'))
        media_player.play()
        media_player.setLoops(10)
        return lable_giai_thich,media_player  
