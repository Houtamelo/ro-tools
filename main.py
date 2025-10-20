import sys

from gui.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QFont
from config.app import APP_FONT, APP_FONT_SIZE, APP_STYLE


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)
    _build_and_set_font(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def _build_and_set_font(app):
    font_id = QFontDatabase.addApplicationFont(APP_FONT)
    # Due to platform issues, the font may fail to load. In that case, 
    #   we can just use the default font but with `APP_FONT_SIZE` instead of the default size.
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font)[0]
    else:
        font_family = app.font().family()
    
    font = QFont(font_family, APP_FONT_SIZE)
    app.setFont(q_font)


if __name__ == "__main__":
    main()
