import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from source.functional import *
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
def output_table(table_name="Таблица НИР"):
    """Функция отображения таблицы"""
    table_dict = {'Таблица НИР': 'VUZ', 'Таблица выставок': 'Vyst_mo', 'Таблица ГРНТИ': 'grntirub'}
    #global db
    #db = db_connect()
    if not db:  # db - глобальная переменная ссылающаяся на базу данных, создается с модуле functional.py строка 23 после функции db_connect()
        form.dbInfo.setText('Ошибка подключения к базе данных "' + table_name + '"')
        return
    form.dbInfo.setText('Подключено к базе данных "' + table_name + '"')
    db_model = QSqlTableModel()  # Создали объект таблицы
    db_model.setTable(table_dict[table_name])     # Привязали таблицу из базы данных
    db_model.select()        # Выбрали все строки из данной таблицы
    form.tableView.setModel(db_model)
    form.tableView.setSortingEnabled(True)


end_of_work = False     # для завершения потока изменения размера окна


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
    global window_AddField, form_AddField
    Form, Window = uic.loadUiType("source/EditWindow.ui")  # файл MainFormResize создается в функции gridLayoutStartResize, если поставить MainForm.ui, интерфейс не будет изменять размер в большую сторону
    # Настройка интерфейса
    window_AddField = Window()
    form_AddField = Form()
    form_AddField.setupUi(window_AddField)
    univer_dict, grnti_code = SQLdata_acquisition_EditWindow()[0:2]
    # Ввод корректных кодов ВУЗов
    univer_code = list(univer_dict.keys()); #univer_code.sort()
    univer_view = [str(code) + "\t" + univer_dict[code] for code in univer_code]   # хитрые пару строк, чтобы выводился и код и название
    form_AddField.university_code_cb.addItems(univer_view)
    # Ввод корректных кодов ГРНТИ
    grnti_code = list(map(str, grnti_code))
    form_AddField.GRNTI1_1_cb.addItems(grnti_code)
    form_AddField.GRNTI1_2_cb.addItems(grnti_code)
    form_AddField.GRNTI1_3_cb.addItems(grnti_code)
    form_AddField.GRNTI2_1_cb.addItems(grnti_code)
    form_AddField.GRNTI2_2_cb.addItems(grnti_code)
    form_AddField.GRNTI2_3_cb.addItems(grnti_code)
    window_AddField.show()
    form_AddField.SaveButton.clicked.connect(window_AddField.close)
    #window.setEnabled(False)   #  Чтобы нельзя было использовать главное окно в этот момент



output_table()
# Взаимодействие с интерфесом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))
form.choiceTable.currentTextChanged.connect(lambda: output_table(table_name=form.choiceTable.currentText()))
form.AddField.clicked.connect(add_field_window)

# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока