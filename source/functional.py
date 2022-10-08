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


def field_editing():
    """Функция для редактирования строк в БД.
    Параметров не принимает, база данных является константой"""
    if not db.open():
        return False
    table_dict = {'Таблица НИР': 'VUZ', 'Таблица выставок': 'Vyst_mo', 'Таблица ГРНТИ': 'grntirub'}
    table_name = 'Таблица НИР'
    db_model = QSqlTableModel()  # Создали объект таблицы
    db_model.setTable(table_dict[table_name])     # Привязали таблицу из базы данных
    db_model.select()        # Выбрали все строки из данной таблицы
    print(db_model)

if __name__ == "__main__":
    field_editing()