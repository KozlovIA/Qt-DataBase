# Файл с пользовательскими функциями для очищения от таковых файла main
# Пока не знаю, как это будет коннектиться с интерфейсом и будет ли файл востребован
from PyQt6.QtSql import *



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


def gridLayoutStartResize():
    """Начальное изменение размера сетки для дальнего шего нормального ресайза окна.
    Связано с тем, что gridLayout не получается сделать больше начального значения"""
    parameter_search = '   <widget class="QWidget" name="gridLayoutWidget">\n    <property name="geometry">\n     <rect>\n      <x>0</x>\n      <y>0</y>\n      <width>'
    GUI_file = open('MainForm.ui', 'r')
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
    GUI_file = open('MainFormResize.ui', 'w')
    GUI_file.write(file_info)
    GUI_file.close()

