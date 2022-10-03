import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from sqlalchemy import false
from source.functional import *
from time import sleep
from PyQt6.QtCore import QThread
import source.editWindow as AddField_window
from PySide6 import QtWidgets

gridLayoutStartResize()     # изменнение размеров основного слоя gridLayout в MainForm для корректного изменения размеров виджетов

Form, Window = uic.loadUiType("MainFormResize.ui")  # файл MainFormResize создается в функции gridLayoutStartResize, если поставить MainForm.ui, интерфейс не будет изменять размер в большую сторону

# Настройка интерфейса
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Функции взаимодйствия
def output_table(db_name="Таблица НИР"):
    """Функция отображения таблицы"""
    table_dict = {'Таблица НИР': 'VUZ', 'Таблица выставок': 'Vyst_mo', 'Таблица ГРНТИ': 'grntirub'}
    db = db_connect()
    if not db:
        form.dbInfo.setText('Ошибка подключения к базе данных "' + db_name + '"')
        return
    form.dbInfo.setText('Подключено к базе данных "' + db_name + '"')
    db = QSqlTableModel()  # Создали объект таблицы
    db.setTable(table_dict[db_name])     # Привязали таблицу из базы данных
    db.select()        # Выбрали все строки из данной таблицы
    form.tableView.setModel(db)
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


def add_field_window():
    global AddFieldWindow, AddFieldForm
    Form, Window = uic.loadUiType("source/EditWindow.ui")  # файл MainFormResize создается в функции gridLayoutStartResize, если поставить MainForm.ui, интерфейс не будет изменять размер в большую сторону
    # Настройка интерфейса
    AddFieldWindow = Window()
    AddFieldForm = Form()
    AddFieldForm.setupUi(AddFieldWindow)
    AddFieldWindow.show()
    #window.setEnabled(False)   #  Чтобы нельзя было использовать главное окно в этот момент



output_table()
# Взаимодействие с интерфесом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))
form.choiceTable.currentTextChanged.connect(lambda: output_table(db_name=form.choiceTable.currentText()))
form.AddField.clicked.connect(add_field_window)

# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока