from multiprocessing.sharedctypes import Value
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from functional import *
from threading import Thread
from time import sleep

gridLayoutStartResize()     # изменнение размеров основного слоя в MainForm для корректного изменения размеров виджетов

Form, Window = uic.loadUiType("MainFormResize.ui")

# Настройка интерфейса
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Функции взаимодйствия
def output_table():
    db = db_connect()
    if not db:
        form.info.setText("Ошибка подключения к базе данных.")
        return
    form.info.setText("Подключено к базе данных.")
    VUZ = QSqlTableModel()  # Создали объект таблицы
    VUZ.setTable('VUZ')     # Привязали таблицу из базы данных
    VUZ.select()        # Выбрали все строки из данной таблицы
    form.tableView.setModel(VUZ)
    form.tableView.setSortingEnabled(True)

end_of_work = False
def widget_resize():
    """Функция для изменения размеров виджетов вместе с размером окна"""
    while True:
        geometry = form.centralwidget.geometry()
        form.gridLayout.setGeometry(geometry)
        sleep(0.1)
        if end_of_work: return
Thread(target=widget_resize).start()

#Thread(target=widget_resize).start()
print(form.gridLayout.maximumSize())
# взаимодействие с интерфесом
form.output_db.clicked.connect(output_table)
#form.pushButton.clicked.connect(widget_resize)


# Запуск приложения
window.show()
app.exec()

end_of_work = True