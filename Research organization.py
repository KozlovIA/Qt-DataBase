# -*- coding: utf-8 -*-
from PyQt6 import uic, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QMessageBox, QFileDialog
from source.functional import *
from time import sleep
from PyQt6.QtCore import QThread, QRect
import pandas as pd
import os

gridLayoutStartResize()     # изменнение размеров основного слоя gridLayout в MainForm для корректного изменения размеров виджетов
GRNTI_dict = get_GRNTI()    # ГРНТИ коды в формате {"[Код_ВУЗа, Рег_номер]": "ГРНТИ"}

Form, Window = uic.loadUiType("MainFormResize.ui")  # файл MainFormResize создается в функции gridLayoutStartResize, если поставить MainForm.ui, интерфейс не будет изменять размер в большую сторону
#Form, Window = uic.loadUiType("MainForm.ui")

# Настройка интерфейса
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

headlines = ["Аббревиатура", "Название_НИР", "Рег_номер", "ГРНТИ", "Тип", "Наличие_экспоната", "Выставки", 
                "Экспонат", "Научный_руководитель", "Статус_руководителя", "Код_ВУЗа"]

def recNum():
    """Функция для подсчета числа строк в таблицах"""
    recCount = 0
    model_temp = form.tableView.model()
    model_temp.fetchMore(QtCore.QModelIndex())
    while True:
        list_values = [model_temp.index(recCount, j).data() for j in range(11)]
        if list_values == [None, None, None, None, None, None, None, None, None, None, None]: break
        recCount+=1
    form.recNum_lb.setText("Всего строк: " + str(recCount))
    if recCount == 0:
        msgError("Записи не найдены!")
        set_filter_value()  # Сброс значений фильтра


def set_tableChoiceItems(table="source"):
    """Открытие таблицы в окне ChoiceTableWindow.ui"""
    if table == "source":
        table_list = ['Таблица НИР', 'Таблица ВУЗов', 'Таблица ГРНТИ']
        ico_file = "source/image/data-integration-icon.png"

    if table == "custom":
        table_list = get_custom_table()
        ico_file = "source/image/create-table-icon.png"
        if len(table_list) == 0:
            msgError("Группы НИР не найдены!")
            return

    ico = QtGui.QIcon()
    ico.addFile(ico_file)

    global window_OpenTable, form_OpenTable
    Form, Window = uic.loadUiType("source/ChoiceTableWindow.ui")
    # Настройка интерфейса
    window_OpenTable = Window()
    form_OpenTable = Form()
    form_OpenTable.setupUi(window_OpenTable)

    for name in table_list:
        form_OpenTable.choiceTable.addItem(ico, name)
    if currentTable in table_list:
        form_OpenTable.choiceTable.setCurrentText(currentTable)
    else:
        form_OpenTable.choiceTable.setCurrentText(table_list[0])
    form_OpenTable.OK_bn.clicked.connect(lambda: output_table(table_name=form_OpenTable.choiceTable.currentText()))

    window_OpenTable.show()


    
def output_table(table_name="Таблица НИР", choice_close="False"):
    """Функция отображения таблицы.
    table_name - имя таблицы, choice_close - логический параметр отвечающий за закрытие окна выбора таблицы"""
    global currentTable # текущая выбранная таблица
    currentTable = table_name
    if choice_close:
        try:
            global window_OpenTable
            window_OpenTable.close()
        except:
            pass
    table_dict = {'Таблица НИР': 'Vyst_mo', 'Таблица ВУЗов': 'VUZ', 'Таблица ГРНТИ': 'grntirub'}
    #global db
    #db = db_connect()
    form.filtering_bn.setEnabled(False)
    form.filtering_prompt.setText("")
    if table_name == "Таблица НИР":
        form.filtering_bn.setEnabled(True)
        form.addGroup_action.setEnabled(True)
        form.EditTable_menu.setEnabled(True)
        form.addToGroup_action.setEnabled(True)
        form.creatingResearchCard_action.setEnabled(True)
        form.deleteFromGroup_action.setEnabled(False)
    else:
        form.EditTable_menu.setEnabled(False)
        form.addGroup_action.setEnabled(False)
        form.addToGroup_action.setEnabled(False)
        form.deleteFromGroup_action.setEnabled(False)
        form.creatingResearchCard_action.setEnabled(False)
    global db_model
    if not (table_name in list(table_dict.keys())):
        if table_name == '': return
        if table_name == '-':
            form.tableView.clearSpans()
            db_model = QSqlTableModel()
            form.tableView.setModel(db_model)
            return
        output_custom_table(table_name=table_name)
        form.addToGroup_action.setEnabled(True)
        form.deleteFromGroup_action.setEnabled(True)
        form.addGroup_action.setEnabled(True)
        form.deleteGroup_action.setEnabled(True)
        form.creatingResearchCard_action.setEnabled(True)
        form.dbInfo.setText('Группа НИР: "' + table_name + '"')
        return
    if not db:  # db - глобальная переменная ссылающаяся на базу данных, создается с модуле functional.py строка 23 после функции db_connect()
        form.dbInfo.setText('Ошибка подключения к базе данных "' + table_name + '"')
        return
    form.dbInfo.setText(table_name)
    db_model = QSqlTableModel()  # Создали объект таблицы
    db_model.setTable(table_dict[table_name])     # Привязали таблицу из базы данных
    db_model.select()        # Выбрали все строки из данной таблицы
    form.tableView.setModel(db_model)
    form.tableView.setSortingEnabled(True)
    
    # model = form.tableView.model(); model.fetchMore() используется для считывания всех данных таблицы
    global modelFetchMore
    modelFetchMore = form.tableView.model()
    modelFetchMore.fetchMore()
    recNum()


def output_custom_table(table_name):
    """Вывод кастомных таблиц"""
    if os.path.exists("data"):
        file = open("data/" + table_name + ".dat", 'r', encoding='utf-8')
        data = []
        for line in file:
            data.append(eval(line))
        file.close()

        table_model = QtGui.QStandardItemModel()
        # set table headers
        table_model.setColumnCount(len(headlines))
        table_model.setHorizontalHeaderLabels(headlines)
        form.tableView.horizontalHeader().setStretchLastSection(True)

        # fill table model data
        for row_idx in range(len(data)):
            row = list()
            for col_idx in range(len(data[row_idx])):
                val = QtGui.QStandardItem(str(data[row_idx][col_idx]))
                row.append(val)
            table_model.appendRow(row)
        # set table model to table object
        form.tableView.setModel(table_model)

        # model = form.tableView.model(); model.fetchMore() используется для считывания всех данных таблицы
        global modelFetchMore
        modelFetchMore = form.tableView.model()
        modelFetchMore.fetchMore(QtCore.QModelIndex())
        recNum()


    
end_of_work = False     # для завершения потока изменения размера окна
class ResizeThread(QThread):
    """Класс для изменения размеров виджетов вместе с размером окна"""
    def __init__(self, parent=None):
        super(ResizeThread, self).__init__(parent)

    def run(self):
        while True:
            try:
                if end_of_work: return
                geometry = form.centralwidget.geometry()
                size = eval(str(geometry)[18:])[2:4]
                form.gridLayout.setGeometry(QRect(0, 0, size[0], int(size[1]*(670/700))))
                sleep(0.1)
            except:
                pass#print("Error Resize")
# с кнопкой почему-то не выдает "Timers cannot be started from another thread", а со слоем выдает
# менять каждый виджет отдельно, как решение, но это нужно ещё один алгоритм писать, пока что лень
resizeThread = ResizeThread()
resizeThread.start()

def saveSQL_data(Edit, orig_univer_code, orig_regNum):
    """Функция сохранения данных в таблицу.
    Входные параметры Edit - если это редактирование,
    так же приреадактировании должн передаваться первичный ключ orig_univer_code - изначальный код ВУЗа, orig_regNum - изначальный регистрационный номер"""
    type_dict = {"Тематический план": "Е", "НТП": "М"}
    typeExhibit_dict = {"Есть": "Е", "Нет": "Н", "Планируется": "П"}

    univer_code_name = form_AddField.university_code_cb.currentText()
    univer_code_name = univer_code_name.split('\t')
    subject = form_AddField.Subject_te.toPlainText()
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
    type_EM = type_dict[form_AddField.type_cb.currentText()]
    TypeExhibit = typeExhibit_dict[form_AddField.TypeExhibit_cb.currentText()]
    Exhibitions = form_AddField.Exhibitions_te.toPlainText()
    Exhibit = form_AddField.Exhibit_te.toPlainText()
    BossName = form_AddField.BossName_le.text()
    BossStatus = form_AddField.BossStatus_le.text()

    data_dict = {
        "Код_ВУЗа": univer_code_name[0],
        "Аббревиатура": univer_code_name[1],
        "Название_НИР": subject,
        "Рег_номер": reg_num,
        "ГРНТИ": GRNTI,
        "Тип": type_EM,
        "Наличие_экспоната": TypeExhibit,
        "Выставки": Exhibitions,
        "Экспонат": Exhibit,
        "Научный_руководитель": BossName,
        "Статус_руководителя": BossStatus
    }
    # Обработка некорректных данных
    msgErr = ""
    if reg_num == '':    msgErr = "Введите регистрационный номер!"; msgError(msgErr); return
    if GRNTI == '':    msgErr = "Введите код ГРНТИ!"; msgError(msgErr); return
    if len(subject) < 5:    msgErr = "Введите тематику НИР!"; msgError(msgErr); return
    if TypeExhibit != 'Н' and len(Exhibitions) < 5:    msgErr = "Введите название выставки!"; msgError(msgErr); return
    if TypeExhibit != 'Н' and len(Exhibit) < 5:    msgErr = "Введите название экспоната!"; msgError(msgErr); return
    if len(BossName) < 3:    msgErr = "Введите имя научного руководителя!"; msgError(msgErr); return
    if len(BossStatus) < 3:    msgErr = "Введите статус научного руководителя!"; msgError(msgErr); return

    editingSQL_NIR(Edit=Edit, parameters_dict=data_dict, orig_univer_code=orig_univer_code, orig_regNum=orig_regNum)
    window_AddField.close()
    #window.setEnabled(True)
    output_table(table_name=currentTable)     # для мгновенного обновления

    # Установка курсора на строку
    i = 0
    model_fetchMore = form.tableView.model()
    model_fetchMore.fetchMore()
    while True:
        list_values = [model_fetchMore.index(i, j).data() for j in range(11)]
        if list_values == [None, None, None, None, None, None, None, None, None, None, None]: break
        list_values = list(map(str, list_values))
        if (str(univer_code_name[0]) and str(reg_num)) in list_values:
            form.tableView.selectRow(i)
            break
        i+=1

def msgError(msgErr):
    """Функция вывода ошибок.
    msgErr - текст ошибки"""
    msg = QMessageBox()
    msg.setWindowTitle("Внимание!")
    msg.setWindowIcon(QtGui.QIcon("source/image/warning-icon.png"))
    msg.setText(msgErr)
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.exec()


def add_field_window(Edit=False):
    """Функция создания окна для добавления или редактирования строк в Таблице НИР"""
    global window_AddField, form_AddField
    Form, Window = uic.loadUiType("source/EditWindow.ui")
    # Настройка интерфейса
    window_AddField = Window()
    form_AddField = Form()
    form_AddField.setupUi(window_AddField)
    window_AddField.setWindowTitle("Добавление")
    univer_dict, grnti_code = SQLdata_acquisition_EditWindow()[0:2]
    # словари типа экспоната и его наличия, служат для более красивого вывода
    type_dict = {'Е': "Тематический план", "М": "НТП"}
    typeExhibit_dict = {"Е": "Есть", "Н": "Нет", "П": "Планируется"}
    # Ввод корректных кодов ВУЗов
    univer_code = list(univer_dict.keys()); #univer_code.sort()
    univer_view = [str(code) + "\t" + univer_dict[code] for code in univer_code]   # хитрые пару строк, чтобы выводился и код и название
    form_AddField.university_code_cb.addItems(univer_view)
    # Ввод корректных кодов ГРНТИ
    form_AddField.GRNTI_1_le.setInputMask('00.00.00;_'); form_AddField.GRNTI_2_le.setInputMask('00.00.00;_')
    orig_univerCode = orig_regNum = ''
    if Edit:
        window_AddField.setWindowTitle("Редактирование")
        # Если это окно редактирования, а не добавления, то мы выводим существующую информацию
        selected = form.tableView.currentIndex().row()  # текущая отмеченная строка
        if selected == -1:
            msgError("Для редактирования выберете строку!")
            return
        list_values = [modelFetchMore.index(selected, i).data() for i in range(11)]     # Получение данных из таблицы
        # для дальнейшего передачи как параметра, сохраняем код ВУЗа и регистрационный номер, чтобы использовать их как метки для редактирования
        orig_univerCode = list_values[10]; orig_regNum = str(list_values[2])
        form_AddField.university_code_cb.setCurrentText(str(list_values[10]) + "\t" + list_values[0])    # Устанавливает значение по текущему тексту, только если такой элемент уже есть в списке QComboBox
        form_AddField.Subject_te.setText(str(list_values[1]))
        form_AddField.regNum_le.setText(str(list_values[2]))
        # ГРНТИ
        GRNTI = str(list_values[3])
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
        form_AddField.type_cb.setCurrentText(type_dict[str(list_values[4])])
        form_AddField.TypeExhibit_cb.setCurrentText(typeExhibit_dict[str(list_values[5])])
        form_AddField.Exhibitions_te.setText(str(list_values[6]))
        form_AddField.Exhibit_te.setText(str(list_values[7]))
        form_AddField.BossName_le.setText(str(list_values[8]))
        form_AddField.BossStatus_le.setText(str(list_values[9]))

    
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
        msgError("Для удаления выберете строку!")
        return
    # инфа о нажатиях QMessageBox https://coderlessons.com/tutorials/python-technologies/izuchite-pyqt/pyqt-qmessagebox
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    if len(index_set) > 1: str_ = "строки"
    else: str_ = "строку"
    msg.setText(f"Вы действительно хотите удалить {str_}?")
    msg.setWindowTitle("Удаление")
    msg.setWindowIcon(QtGui.QIcon("source/image/delete-icon.png"))
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    global reply; reply="Cancel"
    msg.buttonClicked.connect(msgbtn)
    msg.exec()
    if reply == "OK":
        for index in index_set:
            db_model.removeRow(index)
    del reply
    output_table(table_name=currentTable)     # для мгновенного обновления
	
def msgbtn(i):
    """Для получения значения нажатия в случае ошибки QMessageBox"""
    global reply
    reply = i.text()

def set_filter_value(info_dict=False, typeExhibit_dict_revers={"Е": "Есть", "Н": "Нет", "П": "Планируется"}):
    """Добавляет первоначальные значения фильтров в comboboxes
    info_dict - если окно уже есть, то запрос будет создан в зависимости от текущих значений фильтра"""
    form.dbInfo.setText("Фильтрация")
    form.filtering_prompt.setText("На основе фильтрации можно создать группу НИР")
    global form_Filtering
    if info_dict==False: 
        info_dict = get_info_for_filtration()   # словарь по {коду ВУЗа, [Аббревиатура, Федеральный округ, Город, Область]}
        output_table()
        Edit = False
    else:
        Edit = True

    # Сохранение текущих значений
    university_cb_value = form_Filtering.university_cb.currentText()
    federalDistrict_cb_value = form_Filtering.federalDistrict_cb.currentText()
    city_cb_value = form_Filtering.city_cb.currentText()
    region_cb_value = form_Filtering.region_cb.currentText()
    preference_exibit_cb_value = form_Filtering.preference_exibit_cb.currentText()
    GRNTI_1_cb_value = form_Filtering.GRNTI_1_cb.currentText()
    GRNTI_2_cb_value = form_Filtering.GRNTI_2_cb.currentText()

    form_Filtering.federalDistrict_cb.clear()
    form_Filtering.city_cb.clear()
    form_Filtering.region_cb.clear()
    form_Filtering.GRNTI_1_cb.clear()
    form_Filtering.GRNTI_2_cb.clear()
    form_Filtering.university_cb.clear()
    form_Filtering.preference_exibit_cb.clear()
    form_Filtering.preference_exibit_cb.addItem("-")
    form_Filtering.federalDistrict_cb.addItem('-')
    form_Filtering.city_cb.addItem('-')
    form_Filtering.region_cb.addItem('-')
    form_Filtering.GRNTI_1_cb.addItem('-')
    form_Filtering.GRNTI_2_cb.addItem('-')
    form_Filtering.university_cb.addItem('-')
    # Добавление в списки, а затем в QComboBoxes значений
    fed_district = []; city = []; region = []; uni_list = []
    for code_uni in list(info_dict.keys()):
        uni_list.append(info_dict[code_uni][0])
        fed_district.append(info_dict[code_uni][1])
        city.append(info_dict[code_uni][2])
        region.append(info_dict[code_uni][3])
    uni_list.sort()
    fed_district = set(fed_district); fed_district = list(fed_district)
    fed_district.sort()
    city = set(city); city = list(city)
    city.sort()
    region = set(region); region = list(region)
    region.sort()
    preference_exibit = list(typeExhibit_dict_revers.values())
    preference_exibit.sort()
    form_Filtering.university_cb.addItems(uni_list)
    form_Filtering.federalDistrict_cb.addItems(fed_district)
    form_Filtering.city_cb.addItems(city)
    form_Filtering.region_cb.addItems(region)
    form_Filtering.preference_exibit_cb.addItems(preference_exibit)

    # ГРНТИ как обычно отдельно
    GRNTI_list = get_GRNTI_fromGRNTItable()
    GRNTI_list.sort()
    form_Filtering.GRNTI_1_cb.addItems(GRNTI_list)
    form_Filtering.GRNTI_2_cb.addItems(GRNTI_list)

    # Установка значений фильтра на место
    if Edit:
        form_Filtering.university_cb.setCurrentText(university_cb_value)
        form_Filtering.federalDistrict_cb.setCurrentText(federalDistrict_cb_value)
        form_Filtering.city_cb.setCurrentText(city_cb_value)
        form_Filtering.region_cb.setCurrentText(region_cb_value)
        form_Filtering.preference_exibit_cb.setCurrentText(preference_exibit_cb_value)
        form_Filtering.GRNTI_1_cb.setCurrentText(GRNTI_1_cb_value)
        form_Filtering.GRNTI_2_cb.setCurrentText(GRNTI_2_cb_value)



def filtration():
    """Фильтрация таблицы НИР"""
    window_Filtering.hide()
    global form_Filtering
    form.EditTable_menu.setEnabled(False)
    typeExhibit_dict = {"Есть": "Е", "Нет": "Н", "Планируется": "П", "-": "-"}
    fed_Distr = form_Filtering.federalDistrict_cb.currentText()
    city = form_Filtering.city_cb.currentText()
    region = form_Filtering.region_cb.currentText()
    preference_exibit = typeExhibit_dict[form_Filtering.preference_exibit_cb.currentText()]
    GRNTI_1 = form_Filtering.GRNTI_1_cb.currentText()[0:2]      # Коды из фильтра
    GRNTI_2 = form_Filtering.GRNTI_2_cb.currentText()[0:2]
    univer = form_Filtering.university_cb.currentText()


    info_dict = {}
    if fed_Distr != '-': info_dict.update({"Федеральный_округ": fed_Distr})
    if city != '-': info_dict.update({"Город": city})
    if region != '-': info_dict.update({"Область": region})
    if univer != '-': info_dict.update({"Аббревиатура": univer})
    if preference_exibit != '-': info_dict.update({"Наличие_экспоната": preference_exibit})
        #"ГРНТИ": [GRNTI_1, GRNTI_2],
    

    where_VUZ = ""; where_Vyst_mo = "("
    # Создаем условия для запросов SQL
    for key in list(info_dict.keys()):
        if key == "ГРНТИ" or key == "Наличие_экспоната" or key == "Аббревиатура":
            where_Vyst_mo += key + '="' + str(info_dict[key]) + '" AND '
        else:
            where_VUZ += key + '="' + str(info_dict[key]) + '" AND '
    if where_VUZ != "":
        where_VUZ = "WHERE " + where_VUZ[0:(len(where_VUZ)-4)]
    if where_Vyst_mo != "(":
        where_Vyst_mo = where_Vyst_mo[0:(len(where_Vyst_mo)-4)]
        where_Vyst_mo += ')'
    elif where_Vyst_mo == "(":   where_Vyst_mo = ""


    # Делаем запрос сначала в VUZ, получаем номера ВУЗов и добавляем их в условие к таблицу Vyst_mo, изи ГГ
    query = QSqlQuery()

    if where_VUZ != '':
        query.exec(f"""SELECT Код_ВУЗа FROM VUZ {where_VUZ}""")
        first_loop = True
        while query.next():
            if first_loop and where_Vyst_mo != "":
                where_Vyst_mo += " AND "
            if first_loop:
                where_Vyst_mo += "("
            first_loop = False
            where_Vyst_mo = where_Vyst_mo + "Код_ВУЗа=" + str(query.value("Код_ВУЗа")) + " OR "
    if where_Vyst_mo[-3:-1] == "OR":
        where_Vyst_mo = where_Vyst_mo[0:len(where_Vyst_mo)-4]
        where_Vyst_mo += ')'
    
    # фильтрация грнти через регистрационный номер
    code_and_reg_num = []
    for key in list(GRNTI_dict.keys()):
        # отбор кодов по первым 2-м числам в коде грнти
        _grnti = GRNTI_dict[key].split(';')
        if len(_grnti) > 1:
            _grnti_0 = _grnti[0].split('.')
            _grnti_1 = _grnti[1].split('.')
            if len(_grnti_0) == 3:  # Удаление 3-го кода ГРНТИ
                _grnti_0.pop(2)
            if len(_grnti_1) == 3:
                _grnti_1.pop(2)
            if GRNTI_1 != '-' and GRNTI_2 != '-':
                if ((GRNTI_1 in _grnti_0 and GRNTI_2 in _grnti_1) or (GRNTI_1 in _grnti_1 and GRNTI_2 in _grnti_0)):
                #or (GRNTI_1 in _grnti_0 and GRNTI_2 in _grnti_0) or (GRNTI_1 in _grnti_1 and GRNTI_2 in _grnti_1)):
                    code_and_reg_num.append(eval(key))
                    continue
            else:
                if GRNTI_1 != '-' and (GRNTI_1 in _grnti_0 or GRNTI_1 in _grnti_1):
                    code_and_reg_num.append(eval(key))
                elif GRNTI_2 != '-' and (GRNTI_2 in _grnti_0 or GRNTI_2 in _grnti_1):
                    code_and_reg_num.append(eval(key))
        else:
            _grnti_0 = _grnti[0].split('.')
            if len(_grnti_0) == 3:  # Удаление 3-го кода ГРНТИ
                _grnti_0.pop(2)
            if GRNTI_1 != '-' and GRNTI_2 != '-':
                if (GRNTI_1 in _grnti_0 and GRNTI_2 in _grnti_0):
                    code_and_reg_num.append(eval(key))
                    continue
            else:
                if GRNTI_1 != '-' and (GRNTI_1 in _grnti_0):
                    code_and_reg_num.append(eval(key))
                elif GRNTI_2 != '-' and (GRNTI_2 in _grnti_0):
                    code_and_reg_num.append(eval(key))

    if info_dict == {} and code_and_reg_num == []:
        set_filter_value(info_dict=False)

    first_loop = True
    for rNum in code_and_reg_num:
        if first_loop and where_Vyst_mo != "":
            where_Vyst_mo += " AND "
        if first_loop:
            where_Vyst_mo += "("
            first_loop = False
        where_Vyst_mo = where_Vyst_mo + 'Рег_номер="' + str(rNum[1]) + '" AND Код_ВУЗа=' + str(rNum[0]) + ' OR '
    if where_Vyst_mo[-3:-1] == "OR":
        where_Vyst_mo = where_Vyst_mo[0:len(where_Vyst_mo)-4]
        where_Vyst_mo += ')'

        
    if where_Vyst_mo != "":
        where_Vyst_mo = "WHERE " + where_Vyst_mo

    if (not (fed_Distr == '-' and city  == '-' and region == '-' and preference_exibit  == '-' and GRNTI_1 == '-' and GRNTI_2  == '-' and univer == '-')) and where_Vyst_mo == "":
        pass
    else:
        query.exec(f"""SELECT * FROM Vyst_mo {where_Vyst_mo}""")

    
    df_model = pd.DataFrame(
        columns=headlines
    )
    table_dict = {}
    while query.next():
        for head in headlines:
            table_dict.update({head: query.value(head)})
            # table_dict.update({"Код_ВУЗа": query.value("Код_ВУЗа")})
            # table_dict.update({"Аббревиатура": query.value("Аббревиатура")})
            # table_dict.update({"Название_НИР": query.value("Название_НИР")})
            # table_dict.update({"Рег_номер": query.value("Рег_номер")})
            # table_dict.update({"ГРНТИ": query.value("ГРНТИ")})
            # table_dict.update({"Тип": query.value("Тип")})
            # table_dict.update({"Наличие_экспоната": query.value("Наличие_экспоната")})
            # table_dict.update({"Выставки": query.value("Выставки")})
            # table_dict.update({"Экспонат": query.value("Экспонат")})
            # table_dict.update({"Научный_руководитель": query.value("Научный_руководитель")})
            # table_dict.update({"Статус_руководителя": query.value("Статус_руководителя")})
        temp_df = pd.DataFrame.from_dict(table_dict, orient='index').T
        df_model = pd.concat([df_model, temp_df])
    # for the table model
    table_model = QtGui.QStandardItemModel()
    # set table headers
    table_model.setColumnCount(df_model.columns.size)
    table_model.setHorizontalHeaderLabels(df_model.columns.tolist())
    form.tableView.horizontalHeader().setStretchLastSection(True)

    # fill table model data
    for row_idx in range(len(df_model.values)):
        row = list()
        for col_idx in range(df_model.columns.size):
            val = QtGui.QStandardItem(str(df_model.values[row_idx][col_idx]))
            row.append(val)
        table_model.appendRow(row)
    # set table model to table object
    form.tableView.setModel(table_model)

    # Получаем значения таблицы для перенастройки фильтрационных QComboBox 
    k = 0
    code_values = []; grnti_values = []
    typeExhibit_dict_ = {"Е": "Есть", "Н": "Нет", "П": "Планируется"}
    typeExhibit_dict = {}
    modelFetchMore_withFiltering = form.tableView.model()
    modelFetchMore_withFiltering.fetchMore(QtCore.QModelIndex())
    while True:
        code_univer = modelFetchMore_withFiltering.index(k, 10).data()     # Получение кодов ВУЗов из таблицы
        availability = modelFetchMore_withFiltering.index(k, 5).data()     # Получение текущих кодов ГРНТИ из таблицы
        if typeExhibit_dict != typeExhibit_dict_:
            try:
                typeExhibit_dict.update({availability: typeExhibit_dict_[availability]})
            except: pass
        if code_univer == None: break
        code_values.append(code_univer)
        #grnti_values.append(grnti)
        k += 1

    code_values = set(code_values)
    
    #["Код_ВУЗа", "Аббревиатура", "Название_НИР", "Рег_номер", "ГРНТИ", "Тип", "Наличие_экспоната", "Выставки", 
                #"Экспонат", "Научный_руководитель", "Статус_руководителя"]
    # Формируем словарь info_dict по {коду ВУЗа, [Аббревиатура, Федеральный округ, Город, Область]}
    where_VUZ = ''
    # Создаем условия для запросов SQL
    for code in code_values:
        where_VUZ = where_VUZ + "Код_ВУЗа=" + str(code) + " OR "


    if where_VUZ != "":
        where_VUZ = "WHERE " + where_VUZ[0:(len(where_VUZ)-4)]


    query.exec(f"""SELECT Код_ВУЗа, Аббревиатура, Федеральный_округ, Город, Область FROM VUZ {where_VUZ}""")
    
    info_dict = {}
    while query.next():
        info_dict.update({query.value("Код_ВУЗа"): [query.value("Аббревиатура"), query.value("Федеральный_округ"), query.value("Город"), query.value("Область")]})

    set_filter_value(info_dict, typeExhibit_dict)
    recNum()
    

def filtering_window():
    """Открытие окна фильтрации"""
    global window_Filtering, form_Filtering
    # В случае, если окно уже открывалось, мы его спрятали, но не удаляли, поэтому показываем заново
    try:
        if window_Filtering != None:
            window_Filtering.show()
            return
        else:
            window_Filtering = None
    except:
        pass
    Form, Window = uic.loadUiType("source/FilteringWindow.ui")
    # Настройка интерфейса
    window_Filtering = Window()
    form_Filtering = Form()
    form_Filtering.setupUi(window_Filtering)
    form_Filtering.apply_filtering_bn.clicked.connect(filtration)   # В этой функции окно прячется, но не закрывается
    form_Filtering.reset_filtering_bn.clicked.connect(set_filter_value)
    set_filter_value()  # установка значений фильтров
    window_Filtering.show()


def new_tableName():
    """Задание имени новой таблицы"""
    global window_AddTable, form_AddTable
    Form, Window = uic.loadUiType("source/CreateTableWindow.ui")
    # Настройка интерфейса
    window_AddTable = Window()
    form_AddTable = Form()
    form_AddTable.setupUi(window_AddTable)
    global table_name
    form_AddTable.Save_bn.clicked.connect(get_table_name)
    form_AddTable.Cancel_bn.clicked.connect(lambda: window_AddTable.close())
    window_AddTable.show()

def get_table_name():
    """Функция для получения введенного имени для создания новой таблицы"""
    global table_name
    table_name = form_AddTable.TableName_le.text()
    if table_name in get_custom_table():
        msgError("Группа с таким именем уже существует")
        return
    window_AddTable.close()
    if table_name != "":
        create_table(table_name=table_name)
        table_name = ""

def create_table(table_name):
    """Создание группы НИР на основе фильтрации"""
    # Запись всех данных из отфильтрованных элементов
    data = []
    i=0
    temp_model = form.tableView.model()
    temp_model.fetchMore(QtCore.QModelIndex())
    while True:
        list_values = [temp_model.index(i, j).data() for j in range(11)]
        if list_values == [None, None, None, None, None, None, None, None, None, None, None]: break
        list_values = list(map(str, list_values))
        data.append(list_values)
        i+=1
    # Запись данных в текстовый файл
    if not os.path.exists("data"):
        os.mkdir("data")
    file = open("data/" + table_name + ".dat", 'w', encoding='utf-8')
    for dat in data:
        file.write(str(dat) + '\n')
    file.close()
    remove_duplicate_custom_table_entries(table_name)
    output_table(table_name=table_name)


def delete_custom_table(table_name):
    """Удаление группы НИР, функция после окна удаления"""
    window_DelTable.close()
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(f'Вы действительно хотите удалить группу НИР: "{table_name}"?')
    msg.setWindowTitle("Удаление")
    msg.setWindowIcon(QtGui.QIcon("source/image/delete-icon.png"))
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    global reply; reply="Cancel"
    msg.buttonClicked.connect(msgbtn)
    msg.exec()
    if reply == "Cancel":
        del reply
        return
    del reply
    if os.path.exists("data/" + table_name + ".dat"):
        os.remove("data/" + table_name + ".dat")
        if table_name == currentTable:
            output_table()

def del_customTable_window():
    """Окно удаления группы НИР"""
    table_list = get_custom_table()
    ico_file = "source/image/create-table-icon.png"
    if len(table_list) == 0:
        msgError("Группы НИР не найдены!")
        return

    ico = QtGui.QIcon()
    ico.addFile(ico_file)

    global window_DelTable, form_DelTable
    Form, Window = uic.loadUiType("source/ChoiceTableWindow.ui")
    # Настройка интерфейса
    window_DelTable = Window()
    form_DelTable = Form()
    form_DelTable.setupUi(window_DelTable)
    window_DelTable.setWindowTitle("Удалить группы НИР")
    window_DelTable.setWindowIcon(QtGui.QIcon("source/image/delete-icon.png"))

    for name in table_list:
        form_DelTable.choiceTable.addItem(ico, name)
    form_DelTable.choiceTable.setCurrentText(table_list[0])
    form_DelTable.OK_bn.clicked.connect(lambda: delete_custom_table(table_name=form_DelTable.choiceTable.currentText()))

    window_DelTable.show()

def edit_customTable(row="add"):
    """Добавить или удалить строку кастомной таблицы.
    row = add, row = remove"""
    if row == "add":
        addRow_choiceTable()
    if row == "remove":
        selected = form.tableView.currentIndex().row()  # текущая отмеченная строка
        if selected == -1:
            msgError("Для удаления выберете строку!")
            return
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f"Вы действительно хотите удалить запись?")
        msg.setWindowTitle("Удаление")
        msg.setWindowIcon(QtGui.QIcon("source/image/delete-icon.png"))
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        global reply; reply="Cancel"
        msg.buttonClicked.connect(msgbtn)
        msg.exec()
        if reply == "Cancel":
            del reply
            return
        del reply
        temp_model = form.tableView.model()
        temp_model.fetchMore(QtCore.QModelIndex())
        list_values = [temp_model.index(selected, i).data() for i in range(11)]     # Получение данных из таблицы
        removeRow_customTable(list_values)

def addRow_choiceTable():
    """Функция выбора группы НИР для добавления в неё записи"""
    selected = form.tableView.currentIndex().row()  # текущая отмеченная строка
    if selected == -1:
        msgError("Для добавления выберете строку!")
        return
    temp_model = form.tableView.model()
    temp_model.fetchMore(QtCore.QModelIndex())
    list_values = [temp_model.index(selected, i).data() for i in range(11)]     # Получение данных из таблицы
    global window_ChoiceTable, form_ChoiceTable
    Form, Window = uic.loadUiType("source/ChoiceTableWindow.ui")
    # Настройка интерфейса
    window_ChoiceTable = Window()
    form_ChoiceTable = Form()
    form_ChoiceTable.setupUi(window_ChoiceTable)
    window_ChoiceTable.setWindowTitle("Добавить в группу НИР")
    window_ChoiceTable.setWindowIcon(QtGui.QIcon("source/image/pencil-icon.png"))

    table_list = get_custom_table()
    if len(table_list) == 0:
        msgError("Группы НИР не найдены!")
        return -1
    
    ico_file = "source/image/create-table-icon.png"
    ico = QtGui.QIcon()
    ico.addFile(ico_file)
    for name in table_list:
        form_ChoiceTable.choiceTable.addItem(ico, name)

    form_ChoiceTable.OK_bn.clicked.connect(lambda: addRow_to_customTable(tableName=form_ChoiceTable.choiceTable.currentText(), data=list_values))
    window_ChoiceTable.show()


def addRow_to_customTable(tableName, data):
    """Функция добавления записи в кастомную таблицу"""
    window_ChoiceTable.close()
    data = list(map(str, data))
    if os.path.exists("data"):
        file = open("data/" + tableName + ".dat", 'a', encoding='utf-8')
        file.write(str(data) + '\n')
        file.close()
        remove_duplicate_custom_table_entries(tableName)

def remove_duplicate_custom_table_entries(tableName):
    """Удаление повторяющихся записей из группы НИР"""
    if os.path.exists("data"):
        data = []
        file = open("data/" + tableName + ".dat", 'r', encoding='utf-8')
        for line in file:
            data.append(line)
        file.close()
        data = set(data)
        file = open("data/" + tableName + ".dat", 'w', encoding='utf-8')
        for line in list(data):
            file.write(line)
        file.close()


def removeRow_customTable(rowForRemove):
    """Удаление строки кастомной таблицы.
    rowForRemove - список со значениями в строке для удаления"""
    tableName = currentTable
    if os.path.exists("data"):
        file = open("data/" + tableName + ".dat", 'r', encoding='utf-8')
        data = []
        for line in file:
            data.append(eval(line))
        file.close()
        try:
            data.remove(rowForRemove)
        except:
            pass
        file = open("data/" + tableName + ".dat", 'w', encoding='utf-8')
        for dat in data:
            file.write(str(dat) + '\n')
        file.close()
        output_table(tableName)
    

def card_preview_window():
    """Окно предпоказа карточки НИР"""

    
    selected = form.tableView.currentIndex().row()  # текущая отмеченная строка
    if selected == -1:
        msgError("Для формирования карточки НИР выберете строку!")
        return
    temp_model = form.tableView.model()
    temp_model.fetchMore(QtCore.QModelIndex())
    list_values = [temp_model.index(selected, i).data() for i in range(11)]     # Получение данных из таблицы

    global window_cardPreview, form_cardPreview
    Form, Window = uic.loadUiType("source/CardWindow.ui")
    # Настройка интерфейса
    window_cardPreview = Window()
    form_cardPreview = Form()
    form_cardPreview.setupUi(window_cardPreview)
    
    form_cardPreview.SaveButton.clicked.connect(lambda: creating_research_card(list_values=list_values))
    form_cardPreview.CancelButton.clicked.connect(window_cardPreview.close)


    # headlines = ["Аббревиатура", "Название_НИР", "Рег_номер", "ГРНТИ", "Тип", "Наличие_экспоната", "Выставки", 
    #             "Экспонат", "Научный_руководитель", "Статус_руководителя", "Код_ВУЗа"]
    form_cardPreview.Abbreviation_Out_lb.setText(list_values[headlines.index("Аббревиатура")])
    form_cardPreview.Subject_Out_lb.setText(list_values[headlines.index("Название_НИР")])
    form_cardPreview.type_Out_lb.setText(list_values[headlines.index("Тип")])
    form_cardPreview.GRNTI_Out_lb.setText(list_values[headlines.index("ГРНТИ")])
    form_cardPreview.TypeExhibit_Out_lb.setText(list_values[headlines.index("Наличие_экспоната")])
    form_cardPreview.Exhibitions_Out_lb.setText(list_values[headlines.index("Выставки")])
    form_cardPreview.Exhibit_Out_lb.setText(list_values[headlines.index("Экспонат")])
    form_cardPreview.BossName_Out_lb.setText(list_values[headlines.index("Научный_руководитель")])
    form_cardPreview.BossStatus_Out_lb.setText(list_values[headlines.index("Статус_руководителя")])
    form_cardPreview.codeVUZ_Out_lb.setText(str(list_values[headlines.index("Код_ВУЗа")]))

    window_cardPreview.show()



def creating_research_card(list_values):
    """Функция создания карточки НИР. Открывает окно для выбора пути сохранения."""
    window_cardPreview.close()

    path, extension = QFileDialog.getSaveFileUrl(filter="Документ Word (*.docx);;PDF (*.pdf)") # Открывает окно с выбором пути сохранения
    path = path.toString()

    if path == '': return 0
    path = path[8:len(path)]
    res = doc_save(path=path, headlines=headlines, list_values=list_values, extension=extension)
    if res == -1:
        msgError("Файл открыт в другой программе!")



def Group_toDoc_window():
    """Окно для сохранения групп НИР"""
    table_list = get_custom_table()
    ico_file = "source/image/create-table-icon.png"
    if len(table_list) == 0:
        msgError("Группы НИР не найдены!")
        return

    ico = QtGui.QIcon()
    ico.addFile(ico_file)

    global window_DelTable, form_DelTable
    Form, Window = uic.loadUiType("source/ChoiceTableWindow.ui")
    # Настройка интерфейса
    window_DelTable = Window()
    form_DelTable = Form()
    form_DelTable.setupUi(window_DelTable)
    window_DelTable.setWindowTitle("Сохранить группу НИР")
    window_DelTable.setWindowIcon(QtGui.QIcon("source/image/table-icon.png"))

    for name in table_list:
        form_DelTable.choiceTable.addItem(ico, name)
    form_DelTable.choiceTable.setCurrentText(table_list[0])
    form_DelTable.OK_bn.clicked.connect(lambda: research_Group_toDoc(tableSave=form_DelTable.choiceTable.currentText()))

    window_DelTable.show()



def research_Group_toDoc(tableSave):
    """Функция сохранения группы НИР. Открывает окно для выбора пути сохранения."""
    window_DelTable.close()
    file = open("data/" + str(tableSave) + ".dat", 'r', encoding='utf-8')
    data = []
    for line in file:
        data.append(eval(line))
    file.close()


    path, extension = QFileDialog.getSaveFileUrl(filter="Документ Word (*.docx);;PDF (*.pdf)") # Открывает окно с выбором пути сохранения
    path = path.toString()

    if path == '': return 0
    path = path[8:len(path)]
    res = saveTable_toDoc(path=path, table_name=tableSave, headlines=headlines, data=data, extension=extension)
    if res == -1:
        msgError("Файл открыт в другой программе!")


def help_window():
    """Открытие окна помощи"""
    global form_HelpWindow, window_HelpWindow
    Form, Window = uic.loadUiType("source/HelpWindow.ui")

    window_HelpWindow = Window()
    form_HelpWindow = Form()
    form_HelpWindow.setupUi(window_HelpWindow)

    form_HelpWindow.close_bn.clicked.connect(window_HelpWindow.close)

    window_HelpWindow.show()


output_table()

# Настройка ширины столбцов
form.tableView.setColumnWidth(0, 100)
form.tableView.setColumnWidth(1, 200)
form.tableView.setColumnWidth(2, 75)
form.tableView.setColumnWidth(4, 25)
form.tableView.setColumnWidth(6, 200)
form.tableView.setColumnWidth(7, 200)

# Взаимодействие с интерфейсом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))

form.action_sourceTable.triggered.connect(lambda: set_tableChoiceItems(table="source"))
form.action_researchTable.triggered.connect(lambda: set_tableChoiceItems(table="custom"))

form.addEntry_action.triggered.connect(add_field_window)
form.editEntry_action.triggered.connect(lambda: add_field_window(Edit=True))
form.deleteEntry_action.triggered.connect(delete_row)

form.filtering_bn.clicked.connect(filtering_window)

form.addGroup_action.triggered.connect(new_tableName)
form.deleteGroup_action.triggered.connect(del_customTable_window)
form.addToGroup_action.triggered.connect(lambda: edit_customTable(row="add"))
form.deleteFromGroup_action.triggered.connect(lambda: edit_customTable(row="remove"))
form.creatingResearchCard_action.triggered.connect(card_preview_window)
form.creatingTableCard_action.triggered.connect(Group_toDoc_window)

form.help_action.triggered.connect(help_window)

# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока