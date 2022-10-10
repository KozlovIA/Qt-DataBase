import sys
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication
from source.functional import *
from time import sleep
from PyQt6.QtCore import QThread
from PySide6.QtWidgets import QMessageBox

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
    table_dict = {'Таблица НИР': 'Vyst_mo', 'Таблица ВУЗов': 'VUZ', 'Таблица ГРНТИ': 'grntirub'}
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


def add_field_window(Edit=False):
    """Функция создания окна для добавления или редактирования строк в Таблице НИР"""
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
    grnti_code = list(map(str, grnti_code)); grnti_code.insert(0, '-')
    for i in range(1, len(grnti_code)):
        if len(grnti_code[i]) == 1: grnti_code[i] = '0' + grnti_code[i]
    all_code = ['-']; [all_code.append(str(i)) for i in range(0, 91)]
    for i in range(1, len(all_code)):
        if len(all_code[i]) == 1: all_code[i] = '0' + all_code[i]
    form_AddField.GRNTI1_1_cb.addItems(grnti_code)
    form_AddField.GRNTI1_2_cb.addItems(all_code)
    form_AddField.GRNTI1_3_cb.addItems(all_code)
    form_AddField.GRNTI2_1_cb.addItems(grnti_code)
    form_AddField.GRNTI2_2_cb.addItems(all_code)
    form_AddField.GRNTI2_3_cb.addItems(all_code)
    form_AddField.SaveButton.clicked.connect(window_AddField.close)
    if Edit:
        selected = form.tableView.currentIndex().row()
        if selected == -1:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка!")
            #msg.setWindowIcon(QtGui.QIcon("source/warning-icon.png"))
            msg.setText("Для редактирования выберете строку!")
            msg.setIcon(QMessageBox.Warning)
            #msg.icon("source/warning.icon")
            msg.exec()
            return
        list_values = [form.tableView.model().index(selected, i).data() for i in range(11)]
        form_AddField.university_code_cb.setCurrentText(str(list_values[0]) + "\t" + list_values[1])    # Устанавливает значение по текущесу тексту, только если такой элемент уже есть в списке QComboBox
        form_AddField.Subject_le.setText(str(list_values[2]))
        form_AddField.regNum_le.setText(str(list_values[3]))
        # ГРНТИ
        GRNTI = str(list_values[4])
        if ',' in GRNTI:
            GRNTI = GRNTI.split(',')
        elif ';' in GRNTI:
            GRNTI = GRNTI.split(';')
        if str(type(GRNTI)) == "<class 'list'>" and len(GRNTI) > 1:
            GRNTI[0] = GRNTI[0].split('.'); GRNTI[1] = GRNTI[1].split('.')
            form_AddField.GRNTI1_1_cb.setCurrentText(GRNTI[0][0]);  form_AddField.GRNTI2_1_cb.setCurrentText(GRNTI[1][0])
            form_AddField.GRNTI1_2_cb.setCurrentText(GRNTI[0][1]);  form_AddField.GRNTI2_2_cb.setCurrentText(GRNTI[1][1])
            if len(GRNTI[0]) == 3:  form_AddField.GRNTI1_3_cb.setCurrentText(GRNTI[0][2])
            if len(GRNTI[1]) == 3:  form_AddField.GRNTI2_3_cb.setCurrentText(GRNTI[1][2])
        else:
            GRNTI = GRNTI.split('.')
            form_AddField.GRNTI1_1_cb.setCurrentText(GRNTI[0])
            form_AddField.GRNTI1_2_cb.setCurrentText(GRNTI[1])
            if len(GRNTI) == 3: form_AddField.GRNTI1_3_cb.setCurrentText(GRNTI[2])

        form_AddField.type_cb.setCurrentText(str(list_values[5]))
        form_AddField.TypeExhibit_cb.setCurrentText(str(list_values[6]))
        form_AddField.Exhibitions_le.setText(str(list_values[7]))
        form_AddField.Exhibit_le.setText(str(list_values[8]))
        form_AddField.BossName_le.setText(str(list_values[9]))
        form_AddField.BossStatus_le.setText(str(list_values[10]))
        

    window_AddField.show()
    #window.setEnabled(False)   #  Чтобы нельзя было использовать главное окно в этот момент



output_table()
# Взаимодействие с интерфесом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))
form.choiceTable.currentTextChanged.connect(lambda: output_table(table_name=form.choiceTable.currentText()))
form.AddField.clicked.connect(add_field_window)
form.EditField.clicked.connect(lambda: add_field_window(Edit=True))

# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока