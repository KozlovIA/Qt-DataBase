# -*- coding: utf-8 -*-
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMessageBox
from source.functional import *
from time import sleep
from PyQt6.QtCore import QThread, QRect
import pandas as pd

gridLayoutStartResize()     # изменнение размеров основного слоя gridLayout в MainForm для корректного изменения размеров виджетов
GRNTI_dict = get_GRNTI()    # ГРНТИ коды в формате {"[Код_ВУЗа, Рег_номер]": "ГРНТИ"}

Form, Window = uic.loadUiType("MainFormResize.ui")  # файл MainFormResize создается в функции gridLayoutStartResize, если поставить MainForm.ui, интерфейс не будет изменять размер в большую сторону
#Form, Window = uic.loadUiType("MainForm.ui")

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
            try:
                if end_of_work: return
                geometry = form.centralwidget.geometry()
                size = eval(str(geometry)[18:])[2:4]
                form.gridLayout.setGeometry(QRect(0, 0, size[0], int(size[1]*(670/700))))
                form.gridLayoutWidget_2.setGeometry(QRect(0, 0, size[0], int(size[1]*(670/700))))
                form.tabWidget.resize(size[0], size[1])
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

def msgError(msgErr):
    """Функция вывода ошибок при сохранении некорректных данных в таблицу"""
    msg = QMessageBox()
    msg.setWindowTitle("Внимание!")
    msg.setWindowIcon(QtGui.QIcon("source/warning-icon.png"))
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
    univer_dict, grnti_code = SQLdata_acquisition_EditWindow()[0:2]
    # словари типа экспоната и его наличия, служат для более красивого вывода
    type_dict = {'Е': "Тематический план", "М": "НТП"}
    typeExhibit_dict = {"Е": "Есть", "Н": "Нет", "П": "Планируется"}
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
        form_AddField.Subject_te.setText(str(list_values[2]))
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
        form_AddField.type_cb.setCurrentText(type_dict[str(list_values[5])])
        form_AddField.TypeExhibit_cb.setCurrentText(typeExhibit_dict[str(list_values[6])])
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
    """Для получения значения нажатия в случае ошибки QMessageBox"""
    global reply
    reply = i.text()

def set_filter_value(info_dict=False, typeExhibit_dict_revers={}, grnti_values=list(GRNTI_dict.values())):
    """Добавляет первоначальные значения фильтров в comboboxes
    info_dict - если окно уже есть, то запрос будет создан в зависимости от текущих значений фильтра"""
    if info_dict==False: 
        info_dict = get_info_for_filtration()   # словарь по {коду ВУЗа, [Аббревиатура, Федеральный округ, Город, Область]}
        output_table()
        Edit = False
    else:
        university_cb_value = form.university_cb.currentText()
        federalDistrict_cb_value = form.federalDistrict_cb.currentText()
        city_cb_value = form.city_cb.currentText()
        region_cb_value = form.region_cb.currentText()
        preference_exibit_cb_value = form.preference_exibit_cb.currentText()
        GRNTI_1_cb_value = form.GRNTI_1_cb.currentText()
        GRNTI_2_cb_value = form.GRNTI_2_cb.currentText()

        form.federalDistrict_cb.clear()
        form.city_cb.clear()
        form.region_cb.clear()
        form.GRNTI_1_cb.clear()
        form.GRNTI_2_cb.clear()
        form.university_cb.clear()
        form.preference_exibit_cb.clear()
        form.federalDistrict_cb.addItem('-')
        form.city_cb.addItem('-')
        form.region_cb.addItem('-')
        form.GRNTI_1_cb.addItem('-')
        form.GRNTI_2_cb.addItem('-')
        form.university_cb.addItem('-')
        Edit = True
    # Добавление в списки, а затем в QComboBoxes значений
    fed_district = []; city = []; region = []
    for code_uni in list(info_dict.keys()):
        form.university_cb.addItem(info_dict[code_uni][0])
        fed_district.append(info_dict[code_uni][1])
        city.append(info_dict[code_uni][2])
        region.append(info_dict[code_uni][3])
    form.federalDistrict_cb.addItems(set(fed_district))
    form.city_cb.addItems(set(city))
    form.region_cb.addItems(set(region))
    form.preference_exibit_cb.addItems(list(typeExhibit_dict_revers.values()))

    # ГРНТИ как обычно отдельно
    for grnti in grnti_values:
        if ';' in grnti:
            grnti = grnti.split(';')
        if str(type(grnti)) == "<class 'list'>" and len(grnti) > 1:
            form.GRNTI_1_cb.addItem(grnti[0])
            form.GRNTI_1_cb.addItem(grnti[1])
            form.GRNTI_2_cb.addItem(grnti[0])
            form.GRNTI_2_cb.addItem(grnti[1])
        else: form.GRNTI_1_cb.addItem(grnti); form.GRNTI_2_cb.addItem(grnti)

    # Установка значений фильтра на место
    if Edit: 
        form.university_cb.setCurrentText(university_cb_value)
        form.federalDistrict_cb.setCurrentText(federalDistrict_cb_value)
        form.city_cb.setCurrentText(city_cb_value)
        form.region_cb.setCurrentText(region_cb_value)
        form.preference_exibit_cb.setCurrentText(preference_exibit_cb_value)
        form.GRNTI_1_cb.setCurrentText(GRNTI_1_cb_value)
        form.GRNTI_2_cb.setCurrentText(GRNTI_2_cb_value)
set_filter_value()


def filtration():
    typeExhibit_dict = {"Есть": "Е", "Нет": "Н", "Планируется": "П", "-": "-"}
    fed_Distr = form.federalDistrict_cb.currentText()
    city = form.city_cb.currentText()
    region = form.region_cb.currentText()
    preference_exibit = typeExhibit_dict[form.preference_exibit_cb.currentText()]
    GRNTI_1 = form.GRNTI_1_cb.currentText()
    GRNTI_2 = form.GRNTI_2_cb.currentText()
    univer = form.university_cb.currentText()


    info_dict = {}
    if fed_Distr != '-': info_dict.update({"Федеральный_округ": fed_Distr})
    if city != '-': info_dict.update({"Город": city})
    if region != '-': info_dict.update({"Область": region})
    if univer != '-': info_dict.update({"Аббревиатура": univer})
    if preference_exibit != '-': info_dict.update({"Наличие_экспоната": preference_exibit})
        #"ГРНТИ": [GRNTI_1, GRNTI_2],
    
    if info_dict == {}:
        set_filter_value(info_dict=False)

    where_VUZ = ""; where_Vyst_mo = ""
    # Создаем условия для запросов SQL
    for key in list(info_dict.keys()):
        if key == "ГРНТИ" or key == "Наличие_экспоната" or key == "Аббревиатура":
            where_Vyst_mo += key + '="' + str(info_dict[key]) + '" AND '
        else:
            where_VUZ += key + '="' + str(info_dict[key]) + '" AND '
    if where_VUZ != "":
        where_VUZ = "WHERE " + where_VUZ[0:(len(where_VUZ)-4)]
    if where_Vyst_mo != "":
        where_Vyst_mo = where_Vyst_mo[0:(len(where_Vyst_mo)-4)]

    # Делаем запрос сначала в VUZ, получаем номера ВУЗов и добавляем их в условие к таблицу Vyst_mo, изи ГГ
    query = QSqlQuery()

    if where_VUZ != '':
        query.exec(f"""SELECT Код_ВУЗа FROM VUZ {where_VUZ}""")
        first_loop = True
        while query.next():
            if first_loop and where_Vyst_mo != "":
                where_Vyst_mo += " AND "
            first_loop = False
            where_Vyst_mo = where_Vyst_mo + "Код_ВУЗа=" + str(query.value("Код_ВУЗа")) + " OR "
    if where_Vyst_mo[-3:-1] == "OR":
        where_Vyst_mo = where_Vyst_mo[0:len(where_Vyst_mo)-4]
    
    # фильтрация грнти через регистрационный номер
    code_and_reg_num = []
    for key in list(GRNTI_dict.keys()):
        if GRNTI_1 != '-' and GRNTI_2 != '-' and (GRNTI_1 + ';' + GRNTI_2) == GRNTI_dict[key]:
            code_and_reg_num.append(eval(key))
            continue
        if GRNTI_1 != '-' and (GRNTI_1 in GRNTI_dict[key]):
            code_and_reg_num.append(eval(key))
        elif GRNTI_2 != '-' and (GRNTI_2 in GRNTI_dict[key]):
            code_and_reg_num.append(eval(key))

    first_loop = True
    for rNum in code_and_reg_num:
        if first_loop and where_Vyst_mo != "":
            where_Vyst_mo += " AND "
        if first_loop:
            first_loop = False
        where_Vyst_mo = where_Vyst_mo + '(Рег_номер="' + str(rNum[1]) + '" AND Код_ВУЗа=' + str(rNum[0]) + ') OR '
    if where_Vyst_mo[-3:-1] == "OR":
        where_Vyst_mo = where_Vyst_mo[0:len(where_Vyst_mo)-4]
    print(where_Vyst_mo)
        
    if where_Vyst_mo != "":
        where_Vyst_mo = "WHERE " + where_Vyst_mo


    query.exec(f"""SELECT * FROM Vyst_mo {where_Vyst_mo}""")
    df_model = pd.DataFrame(
        columns=["Код_ВУЗа", "Аббревиатура", "Название_НИР", "Рег_номер", "ГРНТИ", "Тип", "Наличие_экспоната", "Выставки", 
                "Экспонат", "Научный_руководитель", "Статус_руководителя"]
    )
    table_dict = {}
    while query.next():
        table_dict.update({"Код_ВУЗа": query.value("Код_ВУЗа")})
        table_dict.update({"Аббревиатура": query.value("Аббревиатура")})
        table_dict.update({"Название_НИР": query.value("Название_НИР")})
        table_dict.update({"Рег_номер": query.value("Рег_номер")})
        table_dict.update({"ГРНТИ": query.value("ГРНТИ")})
        table_dict.update({"Тип": query.value("Тип")})
        table_dict.update({"Наличие_экспоната": query.value("Наличие_экспоната")})
        table_dict.update({"Выставки": query.value("Выставки")})
        table_dict.update({"Экспонат": query.value("Экспонат")})
        table_dict.update({"Научный_руководитель": query.value("Научный_руководитель")})
        table_dict.update({"Статус_руководителя": query.value("Статус_руководителя")})
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
    while True:
        code_univer = form.tableView.model().index(k, 0).data()     # Получение кодов ВУЗов из таблицы
        grnti = form.tableView.model().index(k, 4).data()     # Получение текущих кодов ГРНТИ из таблицы
        if code_univer == None: break
        code_values.append(code_univer)
        grnti_values.append(grnti)
        k += 1
    code_values = set(code_values)
    #["Код_ВУЗа", "Аббревиатура", "Название_НИР", "Рег_номер", "ГРНТИ", "Тип", "Наличие_экспоната", "Выставки", 
                #"Экспонат", "Научный_руководитель", "Статус_руководителя"]
    # Формируем словарь info_dict по {коду ВУЗа, [Аббревиатура, Федеральный округ, Город, Область]}
    where_VUZ = ''
    # Создаем условия для запросов SQL
    for code in code_values:
        where_VUZ = "Код_ВУЗа=" + str(code) + " OR "

    if where_VUZ != "":
        where_VUZ = "WHERE " + where_VUZ[0:(len(where_VUZ)-4)]

    query.exec(f"""SELECT Код_ВУЗа, Аббревиатура, Федеральный_округ, Город, Область FROM VUZ {where_VUZ}""")
    
    info_dict = {}
    while query.next():
        info_dict.update({query.value("Код_ВУЗа"): [query.value("Аббревиатура"), query.value("Федеральный_округ"), query.value("Город"), query.value("Область")]})

    query.exec(f"""SELECT Наличие_экспоната FROM Vyst_mo {where_VUZ}""")    # where_VUZ тут вполне логично, т.к. в нем коды ВУЗов

    typeExhibit_dict_ = {"Е": "Есть", "Н": "Нет", "П": "Планируется"}
    typeExhibit_dict_revers = {"-": "-"}
    while query.next():
        type_exh = query.value("Наличие_экспоната")
        typeExhibit_dict_revers.update({type_exh: typeExhibit_dict_[type_exh]})
        if typeExhibit_dict_revers == typeExhibit_dict_: break
        #"ГРНТИ": [GRNTI_1, GRNTI_2],
    set_filter_value(info_dict, typeExhibit_dict_revers, grnti_values)    # Изменение значений в фильтрах - QComboBox
    



#output_table()
# Взаимодействие с интерфесом
# Передавать параметры в функции через кнопки можно с помощью лямбда функций form.pushButton.clicked.connect(lambda x: test("hello fucking Qt!"))
form.choiceTable.currentTextChanged.connect(lambda: output_table(table_name=form.choiceTable.currentText()))
form.AddField.clicked.connect(add_field_window)
form.EditField.clicked.connect(lambda: add_field_window(Edit=True))
form.deleteButton.clicked.connect(delete_row)

form.apply_filtering_bn.clicked.connect(filtration)
form.reset_filtering_bn.clicked.connect(set_filter_value)



# Запуск приложения
window.show()
app.exec()

end_of_work = True  # для завершения потока