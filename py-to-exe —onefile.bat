pyinstaller --windowed --onefile --onedir "Research organization.py"
copy MainForm.ui "dist\Research organization\"
copy DataBaseExhibitions.db "dist\Research organization"
mkdir "dist\Research organization\source"
xcopy source\ "dist\Research organization\source\" /e
:: xcopy source\ dist\main\source\ - Параметр \t - копирование без пустых каталогов /e - копирование с пустыми каталогами
