# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChoiceTableWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(317, 176)
        Dialog.setMinimumSize(QSize(317, 176))
        Dialog.setMaximumSize(QSize(317, 176))
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"image/choice-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.OK_bn = QPushButton(Dialog)
        self.OK_bn.setObjectName(u"OK_bn")
        self.OK_bn.setGeometry(QRect(100, 110, 121, 31))
        self.choiceTable = QComboBox(Dialog)
        self.choiceTable.setObjectName(u"choiceTable")
        self.choiceTable.setGeometry(QRect(60, 60, 201, 31))
        self.choiceTable.setIconSize(QSize(16, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.OK_bn.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
    # retranslateUi

