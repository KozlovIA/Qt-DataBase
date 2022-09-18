from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from functional import *
from threading import Thread
from time import sleep
from PyQt6.QtCore import QThread

gridLayoutStartResize()     # изменнение размеров основного слоя gridLayout в MainForm для корректного изменения размеров виджетов

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


class ResizeThread(QThread):
    """Класс для изменения размеров виджетов вместе с размером окна"""
    def __init__(self, parent=None):
        super(ResizeThread, self).__init__(parent)

    def run(self):
        while True:
            if end_of_work: return
            geometry = form.centralwidget.geometry()
            form.gridLayout.setGeometry(geometry)
            sleep(0.05)
# с кнопкой почему-то не выдает "Timers cannot be started from another thread", а со слоем выдает
# менять каждый виджет отдельно, как решение, но это нужно ещё один алгоритм писать, пока что лень
resizeThread = ResizeThread()
resizeThread.start()

# взаимодействие с интерфесом
form.output_db.clicked.connect(output_table)
#form.pushButton.clicked.connect(widget_resize)


# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока