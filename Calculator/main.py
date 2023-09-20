import sys
from main_window import ButtonsGrid, Info, MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import Display, setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Create app
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Icon definition
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info (results)
    info = Info('Result')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Execute everything
    window.adjustFixedSize()
    window.show()
    app.exec()
