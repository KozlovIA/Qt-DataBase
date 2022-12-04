pyinstaller -w main.py
copy MainForm.ui dist\main
copy DataBaseExhibitions.db dist\main
mkdir dist\main\source
xcopy source\ dist\main\source\ /e
:: xcopy source\ dist\main\source\ - Параметр \t - копирование без пустых каталогов /e - копирование с пустыми каталогами
