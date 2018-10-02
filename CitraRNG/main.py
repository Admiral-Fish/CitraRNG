import sys

from MainWindow import MainWindow
from PySide2.QtWidgets import QApplication     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("CitraRNG")
    app.setOrganizationName("AdmiralFish")
    
    mainWindow = MainWindow()
    mainWindow.show()
    
    sys.exit(app.exec_())
