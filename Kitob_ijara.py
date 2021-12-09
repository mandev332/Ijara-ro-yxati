import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3

Abdurahmon=sqlite3.connect("Kitob.db")
admin=Abdurahmon.cursor()

class Kitob(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.kutubxona()
    def kutubxona(self):
        
        admin.execute("create table if not exists royxat (knomi text)")
        Abdurahmon.commit()
        
        admin.execute("create table if not exists olindi (ismi text, klent text, tel text, sana1 text, sana2 text)")
        Abdurahmon.commit()
        
        self.nomi=QLineEdit(self)
        self.nomi.setGeometry(50, 50, 250, 40)
        self.nomi.setPlaceholderText("Kitob nomi")
        self.nomi.setFont(QFont("MC PGothic", 15))
        self.nomi.setStyleSheet("background-color: wheat; border: 3px solid green; border-radius: 12px;")
        self.setStyleSheet("background-color: silver")
        
        self.ism=QLineEdit(self)
        self.ism.setGeometry(325, 50, 250, 40)
        self.ism.setPlaceholderText("Kitobxon ismi")
        self.ism.setFont(QFont("MC PGothic", 15))
        self.ism.setStyleSheet("background-color: wheat; border: 3px solid green; border-radius: 12px;")
       
        self.tel=QLineEdit(self)
        self.tel.setGeometry(600, 50, 250, 40)
        self.tel.setPlaceholderText("Tel:")
        self.tel.setFont(QFont("MC PGothic", 15))
        self.tel.setStyleSheet("background-color: wheat; border: 3px solid green; border-radius: 12px;")
        
        self.lis1=QListWidget(self)
        self.lis1.setGeometry(50, 150, 250, 700)
        self.lis1.setFont(QFont("MC PGothic",15))
        self.lis1.setStyleSheet("background-color: wheat; border: 3px solid green; border-radius: 12px;")
        self.lis1.itemClicked.connect(self.chiq1)
        
        self.lis2=QListWidget(self)
        self.lis2.setGeometry(325, 150, 530, 700)
        self.lis2.setFont(QFont("MC PGothic",15))
        self.lis2.setStyleSheet("background-color: wheat; border: 3px solid green; border-radius: 12px;")
        self.lis2.itemClicked.connect(self.chiq2)
        
        self.qosh=QPushButton(self)
        self.qosh.setGeometry(50, 100, 110, 40)
        self.qosh.setFont(QFont("Arial",25))        
        self.qosh.setText("+")
        self.qosh.setStyleSheet("background-color: gray; border: 1px solid red; border-radius: 15px;")
        self.qosh.clicked.connect(self.qoshish)
        
        self.ayir=QPushButton(self)
        self.ayir.setGeometry(190, 100, 110, 40)
        self.ayir.setFont(QFont("Arial",25))        
        self.ayir.setText("-")
        self.ayir.setStyleSheet("background-color: gray; border: 1px solid red; border-radius: 15px;")
        self.ayir.clicked.connect(self.delete)
        
        self.qosh2=QPushButton(self)
        self.qosh2.setGeometry(325, 100, 110, 40)
        self.qosh2.setFont(QFont("Arial",25))        
        self.qosh2.setText("+")
        self.qosh2.setStyleSheet("background-color: gray; border: 1px solid red; border-radius: 15px;")
        self.qosh2.clicked.connect(self.qoshish2)
        
        self.tele=QPushButton(self)
        self.tele.setGeometry(735, 860, 120, 30)
        self.tele.setFont(QFont("Arial",10))        
        self.t=QGraphicsColorizeEffect()
        self.tele.setGraphicsEffect(self.t)
        self.tele.setText("Telegramm")
        self.tele.setStyleSheet("background-color: silver; border: 1px solid blue; border-radius: 5px;")
        self.tele.clicked.connect(self.telegram)
        
        self.sana1=QLineEdit(self)
        self.sana1.setGeometry(445, 100, 190, 40)
        self.sana1.setFont(QFont("Arial",15))        
        self.sana1.setPlaceholderText("berilgan sana")
        self.sana1.setStyleSheet("background-color: white; border: 1px solid red; border-radius: 15px;")
        
        
        self.sana2=QLineEdit(self)
        self.sana2.setGeometry(655, 100, 190, 40)
        self.sana2.setFont(QFont("Arial",15))        
        self.sana2.setPlaceholderText("deadline")
        self.sana2.setStyleSheet("background-color: white; border: 1px solid red; border-radius: 15px;")
        
        self.ishla()
        self.ishla2()
    def telegram(self):
        os.system("start https://t.me/kitob_ijara")
    def ishla(self):
        
        self.lis1.clear()
        admin.execute("select * from royxat")
        jami=admin.fetchall()
        for i in jami:
           self.lis1.insertItem(0,i[0])   
        self.nomi.setText("")  
        
    def ishla2(self):
        
        self.lis2.clear()
        admin.execute("select * from olindi")
        jami=admin.fetchall()
        for i in jami:
           self.lis2.insertItem(0,i[0]+" "+i[1]+" "+i[2])   
        self.nomi.setText("")  
        self.ism.setText("")  
        self.tel.setText("")  
        self.sana2.setText("")  
        self.sana1.setText("")  
        
    def chiq1(self):

        nom=self.lis1.currentItem().text()
        self.nomi.setText(nom)
        self.ism.setText("")  
        self.tel.setText("+998") 
        self.sana2.setText("")  
        self.sana1.setText("")  
        
    def chiq2(self):
        
        self.nomi.clear()
        self.ism.clear()
        self.tel.clear()
        nom=self.lis2.currentItem().text()
        kim=""
        for i in nom:
            if i==" ":
                break
            else:
                kim+=i
        admin.execute("select * from olindi where ismi=?",(kim,))
        kimda=admin.fetchall()
        self.nomi.setText(kimda[0][0])
        self.ism.setText(kimda[0][1])
        self.tel.setText(kimda[0][2])
        self.sana1.setText(kimda[0][3])
        self.sana2.setText(kimda[0][4])
        
    def qoshish(self):
        
        kn=self.nomi.text()
        admin.execute("select knomi from royxat")
        n=admin.fetchall()
        chek=0
        for i in range(len(n)):
            if kn in n[i][0]:
                chek+=1
        if chek==0:
            admin.execute("insert into royxat values(?)",(kn,))
            Abdurahmon.commit()
            self.delete2()
            self.ishla()
        else:
            xabar=QMessageBox()
            xabar.setText(f"{kn} kitobi bor!")
            xabar.setIcon(QMessageBox.Warning)
            xabar.setWindowTitle("ERROR")
            xabar.exec_()
            
    def qoshish2(self):
        
        kn=self.nomi.text()
        ki=self.ism.text()
        kt=self.tel.text()
        s1=self.sana1.text()
        s2=self.sana2.text()
        admin.execute("select ismi from olindi")
        n=admin.fetchall()
        chek=0
        for i in range(len(n)):
            if kn in n[i][0]:
                chek+=1
        if chek==0 and self.ism.text() and self.tel.text() and self.sana1.text() and self.sana2.text():
            admin.execute("insert into olindi values(?,?,?,?,?)",(kn,ki,kt,s1,s2))
            Abdurahmon.commit()
            self.delete()
            self.ishla2()
        elif chek==1:
            xabar=QMessageBox()
            xabar.setText("Qayta kiritayapsiz!")
            xabar.setIcon(QMessageBox.Information)
            xabar.setWindowTitle("ERROR")
            xabar.exec_()
        else:
            xabar=QMessageBox()
            xabar.setText("Malumot kiritishingiz kerak!")
            xabar.setIcon(QMessageBox.Warning)
            xabar.setWindowTitle("ERROR")
            xabar.exec_()
        
    def delete(self):
       
        kn=self.nomi.text()
        admin.execute("delete from royxat where knomi=?",(kn,))
        Abdurahmon.commit()
        self.ishla()
        
    def delete2(self):
       
        kn=self.nomi.text()
        admin.execute("delete from olindi where ismi=?",(kn,))
        Abdurahmon.commit()
        self.ishla2()
                
book=QApplication(sys.argv)
man=Kitob()
man.setGeometry(200, 100, 900, 900)
man.setFixedSize(900, 900)
man.setWindowTitle("Kitob ijara")
man.show()
sys.exit(book.exec_())