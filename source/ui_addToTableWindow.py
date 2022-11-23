# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addToTableWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 120)
        Dialog.setMinimumSize(QSize(400, 120))
        Dialog.setMaximumSize(QSize(400, 120))
        icon = QIcon()
        icon.addFile(u"pencil-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 171, 31))
        self.label.setAlignment(Qt.AlignCenter)
        self.tableName = QComboBox(Dialog)
        self.tableName.setObjectName(u"tableName")
        self.tableName.setGeometry(QRect(180, 20, 211, 31))
        self.Ok_bn = QPushButton(Dialog)
        self.Ok_bn.setObjectName(u"Ok_bn")
        self.Ok_bn.setGeometry(QRect(130, 70, 131, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.Ok_bn.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
    # retranslateUi

