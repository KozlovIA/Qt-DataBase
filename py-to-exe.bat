pyinstaller -w main.py
copy MainForm.ui dist\main
copy DataBaseExhibitions.db dist\main
mkdir dist\main\source
copy source\EditWindow.ui dist\main\source\EditWindow.ui
copy source\database-icon.png dist\main\source\database-icon.png
copy source\pencil-icon.png dist\main\source\pencil-icon.png
copy source\warning-icon.png dist\main\source\warning-icon.png
copy source\delete-icon.png dist\main\source\delete-icon.png