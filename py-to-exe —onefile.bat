pyinstaller -w --onefile main.py
copy MainForm.ui dist\
copy DataBaseExhibitions.db dist
mkdir dist\source
xcopy source\ dist\source\ /e
:: xcopy source\ dist\source\ - Параметр \t - копирование без пустых каталогов /e - копирование с пустыми каталогами
