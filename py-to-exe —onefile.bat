pyinstaller --windowed --onefile --onedir main.py
copy MainForm.ui dist\main\
copy DataBaseExhibitions.db dist
mkdir dist\main\source
xcopy source\ dist\main\source\ /e
:: xcopy source\ dist\main\source\ - Параметр \t - копирование без пустых каталогов /e - копирование с пустыми каталогами
