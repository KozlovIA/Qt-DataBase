# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 510)
        Dialog.setMinimumSize(QSize(640, 510))
        Dialog.setMaximumSize(QSize(640, 510))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 440, 311, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SaveButton = QPushButton(self.horizontalLayoutWidget)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout_2.addWidget(self.SaveButton)

        self.CancelButton = QPushButton(self.horizontalLayoutWidget)
        self.CancelButton.setObjectName(u"CancelButton")

        self.horizontalLayout_2.addWidget(self.CancelButton)

        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 641, 431))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 6, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_8 = QComboBox(self.gridLayoutWidget)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_2.addWidget(self.comboBox_8, 0, 7, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_2.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.comboBox_7 = QComboBox(self.gridLayoutWidget)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_2.addWidget(self.comboBox_7, 0, 6, 1, 1)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 0, 5, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 0, 3, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_2.addWidget(self.comboBox_3, 0, 0, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 4, 1, 1, 1)

        self.Exhibit_lb = QLabel(self.gridLayoutWidget)
        self.Exhibit_lb.setObjectName(u"Exhibit_lb")

        self.gridLayout.addWidget(self.Exhibit_lb, 12, 0, 1, 1)

        self.codeVUZ_lb = QLabel(self.gridLayoutWidget)
        self.codeVUZ_lb.setObjectName(u"codeVUZ_lb")

        self.gridLayout.addWidget(self.codeVUZ_lb, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.BossName_lb = QLabel(self.gridLayoutWidget)
        self.BossName_lb.setObjectName(u"BossName_lb")

        self.gridLayout.addWidget(self.BossName_lb, 8, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 11, 1, 1, 1)

        self.Subject_lb = QLabel(self.gridLayoutWidget)
        self.Subject_lb.setObjectName(u"Subject_lb")

        self.gridLayout.addWidget(self.Subject_lb, 6, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 9, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 12, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 8, 1, 1, 1)

        self.typelb = QLabel(self.gridLayoutWidget)
        self.typelb.setObjectName(u"typelb")

        self.gridLayout.addWidget(self.typelb, 1, 0, 1, 1)

        self.rgNumlb = QLabel(self.gridLayoutWidget)
        self.rgNumlb.setObjectName(u"rgNumlb")

        self.gridLayout.addWidget(self.rgNumlb, 3, 0, 1, 1)

        self.BossTitle_lb = QLabel(self.gridLayoutWidget)
        self.BossTitle_lb.setObjectName(u"BossTitle_lb")

        self.gridLayout.addWidget(self.BossTitle_lb, 9, 0, 1, 1)

        self.TypeExhibit_lb = QLabel(self.gridLayoutWidget)
        self.TypeExhibit_lb.setObjectName(u"TypeExhibit_lb")

        self.gridLayout.addWidget(self.TypeExhibit_lb, 10, 0, 1, 1)

        self.Exhibitions_lb = QLabel(self.gridLayoutWidget)
        self.Exhibitions_lb.setObjectName(u"Exhibitions_lb")

        self.gridLayout.addWidget(self.Exhibitions_lb, 11, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.GRNTI_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_lb.setObjectName(u"GRNTI_lb")

        self.gridLayout.addWidget(self.GRNTI_lb, 4, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.gridLayoutWidget)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout.addWidget(self.comboBox_9, 10, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SaveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Exhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0430\u0442", None))
        self.codeVUZ_lb.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0412\u0423\u0417\u0430", None))
        self.BossName_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0443\u0447\u043d\u044b\u0439 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.Subject_lb.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None))
        self.typelb.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.rgNumlb.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.BossTitle_lb.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.TypeExhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.Exhibitions_lb.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"E", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"M", None))

        self.GRNTI_lb.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("Dialog", u"\u0415", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("Dialog", u"\u041d", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f", None))

    # retranslateUi

