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
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 583)
        Dialog.setMinimumSize(QSize(640, 510))
        Dialog.setMaximumSize(QSize(640, 600))
        icon = QIcon()
        icon.addFile(u"image/pencil-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 520, 311, 61))
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
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 631, 511))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GRNTI_1_le = QLineEdit(self.gridLayoutWidget)
        self.GRNTI_1_le.setObjectName(u"GRNTI_1_le")
        self.GRNTI_1_le.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_3.addWidget(self.GRNTI_1_le)

        self.GRNTI_2_le = QLineEdit(self.gridLayoutWidget)
        self.GRNTI_2_le.setObjectName(u"GRNTI_2_le")
        self.GRNTI_2_le.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_3.addWidget(self.GRNTI_2_le)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.BossStatus_lb = QLabel(self.gridLayoutWidget)
        self.BossStatus_lb.setObjectName(u"BossStatus_lb")

        self.gridLayout.addWidget(self.BossStatus_lb, 18, 0, 1, 1)

        self.BossStatus_le = QLineEdit(self.gridLayoutWidget)
        self.BossStatus_le.setObjectName(u"BossStatus_le")

        self.gridLayout.addWidget(self.BossStatus_le, 18, 1, 1, 1)

        self.BossName_lb = QLabel(self.gridLayoutWidget)
        self.BossName_lb.setObjectName(u"BossName_lb")

        self.gridLayout.addWidget(self.BossName_lb, 16, 0, 1, 1)

        self.university_code_cb = QComboBox(self.gridLayoutWidget)
        self.university_code_cb.setObjectName(u"university_code_cb")

        self.gridLayout.addWidget(self.university_code_cb, 0, 1, 1, 1)

        self.TypeExhibit_lb = QLabel(self.gridLayoutWidget)
        self.TypeExhibit_lb.setObjectName(u"TypeExhibit_lb")

        self.gridLayout.addWidget(self.TypeExhibit_lb, 10, 0, 1, 1)

        self.line_7 = QFrame(self.gridLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 9, 0, 1, 2)

        self.TypeExhibit_cb = QComboBox(self.gridLayoutWidget)
        self.TypeExhibit_cb.addItem("")
        self.TypeExhibit_cb.addItem("")
        self.TypeExhibit_cb.addItem("")
        self.TypeExhibit_cb.setObjectName(u"TypeExhibit_cb")

        self.gridLayout.addWidget(self.TypeExhibit_cb, 10, 1, 1, 1)

        self.Exhibitions_lb = QLabel(self.gridLayoutWidget)
        self.Exhibitions_lb.setObjectName(u"Exhibitions_lb")

        self.gridLayout.addWidget(self.Exhibitions_lb, 12, 0, 1, 1)

        self.Subject_te = QTextEdit(self.gridLayoutWidget)
        self.Subject_te.setObjectName(u"Subject_te")

        self.gridLayout.addWidget(self.Subject_te, 6, 1, 1, 2)

        self.GRNTI_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_lb.setObjectName(u"GRNTI_lb")
        self.GRNTI_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.GRNTI_lb, 4, 0, 1, 1)

        self.line_8 = QFrame(self.gridLayoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 15, 0, 1, 2)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 3)

        self.Exhibitions_te = QTextEdit(self.gridLayoutWidget)
        self.Exhibitions_te.setObjectName(u"Exhibitions_te")

        self.gridLayout.addWidget(self.Exhibitions_te, 12, 1, 1, 2)

        self.type_cb = QComboBox(self.gridLayoutWidget)
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.type_cb.setObjectName(u"type_cb")

        self.gridLayout.addWidget(self.type_cb, 8, 1, 1, 1)

        self.Subject_lb = QLabel(self.gridLayoutWidget)
        self.Subject_lb.setObjectName(u"Subject_lb")

        self.gridLayout.addWidget(self.Subject_lb, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(200, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 2, 1)

        self.line_5 = QFrame(self.gridLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 11, 0, 1, 3)

        self.BossName_le = QLineEdit(self.gridLayoutWidget)
        self.BossName_le.setObjectName(u"BossName_le")

        self.gridLayout.addWidget(self.BossName_le, 16, 1, 1, 1)

        self.line_6 = QFrame(self.gridLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 13, 0, 1, 3)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 2)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 2)

        self.type_lb = QLabel(self.gridLayoutWidget)
        self.type_lb.setObjectName(u"type_lb")
        self.type_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.type_lb, 8, 0, 1, 1)

        self.Exhibit_lb = QLabel(self.gridLayoutWidget)
        self.Exhibit_lb.setObjectName(u"Exhibit_lb")

        self.gridLayout.addWidget(self.Exhibit_lb, 14, 0, 1, 1)

        self.codeVUZ_lb = QLabel(self.gridLayoutWidget)
        self.codeVUZ_lb.setObjectName(u"codeVUZ_lb")
        self.codeVUZ_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.codeVUZ_lb, 0, 0, 1, 1)

        self.regNum_lb = QLabel(self.gridLayoutWidget)
        self.regNum_lb.setObjectName(u"regNum_lb")
        self.regNum_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.regNum_lb, 2, 0, 1, 1)

        self.regNum_le = QLineEdit(self.gridLayoutWidget)
        self.regNum_le.setObjectName(u"regNum_le")
        self.regNum_le.setMaxLength(6)

        self.gridLayout.addWidget(self.regNum_le, 2, 1, 1, 1)

        self.Exhibit_te = QTextEdit(self.gridLayoutWidget)
        self.Exhibit_te.setObjectName(u"Exhibit_te")

        self.gridLayout.addWidget(self.Exhibit_te, 14, 1, 1, 2)

        self.line_9 = QFrame(self.gridLayoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 17, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.SaveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.BossStatus_lb.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.BossName_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0443\u0447\u043d\u044b\u0439 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.TypeExhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.TypeExhibit_cb.setItemText(0, QCoreApplication.translate("Dialog", u"\u0415\u0441\u0442\u044c", None))
        self.TypeExhibit_cb.setItemText(1, QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.TypeExhibit_cb.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f", None))

        self.Exhibitions_lb.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.GRNTI_lb.setText(QCoreApplication.translate("Dialog", u"\u0413\u0420\u041d\u0422\u0418", None))
        self.type_cb.setItemText(0, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u043b\u0430\u043d", None))
        self.type_cb.setItemText(1, QCoreApplication.translate("Dialog", u"\u041d\u0422\u041f", None))

        self.Subject_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u041d\u0418\u0420", None))
        self.type_lb.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.Exhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0430\u0442", None))
        self.codeVUZ_lb.setText(QCoreApplication.translate("Dialog", u"\u0412\u0423\u0417", None))
        self.regNum_lb.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
    # retranslateUi

