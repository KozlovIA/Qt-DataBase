# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HelpWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(641, 657)
        Dialog.setMinimumSize(QSize(641, 590))
        Dialog.setMaximumSize(QSize(641, 657))
        Dialog.setSizeIncrement(QSize(641, 570))
        font = QFont()
        font.setKerning(True)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u"image/help-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 641, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 621, 91))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setKerning(True)
        self.label_2.setFont(font2)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 341, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.label_3.setFont(font3)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 621, 81))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setKerning(True)
        self.label_4.setFont(font4)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 460, 621, 71))
        self.label_5.setFont(font4)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 340, 621, 121))
        self.label_6.setFont(font4)
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 530, 621, 41))
        self.label_7.setFont(font4)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 260, 621, 81))
        self.label_8.setFont(font4)
        self.label_8.setFrameShape(QFrame.Box)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_8.setWordWrap(True)
        self.close_bn = QPushButton(Dialog)
        self.close_bn.setObjectName(u"close_bn")
        self.close_bn.setGeometry(QRect(200, 590, 241, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430\u0443\u0447\u043d\u044b\u0445 \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438 \u043d\u0430\u0443\u0447\u043d\u044b\u0445 \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u043a \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0432 \u0441\u0435\u0431\u0435 \u0432\u0441\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0434\u043b\u044f \u0443\u0434\u043e\u0431\u043d\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430 \u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438 \u043d\u0430\u0443\u0447\u043d\u044b\u0445 \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u043a.\n"
"\u0421 \u0435\u0433\u043e \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043c\u043e\u0436\u043d\u043e \u043d\u0430\u0439\u0442\u0438 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439 \u0442\u0435\u043c\u0430\u0442"
                        "\u0438\u043a\u0438 \u0432 \u043d\u0443\u0436\u043d\u043e\u043c \u0440\u0435\u0433\u0438\u043e\u043d\u0435.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0433\u043b\u0430\u0432\u043d\u043e\u0433\u043e \u043c\u0435\u043d\u044e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"1) \"\u041e\u0442\u043a\u0440\u044b\u0442\u044c\" - \u0432\u043a\u043b\u0430\u0434\u043a\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0433\u043e \u043c\u0435\u043d\u044e, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044e\u0449\u0430\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u043a \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u043f\u043e \u043d\u0430\u0443\u0447\u043d\u044b\u043c \u0440\u0430\u0431\u043e\u0442\u0430\u043c, \u0412\u0423\u0417\u0430\u043c \u0438 \u043a\u043e\u0434\u0430\u043c \u0413\u0420\u041d\u0422\u0418, \u0442\u0430\u043a \u0438, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c, \u043f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u044b \u043d\u0430\u0443\u0447\u043d\u044b\u0445 \u0440\u0430\u0431\u043e\u0442.", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"4) \"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c\" - \u0432\u043a\u043b\u0430\u0434\u043a\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0433\u043e \u043c\u0435\u043d\u044e, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044e\u0449\u0430\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c, \u0443\u0434\u0430\u043b\u044f\u0442\u044c \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u043d\u0430\u0443\u043d\u044b\u0445 \u0440\u0430\u0431\u043e\u0442, \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u0440\u0443\u0433\u0438\u0445 \u0442\u0430\u0431\u043b\u0438\u0446 \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e.", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"3) \"\u0413\u0440\u0443\u043f\u043f\u044b \u041d\u0418\u0420\" - \u0432\u043a\u043b\u0430\u0434\u043a\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0433\u043e \u043c\u0435\u043d\u044e, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044e\u0449\u0430\u044f \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u044b \u041d\u0418\u0420 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 (\u0441\u043c. \u043f\u0443\u043d\u043a\u0442 2). \u041a \u0443\u0436\u0435 \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u043c \u0433\u0440\u0443\u043f\u043f\u0430\u043c \u043c\u043e\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0438, \u0430 \u0442\u0430\u043a \u0436\u0435 \u0443\u0434\u0430\u043b\u044f\u0442\u044c \u0438\u0445. \u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0433\u0440\u0443\u043f\u043f\u044b"
                        " \u043c\u043e\u0436\u043d\u043e \u0443\u0434\u0430\u043b\u044f\u0442\u044c. \u041f\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 \"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0443 \u041d\u0418\u0420\" \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043e \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438 \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043d\u0430\u0443\u0447\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u0435 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 Word \u0438\u043b\u0438 PDF.", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"5) \"\u0421\u043f\u0440\u0430\u0432\u043a\u0430\" - \u043e\u0442\u043a\u0440\u044b\u0432\u0430\u0435\u0442 \u0442\u0435\u043a\u0443\u0449\u0435\u0435 \u043e\u043a\u043d\u043e \u043f\u043e\u043c\u043e\u0449\u0438.", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"2) \"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f\" - \u043a\u043d\u043e\u043f\u043a\u0430 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0433\u0430\u044e\u0449\u0430\u044f\u0441\u044f \u043f\u043e\u0434 \u0442\u0430\u0431\u043b\u0438\u0446\u0435\u0439. \u0414\u0430\u0435\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0438\u0441\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u043d\u0430\u0443\u0447\u043d\u044b\u0445 \u0440\u0430\u0431\u043e\u0442. \u041d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 \u043c\u043e\u0436\u043d\u043e \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443 \u041d\u0418\u0420 (\u0441\u043c. \u043f\u0443\u043d\u043a\u0442 3).", None))
        self.close_bn.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

