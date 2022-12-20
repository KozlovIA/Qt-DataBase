# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 583)
        Dialog.setMinimumSize(QSize(640, 510))
        Dialog.setMaximumSize(QSize(640, 600))
        icon = QIcon()
        icon.addFile(u"image/doc-icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.line_8 = QFrame(self.gridLayoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 17, 0, 1, 3)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 2)

        self.line_9 = QFrame(self.gridLayoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 19, 0, 1, 2)

        self.Abbreviation_Out_lb = QLabel(self.gridLayoutWidget)
        self.Abbreviation_Out_lb.setObjectName(u"Abbreviation_Out_lb")
        font = QFont()
        font.setPointSize(9)
        self.Abbreviation_Out_lb.setFont(font)
        self.Abbreviation_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Abbreviation_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.Abbreviation_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Abbreviation_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.Abbreviation_Out_lb, 0, 1, 1, 1)

        self.TypeExhibit_Out_lb = QLabel(self.gridLayoutWidget)
        self.TypeExhibit_Out_lb.setObjectName(u"TypeExhibit_Out_lb")
        self.TypeExhibit_Out_lb.setFont(font)
        self.TypeExhibit_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.TypeExhibit_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.TypeExhibit_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TypeExhibit_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.TypeExhibit_Out_lb, 8, 1, 1, 1)

        self.BossName_lb = QLabel(self.gridLayoutWidget)
        self.BossName_lb.setObjectName(u"BossName_lb")
        self.BossName_lb.setFont(font)

        self.gridLayout.addWidget(self.BossName_lb, 18, 0, 1, 1)

        self.line_6 = QFrame(self.gridLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 14, 0, 1, 3)

        self.line_7 = QFrame(self.gridLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 7, 0, 1, 2)

        self.type_Out_lb = QLabel(self.gridLayoutWidget)
        self.type_Out_lb.setObjectName(u"type_Out_lb")
        self.type_Out_lb.setFont(font)
        self.type_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.type_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.type_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.type_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.type_Out_lb, 6, 1, 1, 1)

        self.BossName_Out_lb = QLabel(self.gridLayoutWidget)
        self.BossName_Out_lb.setObjectName(u"BossName_Out_lb")
        self.BossName_Out_lb.setFont(font)
        self.BossName_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.BossName_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.BossName_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BossName_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.BossName_Out_lb, 18, 1, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 2)

        self.BossStatus_Out_lb = QLabel(self.gridLayoutWidget)
        self.BossStatus_Out_lb.setObjectName(u"BossStatus_Out_lb")
        self.BossStatus_Out_lb.setFont(font)
        self.BossStatus_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.BossStatus_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.BossStatus_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BossStatus_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.BossStatus_Out_lb, 20, 1, 1, 1)

        self.Subject_Out_lb = QLabel(self.gridLayoutWidget)
        self.Subject_Out_lb.setObjectName(u"Subject_Out_lb")
        self.Subject_Out_lb.setFont(font)
        self.Subject_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Subject_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.Subject_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Subject_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.Subject_Out_lb, 2, 1, 1, 1)

        self.codeVUZ_lb = QLabel(self.gridLayoutWidget)
        self.codeVUZ_lb.setObjectName(u"codeVUZ_lb")
        self.codeVUZ_lb.setFont(font)
        self.codeVUZ_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.codeVUZ_lb, 22, 0, 1, 1)

        self.TypeExhibit_lb = QLabel(self.gridLayoutWidget)
        self.TypeExhibit_lb.setObjectName(u"TypeExhibit_lb")
        self.TypeExhibit_lb.setFont(font)

        self.gridLayout.addWidget(self.TypeExhibit_lb, 8, 0, 1, 1)

        self.codeVUZ_Out_lb = QLabel(self.gridLayoutWidget)
        self.codeVUZ_Out_lb.setObjectName(u"codeVUZ_Out_lb")
        self.codeVUZ_Out_lb.setFont(font)
        self.codeVUZ_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.codeVUZ_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.codeVUZ_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.codeVUZ_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.codeVUZ_Out_lb, 22, 1, 1, 1)

        self.Subject_lb = QLabel(self.gridLayoutWidget)
        self.Subject_lb.setObjectName(u"Subject_lb")
        self.Subject_lb.setFont(font)

        self.gridLayout.addWidget(self.Subject_lb, 2, 0, 1, 1)

        self.BossStatus_lb = QLabel(self.gridLayoutWidget)
        self.BossStatus_lb.setObjectName(u"BossStatus_lb")
        self.BossStatus_lb.setFont(font)

        self.gridLayout.addWidget(self.BossStatus_lb, 20, 0, 1, 1)

        self.line_5 = QFrame(self.gridLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 9, 0, 1, 3)

        self.Exhibitions_Out_lb = QLabel(self.gridLayoutWidget)
        self.Exhibitions_Out_lb.setObjectName(u"Exhibitions_Out_lb")
        self.Exhibitions_Out_lb.setFont(font)
        self.Exhibitions_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Exhibitions_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.Exhibitions_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Exhibitions_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.Exhibitions_Out_lb, 10, 1, 2, 2)

        self.GRNTI_Out_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_Out_lb.setObjectName(u"GRNTI_Out_lb")
        self.GRNTI_Out_lb.setFont(font)
        self.GRNTI_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.GRNTI_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.GRNTI_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.GRNTI_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.GRNTI_Out_lb, 4, 1, 1, 1)

        self.line_10 = QFrame(self.gridLayoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_10, 21, 0, 1, 2)

        self.GRNTI_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_lb.setObjectName(u"GRNTI_lb")
        self.GRNTI_lb.setFont(font)
        self.GRNTI_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.GRNTI_lb, 4, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.type_lb = QLabel(self.gridLayoutWidget)
        self.type_lb.setObjectName(u"type_lb")
        self.type_lb.setFont(font)
        self.type_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.type_lb, 6, 0, 1, 1)

        self.Abbreviation_lb = QLabel(self.gridLayoutWidget)
        self.Abbreviation_lb.setObjectName(u"Abbreviation_lb")
        self.Abbreviation_lb.setFont(font)
        self.Abbreviation_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Abbreviation_lb, 0, 0, 1, 1)

        self.Exhibitions_lb = QLabel(self.gridLayoutWidget)
        self.Exhibitions_lb.setObjectName(u"Exhibitions_lb")
        self.Exhibitions_lb.setFont(font)

        self.gridLayout.addWidget(self.Exhibitions_lb, 10, 0, 2, 1)

        self.verticalSpacer = QSpacerItem(200, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 2, 1)

        self.Exhibit_Out_lb = QLabel(self.gridLayoutWidget)
        self.Exhibit_Out_lb.setObjectName(u"Exhibit_Out_lb")
        self.Exhibit_Out_lb.setFont(font)
        self.Exhibit_Out_lb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Exhibit_Out_lb.setFrameShape(QFrame.StyledPanel)
        self.Exhibit_Out_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Exhibit_Out_lb.setWordWrap(True)

        self.gridLayout.addWidget(self.Exhibit_Out_lb, 15, 1, 2, 2)

        self.Exhibit_lb = QLabel(self.gridLayoutWidget)
        self.Exhibit_lb.setObjectName(u"Exhibit_lb")
        self.Exhibit_lb.setFont(font)

        self.gridLayout.addWidget(self.Exhibit_lb, 15, 0, 2, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u041d\u0418\u0420", None))
        self.SaveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Abbreviation_Out_lb.setText("")
        self.TypeExhibit_Out_lb.setText("")
        self.BossName_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0443\u0447\u043d\u044b\u0439 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.type_Out_lb.setText("")
        self.BossName_Out_lb.setText("")
        self.BossStatus_Out_lb.setText("")
        self.Subject_Out_lb.setText("")
        self.codeVUZ_lb.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0437 \u0412\u0423\u0417\u0430", None))
        self.TypeExhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.codeVUZ_Out_lb.setText("")
        self.Subject_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u041d\u0418\u0420", None))
        self.BossStatus_lb.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.Exhibitions_Out_lb.setText("")
        self.GRNTI_Out_lb.setText("")
        self.GRNTI_lb.setText(QCoreApplication.translate("Dialog", u"\u0413\u0420\u041d\u0422\u0418", None))
        self.type_lb.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.Abbreviation_lb.setText(QCoreApplication.translate("Dialog", u"\u0410\u0431\u0431\u0440\u0435\u0432\u0438\u0430\u0442\u0443\u0440\u0430", None))
        self.Exhibitions_lb.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.Exhibit_Out_lb.setText("")
        self.Exhibit_lb.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0430\u0442", None))
    # retranslateUi

