# from sign_recognition import recogintion
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
# QtCore, QtGui, 
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget 
from BUS import handle_tab_tu_diem,handel_tab_lich_su
from BUS import sign_recognition 

class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(1271, 704)
        self.handle_dic=handle_tab_tu_diem.handle_tab_tu_diem()
        self.handel_tab_lich_su=handel_tab_lich_su.handle_tab_lich_su()
        self.sign_recogintion=sign_recognition.recogintion()
        self.widget = QWidget(parent=Form)
        self.widget.setGeometry(QRect(0, 0, 1301, 71))
        self.widget.setObjectName("widget")
        self.logoImage = QLabel(parent=self.widget)
        self.logoImage.setGeometry(QRect(0, 0, 351, 71))
        self.logoImage.setObjectName("logoImage")
       
        self.btn_dich = QPushButton(parent=self.widget)
        self.btn_dich.setGeometry(QRect(400, 20, 171, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dich.setFont(font)
        self.btn_dich.setObjectName("btn_dich")
        self.btn_tu_dien = QPushButton(parent=self.widget)
        self.btn_tu_dien.setGeometry(QRect(580, 20, 171, 41))
        self.btn_tu_dien.setFont(font)
        self.btn_tu_dien.setObjectName("btn_tu_dien")
        
        self.btn_lich_su = QPushButton(parent=self.widget)
        self.btn_lich_su.setGeometry(QRect(760, 20, 171, 41))
        self.btn_lich_su.setFont(font)
        self.btn_lich_su.setObjectName("btn_lich_su")
        
        self.horizontalLayoutWidget = QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QRect(0, 639, 1301, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QWidget(parent=self.horizontalLayoutWidget)
        self.widget_5.setStyleSheet("\n"
"background-color: rgb(46, 67, 115);")
        self.widget_5.setObjectName("widget_5")
        self.label_2 = QLabel(parent=self.widget_5)
        self.label_2.setGeometry(QRect(180, 20, 31, 31))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_2 = QWidget(parent=self.horizontalLayoutWidget)
        self.widget_2.setStyleSheet("\n"
"background-color: rgb(0, 135, 187);")
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QLabel(parent=self.widget_2)
        self.label_4.setGeometry(QRect(210, 20, 31, 31))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_4 = QWidget(parent=self.horizontalLayoutWidget)
        self.widget_4.setStyleSheet("\n"
"background-color: rgb(1, 111, 178);")
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QLabel(parent=self.widget_4)
        self.label_3.setGeometry(QRect(210, 20, 31, 31))
        self.label_3.setText('asdasdas')
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.widget_4)
        self.tabWidget = QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QRect(0, 80, 1281, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_dich = QWidget()
        self.tab_dich.setObjectName("tab_dich")
        self.video_dich = QLabel(parent=self.tab_dich)
        self.video_dich.setGeometry(QRect(739, 0, 531, 491))
        self.video_dich.setStyleSheet("background-color: rgb(255, 206, 206);")
        self.video_dich.setObjectName("video_dich")
        self.btn_dich_tu = QPushButton(parent=self.tab_dich)
        self.btn_dich_tu.setGeometry(QRect(740, 490, 531, 41))
        self.label_dich = QLabel(parent=self.tab_dich)
        self.label_dich.setObjectName("label_dich")
        self.label_dich.setGeometry(QRect(0, 0, 741, 521))
        self.label_dich.setFont(font)
        self.label_dich.setStyleSheet("background-color:  rgb(228, 228, 228);")
        self.label_dich.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_dich.setMargin(20)
        
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dich_tu.setFont(font)
        self.btn_dich_tu.setObjectName("btn_dich_tu")
        self.btn_dich.setStyleSheet("\n"
"background-color: rgb(100, 149, 237);")
        self.tabWidget.addTab(self.tab_dich, "")
        self.tab_tu_dien = QWidget()
        self.tab_tu_dien.setObjectName("tab_tu_dien")
        self.list_view_tu_dien = QListWidget(parent=self.tab_tu_dien)
        self.list_view_tu_dien.setGeometry(QRect(0, 40, 221, 491))
        self.list_view_tu_dien.setStyleSheet("color: rgb(114, 114, 114);\n"
"background-color: rgb(195, 195, 195);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(114, 114, 114);\n"
"")
        self.mediaPlayer = QMediaPlayer()
        self.list_view_tu_dien.setObjectName("list_view_tu_dien")

        self.video = QVideoWidget(parent=self.tab_tu_dien)
        self.mediaPlayer.setVideoOutput(self.video)
        self.mediaPlayer.setSource(QUrl.fromLocalFile('./assets/videos/W00042.webm'))
        
        self.mediaPlayer.setLoops(10)
        self.video.setGeometry(QRect(800, 40, 471, 441))
        self.video.setStyleSheet("background-color: rgb(0, 0, 127);")
        # self.video.setText("")
        self.video.setObjectName("video")
        self.lable_ten_hanh_dong = QLabel(parent=self.tab_tu_dien)
        self.lable_ten_hanh_dong.setGeometry(QRect(800, 480, 471, 41))
        self.lable_ten_hanh_dong.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lable_ten_hanh_dong.setObjectName("lable_ten_hanh_dong")
        self.lable_giai_thich = QLabel(parent=self.tab_tu_dien)
        self.lable_giai_thich.setGeometry(QRect(220, 40, 581, 481))
        self.lable_giai_thich.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.lable_giai_thich.setObjectName("lable_giai_thich")
        self.lable_giai_thich.setWordWrap(True)
        self.btn_tim_kiem = QTextEdit(parent=self.tab_tu_dien)
        self.btn_tim_kiem.setGeometry(QRect(400, 0, 531, 31))
        self.btn_tim_kiem.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.btn_tim_kiem.setAutoFillBackground(False)
        self.btn_tim_kiem.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);")
        self.btn_tim_kiem.setLocale(QLocale(QLocale.Language.Vietnamese, QLocale.Country.Vietnam))
        self.btn_tim_kiem.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhMultiLine)
        self.btn_tim_kiem.setObjectName("btn_tim_kiem")
        self.tabWidget.addTab(self.tab_tu_dien, "")
        self.tab_lich_su = QWidget()
        self.tab_lich_su.setObjectName("tab_lich_su")
        self.label_lich_su=QLabel(parent=self.tab_lich_su)
        self.label_lich_su.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_lich_su.setWordWrap(True)       
        self.label_lich_su.setGeometry(QRect(0, 0, 1271, 521))
        self.label_lich_su.setMargin(20)
        self.scroll_area_lich_su = QScrollArea(parent=self.tab_lich_su)
        self.scroll_area_lich_su.setWidget(self.label_lich_su)
        self.scroll_area_lich_su.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area_lich_su.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area_lich_su.setGeometry(QRect(0, 0, 1271, 521))
        self.scroll_area_lich_su.setObjectName("scroll_area_lich_su")
        # self.scroll_area_lich_su.
        self.btn_lich_su.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")

        self.btn_tu_dien.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")

        self.tabWidget.addTab(self.tab_lich_su, "")
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(Form)
        self.label_dich_text=[]
        self.text=''
    def retranslateUi(self, Form):
        self.is_click=False
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logoImage.setText(_translate("Form", "<html><head/><body><p><img src=\"assets\images\logo.png\"/></p></body></html>"))
        self.btn_dich.setText(_translate("Form", "Dịch"))
        self.btn_tu_dien.setText(_translate("Form", "Từ điển"))
        self.btn_lich_su.setText(_translate("Form", "Lịch sử"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_dich_tu.setText(_translate("Form", "DỊCH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dich), _translate("Form", "Dịch"))
        __sortingEnabled = self.list_view_tu_dien.isSortingEnabled()
        self.list_view_tu_dien.setSortingEnabled(False)
        self.list_view_tu_dien=self.handle_dic.load_data_to_dic(self.list_view_tu_dien)
        self.lable_ten_hanh_dong.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Cha</span></p></body></html>"))
        self.lable_giai_thich.setText(_translate("Form", '<html><head/><body><p><span style=" font-size:16pt; font-weight:600;">Chụm 5 đầu ngón tay của một bàn tay lại và đặt lên môi đang mím.</span></p><p><span style=" font-size:16pt; font-weight:600;"> Đưa tay ra xa khỏi miệng rồi đặt lên môi lần nữa.</span></p></body></html>'))
        self.btn_tim_kiem.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">search</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tu_dien), _translate("Form", "Từ điển"))
        self.text_lich_su=self.handel_tab_lich_su.load_history()
        self.label_lich_su.setText(_translate("From",f'{self.text_lich_su}'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lich_su), _translate("Form", "Lịch sử"))
        self.btn_dich_tu.clicked.connect(self.dich)
        self.btn_dich.clicked.connect(lambda:self.change_tab(0))
        self.btn_tu_dien.clicked.connect(lambda:self.change_tab(1))
        self.btn_lich_su.clicked.connect(lambda:self.change_tab(2))
        self.list_view_tu_dien.currentItemChanged.connect(self.change_text_lable_giai_thich)
        
        self.label_dich.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\"></span></p></body></html>", None))
    def change_tab(self,index):
        if index==0:
                    self.btn_dich.setStyleSheet("\n"
"background-color: rgb(100, 149, 237);")
                    self.btn_lich_su.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")
                    self.btn_tu_dien.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")
                    self.mediaPlayer.stop()
                    
        if index==1:
                    self.btn_tu_dien.setStyleSheet("\n"
"background-color: rgb(100, 149, 237);")
                    self.btn_lich_su.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")
                    self.btn_dich.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")
                    self.mediaPlayer.play()
        if index==2:
                    self.btn_lich_su.setStyleSheet("\n"
"background-color: rgb(100, 149, 237);")
                    self.btn_tu_dien.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")
                    self.btn_dich.setStyleSheet("\n"
"background-color: rgb(173, 216, 230);")
                    self.mediaPlayer.stop()
                    
        if(self.tabWidget.currentIndex()!=index):
            self.tabWidget.setCurrentIndex(index)
    def dich(self):
            if self.is_click==False:
                    self.sign_recogintion.start()
                    self.sign_recogintion.image_update.connect(self.ImageUpdateSlot)
                    self.sign_recogintion.text_change.connect(self.text_change)
                    self.is_click==True
            else:
                    self.sign_recogintion.start()
                    self.is_click==False
    def text_change(self,text):
        if self.text!=text:
                self.text=text
                if len(self.label_dich_text)>=15:
                        del self.label_dich_text[0]
                        
                text=f'<span style=\" font-size:16pt; font-weight:600;\">{text}</span><br>'
                self.label_dich_text.append(text),
                # self.text_lich_su+=text
                self.label_dich.setText(QCoreApplication.translate("Form", f"<html><head/><body><p>{''.join(self.label_dich_text)}</span></p></body></html>", None))
                self.text_lich_su=''.join([self.text_lich_su[0:self.text_lich_su.rfind('</body>')],text ,self.text_lich_su[self.text_lich_su.rfind('</body>'):-1],])
                self.label_lich_su.setText(QCoreApplication.translate("Form", f"<html><head/><body><p>{self.text_lich_su}</span></p></body></html>", None))
    def change_text_lable_giai_thich(self):
        self.lable_giai_thich,self.mediaPlayer=self.handle_dic.change_text_lable_giai_thich(self.list_view_tu_dien.currentItem().text(),self.lable_giai_thich,self.mediaPlayer)
    def ImageUpdateSlot(self, Image):
        self.video_dich.setPixmap(QPixmap.fromImage(Image))           
def run_app():
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
