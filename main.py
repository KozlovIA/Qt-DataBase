from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog
from cv2 import exp
from source.functional import *
from time import sleep
from PyQt6.QtCore import QThread, QEvent
from threading import Thread
import time

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
    if table_name == "Таблица НИР":
        form.AddField.setEnabled(True); form.EditField.setEnabled(True); form.deleteButton.setEnabled(True)
    else: form.AddField.setEnabled(False); form.EditField.setEnabled(False); form.deleteButton.setEnabled(False)
    if not db:  # db - глобальная переменная ссылающаяся на базу данных, создается с модуле functional.py строка 23 после функции db_connect()
        form.dbInfo.setText('Ошибка подключения к базе данных "' + table_name + '"')
        return
    form.dbInfo.setText('Подключено к базе данных "' + table_name + '"')
    global db_model
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

def saveSQL_data(Edit, orig_univer_code, orig_regNum):
    """Функция сохранения данных в таблицу.
    Входные параметры Edit - если это редактирование,
    так же приреадактировании должн передаваться первичный ключ orig_univer_code - изначальный код ВУЗа, orig_regNum - изначальный регистрационный номер"""
    univer_code_name = form_AddField.university_code_cb.currentText()
    univer_code_name = univer_code_name.split('\t')
    subject = form_AddField.Subject_le.text()
    reg_num = form_AddField.regNum_le.text()

    # ГРНТИ
    GRNTI = ""
    if form_AddField.GRNTI_1_le.text() != '..':
        GRNTI = form_AddField.GRNTI_1_le.text()
        if GRNTI[len(GRNTI)-2:len(GRNTI)-1] == '..':  GRNTI = GRNTI[0:len(GRNTI)-2]     # довольно кринжовая обработка разного количества цифр
        if GRNTI[len(GRNTI)-1] == '.':  GRNTI = GRNTI[0:len(GRNTI)-1]
    if form_AddField.GRNTI_2_le.text() != '..':
        GRNTI += ';' + form_AddField.GRNTI_2_le.text()
        if GRNTI[len(GRNTI)-2:len(GRNTI)-1] == '..':  GRNTI = GRNTI[0:len(GRNTI)-2]
        if GRNTI[len(GRNTI)-1] == '.':  GRNTI = GRNTI[0:len(GRNTI)-1]
    ########################
    type_EM = form_AddField.type_cb.currentText()
    TypeExhibit = form_AddField.TypeExhibit_cb.currentText()
    Exhibitions = form_AddField.Exhibitions_te.toPlainText()
    Exhibit = form_AddField.Exhibit_te.toPlainText()
    BossName = form_AddField.BossName_le.text()
    BossStatus = form_AddField.BossStatus_le.text()

    data_dict = {
        "Код_ВУЗа": univer_code_name[0],
        "Аббревиатура": univer_code_name[1],
        "Предмет": subject,
        "Рег_номер": reg_num,
        "ГРНТИ": GRNTI,
        "Тип": type_EM,
        "Наличие_экспоната": TypeExhibit,
        "Выставки": Exhibitions,
        "Экспонат": Exhibit,
        "Научный_руководитель": BossName,
        "Статус_руководителя": BossStatus
    }
    editingSQL_NIR(Edit=Edit, parameters_dict=data_dict, orig_univer_code=orig_univer_code, orig_regNum=orig_regNum)
    window_AddField.close()
    #window.setEnabled(True)
    output_table(table_name=form.choiceTable.currentText())     # для мгновенного обновления

    # Установка курсора на строку
    i = 0
    while True:
        list_values = [form.tableView.model().index(i, j).data() for j in range(11)]
        if list_values == [None, None, None, None, None, None, None, None, None, None, None]: break
        list_values = list(map(str, list_values))
        if (str(univer_code_name[0]) and str(reg_num)) in list_values:
            form.tableView.selectRow(i)
            break
        i+=1




def add_field_window(Edit=False):
    """Функция создания окна для добавления или редактирования строк в Таблице НИР"""
    global window_AddField, form_AddField
    Form, Window = uic.loadUiType("source/EditWindow.ui")
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
    """ grnti_code = list(map(str, grnti_code)); grnti_code.insert(0, '-')
    for i in range(1, len(grnti_code)):
        if len(grnti_code[i]) == 1: grnti_code[i] = '0' + grnti_code[i]
    all_code = ['-']; [all_code.append(str(i)) for i in range(0, 91)]
    for i in range(1, len(all_code)):
        if len(all_code[i]) == 1: all_code[i] = '0' + all_code[i]
    """
    form_AddField.GRNTI_1_le.setInputMask('00.00.00;_'); form_AddField.GRNTI_2_le.setInputMask('00.00.00;_')
    orig_univerCode = orig_regNum = ''
    if Edit:
        # Если это окно редактирования, а не добавления, то мы выводим существующую информацию
        selected = form.tableView.currentIndex().row()  # текущая отмеченная строка
        if selected == -1:
            msg = QMessageBox()
            msg.setWindowTitle("Внимание!")
            msg.setWindowIcon(QtGui.QIcon("source/warning-icon.png"))
            msg.setText("Для редактирования выберете строку!")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
            return
        list_values = [form.tableView.model().index(selected, i).data() for i in range(11)]     # Получение данных из таблицы
        # для дальнейшего передачи как параметра, сохраняем код ВУЗа и регистрационный номер, чтобы использовать их как метки для редактирования
        orig_univerCode = list_values[0]; orig_regNum = str(list_values[3])
        form_AddField.university_code_cb.setCurrentText(str(list_values[0]) + "\t" + list_values[1])    # Устанавливает значение по текущему тексту, только если такой элемент уже есть в списке QComboBox
        form_AddField.Subject_le.setText(str(list_values[2]))
        form_AddField.regNum_le.setText(str(list_values[3]))
        # ГРНТИ
        GRNTI = str(list_values[4])
        if ',' in GRNTI:
            GRNTI = GRNTI.split(',')
        elif ';' in GRNTI:
            GRNTI = GRNTI.split(';')
        if str(type(GRNTI)) == "<class 'list'>" and len(GRNTI) > 1:
            form_AddField.GRNTI_1_le.setText(GRNTI[0])
            form_AddField.GRNTI_2_le.setText(GRNTI[1])
        else:
            form_AddField.GRNTI_1_le.setText(GRNTI)
        # остальные поля
        form_AddField.type_cb.setCurrentText(str(list_values[5]))
        form_AddField.TypeExhibit_cb.setCurrentText(str(list_values[6]))
        form_AddField.Exhibitions_te.setText(str(list_values[7]))
        form_AddField.Exhibit_te.setText(str(list_values[8]))
        form_AddField.BossName_le.setText(str(list_values[9]))
        form_AddField.BossStatus_le.setText(str(list_values[10]))

    
    form_AddField.CancelButton.clicked.connect(lambda: window_AddField.close() and window.setEnabled(True))    # Не уверен, что подобный вызов 2-х функций корректное занятие, но оно работает
    form_AddField.SaveButton.clicked.connect(lambda: saveSQL_data(Edit=Edit, orig_univer_code=orig_univerCode, orig_regNum=orig_regNum))   # Тут и осуществляется вызов функции для записи данных

    window_AddField.show()
    # проблема при нажатии на крестик, окно не становится Enabled 
    #window.setEnabled(False)   #  Чтобы нельзя было использовать главное окно в этот момент



def delete_row():
    """Удаляет выбранную строку"""
    selected = form.tableView.selectedIndexes()  # текущие отмеченные строки
    index_set = set(index.row() for index in selected)
    if len(selected) == 0:
        msg = QMessageBox()
        msg.setWindowTitle("Внимание!")
        msg.setWindowIcon(QtGui.QIcon("source/warning-icon.png"))
        msg.setText("Для удаления выберете строку!")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()
        return
    # инфа о нажатиях QMessageBox https://coderlessons.com/tutorials/python-technologies/izuchite-pyqt/pyqt-qmessagebox
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    if len(index_set) > 1: str_ = "строки"
    else: str_ = "строку"
    msg.setText(f"Вы действительно хотите удалить {str_}?")
    msg.setWindowTitle("Удаление")
    msg.setWindowIcon(QtGui.QIcon("source/delete-icon.png"))
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    global reply; reply="Cancel"
    msg.buttonClicked.connect(msgbtn)
    msg.exec()
    if reply == "OK":
        for index in index_set:
            db_model.removeRow(index)
    del reply
    output_table(table_name=form.choiceTable.currentText())     # для мгновенного обновления
	
def msgbtn(i):
    global reply
    reply = i.text()


output_table()
# Взаимодействие с интерфесом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))
form.choiceTable.currentTextChanged.connect(lambda: output_table(table_name=form.choiceTable.currentText()))
form.AddField.clicked.connect(add_field_window)
form.EditField.clicked.connect(lambda: add_field_window(Edit=True))
form.deleteButton.clicked.connect(delete_row)
#form.FiltrationButton.clicked.connect(lambda: pass)

# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока