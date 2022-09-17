from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from functional import *

Form, Window = uic.loadUiType("MainForm.ui")

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


# взаимодействие с интерфесом
form.output_db.clicked.connect(output_table)


# Запуск приложения
window.show()
app.exec()