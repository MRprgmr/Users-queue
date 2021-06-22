import sys
from PyQt5.QtWidgets import QApplication
import Handlers as hs


class Main_window(hs.main_window.MainWindow):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = Main_window()
        window.show()
        sys.exit(app.exec_())
    except Exception as er:
        with open("error.txt", "w+") as f:
            f.write(str(er))
