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

