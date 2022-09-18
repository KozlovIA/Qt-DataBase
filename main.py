from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from functional import *
from threading import Thread
from time import sleep
from PyQt6.QtCore import QThread

gridLayoutStartResize()     # изменнение размеров основного слоя gridLayout в MainForm для корректного изменения размеров виджетов

Form, Window = uic.loadUiType("MainFormResize.ui")  # файл MainFormResize создается в функции gridLayoutStartResize, если поставить MainForm.ui, интерфейс не будет изменять размер в большую сторону

# Настройка интерфейса
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Функции взаимодйствия
def output_table(db_name="VUZ"):
    """Функция отображения таблицы"""
    namesUI = ['Таблица ВУЗов', 'Таблица выставок', 'Таблица ГРНТИ']; table_names = ['VUZ', 'Vyst_mo', 'grntirub']; i = 0
    for i in range(len(namesUI)):
        if db_name == namesUI[i]:
            db_name = table_names[i]
            break
    db = db_connect()
    if not db:
        form.dbInfo.setText('Ошибка подключения к базе данных "' + str(namesUI[i]) + '"')
        return
    form.dbInfo.setText('Подключено к базе данных "' + str(namesUI[i]) + '"')
    db = QSqlTableModel()  # Создали объект таблицы
    db.setTable(db_name)     # Привязали таблицу из базы данных
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


output_table()
# Взаимодействие с интерфесом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))
#form.output_db.clicked.connect(output_table)
#form.pushButton.clicked.connect(test)
form.choiceTable.currentTextChanged.connect(lambda: output_table(db_name=form.choiceTable.currentText()))

# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока