# Файл с пользовательскими функциями для очищения от таковых файла main
# Пока не знаю, как это будет коннектиться с интерфейсом и будет ли файл востребован
from PyQt6.QtSql import *
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread



db_name = "DataBaseExhibitions.db"  # имя базы данных

def db_connect():
    """Функция для подключения к базе данных.
    Параметров не принимает, база данных является константой"""
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_name)
    if not db.open():
        return False
    else:
        print("Подключено к базе данных", db_name)
    return db

db = db_connect()    # db - глобальная переменная ссылающаяся на базу данных, создается с модуле functional.py строка 23 после функции db_connect()

def gridLayoutStartResize():
    """Начальное изменение размера сетки для дальнейшего нормального ресайза окна.
    Связано с тем, что gridLayout не получается сделать больше начального значения"""
    parameter_search = '   <widget class="QWidget" name="gridLayoutWidget">\n    <property name="geometry">\n     <rect>\n      <x>0</x>\n      <y>0</y>\n      <width>'
    GUI_file = open('MainForm.ui', 'r', encoding='utf-8')
    file_info = ''
    for line in GUI_file:
        file_info += line
    inx = file_info.find(parameter_search)     # начальный индекс параметра
    inx_end = file_info.find('\n     </rect>', inx)   # конечный индекс настройки grid layout
    setting = file_info[inx:inx_end]
    # замена размеров для последующего уменьшения
    file_info = file_info.replace(setting,
    '   <widget class="QWidget" name="gridLayoutWidget">\n    <property name="geometry">\n     <rect>\n      <x>0</x>\n      <y>0</y>\n      <width>8000</width>\n      <height>6000</height>'
    )
    GUI_file.close()
    GUI_file = open('MainFormResize.ui', 'w', encoding='utf-8')
    GUI_file.write(file_info)
    GUI_file.close()


def SQLdata_acquisition_EditWindow():
    """Получение данных с таблиц для оформления EditWindow
    Выходные данные: словарь с ключами - кодами ВУЗов и значениями - аббревиатурами ВУЗов,
    список кодов ГРНТИ, словарь с регистрационными номерами по ключам кода ВУЗа"""
    query = QSqlQuery()
    query.exec(
        """SELECT Код_ВУЗа, Аббревиатура, Рег_номер FROM Vyst_mo"""
    )
    university_dict = {}
    regNum_dict = {};   # regNum_dict - словарь регистрационных номеров по ключу кода ВУЗа
    while query.next():
        current_code = query.value("Код_ВУЗа")
        university_dict.update({current_code: query.value("Аббревиатура")})  # update заменяет старое значение по ключу, если оно существует или добавляет новое
        if not (current_code in regNum_dict.keys()):
            regNum_dict.update({current_code: list()})
        regNum_dict[current_code].append(query.value("Рег_номер"))
    # сортировка по ключам
    university_dict = dict(sorted(university_dict.items()))
    regNum_dict = dict(sorted(regNum_dict.items()))

    query.exec(
        """SELECT Код_рубрики FROM grntirub"""
    )
    grnti_code = []
    while query.next():
        grnti_code.append(query.value("Код_рубрики"))

    return university_dict, grnti_code, regNum_dict


def editingSQL_NIR(Edit=False, parameters_dict=False, orig_univer_code=False, orig_regNum=False):
    """Редактирование полей таблицы НИР"""
    query = QSqlQuery()
    
    if Edit:
        values = ""
        for key in parameters_dict.keys():
            values += key + "=" + str(parameters_dict[key]) + ", "
        values = values[0:len(values)-2]
        query.exec(
            """UPDATE Vyst_mo SET {values} WHERE Код_ВУЗа={orig_univer_code} AND Рег_номер={orig_regNum}"""
    )
    else:
        keys = '('
        values = ""
        for key in parameters_dict.keys():
            keys += key + ", "
            values += str(parameters_dict[key]) + ", "
        keys = keys[0:len(keys)-2]; keys += ')'
        values = values[0:len(values)-2] + ')'
        query.exec(
            """INSERT INTO Vyst_mo {keys} VALUES {values}"""
        )