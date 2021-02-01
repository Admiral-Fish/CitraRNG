import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("CitraRNG")
    app.setOrganizationName("AdmiralFish")
    
    mainWindow = MainWindow()
    mainWindow.show()
    
    sys.exit(app.exec_())
