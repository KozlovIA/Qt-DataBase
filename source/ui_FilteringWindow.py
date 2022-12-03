# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilteringWindow.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 243)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(481, 243))
        Dialog.setMaximumSize(QSize(600, 243))
        icon = QIcon()
        icon.addFile(u"filtering-data-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 601, 245))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.preference_exibit_lb = QLabel(self.gridLayoutWidget)
        self.preference_exibit_lb.setObjectName(u"preference_exibit_lb")

        self.gridLayout_3.addWidget(self.preference_exibit_lb, 3, 0, 1, 1)

        self.apply_filtering_bn = QPushButton(self.gridLayoutWidget)
        self.apply_filtering_bn.setObjectName(u"apply_filtering_bn")

        self.gridLayout_3.addWidget(self.apply_filtering_bn, 7, 0, 1, 1)

        self.preference_exibit_cb = QComboBox(self.gridLayoutWidget)
        self.preference_exibit_cb.addItem("")
        self.preference_exibit_cb.setObjectName(u"preference_exibit_cb")

        self.gridLayout_3.addWidget(self.preference_exibit_cb, 3, 1, 1, 1)

        self.region_cb = QComboBox(self.gridLayoutWidget)
        self.region_cb.addItem("")
        self.region_cb.setObjectName(u"region_cb")

        self.gridLayout_3.addWidget(self.region_cb, 1, 1, 1, 1)

        self.line_5 = QFrame(self.gridLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 6, 0, 1, 2)

        self.university_lb = QLabel(self.gridLayoutWidget)
        self.university_lb.setObjectName(u"university_lb")

        self.gridLayout_3.addWidget(self.university_lb, 5, 0, 1, 1)

        self.city_lb = QLabel(self.gridLayoutWidget)
        self.city_lb.setObjectName(u"city_lb")

        self.gridLayout_3.addWidget(self.city_lb, 2, 0, 1, 1)

        self.university_cb = QComboBox(self.gridLayoutWidget)
        self.university_cb.addItem("")
        self.university_cb.setObjectName(u"university_cb")

        self.gridLayout_3.addWidget(self.university_cb, 5, 1, 1, 1)

        self.federalDistrict_cb = QComboBox(self.gridLayoutWidget)
        self.federalDistrict_cb.addItem("")
        self.federalDistrict_cb.setObjectName(u"federalDistrict_cb")

        self.gridLayout_3.addWidget(self.federalDistrict_cb, 0, 1, 1, 1)

        self.federalDistrict_lb = QLabel(self.gridLayoutWidget)
        self.federalDistrict_lb.setObjectName(u"federalDistrict_lb")

        self.gridLayout_3.addWidget(self.federalDistrict_lb, 0, 0, 1, 1)

        self.city_cb = QComboBox(self.gridLayoutWidget)
        self.city_cb.addItem("")
        self.city_cb.setObjectName(u"city_cb")

        self.gridLayout_3.addWidget(self.city_cb, 2, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.GRNTI_1_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI_1_cb.addItem("")
        self.GRNTI_1_cb.setObjectName(u"GRNTI_1_cb")

        self.horizontalLayout_4.addWidget(self.GRNTI_1_cb)

        self.GRNTI_2_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI_2_cb.addItem("")
        self.GRNTI_2_cb.setObjectName(u"GRNTI_2_cb")

        self.horizontalLayout_4.addWidget(self.GRNTI_2_cb)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)

        self.GRNTI_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_lb.setObjectName(u"GRNTI_lb")
        self.GRNTI_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.GRNTI_lb, 4, 0, 1, 1)

        self.reset_filtering_bn = QPushButton(self.gridLayoutWidget)
        self.reset_filtering_bn.setObjectName(u"reset_filtering_bn")

        self.gridLayout_3.addWidget(self.reset_filtering_bn, 7, 1, 1, 1)

        self.region_lb = QLabel(self.gridLayoutWidget)
        self.region_lb.setObjectName(u"region_lb")

        self.gridLayout_3.addWidget(self.region_lb, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.preference_exibit_lb.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.apply_filtering_bn.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.preference_exibit_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.region_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.university_lb.setText(QCoreApplication.translate("Dialog", u"\u0412\u0423\u0417", None))
        self.city_lb.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.university_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.federalDistrict_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.federalDistrict_lb.setText(QCoreApplication.translate("Dialog", u"\u0424\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433", None))
        self.city_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.GRNTI_1_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.GRNTI_2_cb.setItemText(0, QCoreApplication.translate("Dialog", u"-", None))

        self.GRNTI_lb.setText(QCoreApplication.translate("Dialog", u"\u0413\u0420\u041d\u0422\u0418", None))
        self.reset_filtering_bn.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441 \u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432", None))
        self.region_lb.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043b\u0430\u0441\u0442\u044c", None))
    # retranslateUi

