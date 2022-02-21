import random
from random import randint
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import sys
import os
import webbrowser
import icons_rc
from PyQt5 import Qt, QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import QPropertyAnimation,QDate
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import  QDialog,QDateEdit,QHeaderView,QComboBox,QApplication, QMessageBox, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip,QFileDialog,QLineEdit
from PyQt5.uic import loadUi
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(
    user='root', 
    password='india123abcd$',
    host='127.0.0.1',
    database='hotel_management')

cursor = conn.cursor()


class Restaurant(QDialog):
    def __init__(self):
        super(Restaurant,self).__init__()
        loadUi("restaurant.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #global b,c
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        ######### Starters##############333333
        self.plus_1.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_1.clicked.connect(lambda : self.goto_plus1())
        self.minus_1.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_1.clicked.connect(lambda : self.goto_minus1())

        self.plus_2.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_2.clicked.connect(lambda : self.goto_plus2())
        self.minus_2.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_2.clicked.connect(lambda : self.goto_minus2())

        self.plus_3.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_3.clicked.connect(lambda : self.goto_plus3())
        self.minus_3.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_3.clicked.connect(lambda : self.goto_minus3())

        self.plus_4.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_4.clicked.connect(lambda : self.goto_plus4())
        self.minus_4.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_4.clicked.connect(lambda : self.goto_minus4())

        self.plus_5.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_5.clicked.connect(lambda : self.goto_plus5())
        self.minus_5.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_5.clicked.connect(lambda : self.goto_minus5())

        self.plus_6.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_6.clicked.connect(lambda : self.goto_plus6())
        self.minus_6.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_6.clicked.connect(lambda : self.goto_minus6())

        ######## Classic Vegetarian Dishes #########################

        self.plus_7.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_7.clicked.connect(lambda : self.goto_plus7())
        self.minus_7.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_7.clicked.connect(lambda : self.goto_minus7())

        self.plus_8.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_8.clicked.connect(lambda : self.goto_plus8())
        self.minus_8.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_8.clicked.connect(lambda : self.goto_minus8())

        self.plus_9.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_9.clicked.connect(lambda : self.goto_plus9())
        self.minus_9.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_9.clicked.connect(lambda : self.goto_minus9())

        self.plus_10.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_10.clicked.connect(lambda : self.goto_plus10())
        self.minus_10.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_10.clicked.connect(lambda : self.goto_minus10())

        self.plus_11.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_11.clicked.connect(lambda : self.goto_plus11())
        self.minus_11.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_11.clicked.connect(lambda : self.goto_minus11())

        self.plus_12.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_12.clicked.connect(lambda : self.goto_plus12())
        self.minus_12.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_12.clicked.connect(lambda : self.goto_minus12())

        ########### Salads ##################

        self.plus_13.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_13.clicked.connect(lambda : self.goto_plus13())
        self.minus_13.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_13.clicked.connect(lambda : self.goto_minus13())

        self.plus_14.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_14.clicked.connect(lambda : self.goto_plus14())
        self.minus_14.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_14.clicked.connect(lambda : self.goto_minus14())

        self.plus_15.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_15.clicked.connect(lambda : self.goto_plus15())
        self.minus_15.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_15.clicked.connect(lambda : self.goto_minus15())

        self.plus_16.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_16.clicked.connect(lambda : self.goto_plus16())
        self.minus_16.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_16.clicked.connect(lambda : self.goto_minus16())

        self.plus_17.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_17.clicked.connect(lambda : self.goto_plus17())
        self.minus_17.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_17.clicked.connect(lambda : self.goto_minus17())

        self.plus_18.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_18.clicked.connect(lambda : self.goto_plus18())
        self.minus_18.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_18.clicked.connect(lambda : self.goto_minus18())

        ########### DESERTS #########################################

        self.plus_19.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_19.clicked.connect(lambda : self.goto_plus19())
        self.minus_19.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_19.clicked.connect(lambda : self.goto_minus19())

        self.plus_20.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_20.clicked.connect(lambda : self.goto_plus20())
        self.minus_20.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_20.clicked.connect(lambda : self.goto_minus20())

        self.plus_21.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_21.clicked.connect(lambda : self.goto_plus21())
        self.minus_21.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_21.clicked.connect(lambda : self.goto_minus21())

        self.plus_22.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_22.clicked.connect(lambda : self.goto_plus22())
        self.minus_22.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_22.clicked.connect(lambda : self.goto_minus22())

        self.plus_23.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_23.clicked.connect(lambda : self.goto_plus23())
        self.minus_23.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_23.clicked.connect(lambda : self.goto_minus23())

        self.plus_24.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_24.clicked.connect(lambda : self.goto_plus24())
        self.minus_24.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_24.clicked.connect(lambda : self.goto_minus24())

        ############ Tandoori Breads ######################

        self.plus_25.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_25.clicked.connect(lambda : self.goto_plus25())
        self.minus_25.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_25.clicked.connect(lambda : self.goto_minus25())

        self.plus_26.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_26.clicked.connect(lambda : self.goto_plus26())
        self.minus_26.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_26.clicked.connect(lambda : self.goto_minus26())

        self.plus_27.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_27.clicked.connect(lambda : self.goto_plus27())
        self.minus_27.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_27.clicked.connect(lambda : self.goto_minus27())

        self.plus_28.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_28.clicked.connect(lambda : self.goto_plus28())
        self.minus_28.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_28.clicked.connect(lambda : self.goto_minus28())

        self.plus_29.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_29.clicked.connect(lambda : self.goto_plus29())
        self.minus_29.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_29.clicked.connect(lambda : self.goto_minus29())

        self.plus_30.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_30.clicked.connect(lambda : self.goto_plus30())
        self.minus_30.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_30.clicked.connect(lambda : self.goto_minus30())

        ########### Ice Creams ############

        self.plus_31.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_31.clicked.connect(lambda : self.goto_plus31())
        self.minus_31.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_31.clicked.connect(lambda : self.goto_minus31())

        self.plus_32.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_32.clicked.connect(lambda : self.goto_plus32())
        self.minus_32.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_32.clicked.connect(lambda : self.goto_minus32())

        self.plus_33.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_33.clicked.connect(lambda : self.goto_plus33())
        self.minus_33.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_33.clicked.connect(lambda : self.goto_minus33())

        self.plus_34.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_34.clicked.connect(lambda : self.goto_plus34())
        self.minus_34.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_34.clicked.connect(lambda : self.goto_minus34())

        self.plus_35.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_35.clicked.connect(lambda : self.goto_plus35())
        self.minus_35.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_35.clicked.connect(lambda : self.goto_minus35())

        self.plus_36.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_36.clicked.connect(lambda : self.goto_plus36())
        self.minus_36.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_36.clicked.connect(lambda : self.goto_minus36())

        ############## Beverages #######################

        self.plus_37.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_37.clicked.connect(lambda : self.goto_plus37())
        self.minus_37.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_37.clicked.connect(lambda : self.goto_minus37())

        self.plus_38.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_38.clicked.connect(lambda : self.goto_plus38())
        self.minus_38.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_38.clicked.connect(lambda : self.goto_minus38())

        self.plus_39.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_39.clicked.connect(lambda : self.goto_plus39())
        self.minus_39.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_39.clicked.connect(lambda : self.goto_minus39())

        self.plus_40.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_40.clicked.connect(lambda : self.goto_plus40())
        self.minus_40.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_40.clicked.connect(lambda : self.goto_minus40())

        self.plus_41.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_41.clicked.connect(lambda : self.goto_plus41())
        self.minus_41.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_41.clicked.connect(lambda : self.goto_minus41())
        
        self.plus_42.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\plus-square.svg"))
        self.plus_42.clicked.connect(lambda : self.goto_plus42())
        self.minus_42.setIcon(QtGui.QIcon(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\icons\minus-square.svg"))
        self.minus_42.clicked.connect(lambda : self.goto_minus42())

        ########### Order Buttons#######
        self.order1.clicked.connect(self.goto_order1)
        self.order2.clicked.connect(self.goto_order2)
        self.order3.clicked.connect(self.goto_order3)
        self.order4.clicked.connect(self.goto_order4)
        self.order5.clicked.connect(self.goto_order5)
        self.order6.clicked.connect(self.goto_order6)
        self.order7.clicked.connect(self.goto_order7)
        self.order8.clicked.connect(self.goto_order8)
        self.order9.clicked.connect(self.goto_order9)
        self.order10.clicked.connect(self.goto_order10)
        self.order11.clicked.connect(self.goto_order11)
        self.order12.clicked.connect(self.goto_order12)
        self.order13.clicked.connect(self.goto_order13)
        self.order14.clicked.connect(self.goto_order14)
        self.order15.clicked.connect(self.goto_order15)
        self.order16.clicked.connect(self.goto_order16)
        self.order17.clicked.connect(self.goto_order17)
        self.order18.clicked.connect(self.goto_order18)
        self.order19.clicked.connect(self.goto_order19)
        self.order20.clicked.connect(self.goto_order20)
        self.order21.clicked.connect(self.goto_order21)
        self.order22.clicked.connect(self.goto_order22)
        self.order23.clicked.connect(self.goto_order23)
        self.order24.clicked.connect(self.goto_order24)
        self.order25.clicked.connect(self.goto_order25)
        self.order26.clicked.connect(self.goto_order26)
        self.order27.clicked.connect(self.goto_order27)
        self.order28.clicked.connect(self.goto_order28)
        self.order29.clicked.connect(self.goto_order29)
        self.order30.clicked.connect(self.goto_order30)
        self.order31.clicked.connect(self.goto_order31)
        self.order32.clicked.connect(self.goto_order32)
        self.order33.clicked.connect(self.goto_order33)
        self.order34.clicked.connect(self.goto_order34)
        self.order35.clicked.connect(self.goto_order35)
        self.order36.clicked.connect(self.goto_order36)
        self.order37.clicked.connect(self.goto_order37)
        self.order38.clicked.connect(self.goto_order38)
        self.order39.clicked.connect(self.goto_order39)
        self.order40.clicked.connect(self.goto_order40)
        self.order41.clicked.connect(self.goto_order41)
        self.order42.clicked.connect(self.goto_order42)
        self.generate_bill.clicked.connect(self.goto_generate_bill)
        self.generate_bill_btn.clicked.connect(self.goto_generate_bill_btn)
        self.allotbtn.clicked.connect(self.allot_billno)
        self.sendbill.clicked.connect(self.send_bill)

    def goto_generate_bill_btn(self):
        a=str(self.billno.text())+'.txt'
        billfile=r'C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\Bills'+'/' +a
        webbrowser.open(billfile)

		
    def goto_plus1(self):
        global a
        a+=1
        self.id1.setText(str(a))

    def goto_minus1(self):
        global a
        if a==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            a-=1
        self.id1.setText(str(a))

    def goto_plus2(self):
        global b
        b+=1
        self.id2.setText(str(b))

    def goto_minus2(self):
        global b
        if b==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            b-=1
        self.id2.setText(str(b))

    def goto_plus3(self):
        global c
        c+=1
        self.id3.setText(str(c))

    def goto_minus3(self):
        global c
        if c==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            c-=1
        self.id3.setText(str(c))

    def goto_plus4(self):
        global d
        d+=1
        self.id4.setText(str(d))

    def goto_minus4(self):
        global d
        if d==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            d-=1
        self.id4.setText(str(d))

    def goto_plus5(self):
        global e
        e+=1
        self.id5.setText(str(e))

    def goto_minus5(self):
        global e
        if e==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            e-=1
        self.id5.setText(str(e))

    def goto_plus6(self):
        global f
        f+=1
        self.id6.setText(str(f))

    def goto_minus6(self):
        global f
        if f==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            f-=1
        self.id6.setText(str(f))

    def goto_plus7(self):
        global g
        g+=1
        self.id7.setText(str(g))

    def goto_minus7(self):
        global g
        if g==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            g-=1
        self.id7.setText(str(g))

    def goto_plus8(self):
        global h
        h+=1
        self.id8.setText(str(h))

    def goto_minus8(self):
        global h
        if h==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            h-=1
        self.id8.setText(str(h))

    def goto_plus9(self):
        global i
        i+=1
        self.id9.setText(str(i))

    def goto_minus9(self):
        global i
        if i==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            i-=1
        self.id9.setText(str(i))

    def goto_plus10(self):
        global j
        j+=1
        self.id10.setText(str(j))

    def goto_minus10(self):
        global j
        if j==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            j-=1
        self.id10.setText(str(j))

    def goto_plus11(self):
        global k
        k+=1
        self.id11.setText(str(k))

    def goto_minus11(self):
        global k
        if k==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            k-=1
        self.id11.setText(str(k))

    def goto_plus12(self):
        global l
        l+=1
        self.id12.setText(str(l))

    def goto_minus12(self):
        global l
        if l==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            l-=1
        self.id12.setText(str(l))

    def goto_plus13(self):
        global m
        m+=1
        self.id13.setText(str(m))

    def goto_minus13(self):
        global m
        if m==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            m-=1
        self.id13.setText(str(m))

    def goto_plus14(self):
        global n
        n+=1
        self.id14.setText(str(n))

    def goto_minus14(self):
        global n
        if n==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            n-=1
        self.id14.setText(str(n))

    def goto_plus15(self):
        global o
        o+=1
        self.id15.setText(str(o))

    def goto_minus15(self):
        global o
        if o==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            o-=1
        self.id15.setText(str(o))

    def goto_plus16(self):
        global p
        p+=1
        self.id16.setText(str(p))

    def goto_minus16(self):
        global p
        if p==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            p-=1
        self.id16.setText(str(p))

    def goto_plus17(self):
        global q
        q+=1
        self.id17.setText(str(q))

    def goto_minus17(self):
        global q
        if q==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            q-=1
        self.id17.setText(str(q))

    def goto_plus18(self):
        global r
        r+=1
        self.id18.setText(str(r))

    def goto_minus18(self):
        global r
        if r==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            r-=1
        self.id18.setText(str(r))

    def goto_plus19(self):
        global s
        s+=1
        self.id19.setText(str(s))

    def goto_minus19(self):
        global s
        if s==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            s-=1
        self.id19.setText(str(s))

    def goto_plus20(self):
        global t
        t+=1
        self.id20.setText(str(t))

    def goto_minus20(self):
        global t
        if t==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            t-=1
        self.id20.setText(str(t))

    def goto_plus21(self):
        global u
        u+=1
        self.id21.setText(str(u))

    def goto_minus21(self):
        global u
        if u==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            u-=1
        self.id21.setText(str(u))

    def goto_plus22(self):
        global v
        v+=1
        self.id22.setText(str(v))

    def goto_minus22(self):
        global v
        if v==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            v-=1
        self.id22.setText(str(v))

    def goto_plus23(self):
        global w
        w+=1
        self.id23.setText(str(w))

    def goto_minus23(self):
        global w
        if w==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            w-=1
        self.id23.setText(str(w))

    def goto_plus24(self):
        global x
        x+=1
        self.id24.setText(str(x))

    def goto_minus24(self):
        global x
        if x==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            x-=1
        self.id24.setText(str(x))

    def goto_plus25(self):
        global y
        y+=1
        self.id25.setText(str(y))

    def goto_minus25(self):
        global y
        if y==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            y-=1
        self.id25.setText(str(y))

    def goto_plus26(self):
        global z
        z+=1
        self.id26.setText(str(z))

    def goto_minus26(self):
        global z
        if z==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            z-=1
        self.id26.setText(str(z))

    def goto_plus27(self):
        global b1
        b1+=1
        self.id27.setText(str(b1))

    def goto_minus27(self):
        global b1
        if b1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            b1-=1
        self.id27.setText(str(b1))

    def goto_plus28(self):
        global c1
        c1+=1
        self.id28.setText(str(c1))

    def goto_minus28(self):
        global c1
        if c1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            c1-=1
        self.id28.setText(str(c1))

    def goto_plus29(self):
        global d1
        d1+=1
        self.id29.setText(str(d1))

    def goto_minus29(self):
        global d1
        if d1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            d1-=1
        self.id29.setText(str(d1))

    def goto_plus30(self):
        global e1
        e1+=1
        self.id30.setText(str(e1))

    def goto_minus30(self):
        global e1
        if e1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            e1-=1
        self.id30.setText(str(e1))

    def goto_plus31(self):
        global f1
        f1+=1
        self.id31.setText(str(f1))

    def goto_minus31(self):
        global f1
        if f1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            f1-=1
        self.id31.setText(str(f1))

    def goto_plus32(self):
        global g1
        g1+=1
        self.id32.setText(str(g1))

    def goto_minus32(self):
        global g1
        if g1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            g1-=1
        self.id32.setText(str(g1))

    def goto_plus33(self):
        global h1
        h1+=1
        self.id33.setText(str(h1))

    def goto_minus33(self):
        global h1
        if h1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            h1-=1
        self.id33.setText(str(h1))

    def goto_plus34(self):
        global i1
        i1+=1
        self.id34.setText(str(i1))

    def goto_minus34(self):
        global i1
        if i1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            i1-=1
        self.id34.setText(str(i1))

    def goto_plus35(self):
        global j1
        j1+=1
        self.id35.setText(str(j1))

    def goto_minus35(self):
        global j1
        if j1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            j1-=1
        self.id35.setText(str(j1))

    def goto_plus36(self):
        global k1
        k1+=1
        self.id36.setText(str(k1))

    def goto_minus36(self):
        global k1
        if k1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            k1-=1
        self.id36.setText(str(k1))

    def goto_plus37(self):
        global l1
        l1+=1
        self.id37.setText(str(l1))

    def goto_minus37(self):
        global l1
        if l1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            l1-=1
        self.id37.setText(str(l1))

    def goto_plus38(self):
        global m1
        m1+=1
        self.id38.setText(str(m1))

    def goto_minus38(self):
        global m1
        if m1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            m1-=1
        self.id38.setText(str(m1))

    def goto_plus39(self):
        global n1
        n1+=1
        self.id39.setText(str(n1))

    def goto_minus39(self):
        global n1
        if n1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            n1-=1
        self.id39.setText(str(n1))

    def goto_plus40(self):
        global o1
        o1+=1
        self.id40.setText(str(o1))

    def goto_minus40(self):
        global o1
        if o1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            o1-=1
        self.id40.setText(str(o1))

    def goto_plus41(self):
        global p1
        p1+=1
        self.id41.setText(str(p1))

    def goto_minus41(self):
        global p1
        if p1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            p1-=1
        self.id41.setText(str(p1))

    def goto_plus42(self):
        global q1
        q1+=1
        self.id42.setText(str(q1))

    def goto_minus42(self):
        global q1
        if q1==0:
            QMessageBox.critical(self," ","Invalid ")
        else:
            q1-=1
        self.id42.setText(str(q1))

    def goto_order(self):
        global a
        with open('test.txt', 'w') as f:
            f.write(str(a))
            print(str(self.l1.text()))
            a=str(self.l1.text())
            print(int(a)*3)
    
    def goto_order1(self):
        global item1
        price1=str(self.l1.text())
        quantity1=str(self.id1.text())
        item1=int(price1)*int(quantity1)
        self.t1.setText(str(item1))
        #print(item1)

    def goto_order2(self):
        global item2
        price2=str(self.l2.text())
        quantity2=str(self.id2.text())
        item2=int(price2)*int(quantity2)
        self.t2.setText(str(item2))
        #print(item2)

    def goto_order3(self):
        global item3
        price3=str(self.l3.text())
        quantity3=str(self.id3.text())
        item3=int(price3)*int(quantity3)
        self.t3.setText(str(item3))
        #print(item3)

    def goto_order4(self):
        global item4
        price4=str(self.l4.text())
        quantity4=str(self.id4.text())
        item4=int(price4)*int(quantity4)
        self.t4.setText(str(item4))
        #print(item4)

    def goto_order5(self):
        global item5
        price5=str(self.l5.text())
        quantity5=str(self.id5.text())
        item5=int(price5)*int(quantity5)
        self.t5.setText(str(item5))
        #print(item5)

    def goto_order6(self):
        global item6
        price6=str(self.l6.text())
        quantity6=str(self.id6.text())
        item6=int(price6)*int(quantity6)
        self.t6.setText(str(item6))
        #print(item6)

    ###################################################################

    def goto_order7(self):
        global item7
        price7=str(self.l7.text())
        quantity7=str(self.id7.text())
        item7=int(price7)*int(quantity7)
        self.t7.setText(str(item7))
        #print(item7)

    def goto_order8(self):
        global item8
        price8=str(self.l8.text())
        quantity8=str(self.id8.text())
        item8=int(price8)*int(quantity8)
        self.t8.setText(str(item8))
        #print(item8)

    def goto_order9(self):
        global item9
        price9=str(self.l9.text())
        quantity9=str(self.id9.text())
        item9=int(price9)*int(quantity9)
        self.t9.setText(str(item9))
        #print(item9)

    def goto_order10(self):
        global item10
        price10=str(self.l10.text())
        quantity10=str(self.id10.text())
        item10=int(price10)*int(quantity10)
        self.t10.setText(str(item10))
        #print(item10)

    def goto_order11(self):
        global item11
        price11=str(self.l11.text())
        quantity11=str(self.id11.text())
        item11=int(price11)*int(quantity11)
        self.t11.setText(str(item11))
        #print(item11)

    def goto_order12(self):
        global item12
        price12=str(self.l12.text())
        quantity12=str(self.id12.text())
        item12=int(price12)*int(quantity12)
        self.t12.setText(str(item12))
        #print(item12)

    def goto_order13(self):
        global item13
        price13=str(self.l13.text())
        quantity13=str(self.id13.text())
        item13=int(price13)*int(quantity13)
        self.t13.setText(str(item13))
        #print(item13)

    def goto_order14(self):
        global item14
        price14=str(self.l14.text())
        quantity14=str(self.id14.text())
        item14=int(price14)*int(quantity14)
        self.t14.setText(str(item14))
        #print(item14)

    def goto_order15(self):
        global item15
        price15=str(self.l15.text())
        quantity15=str(self.id15.text())
        item15=int(price15)*int(quantity15)
        self.t15.setText(str(item15))
        #print(item15)

    def goto_order16(self):
        global item16
        price16=str(self.l16.text())
        quantity16=str(self.id16.text())
        item16=int(price16)*int(quantity16)
        self.t16.setText(str(item16))
        #print(item16)

    def goto_order17(self):
        global item17
        price17=str(self.l17.text())
        quantity17=str(self.id17.text())
        item17=int(price17)*int(quantity17)
        self.t17.setText(str(item17))
        #print(item17)

    def goto_order18(self):
        global item18
        price18=str(self.l18.text())
        quantity18=str(self.id18.text())
        item18=int(price18)*int(quantity18)
        self.t18.setText(str(item18))
        #print(item18)

    ###################################################################

    def goto_order19(self):
        global item19
        price19=str(self.l19.text())
        quantity19=str(self.id19.text())
        item19=int(price19)*int(quantity19)
        self.t19.setText(str(item19))
        #print(item19)

    def goto_order20(self):
        global item20
        price20=str(self.l20.text())
        quantity20=str(self.id20.text())
        item20=int(price20)*int(quantity20)
        self.t20.setText(str(item20))
        #print(item20)

    def goto_order21(self):
        global item21
        price21=str(self.l21.text())
        quantity21=str(self.id21.text())
        item21=int(price21)*int(quantity21)
        self.t21.setText(str(item21))
        #print(item21)

    def goto_order22(self):
        global item22
        price22=str(self.l22.text())
        quantity22=str(self.id22.text())
        item22=int(price22)*int(quantity22)
        self.t22.setText(str(item22))
        #print(item22)

    def goto_order23(self):
        global item23
        price23=str(self.l23.text())
        quantity23=str(self.id23.text())
        item23=int(price23)*int(quantity23)
        self.t23.setText(str(item23))
        #print(item23)

    def goto_order24(self):
        global item24
        price24=str(self.l24.text())
        quantity24=str(self.id24.text())
        item24=int(price24)*int(quantity24)
        self.t24.setText(str(item24))
        #print(item24)

    def goto_order25(self):
        global item25
        price25=str(self.l25.text())
        quantity25=str(self.id25.text())
        item25=int(price25)*int(quantity25)
        self.t25.setText(str(item25))
        #print(item20)

    def goto_order26(self):
        global item26
        price26=str(self.l26.text())
        quantity26=str(self.id26.text())
        item26=int(price26)*int(quantity26)
        self.t26.setText(str(item26))
        #print(item26)

    def goto_order27(self):
        global item27
        price27=str(self.l27.text())
        quantity27=str(self.id27.text())
        item27=int(price27)*int(quantity27)
        self.t27.setText(str(item27))
        #print(item27)

    def goto_order28(self):
        global item28
        price28=str(self.l28.text())
        quantity28=str(self.id28.text())
        item28=int(price28)*int(quantity28)
        self.t28.setText(str(item28))
        #print(item28)

    def goto_order29(self):
        global item29
        price29=str(self.l29.text())
        quantity29=str(self.id29.text())
        item29=int(price29)*int(quantity29)
        self.t29.setText(str(item29))
        #print(item29)

    def goto_order30(self):
        global item30
        price30=str(self.l30.text())
        quantity30=str(self.id30.text())
        item30=int(price30)*int(quantity30)
        self.t30.setText(str(item30))
        #print(item30)

    ###################################################################

    def goto_order31(self):
        global item31
        price31=str(self.l31.text())
        quantity31=str(self.id31.text())
        item31=int(price31)*int(quantity31)
        self.t31.setText(str(item31))
        #print(item31)

    def goto_order32(self):
        global item32
        price32=str(self.l32.text())
        quantity32=str(self.id32.text())
        item32=int(price32)*int(quantity32)
        self.t32.setText(str(item32))
        #print(item32)

    def goto_order33(self):
        global item33
        price33=str(self.l33.text())
        quantity33=str(self.id33.text())
        item33=int(price33)*int(quantity33)
        self.t33.setText(str(item33))
        #print(item33)

    def goto_order34(self):
        global item34
        price34=str(self.l34.text())
        quantity34=str(self.id34.text())
        item34=int(price34)*int(quantity34)
        self.t34.setText(str(item34))
        #print(item34)

    def goto_order35(self):
        global item35
        price35=str(self.l35.text())
        quantity35=str(self.id35.text())
        item35=int(price35)*int(quantity35)
        self.t35.setText(str(item35))
        #print(item35)

    def goto_order36(self):
        global item36
        price36=str(self.l36.text())
        quantity36=str(self.id36.text())
        item36=int(price36)*int(quantity36)
        self.t36.setText(str(item36))
        #print(item36)

    def goto_order37(self):
        global item37
        price37=str(self.l37.text())
        quantity37=str(self.id37.text())
        item37=int(price37)*int(quantity37)
        self.t37.setText(str(item37))
        #print(item37)

    def goto_order38(self):
        global item38
        price38=str(self.l38.text())
        quantity38=str(self.id38.text())
        item38=int(price38)*int(quantity38)
        self.t38.setText(str(item38))
        #print(item38)

    def goto_order39(self):
        global item39
        price39=str(self.l39.text())
        quantity39=str(self.id39.text())
        item39=int(price39)*int(quantity39)
        self.t39.setText(str(item39))
        #print(item39)

    def goto_order40(self):
        global item40
        price40=str(self.l40.text())
        quantity40=str(self.id40.text())
        item40=int(price40)*int(quantity40)
        self.t40.setText(str(item40))
        #print(item40)

    def goto_order41(self):
        global item41
        price41=str(self.l41.text())
        quantity41=str(self.id41.text())
        item41=int(price41)*int(quantity41)
        self.t41.setText(str(item41))
        #print(item41)

    def goto_order42(self):
        global item42
        price42=str(self.l42.text())
        quantity42=str(self.id42.text())
        item42=int(price42)*int(quantity42)
        self.t42.setText(str(item42))
        #print(item42)

    ###################################################################

##################################################################################
    def goto_generate_bill(self):
        global item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12
        global item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24
        global item25,item26,item27,item28,item29,item30,item31,item32,item33,item34,item35,item36
        global item37,item38,item39,item40,item41,item42

        item1=self.t1.text()
        item1=int(item1)

        item2=self.t2.text()
        item2=int(item2)

        item3=self.t3.text()
        item3=int(item3)

        item4=self.t4.text()
        item4=int(item4)

        item5=self.t5.text()
        item5=int(item5)

        item6=self.t6.text()
        item6=int(item6)

        item7=self.t7.text()
        item7=int(item7)

        item8=self.t8.text()
        item8=int(item8)

        item9=self.t9.text()
        item9=int(item9)

        item10=self.t10.text()
        item10=int(item10)

        item11=self.t11.text()
        item11=int(item11)

        item12=self.t12.text()
        item12=int(item12)

        item13=self.t13.text()
        item13=int(item13)

        item14=self.t14.text()
        item14=int(item14)

        item15=self.t15.text()
        item15=int(item15)

        item16=self.t16.text()
        item16=int(item16)

        item17=self.t17.text()
        item17=int(item17)

        item18=self.t18.text()
        item18=int(item18)

        item19=self.t19.text()
        item19=int(item19)

        item20=self.t20.text()
        item20=int(item20)

        item21=self.t21.text()
        item21=int(item21)

        item22=self.t22.text()
        item22=int(item22)

        item23=self.t23.text()
        item23=int(item23)

        item24=self.t24.text()
        item24=int(item24)

        item25=self.t25.text()
        item25=int(item25)

        item26=self.t26.text()
        item26=int(item26)

        item27=self.t27.text()
        item27=int(item27)

        item28=self.t28.text()
        item28=int(item28)

        item29=self.t29.text()
        item29=int(item29)

        item30=self.t30.text()
        item30=int(item30)

        item31=self.t31.text()
        item31=int(item31)

        item32=self.t32.text()
        item32=int(item32)

        item33=self.t33.text()
        item33=int(item33)

        item34=self.t34.text()
        item34=int(item34)

        item35=self.t35.text()
        item35=int(item35)

        item36=self.t36.text()
        item36=int(item36)

        item37=self.t37.text()
        item37=int(item37)

        item38=self.t38.text()
        item38=int(item38)

        item39=self.t39.text()
        item39=int(item39)

        item40=self.t40.text()
        item40=int(item40)

        item41=self.t41.text()
        item41=int(item41)

        item42=self.t42.text()
        item42=int(item42)


        items1=item1+item2+item3+item4+item5+item6+item7+item8+item9+item10+item11+item12
        items2=item13+item14+item15+item16+item17+item18+item19+item20+item21+item22+item23+item24
        items3=item25+item26+item27+item28+item29+item30+item31+item32+item33+item34+item35+item36
        items4=item37+item38+item39+item40+item41+item42
        items=items1+items2+items3+items4
        self.total.setText(str(items))
        
        gstamount=items*(5/100)
        total_bill_amount=items+gstamount 
        #200-(200*(50/100)
        self.gst.setText(str("5% "))
        self.totalbill.setText(str(total_bill_amount))
        self.bill_generate()


    def bill_generate(self):
        global item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12
        global item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24
        global item25,item26,item27,item28,item29,item30,item31,item32,item33,item34,item35,item36
        global item37,item38,item39,item40,item41,item42

        item1=self.t1.text()
        item1=int(item1)

        item2=self.t2.text()
        item2=int(item2)

        item3=self.t3.text()
        item3=int(item3)

        item4=self.t4.text()
        item4=int(item4)

        item5=self.t5.text()
        item5=int(item5)

        item6=self.t6.text()
        item6=int(item6)

        item7=self.t7.text()
        item7=int(item7)

        item8=self.t8.text()
        item8=int(item8)

        item9=self.t9.text()
        item9=int(item9)

        item10=self.t10.text()
        item10=int(item10)

        item11=self.t11.text()
        item11=int(item11)

        item12=self.t12.text()
        item12=int(item12)

        item13=self.t13.text()
        item13=int(item13)

        item14=self.t14.text()
        item14=int(item14)

        item15=self.t15.text()
        item15=int(item15)

        item16=self.t16.text()
        item16=int(item16)

        item17=self.t17.text()
        item17=int(item17)

        item18=self.t18.text()
        item18=int(item18)

        item19=self.t19.text()
        item19=int(item19)

        item20=self.t20.text()
        item20=int(item20)

        item21=self.t21.text()
        item21=int(item21)

        item22=self.t22.text()
        item22=int(item22)

        item23=self.t23.text()
        item23=int(item23)

        item24=self.t24.text()
        item24=int(item24)

        item25=self.t25.text()
        item25=int(item25)

        item26=self.t26.text()
        item26=int(item26)

        item27=self.t27.text()
        item27=int(item27)

        item28=self.t28.text()
        item28=int(item28)

        item29=self.t29.text()
        item29=int(item29)

        item30=self.t30.text()
        item30=int(item30)

        item31=self.t31.text()
        item31=int(item31)

        item32=self.t32.text()
        item32=int(item32)

        item33=self.t33.text()
        item33=int(item33)

        item34=self.t34.text()
        item34=int(item34)

        item35=self.t35.text()
        item35=int(item35)

        item36=self.t36.text()
        item36=int(item36)

        item37=self.t37.text()
        item37=int(item37)

        item38=self.t38.text()
        item38=int(item38)

        item39=self.t39.text()
        item39=int(item39)

        item40=self.t40.text()
        item40=int(item40)

        item41=self.t41.text()
        item41=int(item41)

        item42=self.t42.text()
        item42=int(item42)

        self.goto_uploadfile()
        sql =""" SELECT billno FROM customer_bills ORDER BY billno DESC LIMIT 1"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            #print(i[0])
            self.billno.setText(str(i[0]))

        ##########################################################
        name=str(self.billno.text())+".txt"
        path=r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\Bills"
        with open(os.path.join(path, name), "w") as file1:
            file1.write("\n\n")
            file1.write("                                        Welcome to KS RESTAURANT             \n\n")

            file1.write("\n")
            file1.write("                                            YOUR ORDER BILL             \n\n")

            file1.write(f"\n                Customer Name : "+self.customer_name.text()+"\n")
            file1.write(f"\n                Phone Number  : "+self.phoneno.text()+"\n")
            file1.write(f"\n                Bill Number   : "+self.billno.text()+"\n")
            file1.write(f"\n                Email ID      : "+self.emailid.text()+"\n")

            file1.write("\n\n")

            file1.write("\t\t------------------------------------------------------------------------------------------\n")
            file1.write("\t\t|         Name           |  ID   |   Price (in RS) |  Quantity  |  Total  (in RS)|\n")
            file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item1!=0:
                file1.write(f"\t\t|     Manchow Soup       |  101  |       180       |      "+self.id1.text()+"     |      "+ self.t1.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item2!=0:
                file1.write(f"\t\t|     Spinach Soup       |  102  |       180       |      "+self.id2.text()+"     |      "+ self.t2.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item3!=0:
                file1.write(f"\t\t|     Paneer Tikka       |  103  |       150       |      "+self.id3.text()+"     |      "+ self.t3.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item4!=0:
                file1.write(f"\t\t|  Sweet Potato Tikki    |  104  |       150       |      "+self.id4.text()+"     |      "+ self.t4.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item5!=0:
                file1.write(f"\t\t|       Corn Soup        |  105  |       170       |      "+self.id5.text()+"     |      "+ self.t5.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item6!=0:
                file1.write(f"\t\t|   Hot and Sour Soup    |  106  |       180       |      "+self.id6.text()+"     |      "+ self.t6.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item7!=0:
                file1.write(f"\t\t|   Vegetable Makhani    |  107  |       180       |      "+self.id7.text()+"     |      "+ self.t7.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item8!=0:
                file1.write(f"\t\t|    Paneer Makhani      |  108  |       180       |      "+self.id8.text()+"     |      "+ self.t8.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item9!=0:
                file1.write(f"\t\t|     Malai Kofta        |  109  |       150       |      "+self.id9.text()+"     |      "+ self.t9.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item10!=0:
                file1.write(f"\t\t|    Aloo Matar Gobi     |  110  |       150       |      "+self.id10.text()+"     |      "+ self.t10.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item11!=0:
                file1.write(f"\t\t|       Dhal Fry         |  111  |       170       |      "+self.id11.text()+"     |      "+ self.t11.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item12!=0:
                file1.write(f"\t\t|   Paneer Shahi Korma   |  112  |       180       |      "+self.id12.text()+"     |      "+ self.t12.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item13!=0:
                file1.write(f"\t\t|      Green Salad       |  113  |       180       |      "+self.id13.text()+"     |      "+ self.t13.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item14!=0:
                file1.write(f"\t\t|   Tomato Olive Salad   |  114  |       180       |      "+self.id14.text()+"     |      "+ self.t14.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item15!=0:
                file1.write(f"\t\t|     Beetroot Salad     |  115  |       150       |      "+self.id15.text()+"     |      "+ self.t15.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item16!=0:
                file1.write(f"\t\t|      Greek Salad       |  116  |       150       |      "+self.id16.text()+"     |      "+ self.t16.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item17!=0:
                file1.write(f"\t\t|     Papaya Salad       |  117  |       170       |      "+self.id17.text()+"     |      "+ self.t17.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item18!=0:
                file1.write(f"\t\t|    Mixed Beans Salad   |  118  |       180       |      "+self.id18.text()+"     |      "+ self.t18.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item19!=0:
                file1.write(f"\t\t|     Gulab Jamun        |  119  |       180       |      "+self.id19.text()+"     |      "+ self.t19.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item20!=0:
                file1.write(f"\t\t|      Mango Lassi       |  120  |       180       |      "+self.id20.text()+"     |      "+ self.t20.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item21!=0:
                file1.write(f"\t\t|      Bombay Crush      |  121  |       150       |      "+self.id21.text()+"     |      "+ self.t21.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item22!=0:
                file1.write(f"\t\t|       Rice Firni       |  122  |       150       |      "+self.id22.text()+"     |      "+ self.t22.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item23!=0:
                file1.write(f"\t\t|       Gajar Halwa      |  123  |       170       |      "+self.id23.text()+"     |      "+ self.t23.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item24!=0:
                file1.write(f"\t\t|    Bollywood Delight   |  124  |       180       |      "+self.id24.text()+"     |      "+ self.t24.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item25!=0:
                file1.write(f"\t\t|      Butter Naan       |  125  |       180       |      "+self.id25.text()+"     |      "+ self.t25.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item26!=0:
                file1.write(f"\t\t|      Garlic Naan       |  126  |       180       |      "+self.id26.text()+"     |      "+ self.t26.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item27!=0:
                file1.write(f"\t\t|     Laccha Paratha     |  127  |       150       |      "+self.id27.text()+"     |      "+ self.t27.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item28!=0:
                file1.write(f"\t\t|     Masala Kulcha      |  128  |       150       |      "+self.id28.text()+"     |      "+ self.t28.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item29!=0:
                file1.write(f"\t\t|      Roomali Roti      |  129  |       170       |      "+self.id29.text()+"     |      "+ self.t29.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item30!=0:
                file1.write(f"\t\t|      Tandoori Roti     |  130  |       180       |      "+self.id30.text()+"     |      "+ self.t30.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item31!=0:
                file1.write(f"\t\t|   Vanilla Ice Cream    |  131  |       180       |      "+self.id31.text()+"     |      "+ self.t31.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item32!=0:
                file1.write(f"\t\t|   Strawberry Ice Cream |  132  |       180       |      "+self.id32.text()+"     |      "+ self.t32.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item33!=0:
                file1.write(f"\t\t|   Chocolate Ice Cream  |  133  |       150       |      "+self.id33.text()+"     |      "+ self.t33.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item34!=0:
                file1.write(f"\t\t|  Buttersorch Ice Cream |  134  |       150       |      "+self.id34.text()+"     |      "+ self.t34.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item35!=0:
                file1.write(f"\t\t|     Pista Ice Cream    |  135  |       170       |      "+self.id35.text()+"     |      "+ self.t35.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item36!=0:
                file1.write(f"\t\t|  Pistachio Ice Cream   |  136  |       180       |      "+self.id36.text()+"     |      "+ self.t36.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item37!=0:
                file1.write(f"\t\t|   Cappuccinos Coffee   |  137  |       149       |      "+self.id37.text()+"     |      "+ self.t37.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item38!=0:
                file1.write(f"\t\t|      Hot Chocolate     |  138  |       249       |      "+self.id38.text()+"     |      "+ self.t38.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item39!=0:
                file1.write(f"\t\t|      Black Coffee      |  139  |       149       |      "+self.id39.text()+"     |      "+ self.t39.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item40!=0:
                file1.write(f"\t\t|       Green Tea        |  140  |       129       |      "+self.id40.text()+"     |      "+ self.t40.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item41!=0:
                file1.write(f"\t\t|       Masala Tea       |  141  |       149       |      "+self.id41.text()+"     |      "+ self.t41.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            if item42!=0:
                file1.write(f"\t\t|        Mint Tea        |  142  |       149       |      "+self.id42.text()+"     |      "+ self.t42.text()+"       |\n")
                file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            
            file1.write("\n\n\t\t|--------------------------------------------------------------------------------|\n")
            
            file1.write(f"\t\t|                        |       |                 |    "+self.total_label.text()+"   |      "+ self.total.text()+"       |\n")
            file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            file1.write(f"\t\t|                        |       |                 |    "+self.gst_label.text()+"     |      "+ self.gst.text()+"       |\n")
            file1.write("\t\t|--------------------------------------------------------------------------------|\n")
            file1.write(f"\t\t|                        |       |                 | "+self.totalbill_label.text()+" |      "+ self.totalbill.text()+"     |\n")
            file1.write("\t\t|--------------------------------------------------------------------------------|\n")
        self.upload_blob()
            

    def convert_data(self,file_name):
        customer_name=self.customer_name.text()
        phoneno=self.phoneno.text()
        if len(customer_name) and len(phoneno) > 0:
            with open(file_name, 'rb') as file:
                binary_data = file.read()
                sql1="""SELECT MAX(billno) FROM customer_bills"""
                cursor.execute(sql1)
                result=cursor.fetchall()
                for i in result:
                    print(i[0])
                    res=str(i[0])
                sql="""UPDATE customer_bills SET billfile=%s where id = %s"""
                data=(binary_data,res)
                cursor.execute(sql,data)
                conn.commit()
                #self.show_billno()
                QMessageBox.information(self," ","Bill Saved successfully")
        else:
            QMessageBox.critical(self," ","Fields can't be empty !!")

        return binary_data
    
    def upload_blob(self):
        #print(self.billno.text())
        a=str(self.billno.text())+'.txt'
        billfile=r'C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\Bills'+'/' +a
        print(billfile)
        self.convert_data(billfile)


    def show_billno(self):
        sql1="""UPDATE customer_bills SET billno = id where billno is null """
        cursor.execute(sql1)
        conn.commit()
        sql =""" SELECT billno FROM customer_bills ORDER BY billno DESC LIMIT 1"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            #print(i[0])
            self.billno.setText(str(i[0]))

    def allot_billno(self):
        sql =""" SELECT billno FROM customer_bills ORDER BY billno DESC LIMIT 1"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            #print(i[0])
            a=int(i[0])
            a+=1
            self.billno.setText(str(a))

    def send_bill(self):
        try:    
            email_user = 'ksprojectcode@gmail.com'
            email_password = 'india123abcd$'
            email_send = str(self.emailid.text())

            subject = 'KS Restaurant Bill'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi there, sending this email from KS Restaurant!'
            msg.attach(MIMEText(body,'plain'))
            a= str(self.billno.text()) + '.txt'
            filename=r'C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\Bills' + '/' + a
            attachment  =open(filename,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+a)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)


            server.sendmail(email_user,email_send,text)
            server.quit()
        except Exception as e:
            QMessageBox.critical(self,"BILL","Please enter vaild mail address or check the internet connection")
            print(e)


        
    
    
    def goto_uploadfile(self):
        customer_name=self.customer_name.text()
        phoneno=self.phoneno.text()
        emailid=self.emailid.text()
        if len(customer_name) and len(phoneno) > 0:
            sql = """INSERT INTO customer_bills(cname,phoneno,emailid)VALUES (%s, %s, %s)"""
            data=(customer_name,phoneno,emailid)
            try:
                cursor.execute(sql,data)
                conn.commit()
                self.show_billno()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close()
            QMessageBox.information(self," ","Bill created successfully")
        else:
            QMessageBox.critical(self," ","Fields can't be empty !!")
     





app=QApplication(sys.argv)
mainwindow=Restaurant()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1000)
widget.show()
app.exec_()