# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateTableWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 230)
        Dialog.setMinimumSize(QSize(400, 230))
        Dialog.setMaximumSize(QSize(400, 230))
        icon = QIcon()
        icon.addFile(u"pencil-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Save_bn = QPushButton(Dialog)
        self.Save_bn.setObjectName(u"Save_bn")
        self.Save_bn.setGeometry(QRect(40, 180, 131, 31))
        self.Cancel_bn = QPushButton(Dialog)
        self.Cancel_bn.setObjectName(u"Cancel_bn")
        self.Cancel_bn.setGeometry(QRect(220, 180, 131, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 401, 31))
        self.label.setAlignment(Qt.AlignCenter)
        self.TableName_le = QLineEdit(Dialog)
        self.TableName_le.setObjectName(u"TableName_le")
        self.TableName_le.setGeometry(QRect(20, 80, 361, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.Save_bn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.Cancel_bn.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043d\u043e\u0432\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.TableName_le.setText("")
    # retranslateUi

