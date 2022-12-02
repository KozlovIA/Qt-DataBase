# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm old.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(874, 756)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"source/database-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 871, 711))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.dbInfo = QLabel(self.gridLayoutWidget)
        self.dbInfo.setObjectName(u"dbInfo")
        self.dbInfo.setEnabled(True)
        self.dbInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dbInfo, 0, 1, 1, 2)

        self.region_lb = QLabel(self.gridLayoutWidget)
        self.region_lb.setObjectName(u"region_lb")

        self.gridLayout.addWidget(self.region_lb, 3, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)

        self.preference_exibit_cb = QComboBox(self.gridLayoutWidget)
        self.preference_exibit_cb.addItem("")
        self.preference_exibit_cb.setObjectName(u"preference_exibit_cb")

        self.gridLayout.addWidget(self.preference_exibit_cb, 5, 1, 1, 1)

        self.federalDistrict_lb = QLabel(self.gridLayoutWidget)
        self.federalDistrict_lb.setObjectName(u"federalDistrict_lb")

        self.gridLayout.addWidget(self.federalDistrict_lb, 2, 0, 1, 1)

        self.apply_filtering_bn = QPushButton(self.gridLayoutWidget)
        self.apply_filtering_bn.setObjectName(u"apply_filtering_bn")

        self.gridLayout.addWidget(self.apply_filtering_bn, 8, 0, 1, 1)

        self.GRNTI_lb = QLabel(self.gridLayoutWidget)
        self.GRNTI_lb.setObjectName(u"GRNTI_lb")
        self.GRNTI_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.GRNTI_lb, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset_table_filtering_bn = QPushButton(self.gridLayoutWidget)
        self.reset_table_filtering_bn.setObjectName(u"reset_table_filtering_bn")

        self.horizontalLayout.addWidget(self.reset_table_filtering_bn)

        self.reset_filtering_bn = QPushButton(self.gridLayoutWidget)
        self.reset_filtering_bn.setObjectName(u"reset_filtering_bn")

        self.horizontalLayout.addWidget(self.reset_filtering_bn)


        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 1)

        self.city_cb = QComboBox(self.gridLayoutWidget)
        self.city_cb.addItem("")
        self.city_cb.setObjectName(u"city_cb")

        self.gridLayout.addWidget(self.city_cb, 4, 1, 1, 1)

        self.region_cb = QComboBox(self.gridLayoutWidget)
        self.region_cb.addItem("")
        self.region_cb.setObjectName(u"region_cb")

        self.gridLayout.addWidget(self.region_cb, 3, 1, 1, 1)

        self.university_cb = QComboBox(self.gridLayoutWidget)
        self.university_cb.addItem("")
        self.university_cb.setObjectName(u"university_cb")

        self.gridLayout.addWidget(self.university_cb, 7, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GRNTI_1_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI_1_cb.addItem("")
        self.GRNTI_1_cb.setObjectName(u"GRNTI_1_cb")

        self.horizontalLayout_3.addWidget(self.GRNTI_1_cb)

        self.GRNTI_2_cb = QComboBox(self.gridLayoutWidget)
        self.GRNTI_2_cb.addItem("")
        self.GRNTI_2_cb.setObjectName(u"GRNTI_2_cb")

        self.horizontalLayout_3.addWidget(self.GRNTI_2_cb)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 1, 1, 1)

        self.choiceTable = QComboBox(self.gridLayoutWidget)
        self.choiceTable.setObjectName(u"choiceTable")

        self.gridLayout.addWidget(self.choiceTable, 0, 0, 1, 1)

        self.federalDistrict_cb = QComboBox(self.gridLayoutWidget)
        self.federalDistrict_cb.addItem("")
        self.federalDistrict_cb.setObjectName(u"federalDistrict_cb")

        self.gridLayout.addWidget(self.federalDistrict_cb, 2, 1, 1, 1)

        self.university_lb = QLabel(self.gridLayoutWidget)
        self.university_lb.setObjectName(u"university_lb")

        self.gridLayout.addWidget(self.university_lb, 7, 0, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 9, 0, 1, 2)

        self.preference_exibit_lb = QLabel(self.gridLayoutWidget)
        self.preference_exibit_lb.setObjectName(u"preference_exibit_lb")

        self.gridLayout.addWidget(self.preference_exibit_lb, 5, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 3)

        self.CreateNewTable_bn = QPushButton(self.gridLayoutWidget)
        self.CreateNewTable_bn.setObjectName(u"CreateNewTable_bn")

        self.gridLayout_2.addWidget(self.CreateNewTable_bn, 1, 0, 1, 1)

        self.deleteTable_bn = QPushButton(self.gridLayoutWidget)
        self.deleteTable_bn.setObjectName(u"deleteTable_bn")

        self.gridLayout_2.addWidget(self.deleteTable_bn, 1, 1, 1, 1)

        self.editEntery_bn = QPushButton(self.gridLayoutWidget)
        self.editEntery_bn.setObjectName(u"editEntery_bn")

        self.gridLayout_2.addWidget(self.editEntery_bn, 1, 2, 1, 1)

        self.EditField = QPushButton(self.gridLayoutWidget)
        self.EditField.setObjectName(u"EditField")

        self.gridLayout_2.addWidget(self.EditField, 3, 2, 1, 1)

        self.AddField = QPushButton(self.gridLayoutWidget)
        self.AddField.setObjectName(u"AddField")

        self.gridLayout_2.addWidget(self.AddField, 3, 0, 1, 1)

        self.deleteButton = QPushButton(self.gridLayoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.gridLayout_2.addWidget(self.deleteButton, 3, 1, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 3)


        self.gridLayout.addLayout(self.gridLayout_2, 13, 0, 1, 4)

        self.city_lb = QLabel(self.gridLayoutWidget)
        self.city_lb.setObjectName(u"city_lb")

        self.gridLayout.addWidget(self.city_lb, 4, 0, 1, 1)

        self.tableView = QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setGridStyle(Qt.SolidLine)
        self.tableView.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableView, 10, 0, 1, 4)

        self.recNum_lb = QLabel(self.gridLayoutWidget)
        self.recNum_lb.setObjectName(u"recNum_lb")

        self.gridLayout.addWidget(self.recNum_lb, 11, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 874, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430\u0443\u0447\u043d\u044b\u0445 \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u043a", None))
        self.dbInfo.setText("")
        self.region_lb.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.preference_exibit_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.federalDistrict_lb.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433", None))
        self.apply_filtering_bn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.GRNTI_lb.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0420\u041d\u0422\u0418", None))
        self.reset_table_filtering_bn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.reset_filtering_bn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432", None))
        self.city_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.region_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.university_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.GRNTI_1_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.GRNTI_2_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.federalDistrict_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.university_lb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0423\u0417", None))
        self.preference_exibit_lb.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.CreateNewTable_bn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.deleteTable_bn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.editEntery_bn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.EditField.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.AddField.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.city_lb.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.recNum_lb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u0441\u0442\u0440\u043e\u043a: ", None))
    # retranslateUi

