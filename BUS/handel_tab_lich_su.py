from PyQt6.QtCore import QCoreApplication,QUrl
from DAO import database_layer_sqlite
class handle_tab_lich_su:
    def __init__(self) -> None:
        self.data=database_layer_sqlite.DatabaseLayer()
    def load_history(self):
        default_date=''
        history=''
        data=self.data.get_history()
        default_date=data[0][0]
        sub_history=f'<p><span style=" font-size:13pt; font-weight:300;">{default_date}</span></p></br>'
        history+=sub_history
        for item in data:
            if item[0]!=default_date:
                default_date=item[0]
                sub_history=f'<p><span style=" font-size:13pt; font-weight:300;">{default_date}</span></p></br>'
                history+=sub_history
            history+=f'<p><span style=" font-size:16pt; font-weight:600;">{item[1]}</span></p></br>'
        return f"<html><head/><body>{history}</body></html>"
    
