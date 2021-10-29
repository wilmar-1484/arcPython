import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi

class FormularioPpal(QMainWindow):       # Definir una clase para el dialogo
    def __init__(self):
        encabezados = ("FOTO", "IDENTIFICACIÓN", "NOMBRE(S)", "APELLIDO(S)", "DIRECCIÓN", "TELÉFONO", "CORREO ELECTRÓNICO")
        super(FormularioPpal, self).__init__()
        loadUi("uis/principal.ui", self)   # Cargar el archivo con el dialog box
        self.setFixedWidth(1044)
        self.setFixedHeight(652)
        # self.windowTitle = "LOGIN"
        self.windowTitle = "Empresa XYZ"


app = QApplication(sys.argv)
formularioPpal = FormularioPpal()
formularioPpal.show()
sys.exit(app.exec_())
