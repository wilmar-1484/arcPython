"""
    @author: Harol Mauricio Gomez Zapata
    @date: 22/09/2021
"""

# Modulos o paquetes de PyQt5
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

import sys

import conexion

# Clase para la ui login2
class DlgSesion(QDialog):
    def __init__(self):
        super(DlgSesion, self).__init__()
        loadUi('uis/login2.ui', self)
        self.setFixedWidth(500)
        self.setFixedHeight(515)
        self.bttnIniciar.clicked.connect(self.onBttnIniciar)
        self.bttnRegistrar.clicked.connect(self.onBttnRegistrar)


    def onBttnIniciar(self):
        usuario = self.txtUsuario.text()
        clave = self.txtClave.text()

        if usuario and clave:
            usr = conexion.consultar(usuario, clave)

            if usr is not None:
                # Aquí: Agregar el código para cerrar el diálogo y mostrar
                # el formulario principal con el contenido para realizar el CRUD
                self.lblMensaje.setText("Bienvenido!")
            else:
                self.lblMensaje.setText("Usuario o Contrasena incorrectas ...")
        else:
            self.lblMensaje.setText("* Debe llenar todos los campos...")


    def onBttnRegistrar(self):
        # Aquí: Agregar el código para cerrar este diálogo y mostrar
        # ventana de registro
        self.lblMensaje.setText("Has presionado el boton 'REGISTRARME' ...")


app = QApplication(sys.argv)
dlgSesion = DlgSesion()
dlgSesion.show()
sys.exit(app.exec_())
