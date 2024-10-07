
run:
	python3 src/main.py

build:
	pyside6-uic src/xmlui/mainwindow.ui > src/ui/mainwindow.py

design:
	pyside6-designer src/xmlui/mainwindow.ui
