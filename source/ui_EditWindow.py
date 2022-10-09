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
        icon = QIcon()
        icon.addFile(u"pencil-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
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
        self.Subject_le = QLineEdit(self.gridLayoutWidget)
        self.Subject_le.setObjectName(u"Subject_le")

        self.gridLayout.addWidget(self.Subject_le, 6, 1, 1, 1)

        self.GRNTI_layout = QGridLayout()
        self.GRNTI_layout.setObjectName(u"GRNTI_layout")
        self.GRNTI1_2_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI1_2_cb.setObjectName(u"GRNTI1_2_cb")

        self.GRNTI_layout.addWidget(self.GRNTI1_2_cb, 0, 1, 1, 1)

        self.GRNTI1_3_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI1_3_cb.setObjectName(u"GRNTI1_3_cb")

        self.GRNTI_layout.addWidget(self.GRNTI1_3_cb, 0, 2, 1, 1)

        self.GRNTI2_1_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI2_1_cb.setObjectName(u"GRNTI2_1_cb")

        self.GRNTI_layout.addWidget(self.GRNTI2_1_cb, 2, 0, 1, 1)

        self.GRNTI2_3_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI2_3_cb.setObjectName(u"GRNTI2_3_cb")

        self.GRNTI_layout.addWidget(self.GRNTI2_3_cb, 2, 2, 1, 1)

        self.GRNTI1_1_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI1_1_cb.setObjectName(u"GRNTI1_1_cb")

        self.GRNTI_layout.addWidget(self.GRNTI1_1_cb, 0, 0, 1, 1)

        self.GRNTI2_2_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI2_2_cb.setObjectName(u"GRNTI2_2_cb")

        self.GRNTI_layout.addWidget(self.GRNTI2_2_cb, 2, 1, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.GRNTI_layout.addWidget(self.line, 1, 0, 1, 3)


        self.gridLayout.addLayout(self.GRNTI_layout, 4, 1, 1, 1)

        self.Exhibit_lb = QLabel(self.gridLayoutWidget)
        self.Exhibit_lb.setObjectName(u"Exhibit_lb")

        self.gridLayout.addWidget(self.Exhibit_lb, 12, 0, 1, 1)

        self.codeVUZ_lb = QLabel(self.gridLayoutWidget)
        self.codeVUZ_lb.setObjectName(u"codeVUZ_lb")

        self.gridLayout.addWidget(self.codeVUZ_lb, 0, 0, 1, 1)

        self.regNum_le = QLineEdit(self.gridLayoutWidget)
        self.regNum_le.setObjectName(u"regNum_le")

        self.gridLayout.addWidget(self.regNum_le, 3, 1, 1, 1)

        self.BossName_lb = QLabel(self.gridLayoutWidget)
        self.BossName_lb.setObjectName(u"BossName_lb")

        self.gridLayout.addWidget(self.BossName_lb, 8, 0, 1, 1)

        self.Exhibitions_le = QLineEdit(self.gridLayoutWidget)
        self.Exhibitions_le.setObjectName(u"Exhibitions_le")

        self.gridLayout.addWidget(self.Exhibitions_le, 11, 1, 1, 1)

        self.Subject_lb = QLabel(self.gridLayoutWidget)
        self.Subject_lb.setObjectName(u"Subject_lb")

        self.gridLayout.addWidget(self.Subject_lb, 6, 0, 1, 1)

        self.BossName_le_2 = QLineEdit(self.gridLayoutWidget)
        self.BossName_le_2.setObjectName(u"BossName_le_2")

        self.gridLayout.addWidget(self.BossName_le_2, 9, 1, 1, 1)

        self.Exhibit_le = QLineEdit(self.gridLayoutWidget)
        self.Exhibit_le.setObjectName(u"Exhibit_le")

        self.gridLayout.addWidget(self.Exhibit_le, 12, 1, 1, 1)

        self.BossName_le = QLineEdit(self.gridLayoutWidget)
        self.BossName_le.setObjectName(u"BossName_le")

        self.gridLayout.addWidget(self.BossName_le, 8, 1, 1, 1)

        self.type_lb = QLabel(self.gridLayoutWidget)
        self.type_lb.setObjectName(u"type_lb")

        self.gridLayout.addWidget(self.type_lb, 1, 0, 1, 1)

        self.regNum_lb = QLabel(self.gridLayoutWidget)
        self.regNum_lb.setObjectName(u"regNum_lb")

        self.gridLayout.addWidget(self.regNum_lb, 3, 0, 1, 1)

        self.C = QLabel(self.gridLayoutWidget)
        self.C.setObjectName(u"C")

        self.gridLayout.addWidget(self.C, 9, 0, 1, 1)

        self.TypeExhibit_lb = QLabel(self.gridLayoutWidget)
        self.TypeExhibit_lb.setObjectName(u"TypeExhibit_lb")

        self.gridLayout.addWidget(self.TypeExhibit_lb, 10, 0, 1, 1)

        self.Exhibitions_lb = QLabel(self.gridLayoutWidget)
        self.Exhibitions_lb.setObjectName(u"Exhibitions_lb")

        self.gridLayout.addWidget(self.Exhibitions_lb, 11, 0, 1, 1)

        self.university_code_cb = QComboBox(self.gridLayoutWidget)
        self.university_code_cb.setObjectName(u"university_code_cb")

        self.gridLayout.addWidget(self.university_code_cb, 0, 1, 1, 1)

        self.type_cb = QComboBox(self.gridLayoutWidget)
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.type_cb.setObjectName(u"type_cb")

        self.gridLayout.addWidget(self.type_cb, 1, 1, 1, 1)

        self.GRNTI_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_lb.setObjectName(u"GRNTI_lb")

        self.gridLayout.addWidget(self.GRNTI_lb, 4, 0, 1, 1)

        self.TypeExhibit_cb = QComboBox(self.gridLayoutWidget)
        self.TypeExhibit_cb.addItem("")
        self.TypeExhibit_cb.addItem("")
        self.TypeExhibit_cb.addItem("")
        self.TypeExhibit_cb.setObjectName(u"TypeExhibit_cb")

        self.gridLayout.addWidget(self.TypeExhibit_cb, 10, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.SaveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Exhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0430\u0442", None))
        self.codeVUZ_lb.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0412\u0423\u0417\u0430", None))
        self.BossName_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0443\u0447\u043d\u044b\u0439 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.Subject_lb.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None))
        self.type_lb.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.regNum_lb.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.C.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.TypeExhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.Exhibitions_lb.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.type_cb.setItemText(0, QCoreApplication.translate("Dialog", u"E", None))
        self.type_cb.setItemText(1, QCoreApplication.translate("Dialog", u"M", None))

        self.GRNTI_lb.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418", None))
        self.TypeExhibit_cb.setItemText(0, QCoreApplication.translate("Dialog", u"\u0415", None))
        self.TypeExhibit_cb.setItemText(1, QCoreApplication.translate("Dialog", u"\u041d", None))
        self.TypeExhibit_cb.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f", None))

    # retranslateUi

