# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sara.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#import cv2
import os

class Ui_game_window(object):
    def setupUi(self, game_window):
        game_window.setObjectName("game_window")
        game_window.resize(800, 350)
        self.centralwidget = QtWidgets.QWidget(game_window)
        self.centralwidget.setObjectName("centralwidget")
        self.obs_box = QtWidgets.QGroupBox(self.centralwidget)
        self.obs_box.setGeometry(QtCore.QRect(50, 154, 221, 111))
        self.obs_box.setObjectName("obs_box")
        self.obs_box.setStyleSheet("border:0.5px solid black;")
        self.Longeur = QtWidgets.QLabel(self.obs_box)
        self.Longeur.setGeometry(QtCore.QRect(16, 32, 70, 21))
        self.Longeur.setObjectName("Longeur")
        self.largeur_obs = QtWidgets.QLineEdit(self.obs_box)
        self.largeur_obs.setGeometry(QtCore.QRect(110, 60, 71, 20))
        self.largeur_obs.setObjectName("largeur_obs")
        self.longeur_obs = QtWidgets.QLineEdit(self.obs_box)
        self.longeur_obs.setGeometry(QtCore.QRect(110, 30, 71, 20))
        self.longeur_obs.setObjectName("longeur_obs")
        self.lbl_lrgr = QtWidgets.QLabel(self.obs_box)
        self.lbl_lrgr.setGeometry(QtCore.QRect(16, 62, 71, 21))
        self.lbl_lrgr.setObjectName("lbl_lrgr")
        self.souris_box = QtWidgets.QGroupBox(self.centralwidget)
        self.souris_box.setGeometry(QtCore.QRect(290, 154, 221, 111))
        self.souris_box.setObjectName("souris_box")
        self.souris_box.setStyleSheet("border:1px solid black;")
        self.Longeur_2 = QtWidgets.QLabel(self.souris_box)
        self.Longeur_2.setGeometry(QtCore.QRect(16, 22, 70, 21))
        self.Longeur_2.setObjectName("Longeur_2")
        self.largeur_souris = QtWidgets.QLineEdit(self.souris_box)
        self.largeur_souris.setGeometry(QtCore.QRect(110, 50, 71, 20))
        self.largeur_souris.setObjectName("largeur_souris")
        self.longeur_souris = QtWidgets.QLineEdit(self.souris_box)
        self.longeur_souris.setGeometry(QtCore.QRect(110, 20, 71, 20))
        self.longeur_souris.setObjectName("longeur_souris")

        self.lbl_lrgr_2 = QtWidgets.QLabel(self.souris_box)
        self.lbl_lrgr_2.setGeometry(QtCore.QRect(16, 52, 71, 21))
        self.lbl_lrgr_2.setObjectName("lbl_lrgr_2")
        self.lbl_lrgr_2.setStyleSheet("border:0px solid black;")
        self.vitesse_souris = QtWidgets.QLineEdit(self.souris_box)
        self.vitesse_souris.setGeometry(QtCore.QRect(110, 80, 71, 20))
        self.vitesse_souris.setText("")
        self.vitesse_souris.setObjectName("vitesse_souris")
        self.lbl_lrgr_4 = QtWidgets.QLabel(self.souris_box)
        self.lbl_lrgr_4.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.lbl_lrgr_4.setObjectName("lbl_lrgr_4")
        self.frmg_box = QtWidgets.QGroupBox(self.centralwidget)
        self.frmg_box.setGeometry(QtCore.QRect(550, 154, 221, 111))
        self.frmg_box.setObjectName("frmg_box")
        self.frmg_box.setStyleSheet("border:1px solid black;")
        
        self.Longeur_3 = QtWidgets.QLabel(self.frmg_box)
        self.Longeur_3.setGeometry(QtCore.QRect(16, 30, 70, 21))
        self.Longeur_3.setObjectName("Longeur_3")
        self.largeur_frmg = QtWidgets.QLineEdit(self.frmg_box)
        self.largeur_frmg.setGeometry(QtCore.QRect(110, 58, 71, 20))
        self.largeur_frmg.setObjectName("largeur_frmg")
        self.longeur_frmg = QtWidgets.QLineEdit(self.frmg_box)
        self.longeur_frmg.setGeometry(QtCore.QRect(110, 28, 71, 20))
        self.longeur_frmg.setObjectName("longeur_frmg")
        self.lbl_lrgr_3 = QtWidgets.QLabel(self.frmg_box)
        self.lbl_lrgr_3.setGeometry(QtCore.QRect(16, 60, 71, 21))
        self.lbl_lrgr_3.setObjectName("lbl_lrgr_3")
        self.lbl_obstcl = QtWidgets.QLabel(self.centralwidget)
        self.lbl_obstcl.setGeometry(QtCore.QRect(54, 120, 100, 29))
        self.lbl_obstcl.setObjectName("lbl_obstcl")
        self.comboBox_obstcl = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_obstcl.setGeometry(QtCore.QRect(160, 130, 77, 20))
        self.comboBox_obstcl.setObjectName("comboBox_obstcl")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_obstcl.addItem("")
        self.comboBox_frmg = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_frmg.setGeometry(QtCore.QRect(670, 130, 77, 20))
        self.comboBox_frmg.setObjectName("comboBox_frmg")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.comboBox_frmg.addItem("")
        self.lbl_frmg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_frmg.setGeometry(QtCore.QRect(554, 120, 100, 29))
        self.lbl_frmg.setObjectName("lbl_frmg")
        self.img_obstcl = QtWidgets.QWidget(self.centralwidget)
        self.img_obstcl.setGeometry(QtCore.QRect(110, 50, 81, 61))
        self.img_obstcl.setObjectName("img_obstcl")
        self.img_obstcl.setStyleSheet("image: url(obstacle.png)")
        self.img_souris = QtWidgets.QWidget(self.centralwidget)
        self.img_souris.setGeometry(QtCore.QRect(330, 50, 81, 61))
        self.img_souris.setStyleSheet("image: url(rat1.png)")
        self.img_souris.setObjectName("img_souris")
        self.img_frmg = QtWidgets.QWidget(self.centralwidget)
        self.img_frmg.setGeometry(QtCore.QRect(580, 50, 81, 61))
        self.img_frmg.setObjectName("img_frmg")
        self.img_frmg.setStyleSheet("image: url(cheese.png)")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 40, 801, 241))
        self.widget.setObjectName("widget")
        self.Longeur.setStyleSheet("border:0px solid black;")
        self.lbl_lrgr.setStyleSheet("border:0px solid black;")
        self.Longeur_2.setStyleSheet("border:0px solid black;")
        self.lbl_lrgr_2.setStyleSheet("border:0px solid black;")
        self.lbl_lrgr_4.setStyleSheet("border:0px solid black;")
        self.Longeur_3.setStyleSheet("border:0px solid black;")
        self.lbl_lrgr_3.setStyleSheet("border:0px solid black;")
        self.widget.setStyleSheet("background-color :rgb(253, 237, 236);")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 290, 191, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color :rgb(253, 237, 236);""border:0.5px solid black;" "border-top-left-radius: 10px;""border-bottom-left-radius: 10px;" "border-top-right-radius: 10px;" "border-bottom-right-radius: 10px;")
        self.widget.raise_()
        self.obs_box.raise_()
        self.souris_box.raise_()
        self.frmg_box.raise_()
        self.lbl_obstcl.raise_()
        self.comboBox_obstcl.raise_()
        self.comboBox_frmg.raise_()
        self.lbl_frmg.raise_()
        self.img_obstcl.raise_()
        self.img_souris.raise_()
        self.img_frmg.raise_()
        self.pushButton.raise_()
        game_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(game_window)
        self.statusbar.setObjectName("statusbar")
        game_window.setStatusBar(self.statusbar)

        self.retranslateUi(game_window)
        self.pushButton.clicked.connect(self.lancer)
        QtCore.QMetaObject.connectSlotsByName(game_window)

    def retranslateUi(self, game_window):
        _translate = QtCore.QCoreApplication.translate
        game_window.setWindowTitle(_translate("game_window", "                                                                                                     Jeu Souris"))
        self.obs_box.setTitle(_translate("game_window", "Dimensions de l\'obstacle"))
        self.Longeur.setText(_translate("game_window", "Longeur"))
        self.lbl_lrgr.setText(_translate("game_window", "Largeur"))
        self.souris_box.setTitle(_translate("game_window", "Dimensions de la souris"))
        self.Longeur_2.setText(_translate("game_window", "Longeur"))
        self.lbl_lrgr_2.setText(_translate("game_window", "Largeur"))
        self.lbl_lrgr_4.setText(_translate("game_window", "Vitesse"))
        self.frmg_box.setTitle(_translate("game_window", "Dimensions du fromage"))
        self.Longeur_3.setText(_translate("game_window", "Longeur"))
        self.lbl_lrgr_3.setText(_translate("game_window", "Largeur"))
        self.lbl_obstcl.setText(_translate("game_window", "Nombre d\'obstacles"))
        self.lbl_frmg.setText(_translate("game_window", "Nombre de fromages"))
        self.pushButton.setText(_translate("game_window", "Lancer la partie"))
        self.comboBox_obstcl.setItemText(0, _translate("game_window", "1"))
        self.comboBox_obstcl.setItemText(1, _translate("game_window", "2"))
        self.comboBox_obstcl.setItemText(2, _translate("game_window", "3"))
        self.comboBox_obstcl.setItemText(3, _translate("game_window", "4"))
        self.comboBox_obstcl.setItemText(4, _translate("game_window", "5"))
        self.comboBox_obstcl.setItemText(5, _translate("game_window", "6"))
        self.comboBox_obstcl.setItemText(6, _translate("game_window", "7"))
        self.comboBox_obstcl.setItemText(7, _translate("game_window", "8"))
        self.comboBox_obstcl.setItemText(8, _translate("game_window", "9"))
        self.comboBox_obstcl.setItemText(9, _translate("game_window", "10"))

        self.comboBox_frmg.setItemText(0, _translate("game_window", "1"))
        self.comboBox_frmg.setItemText(1, _translate("game_window", "2"))
        self.comboBox_frmg.setItemText(2, _translate("game_window", "3"))
        self.comboBox_frmg.setItemText(3, _translate("game_window", "4"))
        self.comboBox_frmg.setItemText(4, _translate("game_window", "5"))
        self.comboBox_frmg.setItemText(5, _translate("game_window", "6"))
        self.comboBox_frmg.setItemText(6, _translate("game_window", "7"))
        self.comboBox_frmg.setItemText(7, _translate("game_window", "8"))
        self.comboBox_frmg.setItemText(8, _translate("game_window", "9"))
        self.comboBox_frmg.setItemText(9, _translate("game_window", "10"))
    def lancer(self):
        file  = open("inputs.txt", "w")

        file.write(self.comboBox_obstcl.currentText()+","+self.longeur_obs.text()+","+self.largeur_obs.text()+","+self.longeur_souris.text()+","+self.largeur_souris.text()+","+self.vitesse_souris.text()+","+self.comboBox_frmg.currentText()+","+self.longeur_frmg.text()+","+self.largeur_frmg.text())
        file.close()
        os.system('python script1.py')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LAALgo = QtWidgets.QMainWindow()
    ui = Ui_game_window()
    ui.setupUi(LAALgo)
    LAALgo.show()
    sys.exit(app.exec_())